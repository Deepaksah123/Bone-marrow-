# Main Shell Reconstruction — Batch 22

**Repository:** `Deepaksah123/Bone-marrow-` only  
**Original APK SHA-256:** `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`  
**Decompiler ZIP SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Source-derived shell structure

The launcher shell was adjusted to match the decoded `activity_home_revamp` relationships:

- `FrameLayout` shell root and hidden `screen_blocker`
- `DrawerLayout` → `homeAppBar`
- `lytContent` between the toolbar and divider
  - `upperContainer` for the four tab fragments
  - `popup_notification_container` at the bottom, with non-populated banner hosts
- `toolbar` with source-bound menu, branding, title, bookmark and search IDs
- `thinTopDivider`
- `cvBottomNavigationContainer` → `layoutBottomNavigationContainer` → Material `TabLayout` `bottomNavigation`
- `fullContainer` is a sibling of `lytContent`, not a parent of `upperContainer`
- `drawerMenu` remains an empty include host because the named drawer layout file is absent from the decompiler ZIP; its actual menu rows were not invented

All 22 non-monetization shell IDs recorded in Batch 20 are present. The original Go Pro/plan UI remains excluded. Banner hosts preserve the source ID boundary without inventing banner content.

## Source-derived resources and behavior

- The original menu PNG was extracted from `resources/res/drawable-mdpi/menu` in the verified decompiler ZIP, encoded as a string resource, and decoded into the shell `ImageView` at runtime. This preserves the actual PNG despite the current text-only GitHub file-write path.
- The original selected-tab indicator vector was added as `ic_tab_indicator.xml`, with its color adapted to the replica's existing theme palette.
- Original `Theme.Marrow2` values show `show_home_divider=2` and bottom-nav elevation `8dp` in light mode; `Theme.Marrow2.Dark` shows divider `0` and elevation `0dp`. These values were added as explicit light/night `AppTheme` attributes and bound to the shell XML.
- The source TabLayout's 56dp height, 4dp indicator and 16dp end margin are represented in the replica.
- `upperContainer` and `fullContainer` now remain distinct, as in the decoded source. Main tab navigation still targets `upperContainer`.

## Known gaps

1. The actual `drawer_menu_revamp` resource is referenced in the original shell but absent from the decompiler ZIP. The drawer host is therefore empty, not a fabricated menu.
2. Original custom theme/style definitions are extensive. Only the two shell attributes above were recovered and applied in this batch; other dimensions, typography, colors and state selectors remain partial.
3. The current code does not yet route the menu/search/bookmark actions to reconstructed destinations. Do not add guessed click behavior.
4. The combined shell/Home/Tests/Video code batch passed Android build and evidence guard at commit `2d9b435299fa`: [build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616041), [guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616024). Artifact ID `11671950435`, SHA-256 `f732ff3b05304e31c82db01e3bda0e96a71fd1befb7a69cf8a1608622ab6576f`. No runtime device screenshot QA is claimed.
