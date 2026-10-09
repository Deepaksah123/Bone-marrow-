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

The project contains a native Android app module and CI workflow. The shell now uses a Material `TabLayout`, custom tab views, and source-derived IDs `fullContainer`, `bottomNavigation`, `cvBottomNavigationContainer`, and `homeAppBar`. The four tab order/icon/string resource mapping is grounded in `DataBuffer.java` and the batch-7 source trace. Home/QBank/Test/Video body implementations remain incomplete and are not yet 1:1. Recent CI exposed stale tab ID references in an earlier commit; those references have since been replaced, and the latest build is pending. No device/emulator visual QA has been performed.

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

- These two removals were reversed after the user clarified that existing UI must not be removed just because a search pass did not locate its source string. Header and test filters remain in the implementation while their exact source strings/layout relationships are traced.
- The app bar content and test-filter semantics are still unverified. Preserve them for now; do not treat their presence as proof of original fidelity.
- The screen bodies remain provisional; do not call the UI 1:1.


## Parallel reconstruction batch — 2026-10-09

### Shell/navigation work now applied

- Replaced the shell's hand-wired row selection with the original Material `TabLayout` component family.
- Added the Material Components dependency to the Android module.
- Populated four tab slots from the source-backed model order and original tab vector/string resources.
- Aligned shell IDs with source binding names: `fullContainer`, `bottomNavigation`, `cvBottomNavigationContainer`, and `homeAppBar`.
- Corrected custom tab root sizing so it fills the Material tab slot rather than depending on `0dp` width/weight outside a LinearLayout parent.
- Kept current header/test filter UI intact per instruction; do not remove existing UI solely because a search pass did not locate its source string. Trace original string/layout resources before changing it.

### Verification

- CI failure chain was traced from logs: (1) stale `R.id.home_tab` etc. references after switching to one `TabLayout`; (2) literal `\\n` characters were accidentally written into `app/build.gradle`; (3) the Gradle dependency block was rewritten in valid syntax at commit `d05a820`. The build for `d05a820` is now the active verification target; check its result before declaring the batch build-green.
- Runtime/device visual QA has not been performed. The four content bodies remain incomplete and must not be called 1:1.
