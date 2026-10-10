# Original APK Resource Table Resolution — Batch 31

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Original APK:** `base.apk` SHA-256 `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`  
**Decompiler archive:** SHA-256 `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Source table recovered

The original APK's `resources.arsc` is present (3,327,896 bytes). A local read-only pass over the table identified package `com.marrow`, 22 resource types, 373 type/config chunks and 39,097 parsed entries. The decompiler archive also contains the readable `resources/res/values/colors.xml`, `dimens.xml`, `attrs.xml`, and `styles.xml`; the original resource table was used to verify resource IDs/aliases and theme configuration. The source XML and binary table agree on the values below.

## Verified source values

| Resource | Original value |
|---|---|
| `n_00` | `#FFFFFF` |
| `n_05` | `#F5F5F5` |
| `n_10` | `#E5E6E6` |
| `n_15` | `#D7D9DA` |
| `n_20` | `#CACDCD` |
| `n_40` | `#959A9B` |
| `n_50` | `#7B8182` |
| `n_60` | `#626768` |
| `n_70` | `#4A4D4E` |
| `n_70_a_30` | `#4D4A4D4E` |
| `n_70_a_50` | `#804A4D4E` |
| `n_80` | `#313434` |
| `n_85` | `#252727` |
| `mb_50` | `#62C8DF` |
| `mb_90` | `#16343B` |
| `tGreen` | `#1F4851` |
| `c_7eaaff` | `#7EAAFF` |
| `cloudy_blue` | `#D8E4E6` |
| `shimmer_background` | `#DDDDDD` |

Original dimensions independently confirmed: `tab_height=48dp`, `home_test_toolbar_horizontal_margin=24dp`, `pad_8dp=8dp`, `pad_14=14dp`, `margin_40=40dp`, `module_circular_progress_size=90dp`, `suggested_card_width=150dp`, `suggested_card_image_height=120dp`, `text_primary=16sp`.

## Theme mapping corrections

The original `AppThemeV2` / `AppThemeV2.Dark` table maps:
- Light `backgroundColor → n_05`, `backgroundVariant2 → mb_90`, `colorOnBackground → n_60`, `colorSurfaceVariant5 → mb_50`.
- Dark `backgroundColor → n_85`, `backgroundVariant2 → tGreen`, `colorOnBackground → n_10`, `colorSurfaceVariant5 → n_80`.
- Light `onSurfaceBgLinks → links`; dark `onSurfaceBgLinks → c_7eaaff`.
- Light `onSurfaceBgOutline2 → white`; dark `onSurfaceBgOutline2 → n_70_a_50`.
- `Headline1=36sp/43sp line-height`, `Headline4=20sp/24sp`, `Headline5=18sp/22sp`, `Headline6=16sp/19sp`, `Subtitle1=12sp/14sp`, `Subtitle2=12sp/14sp`. Source fonts are `roboto_medium`, `roboto_bold`, and `roboto_regular` respectively; current app uses Android system equivalents because the original font binaries have not yet been transferred into the target repository.

The target light/dark theme now maps `colorOnSurface`, `colorOnPrimary`, `colorPrimaryVariant`, `colorSurfaceVariant14/6`, `onBackgroundSurface1/2/3/4/5/6/7`, `onBackgroundVariant2`, `onSurfaceBgDivider`, `onSurfaceBgLinks`, `onSurfaceBgOutline/2/3`, and `onSurfaceBlue/2/3` to source resource values. In particular, light `onSurfaceBgOutline2` is `white`; dark `onSurfaceBgOutline2` is `n_70_a_50`; dark `onSurfaceBgLinks` is `c_7eaaff`. The source-specific palette tokens were added and the evidence guard now verifies representative mappings. Android build passed for the complete color/theme code batch at commit `c42441806516`: [run 38074568348](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074568348). Artifact ID `11677648227`, size `8,195,477` bytes, digest `sha256:731fef107ec8d86bd51611272684921ec3486c39e1e32e3def74edbba58f1ac2`. The latest evidence guard passed [run 38074590738](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074590738).

## Important boundary

The original application manifest's application-level theme resolves to `AppTheme`; individual activities may override this with `AppThemeV2` or other variants. Do not assume every screen uses one global theme. The table is decoded, but per-activity/theme-overlay selection still requires resolving the source activity and its runtime path.

## Validation

Evidence guard now checks the corrected dark-theme values. Android build and guard results must be read from the latest CI runs; static resource-table resolution is not on-device visual QA. No 1:1 claim is made.
