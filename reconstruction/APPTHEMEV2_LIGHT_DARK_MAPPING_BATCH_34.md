# AppThemeV2 Light/Dark Theme Mapping — Batch 34

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.

## Source theme mappings restored

- Light `AppTheme` values map the source background/surface palette, primary blue, links, dividers, outline colors, headings, and subtitle styles.
- Night `AppTheme` maps the same semantic attributes to source dark-mode neutral/blue/green values instead of relying on a hand-authored generic dark palette.
- The project now defines the custom theme attributes used by the restored source layouts, including `backgroundColor`, `backgroundVariant2`, `colorSurfaceVariant*`, `onBackgroundSurface*`, `onSurfaceBlue*`, `onSurfaceBg*`, `heading*`, `subtext*` and `smallText2`.
- Theme typography styles used by source XML include Headline1/4/5/6, Body2, SmallText2, Subtitle1 and Subtitle2. Fonts are system sans equivalents because original font files have not yet been restored.
- The horizontal video download progress style is present and references the source progress drawable.

## Scope

This maps semantic theme attributes to the recorded source palette; it does not prove every configuration-qualified value in the original `resources.arsc` is resolved. Color/font resource audits and runtime light/dark screenshot comparison remain open. Monetization surfaces stay excluded.

## Validation

Light theme Android build passed: [run 38074564411](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074564411). Attribute/theme declaration guard passed on [run 38074567890](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074567890). Dark theme Android build also passed: [run 38074568348](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074568348), debug APK artifact ID `11677648227`, size `8,195,477` bytes, digest `sha256:731fef107ec8d86bd51611272684921ec3486c39e1e32e3def74edbba58f1ac2`.
