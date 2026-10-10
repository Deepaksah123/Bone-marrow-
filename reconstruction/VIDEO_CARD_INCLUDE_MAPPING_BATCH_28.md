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

The reconstruction evidence guard now checks the card mappings and theme background. Android build and guard outcomes are pending for this batch; no runtime screenshot or pixel parity is claimed.
