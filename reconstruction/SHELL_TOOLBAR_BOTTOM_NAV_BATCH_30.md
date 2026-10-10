# Main Shell Toolbar + Bottom Navigation — Source Geometry Batch 30

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Corrected from original `activity_home_revamp`

- Shell and upper content backgrounds now use the source theme `backgroundColor`; the toolbar uses `colorSurfaceVariant5` (light blue surface / dark neutral surface).
- Toolbar height uses `wrap_content` plus source `?attr/actionBarSize` minimum height. Menu icon uses `actionBarSize` width/height, 16dp padding and source `colorOnSurfaceVariant` tint.
- Branding now uses the source Headline5 theme style and 16dp start spacing; page title uses Headline4 and is centered across the toolbar, matching the source constraints.
- Search and bookmark icons use 32dp sizing, source padding/tint, and the source 8dp trailing spacing.
- Bottom navigation card uses the source `backgroundColor`, zero corner radius and source elevation attribute. The TabLayout restores source scrollable mode, fill gravity, 0dp max width, indicator, selected-text color, tab text style and text color.
- Divider uses `onSurfaceBgOutline2`; the full-screen fragment container restores the source 8dp outer margin.
- Added `smallText2` text appearance and light/dark divider mappings.

## Scope and remaining gaps

Drawer menu contents remain a documented empty host because the original `drawer_menu_revamp` layout is absent from the decompiler archive. The shell's renew-plan, college-year and KYC banner bodies remain empty/hidden, per the project scope; no replacement monetization UI was invented. The header/menu image is still loaded from the verified source resource in the activity code.

## Validation

The evidence guard checks source toolbar dimensions, theme attributes, tab configuration and fragment-container margin. Build and guard status must be verified after this batch; no device screenshot or pixel-diff is claimed.
