#!/usr/bin/env python3
"""Guard the emulator smoke workflow's bounded execution and evidence retention contract."""
from __future__ import annotations
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/android-ui-smoke.yml"

def main() -> int:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    required = {
        "non-destructive concurrency": r"cancel-in-progress:\s*false",
        "job-level 30-minute ceiling": r"jobs:\s*\n\s+ui-smoke:\s*\n\s+runs-on:.*?\n\s+timeout-minutes:\s*30",
        "bounded 18-minute emulator step": r"name: Launch emulator, verify tab navigation, capture screenshots\s*\n\s+timeout-minutes:\s*18",
        "bounded emulator memory": r"emulator-options:.*?-memory\s+2048(?:\s|$)",
        "bounded emulator CPU allocation": r"emulator-options:.*?-cores\s+2(?:\s|$)",
        "pre-emulator evidence directory": "name: Prepare QA evidence directory before emulator startup",
        "run context records invocation state": "emulator_script_invoked=false",
        "unconditional evidence upload": r"name: Upload UI smoke screenshots, interaction captures, and failure diagnostics\s*\n\s+if:\s*always\(\)",
        "missing evidence fails the upload": r"if-no-files-found:\s*error",
        "QA artifact retention": r"retention-days:\s*14",
    }
    failures = [f"Missing workflow contract: {label}" for label, pattern in required.items()
                if not re.search(pattern, workflow, re.MULTILINE | re.DOTALL)]
    if failures:
        print("ANDROID UI SMOKE WORKFLOW CONTRACT: FAIL")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("ANDROID UI SMOKE WORKFLOW CONTRACT: PASS")
    print("Runtime remains unaccepted until the emulator run and its evidence are reviewed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
