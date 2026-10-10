# Home Loading/Shimmer Subtree — Source Layout Batch 25

**Repository:** `Deepaksah123/Bone-marrow-` only  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Restored source layout include tree

The original `fragment_home` contains a `ShimmerFrameLayout` with:
- one `layout_home_cards_shimmer_m2` skeleton,
- one horizontal row with six `layout_home_lesson_shimmer_m2` includes,
- a second horizontal row with six `layout_home_lesson_shimmer` includes.

These layouts are now present in app resources and wired into `shimmerMain`. The parent remains `gone` by default as in the source, and the skeleton layouts contain no fabricated subjects, lesson titles, scores or account data.

## Source assets and values

- `bg_rounded_white_no_stroke.xml` copied from source; SHA-256 `8c22e2695951e8c94a757e24fc4664f8c19e1d8c5bf054d80bc53360c0f689d2`.
- `ic_marrow_logo_m.xml` copied from source; SHA-256 `2abf2eab5516be8c1f73b0b3178f3e4578a70d99f015ccd84fe3244473fdf379`.
- `ic_complete.xml` copied from source; SHA-256 `394e990f90c86a11a747fdaf027be3b89210da12cc36ef66f8718e3e54690ac7`.
- Source values added: `pure_white=#ffffff`, `shimmer_background=#dddddd`, `cloudy_blue=#d8e4e6`, plus the exact referenced skeleton dimensions.
- Home share/footer spacing was aligned to the decoded binary layout: 36dp share top margin, 10dp label spacing, and 23dp / 94dp margins for the footer group.

## Limitations

The binary source layouts were decoded for hierarchy and resource references. The two source lesson-shimmer layouts are byte-identical in the archive; their text widget is represented with a standard `TextView` because the original custom `com.marrow.ui.views.CustomTextView` implementation is not included in the current app. This is a documented compatibility approximation, not a 1:1 claim. The source skeleton includes remain hidden until the original loading/data flow is reconstructed.

## Validation

The evidence guard checks the include files, exact include counts (6 + 6), and source hashes for the three copied text drawables. Android build and evidence guard status must be confirmed from CI after this batch.
