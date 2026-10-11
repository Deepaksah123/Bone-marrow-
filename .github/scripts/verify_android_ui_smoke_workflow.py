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
        "single active emulator smoke per ref": r"group:\s*android-ui-smoke-\$\{\{ github\.ref \}\}.*?cancel-in-progress:\s*true",
        "job-level 30-minute ceiling": r"jobs:\s*\n\s+ui-smoke:\s*\n\s+runs-on:.*?\n\s+timeout-minutes:\s*30",
        "bounded 18-minute emulator step": r"name: Launch emulator, verify tab navigation, capture screenshots\s*\n\s+timeout-minutes:\s*18",
        "API 35 emulator image": r"api-level:\s*35",
        "emulator memory for stable System UI": r"emulator-options:.*?-memory\s+4096(?:\s|$)",
        "emulator CPU allocation for stable System UI": r"emulator-options:.*?-cores\s+4(?:\s|$)",
        "pre-emulator evidence directory": "name: Prepare QA evidence directory before emulator startup",
        "run context records invocation state": "emulator_script_invoked=false",
        "smoke stdout retained in artifact": "python3 .github/scripts/run_android_ui_smoke.py > qa-screenshots/smoke-run.log 2>&1",
        "smoke status captured after runner": r"status=[$][?]",
        "smoke exit status propagated": r'exit "\$status"',
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
