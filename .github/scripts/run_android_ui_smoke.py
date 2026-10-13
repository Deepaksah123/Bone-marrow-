#!/usr/bin/env python3
"""Source-bound Android UI smoke checks with verified accessibility targeting."""
from __future__ import annotations

import json
import os
import re
import struct
import subprocess
import time
import zlib
import xml.etree.ElementTree as ET
from pathlib import Path

PACKAGE = "com.marrow.reconstruction.replica"
ACTIVITY = f"{PACKAGE}/com.marrow.reconstruction.MainActivity"
OUT = Path("qa-screenshots")
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "run-context.txt").write_text(
    "\n".join((
        f"commit={os.environ.get('GITHUB_SHA', 'unknown')}",
        f"run_id={os.environ.get('GITHUB_RUN_ID', 'local')}",
        f"workflow={os.environ.get('GITHUB_WORKFLOW', 'local')}",
        "emulator_script_invoked=true",
    )) + "\n",
    encoding="utf-8",
)


def adb(args: list[str], timeout: int = 20, check: bool = True) -> subprocess.CompletedProcess[str]:
    cmd = ["adb", *args]
    print("$ " + " ".join(cmd), flush=True)
    return subprocess.run(
        cmd, check=check, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, timeout=timeout,
    )


def ensure_app() -> None:
    result = adb(["shell", "pidof", PACKAGE], timeout=10, check=False)
    if result.returncode != 0 or not result.stdout.strip():
        raise SystemExit("Reconstruction app process exited during interaction QA")


def write_anr_diagnostics(stage: str) -> None:
    # Preserve evidence even when UI smoke fails; the artifact upload step runs
    # with always(), so the next pass can distinguish app ANR from emulator/system UI.
    OUT.mkdir(parents=True, exist_ok=True)
    chunks = [f"ANR detected at: {stage}\n"]
    for label, args in (
        ("window", ["shell", "dumpsys", "window", "windows"]),
        ("activity", ["shell", "dumpsys", "activity", "activities"]),
        ("processes", ["shell", "ps", "-A"]),
        ("recent logcat", ["logcat", "-d", "-t", "2500"]),
    ):
        try:
            result = adb(args, timeout=30, check=False)
            chunks.append(f"\n===== {label} (rc={result.returncode}) =====\n{result.stdout}")
        except Exception as exc:
            chunks.append(f"\n===== {label}: collection failed: {exc} =====\n")
    (OUT / "anr-diagnostics.txt").write_text("\n".join(chunks), encoding="utf-8")


def visible_anr_marker(window_dump: str) -> str | None:
    """Return an ANR marker only when its own window is visibly rendered."""
    blocks = re.split(r"(?=window #\d+\s)", window_dump.lower())
    indicators = (
        "application not responding",
        "isn't responding",
        "is not responding",
        "anrdialog",
    )
    for block in blocks:
        marker = next((item for item in indicators if item in block), None)
        if marker and "isvisible=true" in block and "surface: shown=true" in block:
            return marker
    return None


def assert_no_anr_dialog(stage: str) -> None:
    # A visible ANR is a QA failure regardless of which process owns it. Do not
    # dismiss system dialogs, restart processes, or continue to screenshot a
    # potentially unhealthy emulator; preserve diagnostics and fail immediately.
    windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
    marker = visible_anr_marker(windows)
    if marker:
        write_anr_diagnostics(f"{stage}: visible ANR window marker {marker}")
        raise SystemExit(f"Visible emulator ANR dialog detected {stage}: {marker}")


def find_node(root: ET.Element, *, resource_id: str | None = None,
              content_desc: str | None = None, clickable_only: bool = False) -> ET.Element | None:
    for node in root.iter("node"):
        attrs = node.attrib
        if attrs.get("visible-to-user", "true").lower() == "false":
            continue
        if clickable_only and attrs.get("clickable", "false").lower() != "true":
            continue
        if resource_id is not None and not attrs.get("resource-id", "").endswith(f"/{resource_id}"):
            continue
        if content_desc is not None and attrs.get("content-desc") != content_desc:
            continue
        if attrs.get("bounds"):
            return node
    return None


