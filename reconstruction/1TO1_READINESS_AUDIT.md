# 1:1 Reconstruction Readiness Audit

Source boundary: `Deepaksah123/Bone-marrow-` only.

## Verified available in the working reconstruction environment

- Original `base.apk`
- Original APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- Original APK inventory: 5,128 entries
- Decompiled ZIP: 26,825 entries
- Java/Kotlin source: 20,526 files
- Smali: 817 files
- XML/resource entries: 2,371 XML files plus decoded-resource inventory
- `com/marrow2` source: 401 files
- `com/marrow2/ui` source: 233 files
- Existing APK path/batch inventory and exclusion documentation in the repository

## Previous blockers — status

1. ~~Original `base.apk` unavailable~~ — **RESOLVED**; uploaded and SHA-256 verified.
2. ~~Verified decompiled Java/Kotlin unavailable~~ — **RESOLVED**; uploaded decompiler dump verified.
3. ~~Verified Smali unavailable~~ — **RESOLVED**.
4. ~~Resource evidence unavailable~~ — **RESOLVED**; original resource inventory and binary resource entries are available. Build-ready XML decoding is still an implementation prerequisite.
5. Source-to-screen/behavior map — **PARTIAL, NOT RESOLVED**. Domain ViewModel source files are indexed, but candidate layout names exist in the archive but their screen-to-layout relationships are unverified; exact resource/navigation mapping remains blocked pending source cross-references and resource-table resolution.

## Scope exclusions

- Educational/content data: intentionally deferred; user will provide it after the UI is 1:1.
- Advertising UI: excluded.
- Payment/checkout/subscription/monetization UI: excluded.

## Non-negotiable reconstruction rules

- Original APK/decompiler evidence is the source of truth.
- Screenshots are visual QA/reference only, never implementation source.
- Do not fabricate missing UI or behavior.
- Do not import code, content, assets, UI or assumptions from Marrow or any unrelated repository.
- Keep unresolved evidence gaps explicitly tracked.

## Current state

The project contains a first native Android app module with four tab destinations and original tab vector assets, light/night palettes, and a build workflow. Important distinction: the current bottom tab row is a custom approximation, not the original Material TabLayout hierarchy; the app-bar content is unresolved. Home/QBank/Test/Video body screens are still placeholders/incomplete, and their data/navigation wiring is not reconstructed. A CI APK build is verified for commit `11dbe5057eabcd018d3a6a48b3bac669f0412f96`; later cleanup commits are rebuilding. No device/emulator visual QA has been performed, so this is not 1:1.

Completed in this phase:
- verified original APK/decompiler inputs;
- mapped core source domains;
- indexed Home/QBank/Test/Video source domains; exact resource candidates remain unverified;
- established the reconstruction order.

## Active implementation batch

### Batch A — shell/navigation + Home

1. Decode the original APK's `resources.arsc` and binary XML into build-ready resources; the decompiler ZIP resource names alone do not provide a build-ready exact hierarchy.
2. Generate exact resource and screen mappings from actual source references; mark candidate relationships unverified until traced.
3. Trace main navigation, tab state, deeplink/back-stack behavior and shared Home state with file/method/line evidence.
4. Only then implement shell/Home from verified evidence; do not create a guessed Android project/tree.
5. Build and verify once an evidence-grounded Android project exists; record gaps rather than substituting guessed UI.

### Following batches

- **B:** QBank
- **C:** Test
- **D:** Video
- **E:** supporting UI

No educational content will be inserted during these UI batches.


## Latest evidence-boundary cleanup (2026-10-09)

- Removed the unverified `My Tests` / `Grand Tests` / `Previous Year` filter labels from `MainActivity`; the original test fragment has a Material `TabLayout`, but these exact labels were not established from source strings.
- Removed the unverified `Marrow` text from the reconstructed app bar. The source establishes the `homeAppBar` container, not its exact title/content.
- The custom bottom row and screen bodies remain provisional; do not call the UI 1:1. Latest commits are being rebuilt by CI.
