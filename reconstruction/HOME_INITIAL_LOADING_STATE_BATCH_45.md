# Home Initial Loading State — Batch 45

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Source evidence:** checksum-verified decompiled source, `sources/com/marrow2/ui/home/HomeViewModelV2.java` and `sources/kotlin/makeGooglePlayServicesAvailable.java`.

## Verified source behavior

- `HomeViewModelV2` initializes its `isLoading` state to false and then sets it to true during construction before the home screen observers are attached.
- The Home fragment's loading-state handler maps `isLoading=true` to `rvHomeCard=GONE` and `shimmerMain=VISIBLE`; when loading completes it reverses those states.
- The original `fragment_home` layout includes the full shimmer skeleton hierarchy. The replica had set `rvHomeCard` visible and `shimmerMain` gone, leaving an empty Home body because the real adapter/data layer is not reconstructed.

## Implemented

- On Home-tab inflation, keep the RecyclerView's verified layout manager but hide the empty list and show the original `shimmerMain` skeleton.
- Added evidence-guard checks for this source-backed loading state.
- Did not add sample lessons, fake subjects, progress, account data, or substitute cards.

## Runtime limitation

The replica currently has no original Home ViewModel/data observer. Therefore the skeleton remains visible until the verified adapter/data-loading path is reconstructed. This intentionally represents the known loading state rather than presenting fabricated educational content. A new Android build and guard run are required for this batch.
