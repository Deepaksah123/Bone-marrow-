#!/usr/bin/env python3
"""Unit tests for the Android smoke gate's ANR and accessibility parsers."""
from __future__ import annotations

import struct
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
import xml.etree.ElementTree as ET

from run_android_ui_smoke import assert_text, find_node, node_center, tab_is_selected, tap, validate_png_capture, visible_anr_marker, visible_system_ui_anr, wait_button_center


class VisibleAnrMarkerTests(unittest.TestCase):
    def test_hidden_stale_system_ui_anr_is_ignored(self) -> None:
        dump = """
        WINDOW MANAGER WINDOWS
        Window #4 Window{f2c880f u0 Application Not Responding: com.android.systemui}:
          mViewVisibility=0x0
          isVisible=false
          Surface: shown=false layer=0 alpha=0.0
        """
        self.assertIsNone(visible_anr_marker(dump))

    def test_visible_anr_dialog_is_detected(self) -> None:
        dump = """
        WINDOW MANAGER WINDOWS
        Window #4 Window{f2c880f u0 Application Not Responding: com.android.systemui}:
          mViewVisibility=0x0
          isVisible=true
          Surface: shown=true layer=1 alpha=1.0
        """
        self.assertEqual(visible_anr_marker(dump), "application not responding")
        self.assertTrue(visible_system_ui_anr(dump))

    def test_visible_replica_anr_is_not_classified_as_system_ui(self) -> None:
        dump = """
        Window #4 Window{f2c880f u0 Application Not Responding: com.marrow.reconstruction.replica}:
          isVisible=true
          Surface: shown=true layer=1 alpha=1.0
        """
        self.assertIsNotNone(visible_anr_marker(dump))
        self.assertFalse(visible_system_ui_anr(dump))

    def test_hidden_system_ui_anr_is_not_recoverable(self) -> None:
        dump = """
        Window #4 Window{f2c880f u0 Application Not Responding: com.android.systemui}:
          isVisible=false
          Surface: shown=false layer=0 alpha=0.0
        """
        self.assertFalse(visible_system_ui_anr(dump))

    def test_hidden_system_ui_anr_does_not_inherit_other_window_visibility(self) -> None:
        dump = """
        Window #4 Window{f2c880f u0 Application Not Responding: com.android.systemui}:
          isVisible=false
          Surface: shown=false layer=0 alpha=0.0
        Window #5 Window{f2c880f u0 MainActivity}:
          isVisible=true
          Surface: shown=true layer=1 alpha=1.0
        """
        self.assertFalse(visible_system_ui_anr(dump))

    def test_recovery_classifier_requires_system_ui_owner_and_visible_surface(self) -> None:
        hidden_system_ui = """
        Window #4 Window{f2c880f u0 Application Not Responding: com.android.systemui}:
          isVisible=false
          Surface: shown=false layer=0 alpha=0.0
        """
        visible_replica = """
        Window #4 Window{f2c880f u0 Application Not Responding: com.marrow.reconstruction.replica}:
          isVisible=true
          Surface: shown=true layer=1 alpha=1.0
        """
        visible_system_ui = """
        Window #4 Window{f2c880f u0 Application Not Responding: com.android.systemui}:
          isVisible=true
          Surface: shown=true layer=1 alpha=1.0
        """
        self.assertFalse(visible_system_ui_anr(hidden_system_ui))
        self.assertFalse(visible_system_ui_anr(visible_replica))
        self.assertTrue(visible_system_ui_anr(visible_system_ui))

    def test_hidden_anr_does_not_inherit_visibility_from_another_window(self) -> None:
        dump = """
        Window #4 Window{f2c880f u0 Application Not Responding: com.android.systemui}:
          isVisible=false
          Surface: shown=false layer=0 alpha=0.0
        Window #5 Window{f2c880f u0 MainActivity}:
          isVisible=true
          Surface: shown=true layer=1 alpha=1.0
        """
        self.assertIsNone(visible_anr_marker(dump))


    def test_wait_button_uses_real_accessibility_bounds(self) -> None:
        xml = (
            '<hierarchy><node text="Wait" bounds="[600,700][800,780]" visible-to-user="true" />'
            '<node text="Close app" bounds="[300,700][500,780]" visible-to-user="true" /></hierarchy>'
        )
        self.assertEqual(wait_button_center(xml), (700, 740))

    def test_wait_button_is_not_guessed_when_missing_or_hidden(self) -> None:
        self.assertIsNone(wait_button_center('<hierarchy><node text="Close app" bounds="[1,1][2,2]" /></hierarchy>'))
        self.assertIsNone(wait_button_center('<hierarchy><node text="Wait" bounds="[1,1][2,2]" visible-to-user="false" /></hierarchy>'))
        self.assertIsNone(wait_button_center('<hierarchy>not xml</hierarchy>'))


class AccessibilityParserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = ET.fromstring(
            '<hierarchy rotation="0">'
            '<node content-desc="Home" selected="true" bounds="[20,100][120,200]" visible-to-user="true" />'
            '<node content-desc="QBank" selected="false" bounds="[120,100][240,200]" visible-to-user="true" />'
            '<node resource-id="com.marrow.reconstruction.replica:id/switchInternMode" checked="true" bounds="[300,100][400,180]" visible-to-user="true" />'
            '</hierarchy>'
        )

    def test_find_tab_bounds_from_accessibility_node(self) -> None:
        node = find_node(self.root, content_desc="QBank")
        self.assertIsNotNone(node)
        self.assertEqual(node_center(node), (180, 150))

    def test_source_content_description_can_locate_image_without_resource_id(self) -> None:
        root = ET.fromstring(
            '<hierarchy><node content-desc="Search" text="" bounds="[500,100][560,160]" '
            'visible-to-user="true" /></hierarchy>'
        )
        self.assertIsNone(find_node(root, resource_id="iconSearch"))
        node = find_node(root, content_desc="Search")
        self.assertIsNotNone(node)
        self.assertEqual(node_center(node), (530, 130))

    def test_content_description_fallback_requires_clickable_exact_target(self) -> None:
        root = ET.fromstring(
            '<hierarchy>'
            '<node content-desc="Search" clickable="false" bounds="[0,180][1080,264]" />'
            '<node content-desc="Search" clickable="true" bounds="[1000,100][1080,180]" />'
            '</hierarchy>'
        )
        node = find_node(root, content_desc="Search", clickable_only=True)
        self.assertIsNotNone(node)
        self.assertEqual(node_center(node), (1040, 140))

    def test_source_bound_text_assertion_matches_exact_intern_mode_label(self) -> None:
        root = ET.fromstring(
            '<hierarchy><node resource-id="com.marrow.reconstruction.replica:id/tvInternModeStatus" '
            'text="Intern Mode : ON" bounds="[20,100][220,140]" visible-to-user="true" /></hierarchy>'
        )
        assert_text(root, "tvInternModeStatus", "Intern Mode : ON")

    def test_source_bound_text_assertion_rejects_wrong_or_missing_text(self) -> None:
        root = ET.fromstring(
            '<hierarchy><node resource-id="com.marrow.reconstruction.replica:id/tvInternModeStatus" '
            'text="Intern Mode : OFF" bounds="[20,100][220,140]" visible-to-user="true" /></hierarchy>'
        )
        with self.assertRaisesRegex(SystemExit, "Text mismatch"):
            assert_text(root, "tvInternModeStatus", "Intern Mode : ON")
        with self.assertRaisesRegex(SystemExit, "text view not found"):
            assert_text(root, "missingLabel", "Intern Mode : ON")

    def test_selected_tab_state_is_read_from_hierarchy(self) -> None:
        self.assertTrue(tab_is_selected(self.root, "Home"))
        self.assertFalse(tab_is_selected(self.root, "QBank"))

    def test_hidden_nodes_are_not_tap_targets(self) -> None:
        root = ET.fromstring(
            '<hierarchy><node content-desc="Videos" selected="false" '
            'bounds="[10,10][90,90]" visible-to-user="false" /></hierarchy>'
        )
        self.assertIsNone(find_node(root, content_desc="Videos"))


class ScreenshotEvidenceTests(unittest.TestCase):
    @staticmethod
    def fake_png(width: int = 1080, height: int = 1920) -> bytes:
        # Minimal byte sequence sufficient to exercise PNG signature + IHDR parsing.
        return bytes((137, 80, 78, 71, 13, 10, 26, 10)) + bytes(8) + struct.pack(">II", width, height)

    def test_valid_png_manifest_entry_reports_size_and_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "home.png"
            payload = self.fake_png()
            path.write_bytes(payload)
            self.assertEqual(
                validate_png_capture(path),
                {"file": "home.png", "bytes": len(payload), "width": 1080, "height": 1920},
            )

    def test_corrupt_or_non_png_capture_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "qbank.png"
            path.write_bytes(b"not a png image")
            with self.assertRaisesRegex(SystemExit, "not a valid PNG"):
                validate_png_capture(path)

    def test_too_small_capture_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "tests.png"
            path.write_bytes(self.fake_png(160, 240))
            with self.assertRaisesRegex(SystemExit, "implausible dimensions 160x240"):
                validate_png_capture(path)

    def test_missing_capture_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "videos.png"
            with self.assertRaisesRegex(SystemExit, "evidence missing"):
                validate_png_capture(path)



class TapTimeoutTests(unittest.TestCase):
    def test_timed_out_tap_collects_diagnostics_and_is_not_retried(self) -> None:
        with patch(
            "run_android_ui_smoke.adb",
            side_effect=subprocess.TimeoutExpired(cmd=["adb", "shell", "input", "tap"], timeout=30),
        ) as adb_mock, patch("run_android_ui_smoke.write_anr_diagnostics") as diagnostics:
            with self.assertRaisesRegex(SystemExit, "tap was not retried"):
                tap(514, 1720)

        adb_mock.assert_called_once_with(
            ["shell", "input", "tap", "514", "1720"], timeout=30
        )
        diagnostics.assert_called_once_with(
            "ADB input tap timed out at source-derived bounds (514, 1720)"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
