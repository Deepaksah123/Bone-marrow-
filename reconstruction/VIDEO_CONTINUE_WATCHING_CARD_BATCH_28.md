# Continue Watching Video Card — Source Layout Batch 28

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Source-backed restoration

The Home/video landing source contains a non-monetization `layout_continue_watching_video_suggestion_card` include. The replica now uses a dedicated `layout_continue_watching_video_suggestion_card.xml` rather than the generic empty placeholder.

The layout restores the source view IDs: `ivVideoThumbnail`, `ivPlayPlaceholder`, `btnDismiss`, `layoutVideoInfo`, `tvVideoTitlePrefix`, `tvVideoTitle`, `pbSuggestedVideo`, and the source-typo ID `tvVideoRemainingDuratiom`. The root card remains hidden by its parent include by default; no fake video title, remaining time, progress or account state is supplied.

## Exact source assets restored

- `ic_marrow_logo_blue.xml` — SHA-256 `a5f07798d8dcc95bf425d33e411872d6634c9de8e2f8c1cd67e77d02a6e53d64`.
- `ic_playback_play.xml` — SHA-256 `a06a2c05486e22248ee0e82ec36e914b599e7d6d47c5a4c334f44f26878f1421`.
- `circle_4d000000.xml` — SHA-256 `33bea6070bfcaa443b8eb76eb3c9599a7859bc78614b76194666025038969ee6`.
- `ic_switch_orientation_close.xml` — SHA-256 `f4a9f7a6fd6e080c10881554f592dd17a4fc2d7d0e13d3bfd85384433660b4da`.
- `bg_progressbar_blue_background.xml` — SHA-256 `61b810044ec2d8965a57a8dacd525d02e4cf3c97b37049f0e766311cc5978b32`.

The source `HorizontalProgressBarVideoDownload` style and required light/dark theme color attributes were restored.

## Remaining limits

The original card's runtime model/binding (thumbnail, title, progress and remaining duration) is not connected. The include stays `gone` until the original visibility/data flow is recovered. This is a source-structure restoration, not a claim that the feature is functionally complete or pixel-verified.

## Validation

The evidence guard checks exact hashes for all five copied source drawable files and confirms the include points to the dedicated card layout. Android build and guard results must be checked after this batch.
