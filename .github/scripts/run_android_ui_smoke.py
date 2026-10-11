#!/usr/bin/env python3
"""Source-bound Android UI smoke checks with verified accessibility targeting."""
from __future__ import annotations

import json
import os
import re
import struct
import subprocess
import time
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
SYSTEM_UI_ANR_RECOVERY_ATTEMPTS = 0
MAX_SYSTEM_UI_ANR_RECOVERY_ATTEMPTS = 2


def adb(args: list[str], timeout: int = 20, check: bool = True) -> subprocess.CompletedProcess[str]:
    cmd = ["adb", *args]
    print("$ " + " ".join(cmd), flush=True)
    return subprocess.run(
        cmd, check=check, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, timeout=timeout,
    )


def configure_reference_device_geometry() -> None:
    """Match the reference capture geometry before rendering UI."""
    adb(["shell", "wm", "size", "1080x2400"], timeout=15)
    size_dump = adb(["shell", "wm", "size"], timeout=15).stdout
    if not re.search(r"(?:Override|Physical) size:\s*1080x2400", size_dump):
        raise SystemExit(f"Could not set reference display size 1080x2400: {size_dump.strip()}")
    adb(["shell", "wm", "density", "420"], timeout=15)
    density_dump = adb(["shell", "wm", "density"], timeout=15).stdout
    if not re.search(r"(?:Override|Physical) density:\s*420", density_dump):
        raise SystemExit(f"Could not set reference display density 420 dpi: {density_dump.strip()}")
    print("Reference display geometry verified: 1080x2400 at 420 dpi (20:9).", flush=True)


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


def visible_system_ui_anr(window_dump: str) -> bool:
    """Identify a visible ANR owned by System UI, not by the replica app."""
    blocks = re.split(r"(?=window #\d+\s)", window_dump.lower())
    indicators = ("application not responding", "isn't responding", "is not responding", "anrdialog")
    return any(
        any(marker in block for marker in indicators)
        and "com.android.systemui" in block
        and "isvisible=true" in block
        and "surface: shown=true" in block
        for block in blocks
    )


def wait_button_center(hierarchy_xml: str) -> tuple[int, int] | None:
    """Find the explicit Wait action in Android's ANR dialog without guessed taps."""
    try:
        root = ET.fromstring(hierarchy_xml)
    except ET.ParseError:
        return None
    for node in root.iter("node"):
        if node.attrib.get("visible-to-user", "true").lower() == "false":
            continue
        label = " ".join((node.attrib.get("text", ""), node.attrib.get("content-desc", ""))).strip().lower()
        if label in {"wait", "wait for app", "wait for app to respond"} and node.attrib.get("bounds"):
            try:
                return node_center(node)
            except ValueError:
                return None
    return None


def try_wait_on_system_ui_anr(stage: str) -> bool:
    """Use the dialog's actual accessibility bounds; never guess a screen coordinate."""
    path = "/sdcard/marrow-system-anr-hierarchy.xml"
    result = adb(["shell", "uiautomator", "dump", path], timeout=30, check=False)
    if "dumped to" not in result.stdout.lower():
        write_anr_diagnostics(f"{stage}: unable to dump ANR dialog hierarchy for Wait action")
        return False
    xml = adb(["shell", "cat", path], timeout=10, check=False).stdout
    center = wait_button_center(xml)
    if center is None:
        write_anr_diagnostics(f"{stage}: visible ANR dialog has no accessible Wait button")
        return False
    write_anr_diagnostics(f"{stage}: tapping Android ANR dialog's accessible Wait action at {center}")
    adb(["shell", "input", "tap", str(center[0]), str(center[1])], timeout=15, check=False)
    time.sleep(5)
    windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
    if visible_anr_marker(windows):
        return False
    time.sleep(12)
    windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
    return not visible_anr_marker(windows)


