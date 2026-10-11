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

The project contains a native Android app module and CI workflow. The shell uses a Material `TabLayout`, custom tab views, and source-derived IDs `fullContainer`, `bottomNavigation`, `cvBottomNavigationContainer`, and `homeAppBar`. The four tab order/icon/string resource mapping is grounded in `DataBuffer.java` and the batch-7 source trace. Home/QBank/Test/Video body implementations remain incomplete and are not yet 1:1. The toolbar search route is now traced to the original Better Search fragment and a source-shaped initial overlay is implemented; query/results/history data binding remains incomplete. Android build/evidence-guard results from earlier commits are historical only. The current API 30 emulator run and its screenshot artifact must be reviewed before runtime QA is accepted; no runtime pass or full 1:1 parity is claimed.

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
- Reconciled the source binding IDs against the current replica layouts: QBank 2/2, Tests 9/9, Videos 43/43; Home 17/22 and shell 22/24 because only the identified Pro/upsell IDs remain intentionally excluded. Removed the extra non-source `shell_root` ID; restored `parentFrame` after binary XML inspection confirmed it is the original Video root ID.
- Rebuilt `tooltip_intern_mode_info_replica.xml` from the original binding structure. The previous IDs `tvInternModeTooltipTitle`, `btnCloseInternModeTooltip`, and `tvInternModeTooltipDescription` were not in the original R.java. They were replaced with the verified IDs `cardInternModeTooltip`, `btnInternModeToolTipDone`, `container`, `ivTooltip`, `tvLearnMore`, and `txtToolTipBody`; the default body string, Done label, original dimensions, and arrow drawable are now source-backed.
- Updated `MainActivity` to bind the original Done control rather than the fabricated close-button ID.
- Hardened `.github/workflows/android-ui-smoke.yml`: job timeout is 30 minutes, tab taps are constrained to the bottom-navigation screen region, and tooltip smoke checks use original source IDs.
- **Still not 1:1:** Home/QBank/Tests/Videos data-bound content and complete behavior remain incomplete. Original resource layout entries are binary XML; a verified symbol map is not a pixel comparison.
- **QA gate:** the workflow definition is updated, but the latest run's result and screenshots/hierarchy artifacts must be inspected before marking emulator QA passed.

## Source-bound layout guard and binary-XML correction — Batch 60 (2026-10-11)

- Decoded the original tooltip binary XML's attribute resource map and aligned the replica root, overlay container clipping flags, CardView clickability, action-row layout gravity, and Learn More margin to those original attributes. The vector arrow was byte-content inspected as a decoded XML entry and matches the replica.
- Cross-checked additional original binary layouts and restored Video's `parentFrame` root ID, QBank's horizontal list margins, Tests' root background/orientation/layout gravity/container width, and the bottom tab's clipping flags/frame gravity.
- Added `.github/scripts/verify_source_bound_layouts.py` to enforce exact original ID sets, reject unknown IDs, report explicit Pro/upsell exclusions, parse XML, and validate tooltip resource references. The Android UI smoke workflow now runs this guard before `:app:assembleDebug`.
- Content-level comparison of the checked-in layouts passes: Home 17/17 in-scope IDs, QBank 2/2, Tests 9/9, Videos 43/43 source binding IDs plus original root ID `parentFrame`, shell 22/22 in-scope IDs, bottom tab 3/3, tooltip 7/7 binding IDs. Excluded Home/shell Pro IDs remain explicitly out of scope.
- This is static source/markup validation, not a Gradle or emulator result. The latest workflow status and uploaded screenshots/hierarchies remain unverified; do not mark runtime QA or full 1:1 parity as passed.

## CI guard repair and visible-hierarchy smoke checks — Batch 61 (2026-10-11)

