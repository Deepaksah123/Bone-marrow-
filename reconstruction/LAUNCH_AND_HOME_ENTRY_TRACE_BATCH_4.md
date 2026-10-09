# Launcher and Entry-Flow Trace — Evidence Batch 4

## Verified launcher declaration

The decoded manifest at `resources/AndroidManifest.xml` declares `com.marrow.ui.activities.onboarding.splash.SplashActivity` as the launcher activity:
- `android.intent.action.MAIN`
- `android.intent.category.LAUNCHER`
- `android:exported="true"`
- `android:launchMode="singleTask"`
- portrait orientation
- handles layout direction, screen size/layout, orientation and keyboard configuration changes.

## Direct SplashActivity transitions

Source: `sources/com/marrow/ui/activities/onboarding/splash/SplashActivity.java`.

| Source location | Direct behavior | Destination certainty |
|---|---|---|
| `onPlay()`, lines 460–469 | Builds an Intent via `zadb.Companion.write(this)`, adds `key_override_transition=false`, starts it, then finishes SplashActivity. | Factory returns an Intent targeting `kotlin.zadb` in the decompiled source; its relation to a user-visible home route is **not yet verified**. |
| `onMediaButtonEvent()`, lines 472–479 | Starts `SyncingActivity` directly, then finishes SplashActivity. | Activity class is explicit. |
| `onCustomAction()`, lines 482–500 | Starts an Intent returned by `createFloatList.Companion.RemoteActionCompatParcelizer(this)`, then finishes SplashActivity. | Factory returns an Intent targeting `kotlin.createFloatList`; user-visible route is unresolved. |
| `onCommand()`, lines 504–515 | Starts an Intent returned by `getAnchorU.Companion.IconCompatParcelizer(this)`, adds `key_override_transition=false`, then finishes SplashActivity. | Factory returns an Intent targeting `kotlin.getAnchorU`; user-visible route is unresolved. |

## SyncingActivity evidence

- Manifest declares `com.marrow.kt.ui.activities.sync.SyncingActivity` with `@style/AppTheme`.
- In `SyncingActivity.java:185–198`, a callback builds an Intent via `zadb.Companion.write(syncingActivity)`, sets flags `335544320`, starts the resulting activity, and finishes SyncingActivity.
- The helper target and visible destination are not treated as equivalent to a named Home screen without a verified class/resource mapping.

## Home shell evidence linked to entry work

- The `activity_home_revamp` layout resource exists as `0x7f0d0033` and its generated binding helper is `sources/kotlin/parsePeriod.java`.
- The binding helper binds `bottomNavigation` as a `TabLayout`, plus `fullContainer`, `drawerLayout`, and other home-shell views.
- This proves a home-shell resource and binding exist, but does **not** prove which Splash callback reaches it, how its tabs are wired, or what the complete back stack is.

## Unresolved / next trace

1. Resolve the decompiler/manifest class-name discrepancy for obfuscated `kotlin.*` Intent targets.
2. Trace call sites of the generated Intent factories and the class/resource owners that consume `activity_home_revamp`.
3. Trace tab listeners, fragment replacement/transactions, deep links, and back behavior from actual source call sites.
4. Do not invent a route from a layout name or screenshot alone.

## Validation boundary

This is static-source tracing only. No navigation has been implemented, no Android project has been built, and no runtime behavior is claimed. Reconstruction readiness remains **PARTIAL, NOT RESOLVED**. Excluded payment, subscription, renewal, checkout, upsell, and advertising UI remains excluded.
