# Reconstruction Master Checklist

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Updated:** 2026-10-10  
**Status:** Buildable debug APK; source reconstruction and visual fidelity are still incomplete.

## Verified completed

- [x] Original source evidence inventory and binary-layout decode report recorded in `reconstruction/EXACT_SOURCE_UI_INDEX.md` and `reconstruction/VERIFIED_BINARY_LAYOUT_BATCH_3.md`.
- [x] Four top-level tabs and source-backed order recorded: HOME → QBANK → TESTS → VIDEOS.
- [x] Tab destination/root-layout mappings documented in `reconstruction/HOME_TAB_TO_ROOT_LAYOUT_MAP_BATCH_9.md`.
- [x] QBank landing replica has the verified `ConstraintLayout` root and source-bound IDs `rvSubjectList`, `progressLoadList`.
- [x] Test landing replica includes source-bound `test_tab_toolbar`, `loader_empty_layout`, and `loading_layout` containers.
- [x] Video landing replica includes several source-bound view IDs, including `clMain`, `epoxyRVSubject`, and the documented deck/bookmark/sample-video containers.
- [x] Existing app-bar title/header restored in commit `84d79c004840ddcae485ce61c5ba171ce50547ae`; do not remove existing UI merely because a detail is not yet verified.
- [x] Android debug build succeeded for commit `84d79c004840ddcae485ce61c5ba171ce50547ae`: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38029001898).
- [x] Reconstruction evidence guard succeeded for the same commit: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38029001876).
- [x] Ads, subscriptions, upgrades, renewals, payment/checkout and upsell interfaces are explicitly out of scope.
- [x] No invented question banks, subjects, lessons, or user-account progress are populated.

## Remaining work — do not mark complete until verified

- [ ] Restore the original APK's complete decoded resources, especially `resources.arsc`, layouts, styles, dimensions, colors, drawables, strings and qualifiers; the current decompiler dump lacks the resource table.
- [ ] Replace the hand-built Home content with a faithful implementation of the original `fragment_home` hierarchy after its actual XML and included layouts are available and traced. Do not invent replacement cards or delete existing UI while investigating.
- [ ] Reconstruct the actual `activity_home_revamp` shell dimensions, header, tab layout, content container, drawer and relevant non-monetization elements from source/resources.
- [ ] Compare every implemented screen against the original APK on a device/emulator. Current build success is **not** proof of visual parity.
- [ ] Complete source-to-layout and ID checks for Home, QBank, Tests and Videos; verify each included layout and asset against the original archive.
- [ ] Trace and implement actual navigation/state behavior, loading/empty states, back navigation, saved selection, and screen transitions from decompiled source.
- [ ] Run build + evidence guard after every implementation batch and inspect the latest artifact.
- [ ] Verify the APK installs and opens on the target Android version/device; record the result and artifact checksum.
- [ ] Update this checklist with commit links and QA evidence after each completed batch.

## Guardrails

1. Only use this repository for implementation: `https://github.com/Deepaksah123/Bone-marrow-`.
2. Original APK resources and decompiled source are the source of truth. Screenshots are QA references, not implementation evidence.
3. Preserve existing UI and functionality unless direct source evidence establishes the correct change. **Unknown means investigate, not delete.**
4. Do not claim 1:1 completion without original-resource comparison and runtime visual QA.
5. Do not fabricate educational content, account data, screen labels, or interactions to fill empty space.
6. Keep excluded monetization and advertising UI out of the reconstruction.
