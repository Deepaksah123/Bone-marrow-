# Home Completion Widget — Source Attribute Correction (Batch 24)

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Source ZIP:** `base.apk_Decompiler.com.zip`  
**Verified source ZIP SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`  
**Original APK SHA-256:** `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`

## Source-derived corrections

The original binary `resources/res/layout/fragment_home` was parsed directly from the verified archive. The replica's module-completion section had several incorrect geometry/style values; they are now aligned to the decoded source:

- `tvModuleGenerated`: bottom margin uses `@dimen/margin_20dp`, not top margin; the card remains `gone` by default.
- `tvModuleCompletionNumber`: source `heading1` appearance, 70dp × 70dp, autosize 12sp–36sp, centered and uses `?attr/colorOnSurfaceVariant`.
- `pbModuleCompletion`: source `@dimen/module_circular_progress_size` on both axes (90dp), 24dp top margin, progress 100/100, source progress drawable, and bottom constrained to the subtext. It remains `gone` by default.
- `tvModuleCompletionSubText`: source `heading5` appearance, 18sp, 16dp top/bottom margins, centered, and uses `?attr/colorOnSurfaceVariant`.
- Added the `heading1` theme attribute and source-derived 36sp Headline1 style basis in light/dark themes. The original `@font/roboto_medium` file is not yet in the app; the system medium font is a declared approximation.

## Exclusion and validation

- Source GoPro/plan/upsell nodes remain excluded as required; unrelated Home layout elements are preserved.
- No progress number, module count or account state was invented.
- The evidence guard now checks these source-backed geometry values.
- The build/guard result for the latest code must be read from CI; static checks are not a runtime visual comparison.
