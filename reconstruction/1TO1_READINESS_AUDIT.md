# 1:1 Reconstruction Readiness Audit

Source boundary: `Deepaksah123/Bone-marrow-` only.

## Verified available
- Original APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- Original APK inventory: 5,128 entries
- Excluded interfaces: 51 paths
- Included reconstruction inventory: 5,077 files
- Final batch manifest: 51 batches (50×100 + 77)
- APK-relative path mapping
- Static extraction summary
- Native libraries, fonts, Lottie/CSS/assets inventory

## Blocking gaps for true 1:1 reconstruction
1. The original `base.apk` binary is not stored in this GitHub repository.
2. The 51 local ZIP batch payloads are not stored/transferred in this repository; only their manifest/checksums are recorded.
3. Verified decompiled Java/Kotlin source is not present.
4. Verified Smali output is not present.
5. Decoded `resources.arsc` / complete XML resource source is not present.
6. A complete source-to-screen/behavior mapping is not yet present.

## Scope exclusions
- Educational/content data: intentionally deferred; user will provide it later.
- Advertising UI: excluded.
- Payment/checkout/monetization UI: excluded.

## Rule
Do not fabricate missing source, UI, behavior, or content. Do not import anything from another repository.

## Next unlock
Provide the original `base.apk` or the verified reconstruction batch payloads to this isolated repository/workspace. Then decode resources and DEX, build the source-to-screen map, and proceed with UI reconstruction.
