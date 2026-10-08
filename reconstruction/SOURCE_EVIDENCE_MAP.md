# Bone-marrow — Source Evidence Map

Generated from the uploaded original APK + decompiler dump in the isolated workspace.

## Source inventory

- APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- APK entries: 5,128
- Decompiled ZIP entries: 26,825
- Java/Kotlin source files: 20,526
- Smali files: 817
- XML files: 2,371
- `com/marrow2` source files: 401
- `com/marrow2/ui` source files: 233

## Verified high-value UI feature areas

- Home: HomeViewModelV2, ZenAreaViewModel and related workers
- QBank: landing, introduction, lesson list, play/MCQ, tracker, score
- Test: landing, introduction, play/MCQ, review, score, analytics, GT analytics
- Video: landing, lesson list, player-related flow, revision, downloaded, notes, sample videos
- Main: navigation/home shared state, deeplink destination, tab layout
- Settings/profile/KYC, bookmark, custom module, pearl, schema, feedback and supporting flows

## Resources

The decompiler contains decoded Android resources, including:
- 578 layout XML files
- 16 landscape layout XML files
- 7 sw600dp layout XML files
- 2,210 drawable files
- 216 color files
- 7 font files
- values/values-night resource XML

This materially improves the 1:1 reconstruction evidence because UI can be traced to original layout/resource definitions rather than screenshots alone.

## Hard reconstruction rules

1. Use only the uploaded original APK/decompiler evidence and the isolated `Deepaksah123/Bone-marrow-` repository.
2. **Zero contamination:** do not import code, assets, content, UI assumptions or implementation from Marrow or any unrelated repository.
3. Screenshots are QA/reference evidence only, never implementation source.
4. Educational/content data is deferred until the UI is 1:1. Do not add placeholder/fabricated educational content.
5. Ads, payment, checkout, subscription and monetization interfaces are excluded from implementation.
6. If evidence does not establish a behavior, mark it unresolved rather than inventing it.

## Current status

The previous blocking gap is now resolved in the working environment: both the original `base.apk` and the complete decompiler ZIP are available.

The GitHub repository still contains the evidence documentation rather than the large binary/source dump itself. The uploaded artifacts are the authoritative reconstruction inputs for this work session.

## Next large batch

1. Generate the source-to-screen map for Home/QBank/Test/Video and navigation/state boundaries.
2. Trace original resource IDs/layouts/themes/dimens/colors/strings to those screens.
3. Build the Android project skeleton in the Bone-marrow repo from that evidence.
4. Implement the first complete UI/navigation batch, not a throwaway prototype.
5. Build and verify; keep an explicit unresolved list for anything not established by the source.
