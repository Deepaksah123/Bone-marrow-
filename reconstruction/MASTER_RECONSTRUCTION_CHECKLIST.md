# Reconstruction Master Checklist

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Updated:** 2026-10-10  
**Status:** Home + Tests source-derived hierarchy batches build successfully; shell update is being verified; full visual fidelity is incomplete.

## Verified completed

- [x] Original source evidence inventory and binary-layout decode report recorded in `reconstruction/EXACT_SOURCE_UI_INDEX.md` and `reconstruction/VERIFIED_BINARY_LAYOUT_BATCH_3.md`.
- [x] Four top-level tabs and source-backed order recorded: HOME → QBANK → TESTS → VIDEOS.
- [x] Tab destination/root-layout mappings documented in `reconstruction/HOME_TAB_TO_ROOT_LAYOUT_MAP_BATCH_9.md`.
- [x] QBank landing replica has the verified `ConstraintLayout` root and source-bound IDs `rvSubjectList`, `progressLoadList`.
- [x] Test landing replica includes source-bound `test_tab_toolbar`, `loader_empty_layout`, and `loading_layout` containers.
- [x] Video landing replica includes several source-bound view IDs, including `clMain`, `epoxyRVSubject`, and the documented deck/bookmark/sample-video containers.
- [x] Navigation batch commit `7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b` replaces the prior per-tab `replace()` flow with separate tagged tab fragments and add/show/hide behavior: [commit](https://github.com/Deepaksah123/Bone-marrow-/commit/7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b).
- [x] Navigation follow-up commit `1ef4db62408ad188f2a760eda92d5d2b4ba85f45` aligns Home tab fragment tags with the exact original destination class names recorded in `DataBuffer.java`; local wrapper fragment classes are still a reconstruction boundary, not the original fragment implementations.
- [x] Tests layout follow-up commits `871337b330bde3dc132f9c9587be9fe092cab08f`, `9b4b8102686733c4ce44d664bacfc60561b476aa`, and `7f5b27b778e77bdfc6c19ffccb06b1894d1103aa` align the app-bar ID to source-bound `appbarGTa`, repair its constraint references, and add source-bound `collapsing_toolbar`; wrapper class/attributes remain unverified.
- [x] Recovered `base.apk` and `base.apk_Decompiler.com.zip` from the Library in this session; verified SHA-256 values against the original evidence record. The original APK contains `resources.arsc`; the decompiler ZIP still omits that table.
- [x] Added `reconstruction/DECODED_CORE_LAYOUT_HIERARCHY_BATCH_20.md` with decoded IDs and include trees for Home, shell, Tests, QBank and Videos.
- [x] Rebuilt the Tests root hierarchy around source-backed `toolbar`, `tabs`, `parent`, `appbarGTa`, `collapsing_toolbar`, `composeGta`, `emptyLayout`, `loadingContainer`, and `rvMainList`; copied original text-based vector assets and added the Compose UI dependency required by the source ComposeView.
- [x] Replaced generic hand-built Home cards with `fragment_home_replica.xml`, based on the decoded original Home hierarchy. Original source-derived strings/icons are used; account progress and lesson data remain unpopulated.
- [x] Home hierarchy build and evidence guard passed for commit `8bf4caa70cf08324b5f9a990b9a524b7a98edbee`: [build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054999183), [guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054999216). Artifact ID `11670879127`, digest `sha256:b4c12d6cd93b238595002705c60b73fb5d71dcec36f1c1d24c81c146ba793f24`.
- [ ] Shell hierarchy update commits `28059ddbdacc840e44f06c78a14f3b14dde144cc` and `6f491199731a710661bb9e16d2ee8553611ded7a` separate `upperContainer` and `fullContainer`, restore source-bound shell IDs and decode the original menu PNG at runtime. Latest build/guard still needs confirmation.
- [ ] Android build/evidence guard for the latest combined navigation + Tests layout commit `7f5b27b778e77bdfc6c19ffccb06b1894d1103aa` is running; do not treat earlier commit success as validation of this newer layout.
- [x] Android debug build compiled and assembled successfully for navigation commit `7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b`: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38052847889).
- [x] Evidence guard passed for navigation commit `7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b`: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38052847844).
- [x] Debug APK artifact uploaded: `marrow-reconstruction-debug`, artifact ID `11669882167`, SHA-256 digest `f8adf9e46a32741851a59563ed3cb61e192c08e7248257a342c8dab1e773d921` (artifact is available from the build run above).
- [x] Existing app-bar title/header restored in commit `84d79c004840ddcae485ce61c5ba171ce50547ae`; do not remove existing UI merely because a detail is not yet verified.
- [x] Android debug build succeeded for commit `84d79c004840ddcae485ce61c5ba171ce50547ae`: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38029001898).
- [x] Reconstruction evidence guard succeeded for the same commit: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38029001876).
- [x] Ads, subscriptions, upgrades, renewals, payment/checkout and upsell interfaces are explicitly out of scope.
- [x] No invented question banks, subjects, lessons, or user-account progress are populated.

## Remaining work — do not mark complete until verified

- [ ] Decode and resolve the original APK `resources.arsc` to recover authoritative custom-attribute/theme, dimension, color, style and configuration-qualified values. The decompiler ZIP lacks the resource table, but the verified original APK is now available.
- [ ] Complete Home hierarchy fidelity: the main view tree and direct IDs are now source-derived, but included Zen/shimmer subtrees, exact constraints/styles/dimensions and runtime visibility still need original-resource resolution. Keep monetization UI excluded and do not fabricate account progress.
- [ ] Finish the `activity_home_revamp` shell hierarchy: the main container relationship and source IDs are restored, but drawer content, exact header/action sizing, toolbar state, dimensions/styles and original runtime navigation remain incomplete.
- [ ] Compare every implemented screen against the original APK on a device/emulator. Current build success is **not** proof of visual parity.
- [ ] Complete source-to-layout and ID checks for Home, QBank, Tests and Videos; verify each included layout and asset against the original archive.
- [ ] Finish exact navigation fidelity: current implementation uses local wrapper fragment classes and source-shaped add/show/hide transactions; it is not yet proven equivalent to the original obfuscated destination classes, saved state, back-stack, or all transitions.
- [ ] Trace and implement source-backed loading/empty states, back navigation, saved selection, and screen transitions from decompiled source.
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
