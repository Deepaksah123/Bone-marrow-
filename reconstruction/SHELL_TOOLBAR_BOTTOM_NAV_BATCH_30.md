# Main Shell Toolbar + Bottom Navigation — Source Geometry Batch 30

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Corrected from original `activity_home_revamp`

- Shell and upper content backgrounds now use the source theme `backgroundColor`; the toolbar uses `colorSurfaceVariant5` (light blue surface / dark neutral surface).
- Toolbar uses `wrap_content` and a clickable surface; the source menu icon's `?attr/actionBarSize` width/height determines the toolbar height, with 16dp padding and source `colorOnSurfaceVariant` tint.
- Branding now uses the source Headline5 theme style and 16dp start spacing; page title uses Headline4 and is centered across the toolbar, matching the source constraints.
- Search and bookmark icons use 32dp sizing, source padding/tint, and the source 8dp trailing spacing.
- Bottom navigation card uses the source `backgroundColor`, zero corner radius and source elevation attribute. The TabLayout restores source scrollable mode, fill gravity, 0dp max width, indicator, selected-text color, tab text style and text color. The Java setup previously overrode the XML to fixed mode; it now uses `TabLayout.MODE_SCROLLABLE` so runtime matches the decoded source.
- Divider uses `onSurfaceBgOutline2`; the full-screen fragment container restores the source 8dp elevation, not an outer margin.
- Added `smallText2` text appearance and light/dark divider mappings.

## Scope and remaining gaps

Drawer menu contents remain a documented empty host because the original `drawer_menu_revamp` layout is absent from the decompiler archive. The shell's renew-plan, college-year and KYC banner bodies remain empty/hidden, per the project scope; no replacement monetization UI was invented. The header/menu image is still loaded from the verified source resource in the activity code.

## Validation

The evidence guard passed for the source shell/tab hierarchy: [run 38074219308](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074219308). Android build passed for commit `47d71eef4352`: [run 38074210922](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074210922), artifact ID `11678411729`, digest `sha256:e28b72976cc7360079706b7dcf1a01b7256371ecc51151c4026d16b188a89821`. No device screenshot or pixel-diff is claimed.

## Superseding drawer update — Batch 53

The empty-host decision above was correct while the original drawer XML was unavailable in the decompiler ZIP. The exact binary XML has since been recovered from the SHA-verified original APK and the source-backed non-monetization hierarchy is now reconstructed. See [Drawer Binary XML Recovery — Batch 53](DRAWER_BINARY_XML_RECOVERY_BATCH_53.md). Runtime visibility/data binding and row routes remain open; this does not establish whole-app 1:1 parity.

Batch 54 supersedes the earlier fullContainer geometry note with a direct decode of the original `activity_home_revamp` binary XML: `fullContainer` has 8dp elevation and no 8dp outer margin. See [Shell Binary XML Fidelity Corrections — Batch 54](SHELL_BINARY_XML_FIDELITY_BATCH_54.md).
