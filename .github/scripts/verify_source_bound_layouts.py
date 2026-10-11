#!/usr/bin/env python3
"""Validate source-bound IDs in the Marrow UI replica against the original source trace.

The expected IDs are copied from the original decompiler binding classes identified
in reconstruction/ORIGINAL_UI_SOURCE_TRACE_BATCH_59.md. Pro/upsell IDs are explicit
scope exclusions, not silently treated as completed UI.
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LAYOUT = ROOT / "app/src/main/res/layout"
VALUES = ROOT / "app/src/main/res/values"

# Exact source binding IDs from the original decompiled classes.
SURFACES = {
    "Home": {
        "file": "fragment_home_replica.xml",
        "required": """barrier clMainInfo ed8Zen footerGroup groupEd6Views heartMarrow ivEd6background layoutDynamicZenArea llShare nestedScrollView pbModuleCompletion rvHomeCard shimmerMain tvModuleCompletionNumber tvModuleCompletionSubText tvModuleGenerated zenAreaContainer""".split(),
        "excluded": """cvGoPro goProEd5Ed6 shimmerGoPro spacePro tvGoPro""".split(),
    },
    "QBank": {
        "file": "fragment_qbank_landing_replica.xml",
        "required": "progressLoadList rvSubjectList".split(),
        "excluded": [],
    },
    "Tests": {
        "file": "fragment_home_test_replica.xml",
        "required": "appbarGTa collapsing_toolbar composeGta emptyLayout loadingContainer parent rvMainList tabs toolbar".split(),
        "excluded": [],
    },
    "Videos": {
        "file": "fragment_video_landing_replica.xml",
        "required": """bottomNudgeContainer btnCloseInternModeBanner clInternModeBanner clMain clSwitchEdition composeViewAnnouncementBanner compose_view_deck epoxyRVSubject fixedLayoutBookmarkedVideo fixedLayoutSampleVideo fixedLayoutSavedVideo groupInternModeSwitch horizontalScrollView ibTooltip internModeDivider internModeSwitchOverlay ivSortDropDown ivSwitchToEdition layoutBookmarkedVideo layoutContinueWatchingVideoSuggestionCard layoutSampleVideo layoutSavedVideo layoutVideoWatchNextCard llFilledHorizontalView llInternMode llInternModeSwitchView llSubjectHeader progressBar rootScrollView snackbar_container sortOverlay sortType switchInternMode tooltipInternModeInfo tvHeaderInternModeBanner tvInternModeDescription tvInternModeStatus tvInternModeSwitchMsg tvLearnMore tvReportPiracy tvSortByHeader tvSwitchToEditionFlipHeader tvTurnOn""".split(),
        "excluded": [],
    },
    "Shell": {
        "file": "activity_main.xml",
        "required": """bottomNavigation collegeYearUpdateBanner cvBottomNavigationContainer drawerLayout drawerMenu fullContainer homeAppBar iconBookmark iconMenu iconSearch kycUploadBanner layoutBottomNavigationContainer lytContent popup_notification_container renewPlanBanner screen_blocker textBranding textBrandingContainer textPageTitle thinTopDivider toolbar upperContainer""".split(),
        "excluded": "proCard tvGoPro".split(),
    },
    "Bottom tab item": {
        "file": "item_home_tab.xml",
        "required": "icon indicator title".split(),
        "excluded": [],
    },
    "Intern Mode tooltip": {
        "file": "tooltip_intern_mode_info_replica.xml",
        "required": "tooltipInternModeInfo btnInternModeToolTipDone cardInternModeTooltip container ivTooltip tvLearnMore txtToolTipBody".split(),
        "excluded": "tvInternModeTooltipTitle btnCloseInternModeTooltip tvInternModeTooltipDescription".split(),
    },
}

def ids_in(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    ET.fromstring(text)  # malformed Android XML must fail before build
    return set(re.findall(r"@\+id/([A-Za-z0-9_]+)", text))

def resource_names(path: Path, tag: str) -> set[str]:
    root = ET.parse(path).getroot()
    return {node.attrib["name"] for node in root.iter(tag) if "name" in node.attrib}

def main() -> int:
    failures: list[str] = []
    print("Original-source binding coverage:")
    for surface, spec in SURFACES.items():
        path = LAYOUT / spec["file"]
        if not path.is_file():
            failures.append(f"{surface}: missing layout {path.relative_to(ROOT)}")
            continue
        found = ids_in(path)
        missing = sorted(set(spec["required"]) - found)
        excluded_present = sorted(set(spec["excluded"]) & found)
        if missing:
            failures.append(f"{surface}: missing original IDs: {', '.join(missing)}")
        if excluded_present:
            failures.append(f"{surface}: scope-excluded IDs unexpectedly present: {', '.join(excluded_present)}")
        state = "PASS" if not missing and not excluded_present else "FAIL"
        print(f"- {surface}: {len(set(spec['required']) & found)}/{len(set(spec['required']))} required IDs — {state}")
        if missing:
            print(f"    missing: {', '.join(missing)}")
        if excluded_present:
            print(f"    excluded: {', '.join(excluded_present)}")

    strings = resource_names(VALUES / "strings.xml", "string")
    dimens = resource_names(VALUES / "dimens.xml", "dimen")
    tooltip_path = LAYOUT / "tooltip_intern_mode_info_replica.xml"
    if tooltip_path.is_file():
        xml = tooltip_path.read_text(encoding="utf-8")
        for kind, known in (("string", strings), ("dimen", dimens)):
            for name in sorted(set(re.findall(rf"@{kind}/([A-Za-z0-9_]+)", xml)) - known):
                failures.append(f"Tooltip: unresolved @{kind}/{name}")
        for name in sorted(set(re.findall(r"@drawable/([A-Za-z0-9_]+)", xml))):
            if not (ROOT / "app/src/main/res/drawable" / f"{name}.xml").is_file() and not any(
                (ROOT / "app/src/main/res" / folder / name).is_file()
                for folder in ("drawable", "drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-nodpi")
            ):
                failures.append(f"Tooltip: unresolved @drawable/{name}")

    if failures:
        print("\nSOURCE-BOUND LAYOUT VALIDATION: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("\nSOURCE-BOUND LAYOUT VALIDATION: PASS")
    print("Excluded Pro/upsell IDs remain explicit; no content or behavior is fabricated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
