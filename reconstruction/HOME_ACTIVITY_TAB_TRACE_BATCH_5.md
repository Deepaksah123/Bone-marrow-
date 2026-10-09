# Home Activity & Tab Selection Trace — Evidence Batch 5

## Confirmed entry target

The earlier launcher trace marked the destination of `zadb.Companion.write(context)` unresolved. Further source inspection resolves the immediate target:

- `sources/kotlin/zadb.java:356–358`: `Companion.write(Context)` returns `new Intent(context, zadb.class)`.
- `sources/kotlin/zadb.java:40`: `kotlin.zadb` extends `kotlin.zaaz`.
- `sources/com/marrow/ui/activities/onboarding/splash/SplashActivity.java:460–469`: Splash `onPlay()` creates that Intent, sets `key_override_transition=false`, starts the target and finishes SplashActivity.
- `sources/com/marrow/kt/ui/activities/sync/SyncingActivity.java:191–194`: SyncingActivity uses the same Intent factory, sets flags `335544320`, starts the target and finishes.

**Established:** both startup branches route to the same obfuscated activity class `kotlin.zadb`. This is a verified class-level route; the user-visible screen name should not be inferred from the obfuscated class name alone.

## Home shell and tab handling

- `sources/kotlin/parsePeriod.java:82–83` inflates `R.layout.activity_home_revamp`.
- `sources/kotlin/parsePeriod.java:87–105` binds `bottomNavigation`, `collegeYearUpdateBanner`, and `fullContainer`; `bottomNavigation` is explicitly cast to `com.google.android.material.tabs.TabLayout`.
- `sources/kotlin/zabr.java:192–204` stores the generated `parsePeriod` binding, and `zabr.java:213–224` returns that binding.
- `sources/kotlin/zabz.java:74` declares an abstract activity base implementing the TabLayout listener interface.
- `sources/kotlin/zabz.java:2936–2944` handles a selected tab callback and sends `setTempDir.MediaBrowserCompatItemReceiver(selectedTab.RemoteActionCompatParcelizer())` into the activity's `RatingCompat()` view-model/event path.
- `sources/kotlin/zabz.java:2572–2593` iterates tab items, reads each item as `DataBuffer`, resolves icon resources and registers the TabLayout listener.

**Not yet established:** exact tab labels/order-to-fragment mapping and the full fragment transaction/back-stack behavior. The decompiler output for base `onCreate` is incomplete and contains a decompilation stub; do not invent missing logic.

## What changed versus prior trace

The direct splash target is no longer marked unknown: it is `kotlin.zadb`. The screen label and tab destination graph remain unresolved pending mapping of the view-model/event classes and their consumers.

## Validation boundary

Static source inspection only. No Android project build, install, emulator run, or runtime UI verification has been performed. Readiness remains **PARTIAL, NOT RESOLVED**. Payment, subscription, renewal, checkout, upsell and advertising UI remains excluded.