def node_center(node: ET.Element) -> tuple[int, int]:
    match = re.fullmatch(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", node.attrib.get("bounds", ""))
    if not match:
        raise ValueError(f"Invalid or missing accessibility bounds: {node.attrib.get('bounds')!r}")
    left, top, right, bottom = map(int, match.groups())
    if right <= left or bottom <= top:
        raise ValueError(f"Empty accessibility bounds: {node.attrib.get('bounds')!r}")
    return (left + right) // 2, (top + bottom) // 2


def tab_is_selected(root: ET.Element, label: str) -> bool:
    return any(
        node.attrib.get("selected", "").lower() == "true"
        for node in root.iter("node")
        if node.attrib.get("content-desc") == label
    )


def read_hierarchy() -> ET.Element:
    assert_no_anr_dialog("before accessibility hierarchy dump")
    path = "/sdcard/marrow-ui-hierarchy.xml"
    adb(["shell", "rm", "-f", path], timeout=10, check=False)
    dump = adb(["shell", "uiautomator", "dump", path], timeout=30)
    if "dumped to" not in dump.stdout.lower():
        raise RuntimeError(f"UIAutomator did not confirm a hierarchy dump: {dump.stdout[-500:]}")
    xml = adb(["shell", "cat", path], timeout=10).stdout
    root = ET.fromstring(xml)
    assert_no_anr_dialog("after accessibility hierarchy dump")
    return root


def wait_for_tabs(timeout: int = 120) -> ET.Element:
    labels = ("Home", "QBank", "Tests", "Videos")
    deadline = time.monotonic() + timeout
    last_error = "tab labels not present yet"
    while time.monotonic() < deadline:
        try:
            root = read_hierarchy()
            if all(find_node(root, content_desc=label) is not None for label in labels):
                return root
        except (RuntimeError, subprocess.SubprocessError, ET.ParseError, ValueError) as exc:
            last_error = str(exc)
        time.sleep(2)
    write_anr_diagnostics(f"source-bound tabs did not render within {timeout}s: {last_error}")
    raise SystemExit(f"App did not render all source-bound tabs within {timeout}s: {last_error}")


def tap_view(resource_id: str, *, content_desc_fallback: str | None = None) -> ET.Element:
    root = read_hierarchy()
    node = find_node(root, resource_id=resource_id)
    if node is None and content_desc_fallback is not None:
        # Some Android accessibility providers omit the resource ID on an
        # ImageView but preserve its exact source-declared contentDescription.
        node = find_node(root, content_desc=content_desc_fallback, clickable_only=True)
    if node is None:
        # Keep the exact hierarchy that explains a missing source-bound target.
        (OUT / f"missing-view-{resource_id}-hierarchy.xml").write_text(
            ET.tostring(root, encoding="unicode"), encoding="utf-8"
        )
        raise SystemExit(f"Visible source-bound view not found: {resource_id}")
    tap(*node_center(node))
    time.sleep(1)
    return read_hierarchy()


def tap_tab(label: str, root: ET.Element | None = None) -> ET.Element:
    if root is None:
        root = read_hierarchy()
    node = find_node(root, content_desc=label)
    if node is None:
        raise SystemExit(f"Visible source-bound tab not found: {label}")
    tap(*node_center(node))
    time.sleep(1)
    after = read_hierarchy()
    if not tab_is_selected(after, label):
        raise SystemExit(f"Tab selection did not change to {label}")
    return after


def assert_resource_visibility(root: ET.Element, resource_id: str, expected: bool) -> None:
    node = find_node(root, resource_id=resource_id)
    if (node is not None) != expected:
        state = "visible" if node is not None else "not visible"
        wanted = "visible" if expected else "not visible"
        raise SystemExit(f"Source-bound view {resource_id} is {state}; expected {wanted}")


def assert_text(root: ET.Element, resource_id: str, expected: str) -> None:
    node = find_node(root, resource_id=resource_id)
    if node is None:
        raise SystemExit(f"Visible source-bound text view not found: {resource_id}")
    actual = node.attrib.get("text", "")
    if actual != expected:
        raise SystemExit(
            f"Text mismatch for {resource_id}: expected {expected!r}, got {actual!r}"
        )


def assert_switch_checked(root: ET.Element, resource_id: str, expected: bool) -> None:
    node = find_node(root, resource_id=resource_id)
    if node is None:
        raise SystemExit(f"Visible source-bound switch not found: {resource_id}")
    actual = node.attrib.get("checked", "").lower() == "true"
    if actual != expected:
        raise SystemExit(f"Switch state mismatch for {resource_id}: expected checked={expected}, got {node.attrib.get('checked')!r}")


def assert_interaction_deferred(root: ET.Element, resource_id: str, description: str) -> None:
    node = find_node(root, resource_id=resource_id)
    if node is None:
        raise SystemExit(f"Visible source-bound control not found: {resource_id}")
    if node.attrib.get("clickable", "").lower() != "false":
        raise SystemExit(f"{description} must remain non-clickable until its original ViewModel is integrated: {resource_id}")
    if node.attrib.get("focusable", "").lower() != "false":
        raise SystemExit(f"{description} must remain non-focusable until its original ViewModel is integrated: {resource_id}")


def assert_switch_interaction_deferred(root: ET.Element, resource_id: str) -> None:
    assert_interaction_deferred(root, resource_id, "Intern Mode switch")


def tap(x: int, y: int) -> None:
    # UIAutomator captures and cold-emulator System UI recovery can leave the
    # ADB shell briefly busy. A 10-second timeout caused the latest smoke run
    # to abort during a source-bound Tests-tab tap before ANR diagnostics ran.
    # Do not retry a timed-out tap: it may already have been delivered, and a
    # duplicate could trigger a second state transition.
    try:
        adb(["shell", "input", "tap", str(x), str(y)], timeout=30)
    except subprocess.TimeoutExpired as exc:
        try:
            write_anr_diagnostics(f"ADB input tap timed out at source-derived bounds ({x}, {y})")
        except Exception as diagnostic_error:
            print(f"Failed to collect timeout diagnostics: {diagnostic_error}", flush=True)
        raise SystemExit(
            f"ADB input tap timed out after 30 seconds at source-derived bounds ({x}, {y}); "
            "tap was not retried because its delivery state is unknown"
        ) from exc


def back() -> None:
    adb(["shell", "input", "keyevent", "4"], timeout=10)
    time.sleep(1)


def screenshot(name: str) -> None:
    assert_no_anr_dialog(f"before screenshot {name}")
    # Stream the framebuffer directly; remote-file screencap can fail on headless
    # SwiftShader emulators with an invalid ColorBuffer despite a healthy app.
    cmd = ["adb", "exec-out", "screencap", "-p"]
    print("$ " + " ".join(cmd), flush=True)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    if result.returncode != 0 or not result.stdout.startswith(bytes((137, 80, 78, 71, 13, 10, 26, 10))):
        raise SystemExit(
            f"Framebuffer capture failed for {name}: rc={result.returncode}; "
            f"stderr={result.stderr.decode(errors='replace')[-600:]}; "
            f"bytes={len(result.stdout)}"
        )
    (OUT / f"{name}.png").write_bytes(result.stdout)
    assert_no_anr_dialog(f"after screenshot {name}")
    print(f"Captured screenshot: {name} ({len(result.stdout)} bytes)", flush=True)


def validate_png_capture(image_path: Path, *, minimum_width: int = 320, minimum_height: int = 480) -> dict[str, int | str]:
    """Validate PNG chunk framing, CRCs, image data, terminator, and dimensions."""
    if not image_path.is_file():
        raise SystemExit(f"Required screenshot evidence missing: {image_path}")
    image_bytes = image_path.read_bytes()
    signature = bytes((137, 80, 78, 71, 13, 10, 26, 10))
    if len(image_bytes) < len(signature) or not image_bytes.startswith(signature):
        raise SystemExit(f"Required screenshot is not a valid PNG: {image_path}")

    offset = len(signature)
    width = height = 0
    seen_ihdr = seen_idat = seen_iend = False
    idat_payloads: list[bytes] = []
    while offset < len(image_bytes):
        if offset + 12 > len(image_bytes):
            raise SystemExit(f"Truncated PNG chunk framing: {image_path}")
        chunk_length = struct.unpack(">I", image_bytes[offset:offset + 4])[0]
        chunk_type = image_bytes[offset + 4:offset + 8]
        chunk_end = offset + 12 + chunk_length
        if chunk_end > len(image_bytes):
            raise SystemExit(f"Truncated PNG chunk payload: {image_path}")
        chunk_data = image_bytes[offset + 8:offset + 8 + chunk_length]
        stored_crc = struct.unpack(">I", image_bytes[offset + 8 + chunk_length:chunk_end])[0]
        actual_crc = zlib.crc32(chunk_type + chunk_data) & 0xffffffff
        if stored_crc != actual_crc:
            raise SystemExit(f"PNG chunk CRC mismatch ({chunk_type.decode('ascii', errors='replace')}): {image_path}")
        if not seen_ihdr:
            if chunk_type != b"IHDR" or chunk_length != 13:
                raise SystemExit(f"PNG must begin with a valid IHDR chunk: {image_path}")
            width, height = struct.unpack(">II", chunk_data[:8])
            seen_ihdr = True
        elif chunk_type == b"IHDR":
            raise SystemExit(f"PNG contains duplicate IHDR chunk: {image_path}")
        if chunk_type == b"IDAT":
            seen_idat = True
            idat_payloads.append(chunk_data)
        if chunk_type == b"IEND":
            if chunk_length != 0 or not seen_idat:
                raise SystemExit(f"PNG has invalid IEND or missing image data: {image_path}")
            seen_iend = True
            offset = chunk_end
            break
        offset = chunk_end

    if not seen_ihdr or not seen_idat or not seen_iend or offset != len(image_bytes):
        raise SystemExit(f"PNG is missing required chunks or has trailing data: {image_path}")
    try:
        zlib.decompress(b"".join(idat_payloads))
    except zlib.error as exc:
        raise SystemExit(f"PNG IDAT stream is corrupt: {image_path}: {exc}") from exc
    if width < minimum_width or height < minimum_height:
        raise SystemExit(f"Required screenshot has implausible dimensions {width}x{height}: {image_path}")
    return {"file": image_path.name, "bytes": len(image_bytes), "width": width, "height": height}


def main() -> None:
    # Do not alter unrelated emulator packages or secure settings to make QA pass.
    # The normal accessibility wait below determines whether the app is ready;
    # any visible ANR dialog remains a real test failure with diagnostics.
    adb(["install", "app/build/outputs/apk/debug/app-debug.apk"], timeout=120)
    adb(["shell", "am", "force-stop", PACKAGE], timeout=15)
    adb(["shell", "am", "start", "-n", ACTIVITY], timeout=45)
    for _ in range(20):
        result = adb(["shell", "pidof", PACKAGE], timeout=8, check=False)
        if result.returncode == 0 and result.stdout.strip():
            break
        time.sleep(1)
    else:
        raise SystemExit("App process did not start")
    # Wait for the app's actual accessibility tree, not merely a live PID or splash screen.
    hierarchy = wait_for_tabs(timeout=120)
    hierarchy = tap_tab("Home", hierarchy)
    assert_resource_visibility(hierarchy, "iconBookmark", True)
    screenshot("home")
    for label in ("QBank", "Tests", "Videos", "Home"):
        hierarchy = tap_tab(label)
        assert_resource_visibility(hierarchy, "iconBookmark", label == "Home")
        if label == "Home":
            assert_resource_visibility(hierarchy, "textBranding", True)
            assert_resource_visibility(hierarchy, "textPageTitle", False)
        else:
            assert_resource_visibility(hierarchy, "textBranding", False)
            assert_resource_visibility(hierarchy, "textPageTitle", True)
        time.sleep(1)
        ensure_app()
        screenshot(label.lower())

    # Verify the drawer actually exposes its recovered original source row, not
    # merely that tapping the menu icon leaves the Activity alive.
    hierarchy = tap_view("iconMenu")
    assert_resource_visibility(hierarchy, "navYourCourse", True)
    screenshot("drawer-open")
    back()
    hierarchy = wait_for_tabs(timeout=30)
    assert_resource_visibility(hierarchy, "navYourCourse", False)
    # BACK must close the drawer and leave the app shell on screen; a live PID
    # alone is insufficient because the Activity could have finished.
    hierarchy = wait_for_tabs(timeout=30)

    hierarchy = tap_view("iconSearch", content_desc_fallback="Search")
    assert_resource_visibility(hierarchy, "etSearch", True)
    assert_resource_visibility(hierarchy, "tvInitMessage", True)
    screenshot("search-open")
    # BACK first dismisses the soft keyboard on API 30, leaving the overlay in
    # place. Use its actual source-bound toolbar Back control to close the route.
    hierarchy = tap_view("ivBack")
    assert_resource_visibility(hierarchy, "etSearch", False)
    hierarchy = wait_for_tabs(timeout=30)
    ensure_app()

    # Keep the verified XML default state visible. The original event/state path is
    # traced, but VideoLandingViewModel and its dependencies are not integrated locally.
    # Verify the switch remains non-actionable rather than faking ON/OFF UI.
    hierarchy = tap_tab("Videos")
    assert_switch_checked(hierarchy, "switchInternMode", False)
    assert_switch_interaction_deferred(hierarchy, "switchInternMode")
    assert_text(hierarchy, "tvInternModeStatus", "Intern Mode : OFF")
    # Loading copy depends on the original InternModelLoadedUIData state stream.
    # Until that stream is integrated, no loading overlay or invented message may appear.
    assert_resource_visibility(hierarchy, "internModeSwitchOverlay", False)
    assert_resource_visibility(hierarchy, "llInternModeSwitchView", False)
    assert_resource_visibility(hierarchy, "groupInternModeSwitch", False)
    assert_resource_visibility(hierarchy, "tvInternModeSwitchMsg", False)
    screenshot("videos-intern-mode-unbound")
    # Original tooltip open/dismiss actions dispatch ViewModel events. The local
    # ViewModel is absent, so verify the controls are deliberately non-actionable.
    assert_interaction_deferred(hierarchy, "ibTooltip", "Intern Mode tooltip trigger")
    assert_resource_visibility(hierarchy, "tooltipInternModeInfo", False)
    screenshot("video-tooltip-deferred")
    # The banner and tooltip-dismiss buttons are inside source layouts whose
    # verified default visibility is GONE, so UIAutomator cannot assert their node
    # properties at runtime. Source-level regression tests verify their disabled state.
    ensure_app()

    # Light/dark theme captures.
    adb(["shell", "cmd", "uimode", "night", "yes"], timeout=20)
    time.sleep(2)
    screenshot("video-dark")
    tap_tab("Home")
    time.sleep(1)
    screenshot("home-dark")
    adb(["shell", "cmd", "uimode", "night", "no"], timeout=20)
    time.sleep(1)
    ensure_app()
    # Make the uploaded evidence self-describing and fail closed if any required
    # screen/state capture is absent, corrupt, or has an invalid PNG header.
    required_captures = (
        "home", "qbank", "tests", "videos", "drawer-open", "search-open",
        "videos-intern-mode-unbound", "video-tooltip-deferred",
        "video-dark", "home-dark",
    )
    manifest = []
    for name in required_captures:
        image_path = OUT / f"{name}.png"
        manifest.append(validate_png_capture(image_path))
    manifest_path = OUT / "screenshot-manifest.json"
    manifest_path.write_text(json.dumps({
        "commit": os.environ.get("GITHUB_SHA", "unknown"),
        "run_id": os.environ.get("GITHUB_RUN_ID", "local"),
        "required_capture_count": len(required_captures),
        "captures": manifest,
    }, indent=2) + "\n", encoding="utf-8")
    print(f"Screenshot interaction QA completed; validated {len(manifest)} required captures and wrote {manifest_path}.", flush=True)


if __name__ == "__main__":
    main()
