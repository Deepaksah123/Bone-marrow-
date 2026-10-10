# Core Screen Binary-XML Hierarchy Recovery — Batch 20

**Repository boundary:** `Deepaksah123/Bone-marrow-` only  
**Original APK SHA-256:** `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`  
**Decompiler ZIP SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

The original APK and decompiler ZIP were recovered from the user's Library in this work session and their hashes verified. This batch parses the binary Android XML layout chunks in the decompiler ZIP. It records view classes, IDs and included-layout references; it does not claim full ARSC/theme resolution or runtime visual parity.

## Exact core layout roots, IDs and includes

### `fragment_home` — `ConstraintLayout`, 22 IDs

IDs in the decoded layout:
`tvModuleGenerated`, `nestedScrollView`, `zenAreaContainer`, `ivEd6background`, `tvModuleCompletionNumber`, `pbModuleCompletion`, `tvModuleCompletionSubText`, `cvGoPro`, `tvGoPro`, `shimmerGoPro`, `spacePro`, `barrier`, `goProEd5Ed6`, `groupEd6Views`, `layoutDynamicZenArea`, `ed8Zen`, `clMainInfo`, `rvHomeCard`, `llShare`, `heartMarrow`, `footerGroup`, `shimmerMain`.

Included layouts:
- `layout_dynamic_zen_area`
- `layout_home_cards_shimmer_m2`
- `layout_home_lesson_shimmer_m2` × 6
- `layout_home_lesson_shimmer` × 6

Hierarchy summary:
- Root ConstraintLayout
- Module-generated MaterialCardView
- NestedScrollView → ConstraintLayout → Zen-area ConstraintLayout
- Zen area contains completion views, a GoPro/plan-related group, dynamic Zen include and ComposeView
- `clMainInfo` contains `rvHomeCard`, share/footer views and shimmer skeleton includes

**Exclusion handling:** original GoPro/plan/upsell elements are evidence in the source, not permission to reproduce excluded monetization UI. Keep those excluded while preserving unrelated home hierarchy.

### `activity_home_revamp` — `FrameLayout`, 24 IDs

IDs:
`screen_blocker`, `drawerLayout`, `homeAppBar`, `lytContent`, `upperContainer`, `popup_notification_container`, `renewPlanBanner`, `collegeYearUpdateBanner`, `kycUploadBanner`, `toolbar`, `iconMenu`, `textBrandingContainer`, `textBranding`, `proCard`, `tvGoPro`, `textPageTitle`, `iconBookmark`, `iconSearch`, `thinTopDivider`, `cvBottomNavigationContainer`, `layoutBottomNavigationContainer`, `bottomNavigation`, `fullContainer`, `drawerMenu`.

Included layouts:
- `banner_renew_plan` — excluded monetization
- `banner_update_college_year_revamp` — preserve only if it is not an excluded monetization surface and source behavior is in scope
- `banner_kyc_verify_revamp` — authentication/KYC scope must follow the existing exclusion policy
- `drawer_menu_revamp`

Verified structure includes a DrawerLayout, home app-bar/content containers, toolbar, TabLayout, fullContainer and drawer include. The top-level tab host uses `upperContainer`; do not replace this with an unrelated container.

### `fragment_home_test` — `ConstraintLayout`, 9 IDs

IDs:
`toolbar`, `tabs`, `parent`, `appbarGTa`, `collapsing_toolbar`, `composeGta`, `emptyLayout`, `loadingContainer`, `rvMainList`.

Included layouts:
- `test_tab_toolbar`
- `loader_empty_layout`
- `loading_layout`

Hierarchy:
- Root ConstraintLayout
- Toolbar include
- Separate TabLayout (`tabs`)
- CoordinatorLayout (`parent`)
  - AppBarLayout (`appbarGTa`)
    - CollapsingToolbarLayout (`collapsing_toolbar`)
      - LinearLayoutCompat
        - ComposeView (`composeGta`)
  - Empty-state include (`emptyLayout`)
  - Loading include (`loadingContainer`)
  - RecyclerView (`rvMainList`)

The reconstruction now uses these verified IDs and the same major view-class hierarchy. Some styles, dimensions, scroll attributes and included custom-view implementation remain provisional.

