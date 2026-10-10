# Home Dynamic Zen Area — Exact Asset + Hierarchy Follow-up (Batch 23)

**Repository:** `Deepaksah123/Bone-marrow-` only  
**Verified source archive:** `base.apk_Decompiler.com.zip`  
**Archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`  
**Original APK SHA-256:** `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`

## Exact source assets restored

- `app/src/main/assets/lottie/practical_corner_zen_area_pulse_anim.json` copied from `resources/assets/lottie/practical_corner_zen_area_pulse_anim.json`. Source SHA-256: `7c72ee056690ed4f695e3a7bb656b2fa7d669ff2235ae8a0701485384eb32b93`; Git blob SHA `ba6967e247b6188e92e0fe785c419042f923cec1`; size 3,938 bytes. Source and repo blob SHAs match.
- `app/src/main/res/drawable-mdpi/ic_pc_circle_including_logo.webp` copied from `resources/res/drawable-mdpi/ic_pc_circle_including_logo`. Source SHA-256: `956dc7df0fa49e7065da2a41ae00637f258abc0f15f28707eacf43484ce464e7`; Git blob SHA `e3e0e23d8950b71aeb19988bb27ca9ec9da49879`; size 2,396 bytes. Source and repo blob SHAs match.
- `app/src/main/res/drawable/bg_practical_corner_zen_area_gradient_dark.xml` copied byte-for-byte from the correctly named source drawable. Source SHA-256: `cf93b9ccb0aaf959c173f683f51f94cf80a72ed24c42c385f5b7f8c8ba79d958`.
- The separate `ic_practical_corner_zen_are_pattern.xml` is a 296,606-byte vector in the original archive. A small gradient alias was briefly assigned that name, then removed as soon as the source-path audit revealed the mismatch. The replica currently does **not** reference a substitute for that large vector.
- An earlier rasterized substitute background was removed. The Lottie file was restored and verified against the original source archive by SHA-256; the committed Git blob is identical to the source JSON. Do not reintroduce the raster substitute.

## Source hierarchy cross-check

The binary `resources/res/layout/layout_dynamic_zen_area` establishes this view order:

1. `ConstraintLayout` root `zenContainer`
2. `View` `toolbarPlaceholder`
3. `ImageView` `ivZenAreaBackground`
4. `LinearLayout` `lyt_zen_area_content`
   - `FrameLayout`
     - `ImageView` `logoAnimationBackground`
     - `LottieAnimationView` `logoAnimation`
   - `ConstraintLayout` `lytZenAreaCta`
     - `TextView` `tvPcZenTitle` with source literal `Practicals`
   - sibling `TextView` `tvZenCompletedModules` with source literal `9/35 modules`

The replica has been corrected to keep `tvZenCompletedModules` as a sibling after `lytZenAreaCta` and to use 21dp top padding on the content container, matching the decoded dimension value. The include remains `gone` in `fragment_home_replica.xml`, matching the parent include's default visibility. The static `9/35 modules` is only the layout's default literal; live account progress binding is not implemented.

## Validation status

- The evidence guard passed on commit `962756ca24bf`: [guard run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057133262).
- Android build for the subsequent Zen padding/source asset updates is queued as run [38057164187](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057164187). Do not treat that newer build as passed until it completes.
- No on-device screenshot or pixel-diff verification is claimed.
- Remaining gap: exact compiled XML attributes/styles still need resource-ID resolution against the original APK resource table; this decompiler dump has no `resources.arsc`. Home account/data bindings and click routes remain unimplemented.

## Follow-up — source typography and qualified dimensions

- Restored the source `TextAppearance.Dr.Headline5` style basis (18sp, medium sans-serif, 22sp line height, zero letter spacing) and `TextAppearance.Dr.Body2` basis (14sp, regular sans-serif, 17sp line height) for the completion label, with `heading5`, `bodySmall` and `colorOnSurfaceVariant` theme bindings. The exact original Roboto font file and full theme palette are not yet copied, so font-family and colors remain best-effort rather than a claim of pixel identity.
- Restored `practical_corner_home_banner_content_top_margin` as a dimension resource: 4dp in `values` and 28dp in `values-v35`, matching the decompiler's source values. The layout now references the named dimension rather than hardcoding 4dp.
- Corrected the title's end drawable/tint to the source AppCompat attributes `app:drawableEndCompat` and `app:drawableTint`.
- Latest code commit adds the source `Body2` style and is `5da1cbc59a53`. Evidence guard passed: [run 38057531575](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057531575). Android build passed for latest Zen code commit `5da1cbc59a53`: [run 38057531540](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057531540). Latest debug APK artifact ID `11672053446`, size 8,179,949 bytes, digest `sha256:d6b32d8e40dd64ed150d9f76a002e18c424d89bf0aaafbe571fb7068ce9e15ad`.

## Follow-up — top-margin placement correction

A source-named dimension, `practical_corner_home_banner_content_top_margin`, was previously applied as a uniform margin. Because the resource is explicitly a **top margin**, the Zen content container now uses `android:layout_marginTop` only. The evidence guard now checks this exact attribute, not merely that the dimension name exists. This is a narrow source-fidelity correction; the missing 296,606-byte pattern vector and original font remain unresolved.
