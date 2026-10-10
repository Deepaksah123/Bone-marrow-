# Tests Landing + Toolbar Source Geometry (Batch 26)

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Corrected from original binary XML

- Tests tabs use source `@dimen/tab_height` (48dp), fixed mode, fill gravity, 5dp indicator, and the source `TabTextAppearance` with caps disabled.
- `AppBarLayout` uses source theme background, 4dp top padding, 6dp bottom padding, focusable state, and zero elevation.
- `CollapsingToolbarLayout` restores source background, bottom expanded-title gravity, 24dp horizontal title margins and `scroll|exitUntilCollapsed` flags.
- `ComposeView` restores 8dp top and 6dp bottom margins.
- `rvMainList` now uses source wrap-content height, 10dp bottom padding, clipping disabled and the AppBar scrolling behavior.
- Test toolbar root uses the source theme surface variant and wrap-content sizing; back/search icons use source side padding (16dp), and the title uses the source Headline4 basis (20sp, bold, 24sp line height). The original Roboto bold font file remains absent, so the system font is an approximation.
- The empty-state icon is 50dp × 50dp with 30dp horizontal and 10dp top text spacing, matching the decoded empty-layout geometry.
- Source light/dark colors were added: `mb_50=#62c8df`, `n_00=#ffffff`, `n_05=#f5f5f5`, `n_80=#313434`, `n_85=#252727`, `tGreen=#1f4851`. Theme attributes now map the tab surface/background by mode.

## Deliberate remaining behavior gap

The test screen's empty/loading includes are still hidden at the parent level until the source-backed loading/data flow is implemented. The source resource roots and layouts are preserved; this avoids an invented permanent spinner or fabricated test data. Runtime tab labels and the original Compose test filters remain pending source-data/Compose reconstruction.

## Validation

The evidence guard passed for the Tests geometry batch: [run 38072602160](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072602160). Android build passed for code commit `6bc87b41ed7d`: [run 38072593877](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072593877). Debug APK artifact ID `11677153986`, size `8,185,065` bytes, digest `sha256:57f7d93793e5713bf45c6e3e1143fc291aa3deeb8e948b76f36a766bf56a0933`. No device screenshot or pixel-diff is claimed.
