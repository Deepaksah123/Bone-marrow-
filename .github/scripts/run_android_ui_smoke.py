#!/usr/bin/env python3
"""Source-bound Android UI smoke checks with verified accessibility targeting."""
from __future__ import annotations

import re
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path

PACKAGE = "com.marrow.reconstruction.replica"
ACTIVITY = f"{PACKAGE}/com.marrow.reconstruction.MainActivity"
OUT = Path("qa-screenshots")
OUT.mkdir(parents=True, exist_ok=True)
SYSTEM_UI_ANR_RECOVERY_USED = False


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


def visible_system_ui_anr(window_dump: str) -> bool:
    """Identify a visible ANR owned by System UI, not by the replica app."""
    blocks = re.split(r"(?=window #\\d+\\s)", window_dump.lower())
    indicators = ("application not responding", "isn't responding", "is not responding", "anrdialog")
    return any(
        any(marker in block for marker in indicators)
        and "com.android.systemui" in block
        and "isvisible=true" in block
        and "surface: shown=true" in block
        for block in blocks
    )


def assert_no_anr_dialog(stage: str) -> None:
    # Never capture while any ANR dialog is visible. On this cold-boot emulator,
    # System UI can transiently ANR during first app install/startup; preserve its
    # diagnostics, dismiss that one system-owned dialog once, then re-check that
    # the window is actually gone. App ANRs and repeat System UI ANRs remain fatal.
    global SYSTEM_UI_ANR_RECOVERY_USED
    windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
    marker = visible_anr_marker(windows)
    if not marker:
        return

    if visible_system_ui_anr(windows) and not SYSTEM_UI_ANR_RECOVERY_USED:
        write_anr_diagnostics(f"{stage}: transient visible System UI ANR; diagnostics captured before recovery")
        SYSTEM_UI_ANR_RECOVERY_USED = True
        adb(["shell", "input", "keyevent", "4"], timeout=15, check=False)
        time.sleep(5)
        windows = adb(["shell", "dumpsys", "window", "windows"], timeout=30).stdout
        marker = visible_anr_marker(windows)
        if not marker:
            print(
                "Transient System UI ANR dialog dismissed after diagnostics; "
                "continuing only after verifying its window is no longer visible.",
                flush=True,
            )
            return

    write_anr_diagnostics(f"{stage}: visible ANR window marker {marker}")
    raise SystemExit(f"Visible emulator ANR dialog detected {stage}: {marker}")


def find_node(root: ET.Element, *, resource_id: str | None = None,
              content_desc: str | None = None) -> ET.Element | None:
    for node in root.iter("node"):
        attrs = node.attrib
        if attrs.get("visible-to-user", "true").lower() == "false":
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


def tap_view(resource_id: str) -> ET.Element:
    root = read_hierarchy()
    node = find_node(root, resource_id=resource_id)
    if node is None:
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


def assert_switch_checked(root: ET.Element, resource_id: str, expected: bool) -> None:
    node = find_node(root, resource_id=resource_id)
    if node is None:
        raise SystemExit(f"Visible source-bound switch not found: {resource_id}")
    actual = node.attrib.get("checked", "").lower() == "true"
    if actual != expected:
        raise SystemExit(f"Switch state mismatch for {resource_id}: expected checked={expected}, got {node.attrib.get('checked')!r}")


def tap(x: int, y: int) -> None:
    adb(["shell", "input", "tap", str(x), str(y)], timeout=10)


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


def main() -> None:
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
    screenshot("home")
    for label in ("QBank", "Tests", "Videos", "Home"):
        hierarchy = tap_tab(label)
        time.sleep(1)
        ensure_app()
        screenshot(label.lower())

    # Drawer and Better Search actions use live source-bound view bounds.
    tap_view("iconMenu")
    screenshot("drawer-open")
    back()

    tap_view("iconSearch")
    screenshot("search-open")
    back()
    ensure_app()

    # Intern Mode OFF/ON state and source-traced tooltip open/Done flow.
    hierarchy = tap_tab("Videos")
    hierarchy = tap_view("switchInternMode")
    assert_switch_checked(hierarchy, "switchInternMode", True)
    screenshot("video-switch-on")
    hierarchy = tap_view("switchInternMode")
    assert_switch_checked(hierarchy, "switchInternMode", False)
    screenshot("video-switch-off")
    tap_view("ibTooltip")
    screenshot("video-tooltip-open")
    tap_view("btnInternModeToolTipDone")
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
    print("Screenshot interaction QA completed.", flush=True)


if __name__ == "__main__":
    main()
