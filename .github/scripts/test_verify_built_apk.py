#!/usr/bin/env python3
"""Regression tests for APK package construction verification."""
from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from verify_built_apk import EXPECTED_PACKAGE, EXPECTED_LAUNCHER, REQUIRED_LAYOUTS, inspect_apk


class BuiltApkVerificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.apk = self.root / "app-debug.apk"
        self.aapt = self.root / "aapt"
        self.aapt.write_text(chr(10).join([
            "#!/usr/bin/env python3",
            "print(\"package: name='com.marrow.reconstruction.replica' versionCode='1'\")",
            "print(\"launchable-activity: name='com.marrow.reconstruction.MainActivity'\")",
            "",
        ]), encoding="utf-8")
        self.aapt.chmod(0o755)
        self.make_apk()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def make_apk(self, *, omit_layout: str | None = None) -> None:
        with zipfile.ZipFile(self.apk, "w") as archive:
            archive.writestr("AndroidManifest.xml", b"compiled manifest fixture")
            archive.writestr("classes.dex", b"dex fixture")
            archive.writestr("resources.arsc", b"resource table fixture")
            for layout in REQUIRED_LAYOUTS:
                if layout != omit_layout:
                    archive.writestr(f"res/layout/{layout}.xml", b"compiled layout fixture")

    def test_accepts_well_formed_package_and_emits_non_parity_receipt(self) -> None:
        receipt = inspect_apk(self.apk, self.aapt)
        self.assertEqual(receipt["application_id"], EXPECTED_PACKAGE)
        self.assertEqual(receipt["launcher_activity"], EXPECTED_LAUNCHER)
        self.assertEqual(receipt["zip_integrity"], "PASS")
        self.assertEqual(receipt["ui_parity"], "NOT_ASSERTED")
        self.assertEqual(len(receipt["sha256"]), 64)

    def test_missing_required_layout_fails_closed(self) -> None:
        self.make_apk(omit_layout="fragment_home_replica")
        with self.assertRaisesRegex(SystemExit, "fragment_home_replica"):
            inspect_apk(self.apk, self.aapt)

    def test_corrupt_apk_fails_closed(self) -> None:
        self.apk.write_bytes(b"not an APK")
        with self.assertRaisesRegex(SystemExit, "not a readable ZIP/APK"):
            inspect_apk(self.apk, self.aapt)

    def test_missing_apk_fails_closed(self) -> None:
        self.apk.unlink()
        with self.assertRaisesRegex(SystemExit, "missing or empty"):
            inspect_apk(self.apk, self.aapt)


if __name__ == "__main__":
    unittest.main()
