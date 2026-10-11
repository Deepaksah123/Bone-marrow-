#!/usr/bin/env python3
"""Unit tests for the Android smoke gate's ANR and accessibility parsers."""
from __future__ import annotations

import unittest
import xml.etree.ElementTree as ET

from run_android_ui_smoke import find_node, node_center, tab_is_selected, visible_anr_marker, visible_system_ui_anr


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

    def test_selected_tab_state_is_read_from_hierarchy(self) -> None:
        self.assertTrue(tab_is_selected(self.root, "Home"))
        self.assertFalse(tab_is_selected(self.root, "QBank"))

    def test_hidden_nodes_are_not_tap_targets(self) -> None:
        root = ET.fromstring(
            '<hierarchy><node content-desc="Videos" selected="false" '
            'bounds="[10,10][90,90]" visible-to-user="false" /></hierarchy>'
        )
        self.assertIsNone(find_node(root, content_desc="Videos"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
