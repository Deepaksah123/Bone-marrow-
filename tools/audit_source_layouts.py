#!/usr/bin/env python3
"""Audit resource/layout references in a decompiler ZIP without guessing screen mappings."""
import argparse
import collections
import hashlib
import json
import pathlib
import re
import zipfile

LAYOUT_RE = re.compile(r'R\.layout\.([A-Za-z0-9_]+)')
ID_RE = re.compile(r'public static final int ([A-Za-z0-9_]+) = (0x[0-9a-fA-F]+);')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decompiler_zip")
    ap.add_argument("--json-out")
    ap.add_argument("--markdown-out")
    args = ap.parse_args()
    archive_path = pathlib.Path(args.decompiler_zip)
    archive_sha = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        name_set = set(names)
        layouts = sorted(
            name for name in names
            if name.startswith("resources/res/layout") and "/" in name and not name.endswith("/")
        )
        source_files = [
            name for name in names
            if name.startswith("sources/") and name.endswith((".java", ".kt"))
        ]
        id_map = {}
        r_java = "sources/com/marrow/R.java"
        if r_java in name_set:
            r_source = archive.read(r_java).decode("utf-8", "replace")
            match = re.search(r'class layout\s*\{(.*?)\n\s*\}', r_source, re.S)
            if match:
                id_map = {name: rid for name, rid in ID_RE.findall(match.group(1))}
        references = collections.defaultdict(list)
        for filename in source_files:
            try:
                lines = archive.read(filename).decode("utf-8", "replace").splitlines()
            except Exception:
                continue
            for line_no, line in enumerate(lines, 1):
                for symbol in LAYOUT_RE.findall(line):
                    references[symbol].append({
                        "file": filename,
                        "line": line_no,
                        "excerpt": line.strip()[:240],
                    })

        def resource_name(entry):
            return pathlib.PurePosixPath(entry).name.removesuffix(".xml").removesuffix(".9")

        layout_names = {resource_name(entry) for entry in layouts}
        report = {
            "archive": archive_path.name,
            "archive_sha256": archive_sha,
            "entry_count": len(names),
            "java_kotlin_source_count": len(source_files),
            "layout_entry_count": len(layouts),
            "distinct_layout_symbols_referenced": len(references),
            "total_layout_reference_sites": sum(map(len, references.values())),
            "resources_arsc_present": "resources.arsc" in name_set,
            "layout_resources": layouts,
            "references": {
                symbol: {
                    "resource_id": id_map.get(symbol),
                    "matching_layout_paths": [
                        entry for entry in layouts if resource_name(entry) == symbol
                    ],
                    "source_sites": sites,
                }
                for symbol, sites in sorted(references.items())
            },
            "unmatched_symbols": sorted(symbol for symbol in references if symbol not in layout_names),
            "layout_files_without_source_symbol": sorted(layout_names - set(references)),
            "methodology": (
                "Literal source references and archive paths only. A match is not proof "
                "of a screen route or complete resource resolution."
            ),
        }
    if args.json_out:
        pathlib.Path(args.json_out).write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n"
        )
    if args.markdown_out:
        out = [
            "# Automated Source-to-Layout Audit", "",
            f"- Archive: `{report['archive']}`",
            f"- SHA-256: `{archive_sha}`",
            f"- Archive entries: **{len(names)}**",
            f"- Java/Kotlin files scanned: **{len(source_files)}**",
            f"- Layout entries: **{len(layouts)}**",
            f"- Distinct `R.layout.*` symbols: **{len(references)}**",
            f"- Literal reference sites: **{sum(map(len, references.values()))}**",
            f"- `resources.arsc` in decompiler ZIP: **{'yes' if report['resources_arsc_present'] else 'no'}**", "",
            "> Static inventory only: a source reference or same-named resource does not prove a screen route.", "",
            "## Resource symbol mapping", "",
            "| Symbol | R.java ID | Matching layout entry | Source sites |",
            "|---|---|---|---:|",
        ]
        for symbol, item in report["references"].items():
            matching = "; ".join("`" + entry + "`" for entry in item["matching_layout_paths"]) or "—"
            out.append(
                f"| `{symbol}` | `{item['resource_id'] or 'unresolved'}` | "
                f"{matching} | {len(item['source_sites'])} |"
            )
        out += ["", "## Unmatched source symbols", ""]
        out += [f"- `{symbol}`" for symbol in report["unmatched_symbols"]] or ["- None"]
        out += ["", "## Interpretation boundary", "", report["methodology"], ""]
        pathlib.Path(args.markdown_out).write_text("\n".join(out))
    print(json.dumps({
        key: report[key] for key in (
            "archive_sha256", "entry_count", "java_kotlin_source_count", "layout_entry_count",
            "distinct_layout_symbols_referenced", "total_layout_reference_sites",
            "resources_arsc_present", "unmatched_symbols",
        )
    }, indent=2))

if __name__ == "__main__":
    main()
