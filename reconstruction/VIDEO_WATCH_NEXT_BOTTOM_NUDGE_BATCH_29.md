# Bottom-Nudge Watch Next Card — Source Layout Batch 29

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Source layout restored

The second source include, `layoutContinueWatchingVideoSuggestionCard`, maps to `layout_video_watch_next_card`. It now uses a dedicated `layout_video_watch_next_card.xml` rather than the generic empty host. It contains the source heading `tvWatchNext`, MaterialCardView, `ivPlayPlaceholder`, `layoutVideoInfo`, `tvVideoTitle`, `tvVideoRemainingDuration`, and `btnDismiss` IDs.

The source `Watch Next` heading string, Subtitle1/Subtitle2 styling, source card surface/elevation/padding and source color mappings are restored. The `ic_watch_next_placeholder.xml` vector and 80×80 right-arrow PNG were added from the verified archive.

## Runtime/data boundary

Both the main `layoutVideoWatchNextCard` and bottom-nudge `layoutContinueWatchingVideoSuggestionCard` remain hidden by default, matching the source include visibility. No video title, remaining duration or progress is invented. The source runtime visibility/data binding is still not implemented.

## Validation

The evidence guard passed for both include mappings and exact source asset hashes: [run 38073315067](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38073315067). Android build compiled and uploaded the debug APK for commit `599f2e69305a`: [run 38073302955](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38073302955). Artifact ID `11678100530`, size `8,195,852` bytes, digest `sha256:84ea7c9f6a3732e522460ffe94479e3888954a3653d1a03313d252c3329f44ab`. The workflow is still in post-action finalization; the compile and upload steps succeeded. No on-device visual comparison is claimed.