- The reconstruction evidence guard was failing before it reached UI/build validation because it required the stale exact phrase `PARTIAL, NOT RESOLVED`, while the readiness audit correctly describes the source-to-screen map as `PARTIAL`. Updated the assertion to match the current evidence wording without weakening the unresolved-parity gate.
- Evidence guard run [38111031326](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38111031326) completed successfully on commit `ff50b876cb4094752ca1cf6c88d83a137a63d3be`.
- Corrected the Android smoke workflow's per-tab hierarchy probes to use stable visible source-bound views (`rvSubjectList`, `tabs`, `rootScrollView`, `nestedScrollView`) rather than depending on the visibility of loading-state proxies. UIAutomator can omit views whose visibility is `GONE`; the checks should verify a visible tab surface while separate checks exercise source-bound loading/tooltip states.
- Android debug assembly and the exact-source layout guard completed successfully in smoke run [38110951832](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38110951832). Emulator navigation and artifact upload were still running at the time of this note; this is **not** a runtime QA pass. Inspect the final run result and screenshots/hierarchies before making any parity claim.
- The 1:1 acceptance gate remains unchanged: genuine APK/resource evidence first, then successful emulator navigation, artifact review, and source-grounded visual/state comparison. No content, account state, or paid UI is invented.

## Tests binary-XML fidelity correction — Batch 62 (2026-10-11)

- Re-decoded the original `fragment_home_test` binary XML and corrected replica attributes that differed from the source: the RecyclerView now uses the original 10dp bottom margin (not bottom padding); the source TabLayout keeps its original top gravity and fixed/fill tab configuration without added start/end constraints; source-only toolbar/TabLayout/Coordinator constraints were removed; and the two include nodes now retain the original include defaults instead of overriding dimensions/visibility.
- Extended `.github/scripts/verify_source_bound_layouts.py` to guard the source-decoded Tests attributes in addition to source ID coverage. Corrected regex escaping in the source-layout guard after its checks exposed that the previous attribute patterns did not reliably inspect the intended XML elements.
- Updated the evidence guard's Tests assertion to check the original bottom-margin attribute instead of the removed bottom-padding override.
- Current API 31 UI smoke run [38111711766](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38111711766) has passed source-bound layout validation and debug APK assembly; emulator tab navigation and screenshot/hierarchy artifact upload are still in progress. This remains a runtime QA gate, not a 1:1 parity pass.

## Emulator artifact review and QA false-positive correction — Batch 63 (2026-10-11)

