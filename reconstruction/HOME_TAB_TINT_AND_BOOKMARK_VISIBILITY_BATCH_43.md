# Home Tab Tint and Bookmark Visibility — Batch 43

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Evidence source:** checksum-verified `base.apk_Decompiler.com.zip`, `sources/kotlin/DataBuffer.java` and `sources/kotlin/zabz.java`.

## Source-backed findings

- `DataBuffer.java` defines HOME with the bookmark-visible flag set to `true`; QBANK, TESTS, and VIDEOS use `false`. The same model carries the source tab icons and labels.
- `zabz.java` resolves the selected tab's icon/text tint from `R.attr.colorPrimary` with `R.color.colorPrimary` fallback, and the unselected tint from `R.attr.onBackgroundSurface3` with `R.color.n_40` fallback.
- The replica previously used fixed `mb_50` / `n_40` colors in Java and permanently hid `iconBookmark`. That lost theme-aware selected-state behavior and the Home-only bookmark visibility state.

## Implemented

1. Added a theme-attribute color resolver with the original source fallbacks.
2. Selected tabs now use the theme's `colorPrimary`; unselected tabs use `onBackgroundSurface3`.
3. The bookmark icon is visible on HOME and hidden on QBANK / TESTS / VIDEOS, matching the source tab model.
4. Added evidence-guard assertions for both tint paths and bookmark visibility.

## Explicitly not claimed

The bookmark icon's click destination remains unimplemented in the replica; this batch corrects the source-backed visual state only. No drawer/search routes, account data, question content, or monetization UI was fabricated. Build and evidence-guard outcomes must be checked against the resulting commit before treating this batch as validated.
