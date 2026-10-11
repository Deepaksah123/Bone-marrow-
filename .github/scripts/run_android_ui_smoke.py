#!/usr/bin/env python3
"""Screenshot-based Android UI smoke test; avoids flaky UIAutomator hierarchy dumps."""
from __future__ import annotations

import re
import subprocess
import time
from pathlib import Path

PACKAGE = "com.marrow.reconstruction.replica"
ACTIVITY = f"{PACKAGE}/com.marrow.reconstruction.MainActivity"
OUT = Path("qa-screenshots")
OUT.mkdir(parents=True, exist_ok=True)


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
            chunks.append(f"\\n===== {label} (rc={result.returncode}) =====\\n{result.stdout}")
        except Exception as exc:
            chunks.append(f"\\n===== {label}: collection failed: {exc} =====\\n")
    (OUT / "anr-diagnostics.txt").write_text("\\n".join(chunks), encoding="utf-8")


def assert_no_anr_dialog(stage: str) -> None:
    # A live app PID is not enough: any Android process can put an ANR dialog
    # over the app while taps still return successfully. Inspect both window
    # and activity state and reject all such captures, not only System UI ANRs.
    windows = adb(["shell", "dumpsys", "window", "windows"], timeout=20).stdout.lower()
    activities = adb(["shell", "dumpsys", "activity", "activities"], timeout=20).stdout.lower()
    window_indicators = (
        "application not responding",
        "isn't responding",
        "is not responding",
        "anrdialog",
    )
    activity_indicators = (
        "application not responding",
        "anr dialog",
        "anrdialog",
    )
    found = next((marker for marker in window_indicators if marker in windows), None)
    if found:
        write_anr_diagnostics(f"{stage}: window marker {found}")
        raise SystemExit(f"Emulator ANR dialog detected {stage}: {found}")
    found = next((marker for marker in activity_indicators if marker in activities), None)
    if found:
        write_anr_diagnostics(f"{stage}: activity marker {found}")
        raise SystemExit(f"Emulator ANR activity detected {stage}: {found}")


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
    time.sleep(2)

    size_text = adb(["shell", "wm", "size"], timeout=10).stdout
    density_text = adb(["shell", "wm", "density"], timeout=10).stdout
    size_match = re.search(r"(\d+)x(\d+)", size_text)
    density_match = re.search(r"(\d+)", density_text)
    if not size_match or not density_match:
        raise SystemExit(f"Could not resolve emulator geometry: {size_text!r}; {density_text!r}")
    width, height = map(int, size_match.groups())
    scale = int(density_match.group(1)) / 160.0
    toolbar_y = round(52 * scale)
    nav_bar_height = round(24 * scale)
    tab_y = height - nav_bar_height - round(28 * scale)
    tab_x = [round(width * (i + 0.5) / 4) for i in range(4)]

    screenshot("home")
    for name, index in (("qbank", 0), ("tests", 1), ("videos", 2), ("home", 3)):
        tap(tab_x[index], tab_y)
        time.sleep(2)
        ensure_app()
        screenshot(name)

    # Drawer and Better Search toolbar actions.
    tap(round(24 * scale), toolbar_y)
    time.sleep(1)
    screenshot("drawer-open")
    back()

    tap(width - round(24 * scale), toolbar_y)
    time.sleep(1)
    screenshot("search-open")
    back()
    ensure_app()

    # Intern Mode OFF/ON state and the source-traced tooltip open/Done flow.
    tap(tab_x[2], tab_y)
    time.sleep(2)
    switch_x = width - round(40 * scale)
    row_y = round(104 * scale)
    tap(switch_x, row_y)
    time.sleep(1)
    screenshot("video-switch-on")
    tap(switch_x, row_y)
    time.sleep(1)
    screenshot("video-switch-off")
    tap(round(140 * scale), row_y)
    time.sleep(1)
    screenshot("video-tooltip-open")
    tap(round(292 * scale), round(400 * scale))
    time.sleep(1)
    screenshot("video-tooltip-closed")
    ensure_app()

    # Light/dark theme captures.
    adb(["shell", "cmd", "uimode", "night", "yes"], timeout=20)
    time.sleep(2)
    screenshot("video-dark")
    tap(tab_x[3], tab_y)
    time.sleep(2)
    screenshot("home-dark")
    adb(["shell", "cmd", "uimode", "night", "no"], timeout=20)
    time.sleep(1)
    ensure_app()
    print("Screenshot interaction QA completed.", flush=True)


if __name__ == "__main__":
    main()