- Reviewed the uploaded screenshots from smoke run [38117308229](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38117308229). Although the workflow returned success, multiple captures were obscured by Android's “System UI isn't responding” dialog; some later captures also contained the one-time immersive-mode notice. Therefore that run is **not accepted as valid visual/runtime QA**.
- Updated `.github/scripts/run_android_ui_smoke.py` in commit [d0ef80f](https://github.com/Deepaksah123/Bone-marrow-/commit/d0ef80ff084fd75f00b38bf162734a8c57e030f2) to suppress the one-time immersive confirmation and inspect the active window state before and after every screenshot, failing when a System UI ANR is detected.
- The corrected smoke workflow is [run 38119313874](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38119313874). Its final result and screenshots must be reviewed before runtime QA can be accepted.
- This correction does not change replica UI or prove 1:1 parity. Home/QBank/Tests/Videos data-bound content, complete behavior, and source-grounded visual comparison remain incomplete.


## Toolbar bookmark action — Batch 65

The original toolbar bookmark view is source-backed in the shell binding. An exact-symbol scan of the canonical decompiler archive found no separate Java/Kotlin click-listener reference to `iconBookmark` beyond the generated shell binding and resource declaration. Its click behavior remains unresolved; the replica must not attach a guessed destination. This is a tracked evidence gap, not a claim that the original app's bookmark feature is absent.


## Intern Mode tooltip and QA artifact correction — Batch 66

The original binding distinguishes `btnCloseInternModeBanner` from `ibTooltip`. The former clears `showPytBanner` and dismisses `clInternModeBanner`; the latter emits the ViewModel event that opens `InternModeTooltipState`. The replica now preserves those separate actions. The current-edition-dependent tooltip variant is not data-bound, so only the original default description is shown and Learn More remains hidden until that state is traced.

Run `38120225475` reported success, but its screenshots contain Android “isn't responding” dialogs. The smoke guard now rejects generic ANR dialogs, and the replacement run's screenshots must be reviewed before runtime QA can pass.


## Screenshot QA isolation — Batch 67

The earlier screenshot artifact contained an Android “Digital Wellbeing isn't responding” dialog. Batch 67 disables the optional Digital Wellbeing package in the disposable emulator and strengthens the screenshot gate to inspect both window and activity state for ANR dialogs. This is QA harness isolation only; a new successful run and artifact review are still required for runtime QA.


## Emulator smoke gate hardening — Batch 68 (2026-10-11)

- Reviewed preserved ANR diagnostics from run [38127175232](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38127175232). The `Application Not Responding: com.android.systemui` window record had `isVisible=false` and `Surface: shown=false`; the previous whole-dump substring check treated this hidden/stale record as a live dialog and failed before the Home screenshot.
- Changed the smoke gate to fail only when an ANR window's own record is both visible and has a shown surface. Added unit tests for hidden/stale ANR records, genuinely visible ANR windows, and cross-window visibility isolation.
- Reviewed prior screenshot artifact [11694863778](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38120225475/artifacts/11694863778). Captures were obscured by a Digital Wellbeing ANR dialog, so that green run is not accepted as runtime evidence.
- Identified that the smoke script used equal-quarter x coordinates even though the original shell uses a scrollable `TabLayout` with horizontal margins. Replaced guessed coordinates for tabs, toolbar actions, the Intern Mode switch, tooltip trigger, and Done button with live accessibility-node bounds. The gate now checks selected-tab and switch checked state instead of assuming taps succeeded.
- Added a first-render wait that requires all four source-backed tab accessibility labels before the initial screenshot. The workflow runs parser/targeting unit tests before APK build and emulator startup.
- These are QA harness changes only; no replica UI, educational content, paid UI, or guessed destinations were added. Runtime QA still requires a successful new run and inspection of its screenshot artifact. Home/QBank/Tests/Videos data-bound content, remaining behavior, and pixel-level 1:1 comparison remain incomplete.


## Cold-boot System UI ANR recovery and emulator startup — Batch 69 (2026-10-11)

- Reviewed the latest runtime diagnostics from [smoke run 38129372613](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38129372613). The visible ANR window belonged to `com.android.systemui`; the replica process was alive and its Activity remained resumed, but the splash screen had not yet been replaced when the first hierarchy check ran. This is an emulator startup/runtime failure, not accepted visual evidence.
- Updated the smoke gate to preserve full diagnostics before a single recovery attempt for a visible System UI-owned ANR, dismiss it, and continue only if a fresh window dump confirms the ANR dialog is gone. Replica-owned ANRs and repeated System UI ANRs remain fatal; screenshots are never captured while an ANR dialog is visible.
- Increased the first-render accessibility wait to 120 seconds and removed forced snapshot disabling from emulator launch options to allow the runner's normal boot path.
- Added regression coverage that distinguishes a visible System UI ANR from a replica-owned ANR and from hidden/stale System UI records.
- Runtime QA is still pending until a fresh run completes and its screenshots are reviewed. This batch does not claim pixel-level 1:1 parity; real Home/QBank/Tests/Videos data binding and unresolved source-traced actions remain outstanding.


## Bounded System UI recovery and render stabilization — Batch 70 (2026-10-11)

- Reviewed smoke artifact [11699346924](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38131372105/artifacts/11699346924) and the complete diagnostics. The first System UI ANR dialog cleared after a BACK event, but the same system-owned dialog reappeared before the next accessibility hierarchy read. The replica Activity was eventually displayed; this run is still **failed runtime QA** and no screenshots were accepted.
- Changed recovery from one attempt to a bounded maximum of two System UI-owned ANR recoveries, with diagnostics retained before each attempt and a 12-second clean-window stability check after dismissal. Any replica-owned ANR or a third/recurrent visible ANR remains a hard failure; the script never captures a screenshot while an ANR window is visible.
- Switched headless graphics to the emulator runner's `swiftshader_indirect` mode. Source-layout validation and parser regression tests run before the emulator step.
- Runtime QA remains pending until the new run completes and screenshot artifacts are reviewed. Full 1:1 parity and data-bound Home/QBank/Tests/Videos states remain unverified.


## Disposable emulator System UI restart fallback — Batch 71 (2026-10-11)

- Reviewed smoke artifact [11699532960](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38132099637/artifacts/11699532960). API 30 System UI repeatedly recreated its visible ANR dialog after two BACK recoveries; the replica Activity was eventually displayed, but captures remained correctly blocked.
- Added a final emulator-only recovery: after preserving diagnostics and exhausting two BACK attempts, restart the unresponsive `com.android.systemui` process, then require its process to return and the ANR window to remain absent through a 12-second stability interval. The replica app process is not force-stopped or modified by this recovery.
- A replica-owned ANR, failed System UI restart, or any still-visible/recurrent ANR remains fatal. No screenshot is accepted while an ANR window is visible.
- This is QA-environment recovery only. Runtime QA must still pass and the screenshot artifact must be reviewed; pixel-level 1:1 parity and original data-bound screen states remain unverified.


## System-server-owned ANR dialog dismissal correction — Batch 72 (2026-10-11)

- Inspected artifact [11700091640](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38132812697/artifacts/11700091640) at the window-record level. The visible alert's title names `com.android.systemui`, but its actual window owner is the Android system process (`package=android`); restarting the System UI process alone does not remove that already-created alert window.
- The bounded fallback now sends BACK after System UI has restarted, then rechecks the window dump and requires a 12-second clean stability window. The gate still rejects any visible ANR dialog and never treats a covered screenshot as valid.
- This is a QA-harness-only correction. A fresh successful smoke run and screenshot review are still required; 1:1 parity and data-bound screen states are not yet certified.


## Accessibility-grounded ANR dialog recovery — Batch 73 (2026-10-11)

- The latest runtime artifact shows the visible ANR alert is owned by the Android system process (`package=android`) although its title names `com.android.systemui`; restarting System UI alone does not reliably remove the alert.
- Added a final recovery that dumps the live dialog hierarchy, locates the explicit **Wait** action, taps its reported accessibility bounds, and requires the ANR window to stay absent through a 12-second stability check. No coordinates are guessed. If the dialog hierarchy or Wait button cannot be verified, the test fails closed and retains diagnostics.
- Added unit coverage for actual Wait-button bounds, hidden/missing Wait actions, and malformed hierarchy XML. Runtime QA and screenshot review remain pending; this change does not certify full pixel-level 1:1 parity.


## Search action accessibility fallback and failure capture — Batch 74 (2026-10-11)

- The latest smoke run cleared the System UI ANR and captured the Home, tab-navigation, and drawer-open screens, then failed at the Search toolbar action because UIAutomator did not expose a visible node matching the source resource ID `iconSearch`.
- The original `activity_main.xml` declares the same Search ImageView with the exact accessibility description `Search`. The runner now uses that source-declared description only as a fallback when the resource ID is absent, and still taps the live bounds reported by accessibility. It does not use guessed coordinates.
- On any future missing target, the exact hierarchy XML is retained in the QA artifact to avoid another blind diagnostic cycle.
- This batch is a targeted runtime-test correction; the latest run is not a runtime pass. A fresh smoke run and artifact review are required, and full pixel-level 1:1 parity remains unverified.


## Runtime search target and overlay exit correction — Batch 75 (2026-10-11)

- Reviewed smoke run [38134550913](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38134550913) and artifact [11700568147](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38134550913/artifacts/11700568147). The Search screenshot showed Android's external Google search/voice UI, not the in-app Better Search overlay. The previous fallback had matched a non-clickable accessibility container whose description was `Search`, tapped its center, and then BACK only dismissed the keyboard; the subsequent Videos tab lookup correctly failed because the overlay remained.
- Tightened content-description fallback to require a visible, clickable accessibility node. Added a regression test with a non-clickable parent and a clickable Search control, asserting the latter's reported bounds are used.
- After capturing the in-app Search state, the smoke runner now taps the actual source-bound `ivBack` control to leave the overlay, rather than sending a single system BACK event that only hides the soft keyboard.
- The prior run remains **failed runtime QA**; screenshots from the external Google UI are not accepted as Search parity evidence. New smoke run and artifact review are required. No pixel-level 1:1 completion claim is made.


## Drawer Back behavior and foreground-shell assertion — Batch 76 (2026-10-11)

- Artifact [11701495250](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38135599347/artifacts/11701495250) showed the app's drawer correctly opened, but one Android BACK event left the launcher foregrounded before Search targeting. The captured hierarchy proved the subsequent `Search` description belonged to the launcher search widget, not the app.
- Added a source-shell Back handler in `MainActivity`: when the start drawer is open, BACK closes it and returns without finishing the activity; other Back events continue through `FragmentActivity` so the Search fragment back stack is preserved.
- The smoke runner now requires all four app tabs to be visible again after closing the drawer. This prevents a live process ID or launcher search widget from being mistaken for the app's foreground screen.
- Build, evidence guard, and a fresh emulator smoke run are required before accepting this batch. Full pixel-level parity remains unverified.


## ADB tap-timeout diagnostics hardening — Batch 77 (2026-10-11)

- Inspected the latest API 30 smoke run [38136691295](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38136691295) and its artifact [11701761636](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38136691295/artifacts/11701761636). The evidence/build checks passed, but emulator smoke failed while issuing the source-derived tap for the Tests tab at `(514, 1720)`: the ADB shell tap command exceeded its 10-second timeout.
- The run uploaded only Home and QBank screenshots plus ANR/window diagnostics; the failure happened before Tests, Videos, drawer, Search, or Intern Mode runtime checks could complete. Therefore this run does not validate those interactions.
- Updated `.github/scripts/run_android_ui_smoke.py` to give ADB input taps a 30-second timeout and preserve ANR/window/process/logcat diagnostics if the command still times out. A timed-out tap is deliberately **not retried**, because the device may have received the tap even if the host-side command did not return; repeating it could cause an unintended second state transition.
- Added a unit regression test proving that a timed-out tap requests diagnostics and is not retried.
- This is QA-harness resilience only. It does not change the app UI or establish runtime QA. Wait for the new CI result, inspect its artifact, and continue only from observed evidence. Full pixel-level 1:1 parity remains unverified.


## Cold-emulator system ANR isolation — Batch 78 (2026-10-11)

- Inspected smoke run [38138721286](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38138721286) and artifact [11702054373](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38138721286/artifacts/11702054373). The run failed on a visible `Application Not Responding: com.android.systemui` window; the recorded foreground opaque window remained the reconstruction app's `MainActivity`, and logcat explicitly recorded an ANR in `com.android.phone` while starting `TelephonyDebugService`. The sampled system load included `system_server` at 118% CPU and System UI at 16% CPU. This evidence points to emulator/core-system startup contention, not a confirmed ANR in the reconstruction app.
- Updated the smoke runner to wait 30 seconds after emulator boot and before APK installation, giving core phone/System UI services time to settle before interaction checks. This is a bounded harness-only stabilization, not an app UI change and not proof that the issue is resolved.
- The failed run captured diagnostics only; it did not produce acceptable screenshot evidence for the remaining tab, drawer, Search, or Intern Mode checks. The next run must be reviewed from its own logs and artifact. Full pixel-level 1:1 parity remains unverified.


## CI runner investigation — Batch 79 (2026-10-11)

- Rechecked UI smoke run [38139872048](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38139872048), attempt 2, for commit `8c95d8f1c21b1e8b7d22db1dbcdecf67b0f261db`. Its API state remains `in_progress` in the emulator interaction step, with no uploaded artifact and no final conclusion despite repeated checks.
- The job-log endpoint returns `BlobNotFound`, so the running emulator step's live output cannot currently be inspected through the connected GitHub API. This is an infrastructure/observability blocker, not evidence of a pass or of app failure.
- The same commit's Android build and source-bound layout evidence guard both completed successfully. The newer audit-only commit `bd5c3b0` also passed its build and evidence-guard jobs; its UI smoke run was cancelled by concurrency because the same branch already had the prior smoke job in progress.
- Do not interpret the stuck run as successful runtime QA. A fresh runtime acceptance result still needs a completed emulator job and its screenshot artifact. No 1:1 parity claim is made.


## Bounded emulator-runner execution and non-destructive CI concurrency — Batch 80 (2026-10-11)

- The latest run on `dc0192593f84762e9764ff33ec9a64330c61ea80` passed source-bound layout validation, the ANR/accessibility parser unit tests, and debug APK assembly, but remained in the emulator interaction step without uploaded artifacts. This is not a runtime pass.
- The workflow previously allowed a new commit on the same branch to cancel the in-progress smoke run, which can erase the very emulator evidence needed to diagnose the failure. Changed the concurrency policy to let an active run finish rather than cancel it when another run arrives.
- Added an explicit 18-minute timeout to the emulator step while retaining the job-level 30-minute ceiling and unconditional artifact-upload step. This creates a bounded failure path so a stuck emulator action can hand off to screenshot/diagnostic artifact collection instead of occupying the entire job until the outer timeout.
- This is CI execution/observability hardening only. It does not change application UI or assert a fix for the emulator issue. The next run must finish and its screenshots/hierarchy/diagnostics must be reviewed before accepting runtime QA. Genuine-source data binding and full pixel-level 1:1 parity remain unverified.


## Emulator resource-pressure correction — Batch 81 (2026-10-11)

- Reconciled the current workflow configuration with the earlier runner investigation: the workflow had drifted back to `-memory 4096 -cores 4`, despite Batch 58 documenting that the API emulator run exited with code 137 under runner pressure and reducing its memory reservation to 2048 MB.
- Restored the bounded emulator profile to 2048 MB and 2 virtual CPU cores. This avoids reserving most of a standard hosted runner for the emulator and reduces competition with Gradle, ADB, UIAutomator, and artifact collection.
- Kept the 18-minute emulator-step timeout, 30-minute job ceiling, non-cancelling concurrency, and unconditional evidence upload. This is CI resource tuning only; it changes no app UI, source-bound resource, or interaction behavior.
- Acceptance remains evidence-driven: a completed smoke job and reviewable screenshots/hierarchy/diagnostics are required. Build and static guard success alone do not establish runtime QA or 1:1 parity.


## Smoke-workflow contract regression guard — Batch 82 (2026-10-11)

- Added `.github/scripts/verify_android_ui_smoke_workflow.py` to check the emulator workflow's explicit resource and evidence-retention invariants: 30-minute job ceiling, 18-minute emulator-step timeout, 2048 MB/2-core emulator profile, non-cancelling concurrency, unconditional artifact upload, failure on missing artifacts, and 14-day retention.
- Wired the contract check into the workflow before source-bound layout validation and included the script in path filters so future edits run the gate.
- This prevents the CI resource profile from silently drifting away from the documented runner investigation. It does not test app fidelity or replace screenshot/hierarchy review; emulator runtime QA and full 1:1 parity remain unverified.


## CI path-filter completeness — Batch 83 (2026-10-11)

- Verified the new smoke-workflow contract script is listed under both push and pull-request path filters, so edits to the contract guard itself trigger the intended QA workflow rather than relying on an unrelated workflow-file edit.
- This is trigger coverage only; the new contract check must pass in CI and runtime screenshot artifacts still require inspection.


## Smoke workflow path-filter deduplication — Batch 84 (2026-10-11)

- Removed a duplicate push path-filter entry for the smoke-workflow contract script found during post-commit validation. The script remains included exactly once in both push and pull-request path filters.
- No runtime or UI behavior changed. The workflow guard and full smoke evidence still need their CI results.


## Intern Mode visible-label regression coverage — Batch 85 (2026-10-11)

- Extended the emulator smoke check beyond the switch's checked bit: after each OFF/ON transition it now validates the actual source-bound `tvInternModeStatus` accessibility text against the original string format, `Intern Mode : ON/OFF`.
- Added unit coverage for exact label matching and for missing/wrong labels. This catches a switch that toggles internally while its visible status label fails to update.
- The expected text is grounded in the reconstruction's source-backed `concise_mode` string (`Intern Mode : %s`); no new screen content or behavior was invented. Runtime evidence and pixel-level parity remain separate acceptance gates.


## Search and tooltip route-state assertions — Batch 86 (2026-10-11)

- Hardened runtime checks for the Better Search route: smoke QA now requires the source-bound query field and initial message after opening, then requires the query field to be gone and the four-tab shell to be restored after the original toolbar Back action.
- Added explicit visibility assertions around the Intern Mode tooltip trigger and Done action, rather than relying on screenshots alone to imply that the overlay opened and closed.
- These checks use existing original-source IDs and do not add or fabricate UI. The next emulator run must pass and produce reviewable evidence; the replica is still not certified 1:1.
