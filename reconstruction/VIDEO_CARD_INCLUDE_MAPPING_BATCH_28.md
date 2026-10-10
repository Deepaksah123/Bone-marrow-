# Video Card Include Mapping Correction — Batch 28

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.

## Fix

The two Video landing include IDs were connected to the opposite card layouts. Corrected the include mapping:
- `layoutContinueWatchingVideoSuggestionCard` → `layout_continue_watching_video_suggestion_card.xml`
- `layoutVideoWatchNextCard` → `layout_video_watch_next_card.xml`

The nested scroll content background now uses `?attr/backgroundColor`, so it follows the active theme rather than hardcoding the replica shell background.

## Why it matters

Both include roots expose different view IDs and content structure (continue/resume thumbnail, progress bar and remaining duration vs. a watch-next card). Swapping them could make runtime bindings resolve the wrong child IDs and would misrepresent the source hierarchy.

## Validation

The Android build passed for code commit `32aa3a13e995`: [run 38074064454](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074064454). Debug APK artifact ID `11677922158`, size `8,196,572` bytes, digest `sha256:7944050e0eb69336c69ef5736850f1972ca60f972e95e6756b2daad83b64b30a`. The evidence guard passed after the mapping assertions were corrected: [run 38074106241](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074106241). No runtime screenshot or pixel parity is claimed.
