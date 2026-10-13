#!/usr/bin/env python3
"""Fail-closed checks for the APK produced by the reconstruction build.

This validates package construction only. It does not claim original UI parity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

EXPECTED_PACKAGE = "com.marrow.reconstruction.replica"
EXPECTED_LAUNCHER = "com.marrow.reconstruction.MainActivity"
REQUIRED_LAYOUTS = {
    "activity_main",
    "fragment_home_replica",
    "fragment_qbank_landing_replica",
    "fragment_home_test_replica",
    "fragment_video_landing_replica",
    "layout_dynamic_zen_area_replica",
    "item_home_tab",
    "tooltip_intern_mode_info_replica",
}


def inspect_apk(apk_path: Path, aapt_path: Path, apksigner_path: Path) -> dict[str, object]:
    if not apk_path.is_file() or apk_path.stat().st_size == 0:
        raise SystemExit(f"Built APK is missing or empty: {apk_path}")

    try:
        with zipfile.ZipFile(apk_path) as archive:
            names = set(archive.namelist())
            bad_entries = archive.testzip()
    except (OSError, zipfile.BadZipFile) as exc:
        raise SystemExit(f"Built APK is not a readable ZIP/APK: {apk_path}: {exc}") from exc

    if bad_entries is not None:
        raise SystemExit(f"Built APK contains a corrupt ZIP entry: {bad_entries}")
    required_entries = {"AndroidManifest.xml", "classes.dex", "resources.arsc"}
    missing_entries = sorted(required_entries - names)
    if missing_entries:
        raise SystemExit("Built APK is missing required entries: " + ", ".join(missing_entries))

    packaged_layouts = {
        Path(name).stem for name in names
        if re.fullmatch(r"res/layout(?:-[^/]+)?/[^/]+\.xml", name)
    }
    missing_layouts = sorted(REQUIRED_LAYOUTS - packaged_layouts)
    if missing_layouts:
        raise SystemExit("Built APK is missing required compiled layout resources: " + ", ".join(missing_layouts))

    try:
        result = subprocess.run(
            [str(aapt_path), "dump", "badging", str(apk_path)],
            check=True, capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise SystemExit(f"Unable to inspect built APK manifest with aapt: {exc}") from exc

    package_match = re.search(r"^package: name='([^']+)'", result.stdout, re.MULTILINE)
    launch_match = re.search(r"^launchable-activity: name='([^']+)'", result.stdout, re.MULTILINE)
    if package_match is None or package_match.group(1) != EXPECTED_PACKAGE:
        found = package_match.group(1) if package_match else "unresolved"
        raise SystemExit(f"Unexpected APK applicationId: {found}; expected {EXPECTED_PACKAGE}")
    if launch_match is None or launch_match.group(1) != EXPECTED_LAUNCHER:
        found = launch_match.group(1) if launch_match else "unresolved"
        raise SystemExit(f"Unexpected APK launcher: {found}; expected {EXPECTED_LAUNCHER}")

    try:
        signature = subprocess.run(
            [str(apksigner_path), "verify", "--verbose", str(apk_path)],
            check=True, capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        detail = getattr(exc, "stderr", None)
        raise SystemExit(f"APK signature verification failed: {detail or exc}") from exc

    digest = hashlib.sha256(apk_path.read_bytes()).hexdigest()
    return {
        "apk": apk_path.name,
        "bytes": apk_path.stat().st_size,
        "sha256": digest,
        "application_id": package_match.group(1),
        "launcher_activity": launch_match.group(1),
        "required_layouts": sorted(REQUIRED_LAYOUTS),
        "compiled_layout_count": len(packaged_layouts),
        "zip_integrity": "PASS",
        "signature_verification": "PASS",
        "signature_details": signature.stdout.strip(),
        "ui_parity": "NOT_ASSERTED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apk", type=Path)
    parser.add_argument("--aapt", required=True, type=Path)
    parser.add_argument("--apksigner", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="Optional JSON receipt path.")
    args = parser.parse_args()
    receipt = inspect_apk(args.apk, args.aapt, args.apksigner)
    rendered = json.dumps(receipt, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
