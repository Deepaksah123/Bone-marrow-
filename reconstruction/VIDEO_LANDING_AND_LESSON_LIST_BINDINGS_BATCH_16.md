# Video Landing Core Content Binding Map — Batch 16

## Verified root and bound controls

- The VIDEOS home tab's destination class is `setScrollPosition` (Batch 7).
- `sources/kotlin/buildAndPrepareSampleStreamWrappers.java:125–126` inflates `R.layout.fragment_video_landing`.
- The binding constructor/lookup code in `buildAndPrepareSampleStreamWrappers.java:129 onward` resolves the following concrete view IDs:
  - `clMain`
  - `epoxyRVSubject` (EpoxyRecyclerView)
  - `compose_view_deck` (ComposeView)
  - `composeViewAnnouncementBanner` (ComposeView)
  - `clSwitchEdition`
  - `fixedLayoutBookmarkedVideo`
  - `fixedLayoutSampleVideo`
  - `clInternModeBanner`, `btnCloseInternModeBanner`, `bottomNudgeContainer`
- The landing view-model action handler in `sources/kotlin/setScrollPosition.java:2362–2367` opens a lesson player for a selected typed video item, passing its item ID and default playback start/bookmark-origin values. This is the verified core route to retain.

## Video lesson-list layout binding

The separate lesson-list fragment binding is mapped by `sources/kotlin/deriveAudioFormat.java:64–114`, which inflates `R.layout.fragment_video_lesson_list` and binds:
- `emptyStateGroup`
- `indexGroup`, `indexOverlay`
- `ivBack`, `ivEmptyState`, `ivIndex`
- `llIndex`, `llInternModeRibbon`
- `progressLoadList`
- `rvIndex`, `rvVideoList`
- `tabs` (TabLayout)
- `toolbar`
- `tvEmptyState`, `tvIndex`, `tvSubjectTitle`

These are direct view-binding references; the list's full entry path and data ordering are not inferred here.

## Excluded branches

The video landing binding includes intern-mode/announcement/switch-edition and other banner containers. Their presence in the original layout does not authorize reconstructing plan, renewal, upgrade, payment, checkout, upsell, or advertising interfaces. Core lesson browsing/player flow is in scope; excluded monetization surfaces remain out of scope.

## Validation boundary

Static decompiled-source mapping only. No visual equivalence, runtime navigation, Android build, or APK install is claimed. Readiness remains **PARTIAL, NOT RESOLVED**.
