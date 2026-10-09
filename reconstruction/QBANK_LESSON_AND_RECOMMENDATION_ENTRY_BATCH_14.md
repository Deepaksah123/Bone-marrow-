# QBank Lesson/Recommendation → Introduction Entry Points — Evidence Batch 14

## Direct QBank landing → QBank introduction

- `sources/kotlin/ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:472–476` handles a typed suggested-question item and launches `setTokenBinding` with its ID, source code `2`, and analytics key `suggested_qb`.
- The destination's Intent contract is confirmed in `sources/kotlin/setTokenBinding.java:214–219`: `test_id`, `qbank_source`, and `analytics_source`.
- `setTokenBinding.java:442–445` reads these values during activity creation.
- The QBank introduction layout host is supplied by superclass `getAuthenticatorSelection` at `getAuthenticatorSelection.java:199`, using `R.layout.activity_qbank_introduction_marrow2`.

This establishes the suggested-QBank entry path into the QBank introduction host. It is a distinct entry from the subject → lesson-list route already mapped in Batch 10.

## QBank lesson-list → play host (caller evidence)

The source contains several launch call sites for the QBank play host:
- `sources/kotlin/newArrayList.java:146–152` handles a `mapOfKeyValueArrays.read` event and calls `setAppId.Companion.write(...)`, passing the lesson/step ID, parent type, and a model-derived resume/bookmark ID. The resulting Intent is started by the lesson-list fragment.
- `sources/kotlin/zaai.java:581–587` handles a lesson-list event `zaaj.write`, calls the same QBank play Intent builder, dispatches a view-model reset event, and finishes the current activity.
- `sources/kotlin/setAppId.java:193–205` establishes that this Intent targets `setAppId.class` and passes `step_id`, `lesson_title`, parent type, bookmark index, and bookmark MCQ ID.
- `setAppId` extends `getAllAppIds`, whose constructor supplies `R.layout.activity_qbank_play` (`getAllAppIds.java:140`).

Together with Batch 10, this supports a subject selection → lesson-list screen and a separate lesson-list event → QBank play host. It does not establish the exact intermediate introduction sequence for every lesson type; source branches differ by event/model type.

## Test entry variants

- Home's TESTS fragment `WalletConstantsCardNetwork` launches `addAllowedCountryCodes` with a test ID at `WalletConstantsCardNetwork.java:966–970`.
- The shared test introduction host reads `test_id` and `analyticsSource`, then installs an embedded fragment at `addAllowedCountryCodes.java:533–556`.
- QBank introduction has distinct source codes/analytics keys at callers (for example `suggested_qb` and `qb_<source>`). These values must be preserved; they are not interchangeable defaults.

## Important excluded branches

The QBank landing source also exposes a plan-upgrade route, which remains excluded. No renewal, subscription, payment, checkout, upsell, or advertising UI is to be recreated.

## Validation boundary

Static decompiled-source evidence only. No Android project build, APK installation, or runtime UI verification is claimed. The decompiler omits/stubs several activity lifecycle methods; the full end-to-end navigation and back stack remain **PARTIAL, NOT RESOLVED**.
