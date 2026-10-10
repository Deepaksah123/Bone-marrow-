# Tests Initial Loading State — Batch 47

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Source archive:** checksum-verified `base.apk_Decompiler.com.zip`, SHA-256 recorded in `reconstruction/EXACT_SOURCE_UI_INDEX.md`.

## Source evidence reviewed

- The original landing fragment is `com.marrow2.ui.test.landing.HomeTestFragment`, represented in the decompiler output by `sources/kotlin/WalletConstantsCardNetwork.java`.
- Its recovered Kotlin metadata explicitly lists `showLoading`, `hideLoading`, `showZeroState`, and `hideZeroState` handlers.
- The corresponding original view binding, `sources/kotlin/getNextMediaSequenceAndPartIndex.java`, binds `loadingContainer`, `emptyLayout`, and `rvMainList` from `R.layout.fragment_home_test`.
- `HomeTestViewModel` exposes the test-list UI state and performs initial loading. The replica has no recovered original adapter/ViewModel/data source, so a visible empty RecyclerView would falsely suggest that test content was loaded.

## Implemented

- Retained the source-shaped RecyclerView and its linear layout manager.
- Hid the empty `rvMainList` during the replica's initial state.
- Made the source-provided `loadingContainer` visible and kept `emptyLayout` hidden.
- Added evidence-guard assertions for the three view IDs, layout files, and runtime visibility mapping.
- Did not fabricate test names, grand-test cards, PYQ entries, scores, or account-specific data.

## Explicit limitation

This is a source-backed initial loading presentation, **not** a completed test-data implementation. The loading UI remains visible until the real source-backed data/observer flow is reconstructed. No device-level screenshot or pixel-diff is claimed.

## Validation

**Validated:** Android build [38077629617](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077629617) passed and evidence guard [38077629680](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077629680) passed for code commit `53ce875754dc`. Artifact ID `11679262916`, size `8,194,557` bytes, SHA-256 `3802fc314cb80fc843bde0bd2a76cd451dc958bcdbc12461941306cb9da59b59`. This confirms compile/guard checks only; no device visual QA is claimed.
