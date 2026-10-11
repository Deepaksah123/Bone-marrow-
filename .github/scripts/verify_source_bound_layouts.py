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
        'android:layout_marginHorizontal="@dimen/margin_6dp"',
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
            "onSurfaceSepia": "@color/sepia85",
            "onTag": "@color/darkGrey",
        }),
        (ROOT / "app/src/main/res/values-night/styles.xml", {
            "colorSurfaceVariant19": "@color/n_80",
            "onSurfaceBgOutline4": "@color/c_988d58",
            "cardViewStrokeWidth": "1dp",
            "onSurfaceSepia": "@color/sepia85",
            "onTag": "@color/darkGrey",
        }),
    ):
        style_text = style_path.read_text(encoding="utf-8")
        for name, value in expected_values.items():
            if f'<item name="{name}">{value}</item>' not in style_text:
                failures.append(f"Home completion chip: {style_path.name} missing {name}={value}")

    # Source-decoded Video switch row, state label, and Tests toolbar padding.
    toolbar_xml = (LAYOUT / "test_tab_toolbar_replica.xml").read_text(encoding="utf-8")
    if 'android:paddingVertical="15dp"' not in toolbar_xml:
        failures.append("Tests toolbar: missing original 15dp vertical padding")
    if 'android:paddingStart="15dp"' in toolbar_xml or 'android:paddingEnd="15dp"' in toolbar_xml:
        failures.append("Tests toolbar: non-source horizontal padding override")
    if 'name="concise_mode"' not in (VALUES / "strings.xml").read_text(encoding="utf-8"):
        failures.append("Videos: missing source concise_mode string resource")
    video_source = (LAYOUT / "fragment_video_landing_replica.xml").read_text(encoding="utf-8")
    for expected in (
        'android:background="?attr/backgroundVariant2"',
        'android:paddingHorizontal="@dimen/margin_16dp"',
        'style="?attr/heading7"',
        'android:paddingVertical="@dimen/pad_normal"',
        'android:layout_width="20dp"',
        'android:layout_height="20dp"',
        'android:padding="4dp"',
        'android:layout_marginEnd="@dimen/margin_10dp"',
        'android:text="@string/new_text"',
        'android:background="@drawable/bg_yellow_rounded_2_corner"',
        'app:backgroundTint="?attr/onSurfaceSepia"',
        'android:text="@string/concise_mode"',
        'app:layout_constraintStart_toEndOf="@id/tvInternModeStatus"',
        'android:background="?attr/onSurfaceBgDivider"',
    ):
        if expected not in video_source:
            failures.append(f"Videos: missing source-derived attribute {expected}")
    banner_header = re.search(r'<TextView\s+android:id="@\+id/tvHeaderInternModeBanner"(?:(?!/>).)*?/>', video_source, re.S)
    if not banner_header or 'style="?attr/heading6"' not in banner_header.group(0) or 'android:textColor="?attr/colorOnSurfaceVariant"' not in banner_header.group(0) or 'android:layout_width="wrap_content"' not in banner_header.group(0):
        failures.append("Videos banner: header style, color, or wrap-content width differs from original")
    if 'app:layout_constraintEnd_toStartOf="@id/btnCloseInternModeBanner"' in (banner_header.group(0) if banner_header else ""):
        failures.append("Videos banner: header has a non-source end constraint")
    if not (ROOT / "app/src/main/res/drawable/bg_yellow_rounded_2_corner.xml").is_file():
        failures.append("Videos banner: missing original NEW badge background drawable")
    colors_xml = (VALUES / "colors.xml").read_text(encoding="utf-8")
    if '<color name="darkGrey">#4a4d4e</color>' not in colors_xml:
        failures.append("Videos banner: missing original darkGrey theme color")
    if '<color name="bg_no_guess">#f5f5f5</color>' not in colors_xml:
        failures.append("Intern Mode: missing original APK bg_no_guess fallback color")
    if '<color name="sepia80">#fce795</color>' not in colors_xml:
        failures.append("Intern Mode: missing original APK sepia80 fallback color")
    main_activity = (ROOT / "app/src/main/java/com/marrow/reconstruction/MainActivity.java").read_text(encoding="utf-8")
    if "enabled ? color(R.color.sepia80) : color(R.color.bg_no_guess)" not in main_activity:
        failures.append("Intern Mode: background fallback colors differ from the original fragment")
    if 'configureInternModeSwitch(root);' not in (ROOT / "app/src/main/java/com/marrow/reconstruction/MainActivity.java").read_text(encoding="utf-8"):
        failures.append("Videos: original Intern Mode OFF/ON visual state binding is missing")

    # Source-decoded layout attributes beyond ID coverage.
    if 'android:fillViewport="true"' in home_xml:
        failures.append("Home: original NestedScrollView does not declare fillViewport=true")
    ed6 = re.search(r'<View\s+android:id="@\+id/ivEd6background"(?:(?!/>).)*?/>', home_xml, re.S)
    if not ed6 or 'android:background="?attr/colorSurfaceVariant14"' not in ed6.group(0):
        failures.append("Home: ED6 background View is missing its original theme background")
    progress = re.search(r'<ProgressBar\s+android:id="@\+id/pbModuleCompletion"(?:(?!/>).)*?/>', home_xml, re.S)
    if not progress or 'android:layout_gravity="center"' not in progress.group(0) or 'android:rotation="90"' not in progress.group(0):
        failures.append("Home: completion ProgressBar is missing original center gravity or 90-degree rotation")
    subtext = re.search(r'<TextView\s+android:id="@\+id/tvModuleCompletionSubText"(?:(?!/>).)*?/>', home_xml, re.S)
    if not subtext or 'android:layout_gravity="center"' not in subtext.group(0) or 'android:gravity="center"' in subtext.group(0):
        failures.append("Home: completion subtitle must use the original layout_gravity, not android:gravity")
    qbank_xml = (LAYOUT / "fragment_qbank_landing_replica.xml").read_text(encoding="utf-8")
    qbank_list = re.search(r'<androidx\.recyclerview\.widget\.RecyclerView\s+android:id="@\+id/rvSubjectList"(?:(?!/>).)*?/>', qbank_xml, re.S)
    if not qbank_list or 'android:clipToPadding=' in qbank_list.group(0):
        failures.append("QBank: remove the non-source clipToPadding override from rvSubjectList")
    elif any(attr in qbank_list.group(0) for attr in ('app:layout_constraintStart_toStartOf=', 'app:layout_constraintEnd_toEndOf=')):
        failures.append("QBank: rvSubjectList has non-source horizontal constraints")
    video_xml = (LAYOUT / "fragment_video_landing_replica.xml").read_text(encoding="utf-8")
    video_progress = re.search(r'<ProgressBar\s+android:id="@\+id/progressBar"(?:(?!/>).)*?/>', video_xml, re.S)
    if not video_progress or 'android:layout_marginEnd="2dp"' not in video_progress.group(0):
        failures.append("Videos: progressBar is missing original 2dp end margin")
    video_scroll = re.search(r'<androidx\.core\.widget\.NestedScrollView\s+android:id="@\+id/rootScrollView"(?:(?!/>).)*?>', video_xml, re.S)
    if not video_scroll or 'android:clipToPadding=' in video_scroll.group(0):
        failures.append("Videos: remove the non-source clipToPadding override from rootScrollView")
    elif 'app:layout_constraintTop_toTopOf="parent"' not in video_scroll.group(0):
        failures.append("Videos: rootScrollView is missing the original top constraint")
    cl_main = re.search(r'<androidx\.constraintlayout\.widget\.ConstraintLayout\s+android:id="@\+id/clMain"(?:(?!>).)*?>', video_xml, re.S)
    if not cl_main or 'android:background=' in cl_main.group(0):
        failures.append("Videos: clMain must not add a non-source explicit background")

    # Source-decoded Tests attributes from the original fragment_home_test binary XML.
    tests_xml = (LAYOUT / "fragment_home_test_replica.xml").read_text(encoding="utf-8")
    tabs = re.search(r'<com\.google\.android\.material\.tabs\.TabLayout\s+android:id="@\+id/tabs"(?:(?!/>).)*?/>', tests_xml, re.S)
    if not tabs:
        failures.append("Tests: cannot locate source-bound TabLayout")
    else:
        for expected in (
            'android:layout_gravity="top"',
            'android:background="?attr/colorSurfaceVariant5"',
            'app:tabMode="fixed"',
            'app:tabGravity="fill"',
            'app:tabIndicatorHeight="5dp"',
            'app:tabIndicatorColor="?android:attr/colorAccent"',
        ):
            if expected not in tabs.group(0):
                failures.append(f"Tests TabLayout: missing original attribute {expected}")
        for unsupported in ('app:layout_constraintStart_toStartOf="parent"', 'app:layout_constraintEnd_toEndOf="parent"'):
            if unsupported in tabs.group(0):
                failures.append(f"Tests TabLayout: non-source constraint {unsupported}")
    rv_tests = re.search(r'<androidx\.recyclerview\.widget\.RecyclerView\s+android:id="@\+id/rvMainList"(?:(?!/>).)*?/>', tests_xml, re.S)
    if not rv_tests or 'android:layout_marginBottom="@dimen/margin_10dp"' not in rv_tests.group(0):
        failures.append("Tests: rvMainList must use original 10dp bottom margin")
    elif 'android:paddingBottom=' in rv_tests.group(0):
        failures.append("Tests: rvMainList has non-source bottom padding instead of bottom margin")
    for include_id, layout_name in (("emptyLayout", "loader_empty_layout_replica"), ("loadingContainer", "loading_layout_replica")):
        include = re.search(rf'<include\s+android:id="@\+id/{include_id}"(?:(?!/>).)*?/>', tests_xml, re.S)
        if not include or f'layout="@layout/{layout_name}"' not in include.group(0):
            failures.append(f"Tests: {include_id} must reference original include layout {layout_name}")
        elif any(attr in include.group(0) for attr in ('android:visibility=', 'android:layout_width=', 'android:layout_height=')):
            failures.append(f"Tests: {include_id} must preserve original include defaults")
    appbar = re.search(r'<com\.google\.android\.material\.appbar\.AppBarLayout\s+android:id="@\+id/appbarGTa"(?:(?!>).)*?>', tests_xml, re.S)
    if not appbar or 'android:paddingTop="4dp"' not in appbar.group(0) or 'android:paddingBottom="6dp"' not in appbar.group(0):
        failures.append("Tests: AppBarLayout is missing original 4dp/6dp vertical padding")
    elif 'app:layout_constraintTop_toTopOf="parent"' not in appbar.group(0):
        failures.append("Tests: AppBarLayout is missing the original top constraint")

    # Toolbar title/branding states are transcribed from the original screenshot reference
    # and asserted again against the live accessibility tree by the emulator smoke test.
    strings_root = ET.parse(VALUES / "strings.xml").getroot()
    string_values = {node.attrib.get("name"): (node.text or "") for node in strings_root.findall("string")}
    title_bindings = {
        "replica_tab_title_qbank_edition_85": "QBank Edition 8.5",
        "replica_tab_title_tests": "Tests",
        "replica_tab_title_videos_edition_85": "Videos Edition 8.5",
    }
    for resource_name, expected_text in title_bindings.items():
        if string_values.get(resource_name) != expected_text:
            failures.append(f"Toolbar title resource {resource_name} must remain {expected_text!r}")
    activity_java = (ROOT / "app/src/main/java/com/marrow/reconstruction/MainActivity.java").read_text(encoding="utf-8")
    for resource_name in title_bindings:
        if f"R.string.{resource_name}" not in activity_java:
            failures.append(f"Toolbar title resource {resource_name} is not bound by MainActivity")
    if "textBranding.setVisibility(View.VISIBLE)" not in activity_java or "textPageTitle.setVisibility(View.GONE)" not in activity_java:
        failures.append("Home toolbar must retain branding and hide the centered page title")

    # Source-backed first-frame loading state must not regress into a visible empty list.
    # The real original adapters/ViewModels are not present, so these placeholders are intentional.
    if 'cards.setVisibility(View.GONE)' not in activity_java or 'shimmer.setVisibility(View.VISIBLE)' not in activity_java:
        failures.append("Home initial state must hide empty rvHomeCard and show shimmerMain")
    if 'subjects.setVisibility(View.GONE)' not in activity_java or 'progress.setVisibility(View.VISIBLE)' not in activity_java:
        failures.append("QBank initial state must hide empty rvSubjectList and show progressLoadList")
    if 'list.setVisibility(View.GONE)' not in activity_java or 'loading.setVisibility(View.VISIBLE)' not in activity_java or 'empty.setVisibility(View.GONE)' not in activity_java:
        failures.append("Tests initial state must hide empty rvMainList/emptyLayout and show loadingContainer")
    if 'isSourceTablet() ? 3 : 2' not in activity_java or 'return false;' not in activity_java[activity_java.find('supportsPredictiveItemAnimations')-100:activity_java.find('supportsPredictiveItemAnimations')+180]:
        failures.append("Videos subject grid must retain source tablet columns and disable predictive animations")
    if 'outRect.top = verticalSpacing;' not in activity_java or 'outRect.left = horizontalSpacing;' not in activity_java:
        failures.append("Videos subject grid must retain source 6dp vertical / 4dp horizontal offsets")

    # Do not present a local-only switch animation as the original Intern Mode state flow.
    intern_method_start = activity_java.find("private void configureInternModeSwitch")
    intern_method_end = activity_java.find("private int resolveThemeColor", intern_method_start)
    intern_method = activity_java[intern_method_start:intern_method_end] if intern_method_start >= 0 and intern_method_end > intern_method_start else ""
    if not intern_method or "modeSwitch.setClickable(false)" not in intern_method or "modeSwitch.setFocusable(false)" not in intern_method:
        failures.append("Intern Mode switch must remain non-actionable until its original state/event flow is traced")
    if "setOnCheckedChangeListener" in intern_method or "updateInternModeVisualState" in activity_java:
        failures.append("Intern Mode must not fake an ON/OFF state transition without the original ViewModel/observer flow")
    if 'modeSwitch.isChecked() ? "ON" : "OFF"' not in intern_method:
        failures.append("Intern Mode status must reflect the source XML's existing checked state without inventing a transition")

    # Source-bound Videos affordances must remain wired to their own verified targets.
    if 'closeInternModeBanner.setOnClickListener' not in activity_java or 'internModeBanner.setVisibility(View.GONE)' not in activity_java:
        failures.append("Videos Intern Mode close action must dismiss clInternModeBanner")
    if 'internModeTooltipTrigger.setOnClickListener' not in activity_java or 'internModeTooltip.setVisibility(View.VISIBLE)' not in activity_java:
        failures.append("Videos tooltip trigger must reveal tooltipInternModeInfo")
    if 'doneInternModeTooltip.setOnClickListener' not in activity_java or 'internModeTooltip.setVisibility(View.GONE)' not in activity_java:
        failures.append("Videos tooltip Done action must dismiss tooltipInternModeInfo")
    if 'R.string.text_concise_tooltip_description' not in activity_java:
        failures.append("Videos tooltip must use the verified default original body string")

    # Emulator QA must publish a complete, validated screenshot manifest rather than
    # relying on a green build or a handful of screenshots from an interrupted run.
    smoke_script = (ROOT / ".github/scripts/run_android_ui_smoke.py").read_text(encoding="utf-8")
    for capture in (
        "home", "qbank", "tests", "videos", "drawer-open", "search-open",
        "videos-intern-mode-unbound", "video-tooltip-open",
        "video-tooltip-closed", "video-dark", "home-dark",
    ):
        if f'"{capture}"' not in smoke_script:
            failures.append(f"Emulator QA: required screenshot capture {capture} is not declared")
    for required_contract in (
        "screenshot-manifest.json",
        "required_capture_count",
        "struct.unpack(\">II\", image_bytes[16:24])",
        "Required screenshot evidence missing",
        "Required screenshot is not a valid PNG",
        "implausible dimensions",
    ):
        if required_contract not in smoke_script:
            failures.append(f"Emulator QA: screenshot evidence validation missing {required_contract}")

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
