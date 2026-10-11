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
5. Source-to-screen/behavior map — **PARTIAL**. Batch 59 verified the core shell/Home/QBank/Tests/Videos layout symbols against the original R.java, public.xml, binary layout entries, and source binding classes. Full navigation behavior, all binary-XML attributes, data-bound states, and pixel parity remain unresolved.

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

The project contains a native Android app module and CI workflow. The shell uses a Material `TabLayout`, custom tab views, and source-derived IDs `fullContainer`, `bottomNavigation`, `cvBottomNavigationContainer`, and `homeAppBar`. The four tab order/icon/string resource mapping is grounded in `DataBuffer.java` and the batch-7 source trace. Home/QBank/Test/Video body implementations remain incomplete and are not yet 1:1. The toolbar search route is now traced to the original Better Search fragment and a source-shaped initial overlay is implemented; query/results/history data binding remains incomplete. Android build/evidence-guard results from earlier commits are historical only. A successful API 31 emulator run and artifact review are not yet confirmed for the latest source-bound tooltip correction; no runtime pass is claimed.

Completed in this phase:
- verified original APK/decompiler inputs;
- mapped core source domains;
- indexed Home/QBank/Test/Video source domains; exact resource candidates remain unverified;
- established the reconstruction order.

## Active implementation batch

### Batch A — shell/navigation + Home

1. Decode the original APK's `resources.arsc` and binary XML into build-ready resources. **Drawer resolution completed in Batch 53** by mapping `drawer_menu_revamp` to its obfuscated APK entry and reconstructing the source-backed layout; equivalent resolution for remaining unresolved screens/resources is still pending.
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

- Historical CI failure chain: stale `R.id.home_tab` references and malformed Gradle dependency syntax were corrected in later commits; the current Android build passes at [run 38086133865](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133865), with evidence guard pass at [run 38086133816](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133816).
- The earlier API 31 smoke run [38086133823](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133823) **failed** on its older checkout: activity start timed out and the job exited with code 137 before screenshot artifacts were uploaded. It is not a runtime-QA pass. Batch 57 corrected three over-escaped bounds regexes in the Video interaction smoke checks; the new workflow run must pass and its artifacts must be reviewed before runtime fidelity is claimed. The four tab content bodies and full-app pixel parity remain incomplete and must not be called 1:1.

## Drawer binary XML recovery (Batch 53)

- Original APK SHA-256 and decompiler ZIP SHA-256 were verified against the recorded source artifacts.
- `R.layout.drawer_menu_revamp` (`0x7f0d00b3`) resolves to obfuscated APK entry `On`; its binary XML was decoded and used to rebuild the drawer hierarchy.
- Purchase/upsell/referral/debug rows are excluded. Source-row visibility/data binding, profile/course values, and non-monetization click destinations remain unresolved.
- Android build passed [run 38082219855](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082219855); evidence guard passed [run 38082552280](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082552280). Emulator UI smoke remains in progress.

## Shell binary XML geometry correction (Batch 54)

The original `activity_home_revamp` binary XML (`0x7f0d0033`, obfuscated APK entry `zZ`) has been decoded directly. Shell clipping, toolbar trailing-action grouping/padding, bottom-nav margins, blocker elevation and `fullContainer` elevation are corrected to match the binary XML. The source-traced Better Search overlay and source slide animations are now present. Latest build/evidence validation and API 31 UI smoke are tracked at [build run 38086133865](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133865), [guard run 38086133816](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133816), and [smoke run 38086133823](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133823). Whole-app 1:1 parity remains incomplete.


## Video UI smoke correction — Batch 57 (2026-10-11)