def assert_no_anr_dialog(stage: str) -> None:
    # Never capture while any ANR dialog is visible. Cold boot can briefly overload
    # System UI while the replica's first Activity is being displayed. Preserve
    # diagnostics before each bounded recovery, then require a 12-second clean
    # window interval. Replica-owned ANRs and a third/recurrent system ANR are fatal.
    global SYSTEM_UI_ANR_RECOVERY_ATTEMPTS
    windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
    marker = visible_anr_marker(windows)
    if not marker:
        return

    while marker and visible_system_ui_anr(windows) and SYSTEM_UI_ANR_RECOVERY_ATTEMPTS < MAX_SYSTEM_UI_ANR_RECOVERY_ATTEMPTS:
        SYSTEM_UI_ANR_RECOVERY_ATTEMPTS += 1
        write_anr_diagnostics(
            f"{stage}: visible System UI ANR recovery "
            f"{SYSTEM_UI_ANR_RECOVERY_ATTEMPTS}/{MAX_SYSTEM_UI_ANR_RECOVERY_ATTEMPTS}"
        )
        adb(["shell", "input", "keyevent", "4"], timeout=15, check=False)
        time.sleep(5)
        windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
        marker = visible_anr_marker(windows)
        if marker:
            continue

        # A single absent dump was insufficient in run 38131372105: the same
        # System UI dialog reappeared before UIAutomator could read the app tree.
        time.sleep(12)
        windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
        marker = visible_anr_marker(windows)
        if not marker:
            print(
                "System UI ANR dialog cleared and stayed absent through the stability window; "
                "no screenshot is taken unless subsequent checks also remain clear.",
                flush=True,
            )
            return

    if marker and visible_system_ui_anr(windows):
        # The disposable API 30 image repeatedly re-created the same System UI
        # ANR dialog even after BACK cleared it twice. Preserve evidence, restart
        # only the emulator's System UI process, and continue only if the ANR
        # window disappears and remains absent through another stability window.
        write_anr_diagnostics(f"{stage}: restarting unresponsive emulator System UI after bounded BACK recovery")
        pids = adb(["shell", "pidof", "com.android.systemui"], timeout=15, check=False).stdout.split()
        for pid in pids:
            if pid.isdigit():
                adb(["shell", "kill", "-9", pid], timeout=10, check=False)
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            time.sleep(3)
            restarted = adb(["shell", "pidof", "com.android.systemui"], timeout=15, check=False)
            if restarted.returncode == 0 and restarted.stdout.strip():
                break
        else:
            write_anr_diagnostics(f"{stage}: System UI did not restart after bounded recovery")
            raise SystemExit("Emulator System UI did not restart after its visible ANR")

        # The ANR dialog is a system_server-owned alert window even though its
        # title names System UI. Restarting System UI alone does not dismiss it;
        # send BACK after the process returns, then verify a clean stability window.
        time.sleep(5)
        adb(["shell", "input", "keyevent", "4"], timeout=15, check=False)
        time.sleep(5)
        windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
        marker = visible_anr_marker(windows)
        if not marker:
            time.sleep(12)
            windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
            marker = visible_anr_marker(windows)
            if not marker:
                print(
                    "Emulator System UI restarted; ANR window stayed absent through the stability window.",
                    flush=True,
                )
                return

    if marker and visible_system_ui_anr(windows):
        # The alert is system_server-owned even though its title names System UI.
        # If BACK and process restart cannot clear it, use the actual accessible
        # Wait-button bounds rather than a guessed screen coordinate.
        if try_wait_on_system_ui_anr(stage):
            print("Visible System UI ANR cleared through its accessible Wait action.", flush=True)
            return
        windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
        marker = visible_anr_marker(windows)
    if marker:
        write_anr_diagnostics(f"{stage}: unrecovered visible ANR window marker {marker}")
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
    """Validate a required screenshot's PNG signature, IHDR dimensions and byte count."""
    if not image_path.is_file():
        raise SystemExit(f"Required screenshot evidence missing: {image_path}")
    image_bytes = image_path.read_bytes()
    if (len(image_bytes) < 24 or not image_bytes.startswith(bytes((137, 80, 78, 71, 13, 10, 26, 10)))
            or image_bytes[12:16] != b"IHDR"):
        raise SystemExit(f"Required screenshot is not a valid PNG: {image_path}")
    width, height = struct.unpack(">II", image_bytes[16:24])
    if width < minimum_width or height < minimum_height:
        raise SystemExit(f"Required screenshot has implausible dimensions {width}x{height}: {image_path}")
    return {"file": image_path.name, "bytes": len(image_bytes), "width": width, "height": height}