### `fragment_qbank_landing` — `ConstraintLayout`, 2 IDs

IDs: `rvSubjectList`, `progressLoadList`.  
No included layouts. These IDs are bound directly by the decompiled source.

### `fragment_video_landing` — `FrameLayout`, 44 IDs

IDs:
`parentFrame`, `progressBar`, `bottomNudgeContainer`, `snackbar_container`, `layoutContinueWatchingVideoSuggestionCard`, `rootScrollView`, `clMain`, `composeViewAnnouncementBanner`, `clSwitchEdition`, `tvSwitchToEditionFlipHeader`, `ivSwitchToEdition`, `llInternMode`, `tvInternModeStatus`, `ibTooltip`, `switchInternMode`, `internModeDivider`, `clInternModeBanner`, `tvHeaderInternModeBanner`, `btnCloseInternModeBanner`, `tvInternModeDescription`, `tvTurnOn`, `tvLearnMore`, `horizontalScrollView`, `layoutSavedVideo`, `layoutBookmarkedVideo`, `layoutSampleVideo`, `llFilledHorizontalView`, `fixedLayoutSavedVideo`, `fixedLayoutBookmarkedVideo`, `fixedLayoutSampleVideo`, `compose_view_deck`, `layoutVideoWatchNextCard`, `llSubjectHeader`, `tvSortByHeader`, `sortType`, `ivSortDropDown`, `epoxyRVSubject`, `tvReportPiracy`, `sortOverlay`, `groupInternModeSwitch`, `internModeSwitchOverlay`, `llInternModeSwitchView`, `tvInternModeSwitchMsg`, `tooltipInternModeInfo`.

Included layouts:
- `layout_continue_watching_video_suggestion_card`
- `horizontal_item_video_landing_scrollable_components` × 3
- `horizontal_item_video_landing_components` × 3
- `layout_video_watch_next_card`
- `tooltip_intern_mode_info`

The video replica remains partial; it must not populate invented lessons or restore excluded upsell/advertising UI.

## CI evidence for current implementation batch

- Navigation + Tests hierarchy source batch commit: `7f5b27b778e77bdfc6c19ffccb06b1894d1103aa`
- Android debug build: [run 38054408121](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054408121)
- Evidence guard: [run 38054408113](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054408113)
- Artifact ID: `11670573616`
- Artifact digest: `sha256:ff45647c76169445aa6f3946ea155e58ce9ff9c2985c13a6064cdb6c9bd4a0dc`

The newer Tests hierarchy/resource batch is being built separately. Do not treat the earlier artifact as containing that newer batch.

## Next implementation gate

1. Resolve resource IDs against the original APK's `resources.arsc` for dimensions, styles, custom attributes, strings and drawables.
2. Reconstruct Home from the decoded hierarchy, not from the current generic card layout; preserve only the user-authorized exclusions.
3. Finish Videos' 44-ID hierarchy and included-layout cross-reference.
4. Rebuild after the latest source/layout commit, then perform device-level visual QA. Build success alone is not 1:1 validation.

## Implementation follow-up — Home dynamic Zen area (Batch 23)

The decoded `layout_dynamic_zen_area` include is now a separate `layout_dynamic_zen_area_replica.xml` resource with the original root/include identity (`zenContainer` overridden by include ID `layoutDynamicZenArea`) and source-bound child IDs: `toolbarPlaceholder`, `ivZenAreaBackground`, `lyt_zen_area_content`, `logoAnimationBackground`, `logoAnimation`, `lytZenAreaCta`, `tvPcZenTitle`, and `tvZenCompletedModules`.

The Home include remains `gone` by default, matching the original `fragment_home` include visibility. The title uses the original source text `Practicals`; the completion count is intentionally empty because `9/35 modules` in the source XML is placeholder/account-progress content and must not be shown without the original data flow.

Remaining source asset gaps: `ic_practical_corner_zen_are_pattern` is a 296 KB vector and `ic_pc_circle_including_logo` is a binary WebP in the original archive; the current text-only GitHub write workflow cannot add those binaries as native resource files. They are not substituted with invented artwork. The original Lottie JSON and large background vector have not been reproduced. Unverified substitute animation/background files were removed; the Lottie view remains hidden until the exact original assets can be recovered.
