# Verified Home Fragment Transaction Mechanics — Evidence Batch 8

## Tab model to fragment transaction

The earlier batches established the four tab models and each model's `Class<?>` destination. This batch confirms how the base activity switches fragments.

### Evidence chain

- `sources/kotlin/DataBuffer.java:108–123`: tab models carry the destination class and are ordered HOME, QBANK, TESTS, VIDEOS.
- `sources/kotlin/zabz.java:2433–2443`: for each tab model, the UI inflates `R.layout.custom_home_tab`, binds icon/title, stores the `DataBuffer` model on the tab, and adds the tab to the `TabLayout`.
- `sources/kotlin/zabz.java:2616–2628`: the activity's tab handler calls `copyToBuffer.write(dataBuffer.write())`, passing the selected model's destination class.
- `sources/kotlin/copyToBuffer.java:163–192`: navigation helper builds the tag `Home_<fully-qualified fragment class>`, removes existing fragments whose tags start with `Home_`, looks up the destination by tag, instantiates it if absent and adds it to `R.id.upperContainer`; otherwise it shows the existing fragment, then commits the transaction.
- `sources/kotlin/copyToBuffer.java:195–207`: a separate helper handles fragments in `R.id.fullContainer` and `R.id.upperContainer`.

## Confirmed navigation behavior

- Home tab changes use a FragmentManager-backed helper rather than an external screen route for each tab.
- The selected model's class is the navigation destination input.
- The fragment tag convention is `Home_<class name>`.
- Existing home fragments are removed from the transaction before the selected fragment is found/created/shown.
- The destination container for this home-tab route is `R.id.upperContainer`.

## Caveat

The decompiled FragmentTransaction wrapper uses obfuscated method names, so this report describes only operations visible in the helper implementation. Exact animation/transitions and full state restoration remain unverified. Do not infer these from the tag convention.

## Validation boundary

Static source evidence only. No Android project build, install or runtime UI validation is claimed. Readiness remains **PARTIAL, NOT RESOLVED** because the reconstruction repository still lacks a complete Gradle Android app and resolved resource dependencies. Payment, subscription, renewal, checkout, upsell and advertising UI remains excluded.
