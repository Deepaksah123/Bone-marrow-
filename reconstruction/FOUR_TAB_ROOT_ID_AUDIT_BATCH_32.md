# Four-Tab Root Direct-ID Audit — Batch 32

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Authority:** decoded original layout inventory in `reconstruction/VERIFIED_BINARY_LAYOUT_BATCH_3.md`, source navigation map in `reconstruction/HOME_TAB_TO_ROOT_LAYOUT_MAP_BATCH_9.md`.

## Direct-ID and root-class audit

| Tab | Active XML root | Direct IDs in replica | Source direct IDs accounted for |
|---|---|---:|---|
| HOME | `ConstraintLayout` | 17 | 17 non-monetization IDs; source root has 22 overall, with monetization-only IDs intentionally excluded |
| QBANK | `ConstraintLayout` | 2 | 2/2 |
| TESTS | `ConstraintLayout` | 9 | 9/9 |
| VIDEOS | `FrameLayout` | 44 | 44/44 |

The HOME include tree contains the source dynamic Zen area, one cards shimmer layout, six `layout_home_lesson_shimmer_m2` entries and six `layout_home_lesson_shimmer` entries. Exact subtree asset checks are maintained in Batch 25.

## Guard changes

The CI evidence guard now enforces all four root classes and exact direct-ID counts. This prevents accidental removal or insertion of root IDs as the reconstruction evolves. It does not claim that included descendants, all attribute values, navigation behavior or runtime visuals are exact.

## Limits

The original resource table is not available in the decompiler archive; attribute/configuration resolution and on-device pixel comparison remain open. The original APK checksum is recorded in `analysis/APK_SHA256.txt`. Monetization-only UI remains excluded; no fake educational or account data is added.

## Validation

The CI evidence guard result for this batch must be checked after commit. Build and runtime visual QA are separate checks.
