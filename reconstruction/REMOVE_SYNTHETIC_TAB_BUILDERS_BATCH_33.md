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

The evidence guard now fails if the old `buildHome/buildQbank/buildTests/buildVideos` methods or a placeholder module-completion label are reintroduced. Android build must pass after this batch; runtime visual comparison remains pending.
