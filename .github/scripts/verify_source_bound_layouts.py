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
        "required": """parentFrame bottomNudgeContainer btnCloseInternModeBanner clInternModeBanner clMain clSwitchEdition composeViewAnnouncementBanner compose_view_deck epoxyRVSubject fixedLayoutBookmarkedVideo fixedLayoutSampleVideo fixedLayoutSavedVideo groupInternModeSwitch horizontalScrollView ibTooltip internModeDivider internModeSwitchOverlay ivSortDropDown ivSwitchToEdition layoutBookmarkedVideo layoutContinueWatchingVideoSuggestionCard layoutSampleVideo layoutSavedVideo layoutVideoWatchNextCard llFilledHorizontalView llInternMode llInternModeSwitchView llSubjectHeader progressBar rootScrollView snackbar_container sortOverlay sortType switchInternMode tooltipInternModeInfo tvHeaderInternModeBanner tvInternModeDescription tvInternModeStatus tvInternModeSwitchMsg tvLearnMore tvReportPiracy tvSortByHeader tvSwitchToEditionFlipHeader tvTurnOn""".split(),
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
        required = set(spec["required"])
        missing = sorted(required - found)
        excluded_present = sorted(set(spec["excluded"]) & found)
        unexpected = sorted(found - required - set(spec["excluded"]))
        if missing:
            failures.append(f"{surface}: missing original IDs: {', '.join(missing)}")
        if excluded_present:
            failures.append(f"{surface}: scope-excluded IDs unexpectedly present: {', '.join(excluded_present)}")
        if unexpected:
            failures.append(f"{surface}: IDs absent from original source map: {', '.join(unexpected)}")
        state = "PASS" if not missing and not excluded_present and not unexpected else "FAIL"
        print(f"- {surface}: {len(required & found)}/{len(required)} original IDs; exact set — {state}")
        if missing:
            print(f"    missing: {', '.join(missing)}")
        if excluded_present:
            print(f"    excluded: {', '.join(excluded_present)}")
        if unexpected:
            print(f"    unexpected: {', '.join(unexpected)}")

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

    # Source-decoded Home completion-chip attributes (original fragment_home binary XML).
    home_xml = (LAYOUT / "fragment_home_replica.xml").read_text(encoding="utf-8")
    for expected in (
        'app:cardBackgroundColor="?attr/colorSurfaceVariant19"',
        'app:strokeColor="?attr/onSurfaceBgOutline4"',
        'app:strokeWidth="?attr/cardViewStrokeWidth"',
        'android:paddingHorizontal="19dp"',
        'android:paddingVertical="6dp"',
        'android:layout_marginEnd="@dimen/margin_4dp"',
        'android:layout_marginStart="@dimen/margin_6dp"',
        'style="?attr/subtext2"',
        'android:tint="?attr/onBackgroundSurface3"',
    ):
        if expected not in home_xml:
            failures.append(f"Home completion chip: missing source-derived attribute {expected}")
    attrs_xml = (VALUES / "attrs.xml").read_text(encoding="utf-8")
    for name in ("colorSurfaceVariant19", "onSurfaceBgOutline4", "cardViewStrokeWidth"):
        if f'name="{name}"' not in attrs_xml:
            failures.append(f"Home completion chip: missing theme attribute declaration {name}")
    for style_path, expected_values in (
        (VALUES / "styles.xml", {
            "colorSurfaceVariant19": "@color/sepia05",
            "onSurfaceBgOutline4": "@color/n_00",
            "cardViewStrokeWidth": "0dp",
        }),
        (VALUES / "values-night" / "styles.xml", {
            "colorSurfaceVariant19": "@color/n_80",
            "onSurfaceBgOutline4": "@color/c_988d58",
            "cardViewStrokeWidth": "1dp",
        }),
    ):
        style_text = style_path.read_text(encoding="utf-8")
        for name, value in expected_values.items():
            if f'<item name="{name}">{value}</item>' not in style_text:
                failures.append(f"Home completion chip: {style_path.name} missing {name}={value}")

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
