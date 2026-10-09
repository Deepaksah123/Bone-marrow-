import json
import pathlib
import subprocess
import sys
import tempfile
import unittest
import zipfile

SCRIPT = pathlib.Path(__file__).with_name("audit_source_layouts.py")

class SourceLayoutAuditTests(unittest.TestCase):
    def make_archive(self, root):
        archive = root / "fixture.zip"
        with zipfile.ZipFile(archive, "w") as z:
            z.writestr(
                "sources/com/marrow/R.java",
                "public final class R { public static final class layout { "
                "public static final int fragment_home = 0x7f0d00d9; "
                "public static final int activity_missing = 0x7f0d0051; } }",
            )
            z.writestr(
                "sources/com/marrow/Home.java",
                "class Home { int layout = R.layout.fragment_home; }\n"
                "class Home2 { int layout = R.layout.activity_missing; }",
            )
            z.writestr("resources/res/layout/fragment_home", "compiled layout placeholder")
            z.writestr("resources/res/layout-land/fragment_home", "landscape layout placeholder")
        return archive

    def test_counts_references_and_unmatched_symbol(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            archive = self.make_archive(root)
            output_json = root / "audit.json"
            output_md = root / "audit.md"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(archive),
                 "--json-out", str(output_json), "--markdown-out", str(output_md)],
                check=True, capture_output=True, text=True,
            )
            data = json.loads(output_json.read_text())
            self.assertEqual(data["entry_count"], 4)
            self.assertEqual(data["java_kotlin_source_count"], 2)
            self.assertEqual(data["layout_entry_count"], 2)
            self.assertEqual(data["distinct_layout_symbols_referenced"], 2)
            self.assertEqual(data["total_layout_reference_sites"], 2)
            self.assertEqual(data["references"]["fragment_home"]["resource_id"], "0x7f0d00d9")
            self.assertEqual(data["unmatched_symbols"], ["activity_missing"])
            self.assertIn("Static inventory only", output_md.read_text())
            self.assertIn("archive_sha256", result.stdout)

    def test_json_only_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            archive = self.make_archive(root)
            output_json = root / "audit.json"
            subprocess.run(
                [sys.executable, str(SCRIPT), str(archive), "--json-out", str(output_json)],
                check=True, capture_output=True, text=True,
            )
            self.assertTrue(output_json.exists())
            self.assertEqual(json.loads(output_json.read_text())["total_layout_reference_sites"], 2)

if __name__ == "__main__":
    unittest.main()