def main() -> None:
    # A cold API 30 emulator can report boot-complete while core phone/System UI
    # services are still under heavy startup load. Recent evidence showed ANRs in
    # com.android.phone and com.android.systemui before any replica-app ANR; allow
    # the emulator to settle before installing and interacting with the app.
    print("Allowing cold-emulator system services to settle for 30 seconds.", flush=True)
    time.sleep(30)
    configure_reference_device_geometry()
    adb(["install", "app/build/outputs/apk/debug/app-debug.apk"], timeout=120)
    adb(["shell", "am", "force-stop", PACKAGE], timeout=15)
    # Suppress Android's one-time immersive-mode confirmation so it cannot
    # cover the first source-screen capture or steal interaction taps.
    adb(["shell", "settings", "put", "secure", "immersive_mode_confirmations", "confirmed"], timeout=10)
    # The Google APIs emulator can surface Digital Wellbeing's own ANR dialog
    # over app screenshots. It is unrelated to this app's behavior; disable
    # that optional system package when present so it cannot invalidate captures.
    adb(["shell", "am", "force-stop", "com.google.android.apps.wellbeing"], timeout=10, check=False)
    adb(["shell", "pm", "disable-user", "--user", "0", "com.google.android.apps.wellbeing"], timeout=10, check=False)
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
    expected_toolbar_titles = {
        "QBank": "QBank Edition 8.5",
        "Tests": "Tests",
        "Videos": "Videos Edition 8.5",
    }
    for label in ("QBank", "Tests", "Videos", "Home"):
        hierarchy = tap_tab(label)
        assert_resource_visibility(hierarchy, "iconBookmark", label == "Home")
        if label == "Home":
            assert_resource_visibility(hierarchy, "textBranding", True)
            assert_resource_visibility(hierarchy, "textPageTitle", False)
        else:
            assert_resource_visibility(hierarchy, "textBranding", False)
            assert_resource_visibility(hierarchy, "textPageTitle", True)
            assert_text(hierarchy, "textPageTitle", expected_toolbar_titles[label])
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

    # Intern Mode OFF/ON state and source-traced tooltip open/Done flow.
    hierarchy = tap_tab("Videos")
    hierarchy = tap_view("switchInternMode")
    assert_switch_checked(hierarchy, "switchInternMode", True)
    assert_text(hierarchy, "tvInternModeStatus", "Intern Mode : ON")
    screenshot("video-switch-on")
    hierarchy = tap_view("switchInternMode")
    assert_switch_checked(hierarchy, "switchInternMode", False)
    assert_text(hierarchy, "tvInternModeStatus", "Intern Mode : OFF")
    screenshot("video-switch-off")
    hierarchy = tap_view("ibTooltip")
    assert_resource_visibility(hierarchy, "tooltipInternModeInfo", True)
    screenshot("video-tooltip-open")
    hierarchy = tap_view("btnInternModeToolTipDone")
    assert_resource_visibility(hierarchy, "tooltipInternModeInfo", False)
    screenshot("video-tooltip-closed")
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
        "video-switch-on", "video-switch-off", "video-tooltip-open",
        "video-tooltip-closed", "video-dark", "home-dark",
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
        "display_geometry": {"size": "1080x2400", "density_dpi": 420, "aspect_ratio": "20:9"},
        "captures": manifest,
    }, indent=2) + "\n", encoding="utf-8")
    print(f"Screenshot interaction QA completed; validated {len(manifest)} required captures and wrote {manifest_path}.", flush=True)


if __name__ == "__main__":
    main()
