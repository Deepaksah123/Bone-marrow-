# Reconstruction Master Checklist

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Updated:** 2026-10-10  
**Status:** Home, Tests, Video-root and shell hierarchy batches compile and pass the evidence guard; included subtrees, runtime behavior and visual parity remain incomplete.

## Verified completed

- [x] Original source evidence inventory and binary-layout decode report recorded in `reconstruction/EXACT_SOURCE_UI_INDEX.md` and `reconstruction/VERIFIED_BINARY_LAYOUT_BATCH_3.md`.
- [x] Evidence guard now verifies SHA-256 for the exact source Lottie JSON, mdpi logo WebP and dark Zen gradient, checks the layout references and source-qualified 4dp/28dp dimensions, and fails if the incorrect pattern-gradient substitute is reintroduced.
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
- [x] Home dynamic Zen include now references the exact source Lottie JSON, mdpi circle-logo WebP and source gradient XML; the completion label's sibling position, 21dp top padding, and source-qualified 4dp / API 35 28dp margin were corrected from the binary layout. The distinct 296,606-byte pattern vector remains a documented transfer gap and is not replaced with another image. Full asset hashes and limitations are recorded in [Batch 23](HOME_DYNAMIC_ZEN_EXACT_ASSET_BATCH_23.md). A temporary unverified raster substitute was removed before finalizing source assets.
- [x] The previous code build at `ed1d2c860f38` passed: [run 38057383849](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057383849), artifact ID `11671933327` (8,180,745 bytes; digest `sha256:071fb864cfda06ecd2cd11bb22e82497f55aa44c0fcfeebcacb283fe2d18acf6`). The latest Body2 style update is commit `5da1cbc59a53`; its evidence guard passed [run 38057531575](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057531575) and Android build passed [run 38057531540](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057531540). Latest debug APK artifact ID `11672053446`, size 8,179,949 bytes, digest `sha256:d6b32d8e40dd64ed150d9f76a002e18c424d89bf0aaafbe571fb7068ce9e15ad`. The Zen top-margin dimension is now applied with `android:layout_marginTop` and the guard checks that exact attribute. Layout commit `3d8bc391738c` build passed: [run 38071524241](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38071524241). Evidence guard passed for the top-margin correction [run 38071531370](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38071531370) and checklist follow-up [run 38071542304](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38071542304). The 296,606-byte original pattern vector and original font file remain explicit transfer gaps; no substitute pattern artwork is used.
- [x] Home hierarchy build and evidence guard passed for commit `8bf4caa70cf08324b5f9a990b9a524b7a98edbee`: [build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054999183), [guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054999216). Artifact ID `11670879127`, digest `sha256:b4c12d6cd93b238595002705c60b73fb5d71dcec36f1c1d24c81c146ba793f24`.
- [x] Shell hierarchy commits `28059ddbdacc840e44f06c78a14f3b14dde144cc` and `6f491199731a710661bb9e16d2ee8553611ded7a` separate `upperContainer` and `fullContainer`, restore source-bound shell IDs and render the original menu PNG at runtime. The selected-tab indicator and light/dark divider/elevation attributes are also source-derived.
- [x] Video landing root rebuilt from decoded source with **44/44 source-bound IDs**; uses `EpoxyRecyclerView`, responsive 2-column phone / 3-column tablet grid, original source-derived labels/icons, and empty hosts instead of invented lessons: [Video batch report](VIDEO_LANDING_ROOT_RECONSTRUCTION_BATCH_21.md).
- [x] Shell source hierarchy and theme behavior recorded in [Batch 22 report](SHELL_ROOT_RECONSTRUCTION_BATCH_22.md); shell ID coverage is 22/22 non-monetization IDs. Drawer menu content remains unimplemented because its source layout file is absent from the decompiler ZIP.
- [x] Latest combined Home/Tests/Video/shell code build succeeded for commit `2d9b435299fa`: [Android build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616041), [evidence guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616024).
- [x] Latest debug APK artifact uploaded: `marrow-reconstruction-debug`, artifact ID `11671950435`, SHA-256 `f732ff3b05304e31c82db01e3bda0e96a71fd1befb7a69cf8a1608622ab6576f`.
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
- [x] Root ID coverage audit completed: Home non-monetization IDs 17/17, QBank 2/2, Tests 9/9, Videos 44/44, shell 22/22 non-monetization IDs.
- [ ] Complete included-layout subtree, attribute, drawable and configuration-qualifier audits against the original archive.
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
