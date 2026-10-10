# Video Scroll Content Theme Background — Batch 48

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.

## Audit finding

The outer Video landing `parentFrame` already used `?attr/backgroundColor`, but the inner `clMain` ConstraintLayout inside `rootScrollView` still used the fixed `@color/shell_background`. Because `clMain` fills the scroll content, that fixed color could diverge from the resolved app theme in dark mode even when the outer frame was correct.

## Change

- Changed only `clMain` background to the existing source theme attribute `?attr/backgroundColor`.
- Kept the source-shaped view hierarchy, IDs, card include mappings, visibility, and content unchanged.
- Added a targeted CI assertion scoped to `clMain`; a generic background check alone was insufficient to catch the nested fixed-color value.
- No content, lesson cards, or other UI were invented.

## Validation

Android build and evidence guard are pending for this batch. Device-level light/dark screenshots and pixel comparison remain outstanding.
