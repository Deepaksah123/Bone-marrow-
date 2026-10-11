#!/usr/bin/env python3
"""Check XML integrity and source-traced binding IDs only.

This guard intentionally does not infer pixel parity, runtime behavior, populated data,
or screenshot-derived implementation. Android resource linking and emulator QA are
validated by their own jobs.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LAYOUT = ROOT / "app/src/main/res/layout"

# ID sets recorded from the original decompiler binding/source trace.
# Excluded monetization IDs are kept explicit so they cannot silently reappear.
SURFACES = {
    "Home": ("fragment_home_replica.xml",
        "barrier clMainInfo ed8Zen footerGroup groupEd6Views heartMarrow ivEd6background layoutDynamicZenArea llShare nestedScrollView pbModuleCompletion rvHomeCard shimmerMain tvModuleCompletionNumber tvModuleCompletionSubText tvModuleGenerated zenAreaContainer".split(),
        "cvGoPro goProEd5Ed6 shimmerGoPro spacePro tvGoPro".split()),
    "QBank": ("fragment_qbank_landing_replica.xml",
        "progressLoadList rvSubjectList".split(), []),
    "Tests": ("fragment_home_test_replica.xml",
        "appbarGTa collapsing_toolbar composeGta emptyLayout loadingContainer parent rvMainList tabs toolbar".split(), []),
    "Videos": ("fragment_video_landing_replica.xml",
        "parentFrame bottomNudgeContainer btnCloseInternModeBanner clInternModeBanner clMain clSwitchEdition composeViewAnnouncementBanner compose_view_deck epoxyRVSubject fixedLayoutBookmarkedVideo fixedLayoutSampleVideo fixedLayoutSavedVideo groupInternModeSwitch horizontalScrollView ibTooltip internModeDivider internModeSwitchOverlay ivSortDropDown ivSwitchToEdition layoutBookmarkedVideo layoutContinueWatchingVideoSuggestionCard layoutSampleVideo layoutSavedVideo layoutVideoWatchNextCard llFilledHorizontalView llInternMode llInternModeSwitchView llSubjectHeader progressBar rootScrollView snackbar_container sortOverlay sortType switchInternMode tooltipInternModeInfo tvHeaderInternModeBanner tvInternModeDescription tvInternModeStatus tvInternModeSwitchMsg tvLearnMore tvReportPiracy tvSortByHeader tvSwitchToEditionFlipHeader tvTurnOn".split(), []),
    "Shell": ("activity_main.xml",
        "bottomNavigation collegeYearUpdateBanner cvBottomNavigationContainer drawerLayout drawerMenu fullContainer homeAppBar iconBookmark iconMenu iconSearch kycUploadBanner layoutBottomNavigationContainer lytContent popup_notification_container renewPlanBanner screen_blocker textBranding textBrandingContainer textPageTitle thinTopDivider toolbar upperContainer".split(),
        "proCard tvGoPro".split()),
    "Bottom tab item": ("item_home_tab.xml", "icon indicator title".split(), []),
    "Intern Mode tooltip": ("tooltip_intern_mode_info_replica.xml",
        "tooltipInternModeInfo btnInternModeToolTipDone cardInternModeTooltip container ivTooltip tvLearnMore txtToolTipBody".split(),
        "tvInternModeTooltipTitle btnCloseInternModeTooltip tvInternModeTooltipDescription".split()),
}

def main() -> int:
    failures: list[str] = []
    print("Original-source layout ID validation:")
    for surface, (filename, expected_ids, excluded_ids) in SURFACES.items():
        path = LAYOUT / filename
        if not path.is_file():
            failures.append(f"{surface}: missing layout file {path.relative_to(ROOT)}")
            continue
        try:
            xml = path.read_text(encoding="utf-8")
            ET.fromstring(xml)
        except (OSError, ET.ParseError) as exc:
            failures.append(f"{surface}: invalid or unreadable XML: {exc}")
            continue
        actual = set(re.findall(r"@\+id/([A-Za-z0-9_]+)", xml))
        expected = set(expected_ids)
        excluded = set(excluded_ids)
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected - excluded)
        present_excluded = sorted(actual & excluded)
        if missing:
            failures.append(f"{surface}: missing traced IDs: {', '.join(missing)}")
        if unexpected:
            failures.append(f"{surface}: IDs absent from the source trace: {', '.join(unexpected)}")
        if present_excluded:
            failures.append(f"{surface}: excluded monetization IDs present: {', '.join(present_excluded)}")
        print(f"- {surface}: {len(expected & actual)}/{len(expected)} traced IDs")
    if not (ROOT / "reconstruction/EXACT_SOURCE_UI_INDEX.md").is_file():
        failures.append("Missing original-source trace record")

    # The original toolbar title is configuration-bound, not screenshot-derived.
    # Guard against reintroducing the static values removed in source-fidelity Batch 63.
    strings_path = ROOT / "app/src/main/res/values/strings.xml"
    activity_path = ROOT / "app/src/main/java/com/marrow/reconstruction/MainActivity.java"
    try:
        strings_xml = strings_path.read_text(encoding="utf-8")
        activity_java = activity_path.read_text(encoding="utf-8")
        forbidden_title_tokens = (
            "replica_tab_title_qbank_edition_85",
            "replica_tab_title_tests",
            "replica_tab_title_videos_edition_85",
        )
        for token in forbidden_title_tokens:
            if token in strings_xml or token in activity_java:
                failures.append(f"Screenshot-derived toolbar title token reintroduced: {token}")
        if '<string name="app_name">Marrow</string>' not in strings_xml:
            failures.append("App label must match the verified original string: Marrow")
        if 'textPageTitle.setText("");' not in activity_java:
            failures.append("Unbound toolbar title must remain empty until original config binding is integrated")
        original_dex_tags = (
            "Home_o.makeGooglePlayServicesAvailable",
            "Home_o.ResidentKeyRequirementUnsupportedResidentKeyRequirementException",
            "Home_o.WalletConstantsCardNetwork",
            "Home_o.setScrollPosition",
        )
        for tag in original_dex_tags:
            if tag not in activity_java:
                failures.append(f"Missing raw-DEX source destination tag: {tag}")
        if "Home_kotlin." in activity_java:
            failures.append("Decompiler package aliases must not be used as runtime Fragment tags")
        # The original Intern Mode interaction requires its ViewModel/state pipeline.
        # Until those dependencies are source-integrated, never permit a cosmetic local toggle.
        intern_switch_layout = ROOT / "app/src/main/res/layout/fragment_video_landing_replica.xml"
        try:
            video_xml = intern_switch_layout.read_text(encoding="utf-8")
            if 'modeSwitch.setClickable(false);' not in activity_java:
                failures.append("Intern Mode switch must remain non-clickable until original ViewModel integration")
            if 'modeSwitch.setFocusable(false);' not in activity_java:
                failures.append("Intern Mode switch must remain non-focusable until original ViewModel integration")
            if "VideoLandingViewModel" not in video_xml and "switchInternMode" not in video_xml:
                failures.append("Intern Mode source-bound switch ID missing from Videos layout")
        except OSError as exc:
            failures.append(f"Could not validate deferred Intern Mode interaction: {exc}")
    except OSError as exc:
        failures.append(f"Could not validate source-bound toolbar strings: {exc}")
    if failures:
        print("SOURCE-BOUND LAYOUT CHECK: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("SOURCE-BOUND LAYOUT CHECK: PASS")
    print("This checks XML and traced IDs only; it does not certify 1:1 UI parity.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
