# Test and Video Tab Internal Route Evidence — Batch 13

## TESTS tab → test introduction host

- The TESTS home tab destination is `WalletConstantsCardNetwork` (Batch 7).
- `sources/kotlin/WalletConstantsCardNetwork.java:966–970` starts `addAllowedCountryCodes.Companion.read(context, testId, null)`.
- `sources/kotlin/addAllowedCountryCodes.java:154–160` creates an Intent targeting `addAllowedCountryCodes.class` and passes `test_id` and `analyticsSource`.
- `sources/kotlin/addAllowedCountryCodes.java:34` declares `addAllowedCountryCodes extends PaymentInstrumentType`.
- `sources/kotlin/PaymentInstrumentType.java:195–198` passes `R.layout.activity_test_introduction_marrow2` to its base activity constructor.
- `addAllowedCountryCodes.java:533–556` reads the analytics/test IDs, finishes if `test_id` is absent, and on first creation inserts a fragment created by `PaymentMethodTokenizationParametersBuilder.Companion.read(testId, analyticsSource)` into `R.id.fragment_container`.

This verifies the TESTS tab has an internal path to the test-introduction activity host using a test ID and analytics-source argument. It does not by itself establish every test category or the full test-taking lifecycle.

## VIDEOS tab → lesson player

- The VIDEOS tab destination is `setScrollPosition` (Batch 7).
- `sources/kotlin/setScrollPosition.java:2362–2367` handles a typed video item action, creates an Intent through `LessonVideoActivity.Companion.RemoteActionCompatParcelizer(context, itemId, 0, false, 28)`, starts the activity, and dispatches a state event to `VideoLandingViewModel`.
- `sources/com/marrow/ui/activities/learn/video/LessonVideoActivity.java:11080` directly references `R.layout.activity_lesson_video`.
- `sources/kotlin/setScrollPosition.java:2366` is a direct source call site; the action is not inferred from a screenshot.

This confirms a source-backed video landing item → lesson-player activity route. The intent factory's defaults and all player state/argument semantics still need to be traced in the named activity source.

## Excluded video branches

The video landing fragment also contains source paths to plan/upgrade or other unrelated activities. The reconstruction must continue to exclude renewal, subscription, payment, checkout, upsell, and advertising UI. Only the core lesson/player route is included in this mapping.

## Validation boundary

Static source only. No Android build, APK install, or runtime UI verification is claimed. Overall readiness remains **PARTIAL, NOT RESOLVED**.
