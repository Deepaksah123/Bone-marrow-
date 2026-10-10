# Video Landing Visible Controls — Source Theme/Spacing (Batch 27)

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Corrected from original `fragment_video_landing`

- Root background now uses source `?attr/backgroundColor`; the bottom nudge host uses the source full-screen container geometry.
- Intern Mode row uses source `backgroundVariant2` and vertical-only 8dp padding. The status label uses Headline6 and source `colorOnBackground`; tooltip and switch now use source padding and theme tint mappings.
- Edition switch/intern-mode banner constraints and hidden-state structure remain source-shaped; no fabricated video cards or subject rows are inserted.
- Subject header uses the source 16dp overall margin. Sort label/type use source Subtitle1/Subtitle2 bases and `onBackgroundSurface3` / `colorOnBackground` colors.
- Epoxy subject grid uses source 14dp horizontal padding, retaining the code-level responsive 2-column phone / 3-column tablet behavior.
- Report Video Piracy footer now uses the source Subtitle1 basis, 10dp padding, 40dp vertical margin, centered gravity and both horizontal constraints.
- Added the source neutral palette and light/dark theme mappings for `backgroundVariant2`, `colorOnBackground`, `onBackgroundSurface2/3/5`, `onSurfaceBgOutline`, Headline6 and Subtitle1/2.

## Remaining limits

The original Roboto font files are not copied, so system-font equivalents are used. Several hidden sublayouts (watch-next card, saved/bookmarked/sample video cards and tooltip) still use an empty host while their original child layouts are absent from the app. The Intern Mode status string contains a runtime format placeholder in the source; this replica keeps a neutral label until its source data binding is recovered. No lessons or account data were invented.

## Validation

The evidence guard checks the source theme and spacing attributes. Verify CI after this batch; a successful build is not a runtime visual comparison.
