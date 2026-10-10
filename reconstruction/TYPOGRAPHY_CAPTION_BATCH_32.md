# Source Caption / Bottom-Tab Typography — Batch 32

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Source evidence

Original `resources/res/values/styles.xml` defines `TextAppearance.Dr.Caption` as 10sp text with 12sp line height, zero letter spacing and `@font/roboto_regular`. Original `TextAppearance.Dr.SmallText2` inherits Caption and switches to `@font/roboto_medium`. The source shell's custom tab uses `?attr/smallText2`, so the prior 12sp replica style was too large.

## Change

- Added `TextAppearance.Dr.Caption` with source 10sp/12sp metrics.
- Changed `TextAppearance.Dr.SmallText2` to inherit Caption and use the closest system-medium font family.
- Left the existing tab icon sizing, labels, selection behavior and shell hierarchy unchanged.

## Remaining approximation

The exact Roboto font binaries are in the original APK under obfuscated archive names; the replica currently uses Android's system `sans-serif` / `sans-serif-medium` equivalents. No font files from another project were imported.

## Validation

The evidence guard now checks Caption inheritance and the 10sp/12sp metrics. Android build and guard must be confirmed for this exact style commit; this change has not been device/pixel-diff verified.
