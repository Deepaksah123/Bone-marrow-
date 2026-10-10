# Remove Dormant Synthetic Tab Screens — Batch 33

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.

## Change

Removed the inactive programmatic screen builders and their hand-authored card/text/palette helpers from `MainActivity`. The four source-shaped XML layouts remain the only top-level tab content path. Source-backed RecyclerView layout managers remain configured at inflation time:
- Home module list: LinearLayoutManager
- QBank subjects: LinearLayoutManager
- Tests list: LinearLayoutManager
- Videos subjects: 2 columns on phones / 3 columns on tablets, as recorded in the source trace

The existing activity header, source tab icons/labels, selected-state tint, and fragment transaction path are unchanged.

## Why

The old builders were no longer called but still contained invented UI labels and manually constructed cards. Removing dead code reduces the risk of accidentally reactivating synthetic content and makes the implementation path auditable. No source-backed behavior or current visible shell UI was removed.

## Validation boundary

The Android build passed for cleanup commit `ca60723df92e`: [run 38074469213](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074469213). Debug APK artifact ID `11678407183`, size `8,195,170` bytes, digest `sha256:e9c910eac41a1b087b39d8d2517c2b06e5050db7891f4c4cdcc9b707e46d5880`. The corrected evidence guard passed: [run 38074557943](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074557943). Runtime visual comparison remains pending.
