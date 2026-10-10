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

Validation (11 Oct 2026): Android reconstruction build passed [run 38078006253](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006253) and evidence guard passed [run 38078006278](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006278) on commit `884aaf01821899e0c5fd7c7dcc0f7b22f74a4b8e`. The build artifact is `marrow-reconstruction-debug`, ID `11678864090`, ZIP size `8,195,237` bytes, ZIP SHA-256 `fadbe68bceb34a26f8db64c07e519067ab0e1073f50f7ca0b8fe924230911fb7`. Device-level light/dark screenshots and pixel comparison remain outstanding.
