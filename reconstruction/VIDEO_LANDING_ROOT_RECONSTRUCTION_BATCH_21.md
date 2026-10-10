# Video Landing Root Reconstruction — Batch 21

**Repository:** `Deepaksah123/Bone-marrow-`  
**Source APK SHA-256:** `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`  
**Decompiler ZIP SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Source hierarchy implemented

The replica now follows the decoded `fragment_video_landing` root hierarchy:

- `FrameLayout` → `parentFrame`
- Loading `ProgressBar` → `progressBar`
- Bottom overlay `ConstraintLayout` → `bottomNudgeContainer`
  - `CoordinatorLayout` → `snackbar_container`
  - continue-watching component host → `layoutContinueWatchingVideoSuggestionCard`
- `NestedScrollView` → `rootScrollView`
  - `ConstraintLayout` → `clMain`
  - Compose announcement host → `composeViewAnnouncementBanner`
  - edition switch container and children
  - intern-mode container and children
  - intern-mode banner and children
  - horizontal/fixed saved, bookmarked and sample-video component hosts
  - Compose deck host
  - watch-next component host
  - subject header and sort controls
  - `EpoxyRecyclerView` → `epoxyRVSubject`
  - report-piracy label
  - sort/intern-mode overlays and loading-message group

## ID coverage audit

The original binary layout contains **44 IDs**. The current replica XML contains all **44/44 source-bound IDs**, with no missing or additional IDs among that verified set:

`parentFrame`, `progressBar`, `bottomNudgeContainer`, `snackbar_container`, `layoutContinueWatchingVideoSuggestionCard`, `rootScrollView`, `clMain`, `composeViewAnnouncementBanner`, `clSwitchEdition`, `tvSwitchToEditionFlipHeader`, `ivSwitchToEdition`, `llInternMode`, `tvInternModeStatus`, `ibTooltip`, `switchInternMode`, `internModeDivider`, `clInternModeBanner`, `tvHeaderInternModeBanner`, `btnCloseInternModeBanner`, `tvInternModeDescription`, `tvTurnOn`, `tvLearnMore`, `horizontalScrollView`, `layoutSavedVideo`, `layoutBookmarkedVideo`, `layoutSampleVideo`, `llFilledHorizontalView`, `fixedLayoutSavedVideo`, `fixedLayoutBookmarkedVideo`, `fixedLayoutSampleVideo`, `compose_view_deck`, `layoutVideoWatchNextCard`, `llSubjectHeader`, `tvSortByHeader`, `sortType`, `ivSortDropDown`, `epoxyRVSubject`, `tvReportPiracy`, `sortOverlay`, `groupInternModeSwitch`, `internModeSwitchOverlay`, `llInternModeSwitchView`, `tvInternModeSwitchMsg`, `tooltipInternModeInfo`.

## Source-backed behavior applied

- Decompiled `VideoLandingFragment` configures a `GridLayoutManager` with 2 columns on phones and 3 on tablets; the replica now uses a responsive 2/3-column grid.
- `EpoxyRecyclerView` is used instead of a generic RecyclerView; Epoxy dependency was added because this exact class is present in the original source.
- Original source-based labels and icon vectors were added for the subject header, sort label, report-piracy label, info icon, close icon and sort arrow.
- No subjects, lessons, saved videos, bookmarks, watch-next items, or account data were fabricated. Content-dependent included components are currently empty hosts and several are hidden until their source subtrees/data flow are reconstructed.

## Remaining gaps

1. The 44-ID/root hierarchy audit does not prove pixel-level parity. Exact constraints, dimensions, custom theme attributes, colors and included component subtrees still need resource-table resolution.
2. Empty hosts for the continue-watching card, saved/bookmarked/sample cards, watch-next card and tooltip are deliberate non-fabrication gates; they are not claimed to be final UI.
3. Switch, sort, piracy-report and player navigation interactions must be implemented from direct source routes; do not attach guessed click behavior.
4. The combined Home/Tests/Video/shell code batch passed Android build and evidence guard at commit `2d9b435299fa`: [build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616041), [guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616024). The uploaded APK artifact is `11671950435` with SHA-256 `f732ff3b05304e31c82db01e3bda0e96a71fd1befb7a69cf8a1608622ab6576f`. This validates compilation, not runtime visual parity.
