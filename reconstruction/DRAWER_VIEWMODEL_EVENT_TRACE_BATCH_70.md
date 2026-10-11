# Batch 70 — original drawer event and destination trace

## Scope

This batch traces the original drawer-facing event model and the source ViewModel handlers from the checksum-verified `base.apk_Decompiler.com.zip`. It does not add local click handlers, guessed row destinations, account values, or purchase/referral/monetization surfaces.

## Verified source chain

- The original host is `sources/kotlin/zabz.java` (runtime DEX class `o.zabz`). Its `onCreate(Bundle)` body is decompiler-skipped, so its full listener-to-event wiring cannot be asserted from this Java output.
- The original host exposes concrete click-listener registrations around lines 2206–2337, tab rendering around lines 2522–2595, and the ViewModel event-effect collector around lines 1419–1508. The collector is recovered; the full drawer row-to-listener map is still incomplete.
- `sources/com/marrow2/ui/main/viewmodel/HomeUIActivityViewModel.java` consumes `onDataRangeChanged` events in its recovered event-dispatch coroutine (around lines 620–650) and translates them into navigation/effect state. Its state/effect consumer is not integrated into the reconstruction.
- `sources/kotlin/onDataRangeChanged.java` defines the original event variants, including URL/title payload events and singleton effects. These are typed ViewModel events, not permission to map arbitrary local rows directly to destinations.
- The drawer item model uses source types including `CourseConfigV2NavDrawerItemFreeExtension`, `CourseConfigV2NavDrawerItemRateUs`, and `CourseConfigV2NavDrawerItems`; selection/filtering logic in `getNavDrawerItems.java` and `getNavDrawerKey.java` is decompiler-skipped.
- The original host event collector in `zabz.java:1419–1508` confirms effect consumption: URL/title payloads are sent to `CmcdConfigurationRequestConfig.write(...)`; the Share App event checks connectivity and starts the original share flow; Know More starts the original `PlanActivity` intent; Marrow Notes, Rate Us, Terms, Report Piracy, and other singleton events dispatch to original host helpers/activities. This identifies the original consumer path but does not integrate that path into the local reconstruction.

## Explicitly recovered ViewModel actions

| Original handler | Verified effect/event |
| --- | --- |
| `RatingCompat()` | Analytics key `click_aboutus`; emits URL/title `https://www.neurogliahealth.com/`, `About Us` |
| `MediaMetadataCompat()` | Analytics key `click_faq`; emits `https://www.marrow.com/home/faq`, `FAQs` |
| `handleMediaPlayPauseIfPendingOnHandler()` | Analytics key `click_knowmore`; emits singleton `onDataRangeChanged.AudioAttributesImplApi26Parcelizer` |
| `MediaControllerCompatMediaControllerImplApi21ExtraBinderRequestResultReceiver()` | Analytics key `click_marrownotes`; emits singleton `onDataRangeChanged.RemoteActionCompatParcelizer` |
| `onFastForward()` | Analytics key `click_rateus`; emits singleton `onDataRangeChanged.onAddQueueItem` |
| `onPlay()` | Analytics key `click_reportcopyrightissue`; emits URL/title `https://medengageclinical.firebaseapp.com/reportpiracy.html`, `Report Video Piracy` |
| `onPause()` | Analytics key `click_t_c`; emits URL/title `https://www.marrow.com/home/terms`, `Terms` |
| `onCommand()` | Analytics key `click_sharetheapp`; emits singleton `onDataRangeChanged.onCustomAction` |

These are verified ViewModel-level actions plus the corresponding original host effect consumer. They still do **not** establish which current reconstructed drawer view ID maps to each handler, nor row visibility predicates for the active account/course. The consumer is source-recovered but not integrated into the local reconstruction.

## Source fingerprints (from original decompiler archive)

- `sources/com/marrow2/ui/main/viewmodel/HomeUIActivityViewModel.java`: 95,459 bytes; SHA-256 `8bde2c019f605b480d45baad87e12105db5f3bdb15460ea6b360b9470ca55936`
- `sources/kotlin/zadb.java`: 71,238 bytes; SHA-256 `4fc68899a3857dad490acc5102fc55c0bda58952162b599d080e14f977ce1bbc`
- `sources/kotlin/zabz.java`: 210,323 bytes; SHA-256 `6ef9ba909d81f653770ac4d86ecf34b07f3dc3dc0af5df8248ac2f37bea58676` (effect collector around lines 1419–1508)
- `sources/kotlin/onDataRangeChanged.java`: 15,764 bytes; SHA-256 `<escape>not recorded in this pass</escape>`
- `sources/kotlin/getNavDrawerItems.java`: 5,649 bytes; SHA-256 `4e3a20d61587f1c268a9c91a49dbbafe0cf542ffced5babbc7b040822b36709e`
- `sources/kotlin/CourseConfigV2NavDrawerItems.java`: 811 bytes; SHA-256 `aceee54924cc0938269fde03b937ef82e8efdd5abb210addf170259e29287599`

## Reconstruction decision

Do not add destination listeners or hard-code these URL/effect actions into `MainActivity` yet. The local drawer has the source-backed hierarchy, but the original drawer binding/listener mapping, ViewModel/provider lifecycle, and effect consumer are not integrated. Adding listeners now would be a plausible substitute, not a verified 1:1 restoration. Keep unresolved routes inert until the genuine chain is recovered.

## Validation boundary

This is a source trace, not runtime parity evidence. The Android build, source-evidence guard, layout audit, and emulator smoke must be checked against the current PR head after this batch. No full drawer interaction or whole-app 1:1 claim is made.