- Inspected the failed API 31 smoke run and found the three Video interaction bounds checks used over-escaped raw-string regexes, unlike the already-working shell/search checks. They could not parse normal Android bounds such as `[x1,y1][x2,y2]`.
- Corrected the Video tab, tooltip trigger, and tooltip close-control bounds regexes in `.github/workflows/android-ui-smoke.yml` in commit [`dbf3245`](https://github.com/Deepaksah123/Bone-marrow-/commit/dbf3245aae661f42583e257f37c03d01cb88b1ea).
- This is a QA harness correction only; it does not add UI, educational data, or behavior and does not prove the UI is 1:1. Await the workflow triggered by the correction and inspect its screenshots/hierarchies before marking runtime QA passed.

## Emulator smoke stability correction — Batch 58 (2026-10-11)

- Reviewed the failed API 31 job log for run `38086133823`. Emulator boot completed, but app launch/smoke was terminated with exit code 137 while emulator graphics reported ColorBuffer bind errors; the failure did not establish whether the app's UI passed.
- Updated `.github/workflows/android-ui-smoke.yml` in commit [`d841120`](https://github.com/Deepaksah123/Bone-marrow-/commit/d841120a9dd7401a8b0c78624f514244261a9c66): reduced emulator memory reservation from 3072 MB to 2048 MB to reduce runner pressure, disabled boot animation, and increased initial app-launch command timeout from 15 seconds to 45 seconds. The script continues to require the app process, source-backed view IDs, navigation checks, and screenshots.
- Together with Batch 57's corrected Video bounds regexes, the smoke harness now has both fixes committed. **A new successful CI run and artifact review are still required**; no runtime pass or full 1:1 parity is claimed until then.


## Frozen parallel reconstruction batch — Batch 59 (2026-10-11)

- **Scope frozen for this batch:** source-verified shell plus Home, QBank, Tests, Videos, and the Intern Mode tooltip only. No educational content, account data, advertising, payments, checkout, subscriptions, or upsell screens.
- Original APK SHA-256 rechecked: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`.
- Decompiler ZIP SHA-256: `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`.
- Added [original UI source trace](ORIGINAL_UI_SOURCE_TRACE_BATCH_59.md). It cross-checks seven core layout symbols against `sources/com/marrow/R.java`, `resources/res/values/public.xml`, source inflation references, and binary layout entries. It also records the source binding IDs for all four tabs.
- Reconciled the source binding IDs against the current replica layouts: QBank 2/2, Tests 9/9, Videos 43/43; Home 17/22 and shell 22/24 because only the identified Pro/upsell IDs remain intentionally excluded. Removed the extra non-source `parentFrame` and `shell_root` IDs.
- Rebuilt `tooltip_intern_mode_info_replica.xml` from the original binding structure. The previous IDs `tvInternModeTooltipTitle`, `btnCloseInternModeTooltip`, and `tvInternModeTooltipDescription` were not in the original R.java. They were replaced with the verified IDs `cardInternModeTooltip`, `btnInternModeToolTipDone`, `container`, `ivTooltip`, `tvLearnMore`, and `txtToolTipBody`; the default body string, Done label, original dimensions, and arrow drawable are now source-backed.
- Updated `MainActivity` to bind the original Done control rather than the fabricated close-button ID.
- Hardened `.github/workflows/android-ui-smoke.yml`: job timeout is 30 minutes, tab taps are constrained to the bottom-navigation screen region, and tooltip smoke checks use original source IDs.
- **Still not 1:1:** Home/QBank/Tests/Videos data-bound content and complete behavior remain incomplete. Original resource layout entries are binary XML; a verified symbol map is not a pixel comparison.
- **QA gate:** the workflow definition is updated, but the latest run's result and screenshots/hierarchy artifacts must be inspected before marking emulator QA passed.

## Source-bound layout guard and binary-XML correction — Batch 60 (2026-10-11)

- Decoded the original tooltip binary XML's attribute resource map and aligned the replica root, overlay container, CardView, action row, and Learn More margin to those original attributes. The vector arrow was byte-content inspected as a decoded XML entry and matches the replica.
- Added `.github/scripts/verify_source_bound_layouts.py` to check required original binding IDs, scope-excluded Pro/upsell IDs, XML parsing, and tooltip resource references. The Android UI smoke workflow now runs this guard before `:app:assembleDebug`.
- Content-level comparison of the checked-in layouts passes: Home 17/17 in-scope IDs, QBank 2/2, Tests 9/9, Videos 43/43, shell 22/22 in-scope IDs, bottom tab 3/3, tooltip 7/7 binding IDs. Excluded Home/shell Pro IDs remain explicitly out of scope.
- This is static source/markup validation, not a Gradle or emulator result. The latest workflow status and uploaded screenshots/hierarchies remain unverified; do not mark runtime QA or full 1:1 parity as passed.
