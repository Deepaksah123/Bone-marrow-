# Video Player Intent Contract and Test Flow Boundary — Batch 15

## Video landing → lesson player

The source-backed caller is `sources/kotlin/setScrollPosition.java:2362–2367`: selecting a typed video item launches `LessonVideoActivity.Companion.RemoteActionCompatParcelizer(context, itemId, 0, false, 28)`.

The Intent factory is defined in `sources/com/marrow/ui/activities/learn/video/LessonVideoActivity.java:5245–5270`. It targets `LessonVideoActivity.class` and sets:
- `lesson_id`: selected video item's ID
- `video_autoplay`: `false`
- `is_video_origin`: `false`
- `exclude_optional_videos`: `false`
- `start_time`: `0`
- `is_from_bookmark_screen`: `false`
- `source`: `null` for this overload/call

If the device supports Android picture-in-picture, the factory also sets Intent flag `268435456` (`FLAG_ACTIVITY_NEW_TASK`) at lines 5259–5262. Preserve the exact condition and flag if reproducing this route; do not generalize it to every launch.

The player host references `R.layout.activity_lesson_video` at `LessonVideoActivity.java:11080`. This confirms the launch contract and host layout reference, not the full player rendering, playback state machine, or every other entry path.

## Test flow — what is verified and what is not

The TESTS home tab's test-introduction route is verified in Batch 13:
- `WalletConstantsCardNetwork.java:966–970` launches `addAllowedCountryCodes` with a test ID.
- `addAllowedCountryCodes.java:154–160` defines the Intent contract (`test_id`, `analyticsSource`).
- `addAllowedCountryCodes.java:533–556` reads those values and installs an embedded fragment.

Test analytics source contains events named `test_play_start`, `test_review_test_sheet`, `test_review_detail`, `test_review_list`, and `test_review_filter` in `sources/kotlin/interceptEvent.java:81, 203, 359, 364, 374`. These event names are evidence that the test/review domain includes these event categories; event strings alone do not establish the exact navigation route, screens, or interaction behavior.

A separate `activity_test_play_2` layout resource is present in the recovered resource inventory, but source cross-reference in the decompiled Java did not establish a reliable concrete activity/layout constructor mapping. Do not infer the test-taking activity class from that resource name alone.

## Next source recovery target

The next pass should inspect smali call sites and the original APK resource table to recover missing test play/review host mappings and exact player argument consumption. Decompiler lifecycle stubs prevent a safe full-flow claim at this point.

## Fidelity boundary

Only core video playback and test/review navigation are in scope. Ads, subscriptions, plan upgrades, renewals, payments, checkout, and upsell interfaces remain excluded. Static evidence only; no Android build, APK install, or runtime QA is claimed. Readiness remains **PARTIAL, NOT RESOLVED**.
