# Bone-marrow — Source-to-Screen Reconstruction Map

Generated from the uploaded original APK/decompiler workspace. This is a preliminary source-domain index, not yet an exact implementation map. Resource/layout names below are unverified candidates unless a direct source/resource-table reference is recorded.

## Source boundary
- Repository: `Deepaksah123/Bone-marrow-`
- APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- UI source evidence: 401 `com/marrow2` files; 233 under `com/marrow2/ui`.
- No educational content is introduced by this map.
- Ads/payment/subscription/monetization remain excluded.

## Core navigation/UI domains

| Domain | Verified source classes | Verified resource/layout candidates |
|---|---|---|
| Main/Home | `HomeNavigationActivityViewModel`, `HomeUIActivityViewModel`, `RevampHomeActivityViewModel`, `HomeBlockingActivityViewModel`, `HomeSharedViewModel`, `MarrowTabLayout` | `activity_home_revamp`, `fragment_home`, `custom_home_tab`, navigation/tab resources |
| QBank | `QBankLandingViewModel`, `QbankIntroductionViewModel`, `QBankLessonListViewModel`, `QBankPlayViewModel`, `QBankMcqViewModel`, `QbankTrackerViewModel`, `QbankScoreViewModel` | `fragment_qbank_landing`, `fragment_qbank_introduction_marrow2`, `activity_qbank_lesson_list`, `activity_qbank_play`, `activity_qbank_score`, `fragment_qbank_tracker`, `activity_search_qbank_play` |
| Test | `HomeTestViewModel`, `TestIntroductionViewModel`, `TestPlayViewModel`, `TestMcqViewModel`, `TestSubmitWorker`, `TestTimesUpWorker`, `ReviewViewModel`, `CommonReviewViewModel`, `TestScoreViewModel`, `TestAnalyticsViewModel`, `GTAnalyticsViewModel`, `GTAnalyticsSubjectViewModel` | `activity_home_test`, `fragment_test_introduction_marrow2`, `activity_test_introduction_marrow2`, `activity_test_play_2`, `activity_review`, `fragment_test_score`, `fragment_test_analytics`, score/analytics/GT analytics resources |
| Video | `VideoLandingViewModel`, `VideoLessonListViewModel`, `VideoLessonListActivityViewModel`, `DownloadedVideoListViewModel`, `VideoRevisionListViewModel`, `RevisionCompletedViewModel`, `VideoNotesViewModel`, `SampleVideosViewModel` | `fragment_video_landing`, `fragment_video_lesson_list`, `fragment_video`, `activity_lesson_video`, `fragment_downloaded_video_list`, `fragment_video_notes`, revision/sample video resources |
| Supporting | Bookmark, Custom Module, Pearl, Settings/Profile, Search, Feedback, Theme, Recent Updates | Corresponding verified package/resource candidates in decompiler dump |

## Runtime tab mapping verified from original source

The earlier `sources/com/marrow2/ui/...` package inventory was not sufficient to establish tab routes. Direct inspection of `resources/AndroidManifest.xml`, `sources/com/marrow/ui/activities/onboarding/splash/SplashActivity.java`, `sources/kotlin/zadb.java`, and `sources/kotlin/DataBuffer.java` now verifies the launcher-to-main activity handoff and four tab enum class values:

| Tab enum | Index | Original Fragment class | Layout binding used by that Fragment |
|---|---:|---|---|
| `HOME` | 0 | `kotlin.makeGooglePlayServicesAvailable` | `kotlin/getNextSegmentHolder.java` inflates `R.layout.fragment_home` |
| `QBANK` | 1 | `kotlin.ResidentKeyRequirementUnsupportedResidentKeyRequirementException` | `kotlin/HlsMediaChunk.java` inflates `R.layout.fragment_qbank_landing` |
| `TESTS` | 2 | `kotlin.WalletConstantsCardNetwork` | `kotlin/getNextMediaSequenceAndPartIndex.java` inflates `R.layout.fragment_home_test` |
| `VIDEOS` | 3 | `kotlin.setScrollPosition` | `kotlin/buildAndPrepareSampleStreamWrappers.java` inflates `R.layout.fragment_video_landing` |

Direct source evidence: `DataBuffer.java` lines 107 and 113–115 instantiate each `DataBuffer` with its enum name, index, tab string/drawable, and Fragment class. The named Fragment classes are present and extend Fragment-derived bases; QBank, Tests, and Video `onCreateView` methods invoke their generated binding classes. This establishes source class/layout ownership more strongly than package-name inference.

**Correction to local shell (verified against `sources/kotlin/copyToBuffer.java:163–192`):** the original tag is exactly `"Home_" + cls.getName()`. The original helper removes every managed fragment whose tag starts with `Home_`, looks up the selected exact tag, instantiates the original class if absent, and adds it to `R.id.upperContainer`. The local shell now restores that original prefix and cleanup rule. Its fragment objects are still local wrappers rather than the original Fragment classes, so this corrects tag semantics only; it does not claim source-native navigation parity.

**Still unresolved:** the original launcher component is `com.marrow.ui.activities.onboarding.splash.SplashActivity`, not the local `MainActivity`. The original activity/fragment transition through splash, onboarding, and the main host has not yet been fully traced. The reconstructed app's local wrapper architecture therefore remains non-parity code until that runtime route and genuine dependencies are integrated.

## Launcher → main host trace from the original decompiler archive

1. `resources/AndroidManifest.xml` marks `com.marrow.ui.activities.onboarding.splash.SplashActivity` as the exported launcher (`MAIN` + `LAUNCHER` intent filter), with `SplashTheme`, `singleTask`, portrait orientation, and explicit configuration-change flags.
2. `sources/com/marrow/ui/activities/onboarding/splash/SplashActivity.java` contains `onPlay()` (around line 462). It calls `zadb.Companion.write(this)`, adds `key_override_transition=false`, starts that Intent, and finishes the splash Activity. The same class has separate callbacks that launch `SyncingActivity`, `createFloatList`, or `getAnchorU`; those are conditional routes and must not be mistaken for the unconditional `onPlay()` handoff.
3. `sources/kotlin/zadb.java` is the Activity targeted by `zadb.Companion.write(Context)`; that factory explicitly returns `new Intent(context, zadb.class)`. The Activity holds a `RevampHomeActivityViewModel` delegate. This establishes the splash-to-main Activity handoff from original source, while the decompiler's `SplashActivity.onCreate` body is marked “Method not decompiled”; its condition selecting `onPlay()` versus the other callbacks is therefore still unresolved.
4. `sources/kotlin/DataBuffer.java` supplies HOME/QBANK/TESTS/VIDEOS in indices 0–3, including their original Fragment class, tab string/drawable, and route key. Each of the four named class bindings directly inflates its matching layout (the four rows in the table above).

### Consequence for reconstruction

The local app's `app/src/main/AndroidManifest.xml` currently launches the self-authored `.MainActivity` and does not declare the original `SplashActivity` or raw runtime host `o.zadb` (the decompiler Java alias is `kotlin.zadb`). Its wrapper Fragments inflate local `*_replica.xml` files. Therefore this is not yet a faithful original Activity/navigation reconstruction. Do not “fix” that by simply changing the launcher to an obfuscated class: its original superclass, Hilt/application setup, base layout, and dependencies must be integrated from the genuine source together. Until that integration is feasible and validated, preserve this mismatch as an explicit unresolved gap rather than implying 1:1 parity.

## Main host class hierarchy and tab behavior — additional source trace

The main host's runtime identity comes from the raw APK manifest/DEX, not the decompiler's package aliases. The decompiler source path `sources/kotlin/zadb.java` corresponds to runtime class `o.zadb`; its raw DEX inheritance chain is:

`o.zadb` → `o.zaaz` → `o.zaay` → `o.zabz` → `o.zaO` → `o.zabr` → `o.addObserverForBackInvoker`.

Evidence:
- The decompiler's `resources/AndroidManifest.xml` remaps the runtime class name to `kotlin.zadb`; the original APK binary `AndroidManifest.xml` contains `o.zadb` as a non-exported Activity with `@style/Marrow2` and `singleTop`; it is not the launcher.
- `sources/kotlin/zadb.java` declares `public final class zadb extends zaaz`, owns a `RevampHomeActivityViewModel` delegate, and calls `super.onCreate(p0)` before continuing its own initialization.
- `sources/kotlin/zaaz.java` declares `zaaz extends zaay`; `sources/kotlin/zaay.java` declares `zaay extends zabz`; `sources/kotlin/zabz.java` declares `zabz extends zaO`; `sources/kotlin/zaO.java` declares `zaO extends zabr`.
- `sources/kotlin/zabr.java` owns the generated `parsePeriod` activity binding field/accessor. `sources/kotlin/parsePeriod.java` explicitly inflates `R.layout.activity_home_revamp`. This ties the original main shell binding to the original home-revamp layout, but the precise call chain attaching that binding is not recovered from the decompiler's skipped/obfuscated `onCreate` bodies.
- `sources/kotlin/zabz.java` contains source-backed tab behavior: it populates the Material `TabLayout` from a `List<DataBuffer>`, obtains each tab's custom view, checks the selected `DataBuffer`, updates the toolbar/bookmark state, and invokes tab-specific behavior. Around source lines 2419–2593, this behavior uses the four exact `DataBuffer` values and iterates the tab widgets.
- The original `DataBuffer` values map indices 0–3 to `makeGooglePlayServicesAvailable`, `ResidentKeyRequirementUnsupportedResidentKeyRequirementException`, `WalletConstantsCardNetwork`, and `setScrollPosition`, as recorded in the table above.

**Important boundary:** Several lifecycle methods (`SplashActivity.onCreate`, `zabr.onCreate`, `zaO.onCreate`, `zaay.onCreate`) are explicitly emitted as `Method not decompiled`. Their bodies must not be reverse-invented from neighboring methods. The evidence now identifies the original launcher, main Activity, class hierarchy, main layout binding, and tab mapping; it does not yet prove a full runnable integration into the reconstruction project.

## Tab selection → original Fragment transaction (verified code path)

The tab controller's selection handler does not just assign labels. In `sources/kotlin/zabz.java`:
- `RemoteActionCompatParcelizer(List<? extends DataBuffer>)` (lines 2419–2449) clears/rebuilds the tab layout and inflates `R.layout.custom_home_tab`, binding each `DataBuffer`'s icon, title, and enum object to the custom tab.
- `read(int)` (lines 2522–2614) reads the selected tab's stored `DataBuffer`, applies Home-only toolbar/bookmark behavior, and updates tab colors/indicator visibility.
- `read(DataBuffer)` (lines 2616–2634) passes `dataBuffer.write()` (the exact original Fragment class) to `copyToBuffer.write(Class)`. This is the source-backed class-selection/fragment-transaction entry point; it does not instantiate a hand-written wrapper.
- The original `DataBuffer` enum declares HOME index 0 and QBANK/TESTS/VIDEOS indices 1/2/3 with the original classes and route keys (`KEY_HOME`, `qbank`, `test`, `video`). The selected item is carried as the actual `DataBuffer` object in each custom tab.

This verifies that the reconstruction's `newTabFragment(index)` wrapper mechanism is not a 1:1 implementation of the original transaction path, even though its tags now match the verified class names. No wrapper change is being presented as full parity. The source-native integration target is the original `zadb` Activity/base hierarchy plus its `parsePeriod` binding and `copyToBuffer` fragment host, with their genuine dependencies/resources intact.

## Original shell includes and runtime identity (additional verification)

The original `activity_home_revamp` root binding (`sources/kotlin/parsePeriod.java:78–100`) identifies the root FrameLayout, drawer, content containers, and bottom TabLayout. Its binary XML includes these original resources by exact resource ID, resolved through `sources/com/marrow/R.java`:

| Original include/resource | Resolved resource ID | Source role |
|---|---:|---|
| `banner_renew_plan` | `0x7f0d006b` | Monetization-related banner; intentionally excluded by project scope |
| `banner_update_college_year_revamp` | `0x7f0d006c` | Original college-year update banner |
| `banner_kyc_verify_revamp` | `0x7f0d006a` | Original KYC verification banner |
| `drawer_menu_revamp` | `0x7f0d00b3` | Original drawer hierarchy |

The current local `activity_main.xml` instead uses gone FrameLayout shells for the college-year/KYC banner IDs and includes `drawer_menu_empty_host_replica`. Those are not proven to be the original include hierarchies; they remain a verified parity gap until the binary XML resources are decoded and integrated from the source archive. No screenshot-derived replacements are being added.

The original manifest also declares `com.marrow.TrainingApplication` as the Application class and `o._coerceBooleanFromInt` as `appComponentFactory`; the local manifest declares neither. The original package is `com.marrow`, version `12.0.0`, min SDK 29 and target SDK 35. The reconstruction module currently uses a different application ID and SDK levels. Changing those values alone would not restore the original Hilt/application/dependency graph, so they remain unresolved rather than being silently approximated.

## Runtime bootstrap dependency trace — verified from the original archive

The launcher-to-host trace has a second, independent prerequisite: the original application bootstrap is not equivalent to the reconstruction's default Application setup.

| Concern | Original archive evidence | Reconstruction difference / boundary |
|---|---|---|
| Application | Manifest declares `com.marrow.TrainingApplication`; `sources/com/marrow/TrainingApplication.java` is the class source. | Local manifest has no `android:name`. Original `TrainingApplication.onCreate()` is explicitly emitted as “Method dump skipped” (6,474 instruction units) and ends in a decompiler stub; its initialization cannot be recreated safely from this dump alone. |
| App component factory | Manifest declares `o._coerceBooleanFromInt` in the original APK manifest; its decompiler alias is in `sources/kotlin/_coerceBooleanFromInt.java` and extends Android `AppComponentFactory`. It overrides instantiation of Activities, Application, receivers, providers, and services, and may replace an instance when it implements the nested factory interface. | Local manifest does not declare the factory. This is a real runtime-identity/instantiation gap, not just a UI setting. Do not add a guessed replacement factory. |
| Launcher | Original manifest declares `com.marrow.ui.activities.onboarding.splash.SplashActivity` as MAIN/LAUNCHER, exported, `singleTask`, portrait, `SplashTheme`. | Local launcher is `.MainActivity`; direct replacement is unsafe until Application/factory, superclass initialization, original resources, and dependencies are integrated. |
| Main host | Original APK manifest declares `o.zadb`, non-exported, `singleTop`, theme `@style/Marrow2` (decompiler alias `kotlin.zadb`); it owns `RevampHomeActivityViewModel` and inherits the obfuscated host chain already recorded above. | `zadb.onCreate` contains decompiler-skipped instructions and explicit stubs. Multiple inherited lifecycle methods are also not recovered. |

**Source completeness check:** `SplashActivity.onCreate` is a decompiler stub; `TrainingApplication.onCreate` is skipped; `zabr.onCreate` is skipped; `zaO.onCreate` is an explicit “Method not decompiled” stub. The `zadb.onCreate` body contains large recovered regions but is not a complete, trustworthy lifecycle implementation. These gaps must remain unresolved until stronger original artifacts (complete decompilation/bytecode evidence and exact dependencies) close them.

**Decision:** Do not change the app manifest to point at original classes in isolation. That would create an unverified launch path and likely fail before the UI host is initialized. The current app is buildable, but its startup architecture is not yet source-native and 1:1 parity is not established.

## Resource evidence — corrected boundary

The inspected `base.apk_Decompiler.com.zip` contains 26,825 entries, including `resources/res/layout/` (578), `resources/res/layout-land/` (16), `resources/res/layout-sw600dp/` (7), `resources/res/drawable/` (2,210), `resources/res/color/` (216), and `resources/res/font/` (7). These counts are directly verified against the ZIP. The decompiler ZIP does not contain a file named `resources.arsc`; however, the separately uploaded original `/mnt/data/base.apk` does contain `resources.arsc` (3,327,896 bytes), verified from its ZIP directory. Resource-ID resolution therefore remains a tooling/decoding step, not an absence of the original resource table.

## Direct source-to-layout references verified in decompiler Java

These are generated binding/inflater methods containing explicit `R.layout` references, so they prove that the named layout is inflated by that generated class. They do not, by themselves, prove the runtime route or the owning activity/fragment.

| Layout resource | Decompiled binding class | Direct evidence |
|---|---|---|
| `activity_home_revamp` | `sources/kotlin/parsePeriod.java` | `LayoutInflater.inflate(R.layout.activity_home_revamp, (ViewGroup) null, false)` |
| `fragment_home` | `sources/kotlin/getNextSegmentHolder.java` | `LayoutInflater.inflate(R.layout.fragment_home, viewGroup, false)` |
| `fragment_home_test` | `sources/kotlin/getNextMediaSequenceAndPartIndex.java` | `LayoutInflater.inflate(R.layout.fragment_home_test, viewGroup, false)` |
| `fragment_qbank_landing` | `sources/kotlin/HlsMediaChunk.java` | `LayoutInflater.inflate(R.layout.fragment_qbank_landing, viewGroup, false)` |
| `activity_home_test` | `sources/kotlin/parseLabel.java` | `LayoutInflater.inflate(R.layout.activity_home_test, (ViewGroup) null, false)` |
| `fragment_video_landing` | `sources/kotlin/buildAndPrepareSampleStreamWrappers.java` | `LayoutInflater.inflate(R.layout.fragment_video_landing, viewGroup, false)` |

The referenced layout files exist in `resources/res/layout/` as binary XML. `reconstruction/VERIFIED_BINARY_LAYOUT_BATCH_3.md` records a successful structural decode of 616 layout resources, including root widget types, direct view IDs, and included-layout names. The source trace now also establishes the launcher manifest, `SplashActivity.onPlay()` → runtime `o.zadb` handoff (decompiler alias `kotlin.zadb`), main Activity inheritance chain, and DataBuffer tab-to-Fragment mapping. Still unresolved: full attribute/style/theme/dimension resolution against the original `resources.arsc`, configuration variants, and the conditions in `SplashActivity.onCreate()` plus inherited lifecycle methods explicitly marked not decompiled. Those source gaps prevent claiming a complete runnable 1:1 reconstruction. Screenshots remain QA only; no XML or tree will be fabricated.

## Reconstruction order

### Batch A — shell/navigation
1. Splash/entry and main activity boundary.
2. Home navigation container and tab state.
3. Home screen and shared state.
4. Theme/light-dark resource binding.
5. Back-stack/deeplink boundaries.

### Batch B — QBank
1. Landing.
2. Introduction.
3. Lesson list.
4. Play/MCQ.
5. Tracker.
6. Score/review/search boundaries.

### Batch C — Test
1. Test landing.
2. Introduction.
3. Test play/timer/submit.
4. Review.
5. Score.
6. Analytics/GT analytics.

### Batch D — Video
1. Landing.
2. Lesson list.
3. Player boundary.
4. Revision.
5. Downloaded.
6. Notes/sample flows.

### Batch E — supporting UI
Bookmark, custom module, pearl, profile/settings, search, feedback, recent updates, theme.

## Evidence rules

- Exact source/decompiler evidence outranks screenshots.
- Screenshots are QA only.
- If a behavior cannot be established from source/evidence, record it as unresolved.
- Do not import implementation/content from Marrow or any unrelated repository.
- Do not add placeholder educational content.
- Do not implement payment, subscription, checkout or advertising interfaces.

## Current execution state

Source inventory, six explicit generated inflater-to-layout references, and all four original DataBuffer tab-to-Fragment mappings are verified. The original APK's `resources.arsc` is present, but this environment has no `aapt`, `aapt2`, `apktool`, or `jadx` executable, and external package installation is unavailable. Do **not** claim the exact screen tree is resolved or change runtime UI based on guesses. Next gate: use an available Android resource decoder against the checksum-verified APK, resolve binary XML/resource IDs, then trace the genuine launcher/navigation path to Home before any UI integration.
## Toolbar page-title binding — screenshot-only strings removed (Batch 63)

The original source does not establish the static strings previously copied into the reconstruction:
- `sources/kotlin/zabz.java:2563–2567` sets the non-Home toolbar title from `dataBuffer.getRemoteActionCompatParcelizer()`.
- `sources/kotlin/DataBuffer.java:43–51, 63–70, 105–115` initializes that mutable title field to `""` for all four enum entries and exposes a setter. The Home tab takes a separate branch that hides the page title and restores the Home toolbar region.
- Additional raw-DEX call-site scan of the original `classes.dex` recovered the three setter calls inside `Lcom/marrow2/ui/main/viewmodel/HomeUIActivityViewModel$read;->invokeSuspend`: each calls `DataBuffer.read(String)` after obtaining a value from `CourseConfigV2.CourseStrings.getQbankHeaderTitle()`, `getTestHeaderTitle()`, or `getVideoHeaderTitle()`. The decompiled Java body for that coroutine is explicitly skipped, but the DEX call references establish the dynamic source of the three non-Home toolbar titles. The values themselves come from the course configuration; no fixed edition string is source-authorized here.

The former local strings `QBank Edition 8.5`, `Tests`, and `Videos Edition 8.5` were explicitly transcribed from screenshots, not established as the original source-bound toolbar values. They have been removed from `strings.xml`; `MainActivity.updateToolbarTitle` now keeps the non-Home title view visible but empty until its original data-binding path is recovered. This is an intentional unresolved binding, not a claim that the original app's title is always empty.

The installed app label is now `Marrow`, matching the original manifest's `@string/app_name` and the original `resources/res/values/strings.xml`. The separate application ID remains distinct to avoid replacing the installed original app.

## Raw APK package identity versus decompiler aliases — correction (Batch 65)

The decompiler archive's Java package declarations are not always the runtime class names. Raw original APK binary `AndroidManifest.xml` and DEX type descriptors were checked directly:

| Runtime identity in APK | Decompiled source path/alias |
|---|---|
| `o.zadb` | `sources/kotlin/zadb.java` / `kotlin.zadb` |
| `o.zaaz`, `o.zaay`, `o.zabz`, `o.zaO`, `o.zabr`, `o.addObserverForBackInvoker` | Corresponding `sources/kotlin/*.java` aliases |
| `o.DataBuffer` | `sources/kotlin/DataBuffer.java` / `kotlin.DataBuffer` |
| `o.copyToBuffer` | `sources/kotlin/copyToBuffer.java` / `kotlin.copyToBuffer` |
| `o._coerceBooleanFromInt` | `sources/kotlin/_coerceBooleanFromInt.java` / `kotlin._coerceBooleanFromInt` |
| `o.makeGooglePlayServicesAvailable` | `sources/kotlin/makeGooglePlayServicesAvailable.java` / `kotlin.makeGooglePlayServicesAvailable` |
| `o.ResidentKeyRequirementUnsupportedResidentKeyRequirementException` | `sources/kotlin/ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java` / decompiler alias |
| `o.WalletConstantsCardNetwork` | `sources/kotlin/WalletConstantsCardNetwork.java` / decompiler alias |
| `o.setScrollPosition` | `sources/kotlin/setScrollPosition.java` / decompiler alias |

The raw APK manifest contains `o.zadb` and `o._coerceBooleanFromInt`; the decoded decompiler manifest writes `kotlin.zadb` and `kotlin._coerceBooleanFromInt`. This is a decompiler package remapping, not a runtime package rename. The local shell's original-tag convention has therefore been corrected to use `Home_o.*`, matching the actual `Class.getName()` values used by the original `o.copyToBuffer.write(Class)`. The local Fragments remain wrappers, so tag identity is now corrected but Fragment implementation parity remains unresolved.

## Splash callback routes recovered from source and raw DEX — Batch 66

The source confirms that `SplashActivity.onCreate()` is incomplete, but its distinct callback methods and destinations are recovered:

| Splash callback | Verified handoff in decompiler source | Runtime destination identity |
|---|---|---|
| `onPlayFromMediaId()` → private `onPlay()` | Calls `zadb.Companion.write(this)`, adds `key_override_transition=false`, starts the returned Intent, then finishes | Raw DEX Activity `o.zadb` |
| `onMediaButtonEvent()` | Starts `com.marrow.kt.ui.activities.sync.SyncingActivity`, then finishes | Manifest-declared SyncingActivity |
| `onCustomAction()` | Calls `createFloatList.Companion.RemoteActionCompatParcelizer(this)`, starts its Intent, then finishes | Raw DEX class `o.createFloatList` (decompiler alias `kotlin.createFloatList`) |
| `onCommand()` | Calls `getAnchorU.Companion.IconCompatParcelizer(this)`, adds `key_override_transition=false`, starts its Intent, then finishes | Raw DEX class `o.getAnchorU` (decompiler alias `kotlin.getAnchorU`) |

Raw DEX control flow at code-unit offsets 9811–9849 in `SplashActivity.onCreate` recovers this duplicate-launch guard: when `isTaskRoot()` is false, the incoming Intent has category `android.intent.category.LAUNCHER`, and its action equals `android.intent.action.MAIN`, the Activity calls `finish()`. The branch targets and boolean inversion were read from the original `classes.dex`; this guard is separate from the callback-selection logic and should not be conflated with the main-host handoff.

**Still unresolved:** `SplashActivity.onCreate` is a 12,952-code-unit method whose decompiler output is skipped. Its recovered callback implementations establish the destinations, but do not establish which callback is selected for a particular session, account state, deep link, or startup condition. Do not choose one callback as the unconditional launcher path without recovering that decision logic.



## Intern Mode switch source trace — event, state, observer, and unresolved dependency boundary (Batch 66)

The original Videos fragment is `sources/kotlin/setScrollPosition.java` (runtime DEX class `o.setScrollPosition`); its ViewModel is `sources/com/marrow2/ui/video/landing/VideoLandingViewModel.java`.

**Verified original event chain**
1. `setScrollPosition.onViewCreated()` installs the source listener on the original binding's `onPlayFromSearch` SwitchMaterial.
2. The listener receives the real checked boolean and calls `setScrollPosition.RemoteActionCompatParcelizer(fragment, checked)`.
3. That handler dispatches `new TransformationChildCard.MediaBrowserCompatItemReceiver(checked)` to `VideoLandingViewModel.IconCompatParcelizer(event)`.
4. The ViewModel compares the event boolean to its current state `TransformationChildLayout.getIconCompatParcelizer()`. If changed, it writes a new state carrying that boolean. If enabling Intern Mode while the existing state indicates the related condition, it clears a separate state flag before launching the next coroutine.
5. The ViewModel launches its `onFastForward` coroutine for the state transition. The recovered coroutine call sequence invokes a ViewModel state-loading method, then an injected `isEncodingHighResolutionPcm.IconCompatParcelizer(checked)` use-case method, then another ViewModel transition method and a final refresh method. The coroutine's Java body is decompiler-skipped, so those deeper repository/network side effects cannot be reconstructed from this dump alone. The fragment collects the resulting `InternModelLoadedUIData` and `VideoLandingUIState` flows and updates the real switch, OFF/ON text, theme-derived track/thumb colors, Intern Mode banners, and loading/transition labels. This is model/observer-driven; it is not merely a cosmetic label toggle.

**What remains unresolved**
- The current local app does not integrate `VideoLandingViewModel`, its repositories/use cases, or the original event/state flow. Some relevant ViewModel coroutine bodies are decompiler-skipped. Wiring the local switch to a made-up boolean or changing only label/colors would be fabricated behavior.
- Therefore the local switch remains non-clickable and non-focusable until the source ViewModel/state/repository dependency chain is integrated. Do not mark the interaction as implemented because the original event shape is known.
- The original ViewModel's checked state is data-bound; do not infer that every account/course always starts OFF solely from the local reconstruction's initial XML state.

The relevant source evidence is in `setScrollPosition.java:265–276, 2816–2821, 3038–3040`, `VideoLandingViewModel.java:1897–2000`, and `ExpandableTransformationBehavior.java`. The raw runtime class is `o.setScrollPosition`; the decompiler's source package alias is `kotlin.setScrollPosition`.



## VideoLandingUIState field semantics from original data class

The original `sources/kotlin/TransformationChildLayout.java` carries Kotlin metadata identifying its runtime type as `com.marrow2.ui.video.landing.model.VideoLandingUIState`. Its six fields are explicitly named in that metadata and accessor methods:

| State field | Verified meaning |
|---|---|
| `editionSwitchBannerText` | nullable banner text for edition switching |
| `isInternModeEnabled` | whether the Intern Mode feature is enabled/available |
| `isInternModeOn` | the current Intern Mode checked/on state used by the switch event comparison |
| `showPytBanner` | visibility state for the PYT banner |
| `sortOrder` | current sort-order integer |
| `showInternModeSnackBar` | whether the Intern Mode snackbar should be shown |

The zero-argument data-class constructor defaults these fields to null/false/false/false/0/false, but this is only the data class's default construction—not proof that every account/course remains in this state after repository/configuration loading. The separate loaded-state model `InternModelLoadedUIData` tracks loading and the checked/on values used during transition rendering. These state distinctions must be preserved if the original ViewModel is integrated; do not collapse feature availability and checked/on state into one local boolean.

## Intern Mode preference persistence — source-traced boundary

The transition coroutine's injected use case is `sources/kotlin/isMediaStoreExternalContentUri.java`, implementing `isEncodingHighResolutionPcm`. Its `IconCompatParcelizer(boolean, continuation)` overload delegates to `unlockFolder.write(boolean, continuation)`. The concrete repository is `sources/kotlin/removeStaleSpans.java`; its corresponding method writes the boolean under preference key `is_concise_mode_on` through its injected storage dependency. The same repository's `addOnContextAvailableListener()` stores `concise_banner_shown`, and `write(int, continuation)` stores sort order under `sort_video_subject`.

This proves a persistence step exists in the original event chain, but not that the switch is only a preference toggle: the coroutine also performs state loading, a separate transition call, and a refresh. The repository's injected storage implementation and remaining ViewModel/use-case dependencies are not integrated in the local app. Do not replace them with an independently written SharedPreferences handler and call it source-native parity.





## Batch 67 — defer video controls whose original ViewModel event effects are absent

The original binding confirms that these are event-driven controls, not direct visibility mutations: `setScrollPosition.java:2816–2821` forwards the Intern Mode checked boolean; the click handlers around `2761–2871` dispatch typed `TransformationChildCard` events to `VideoLandingViewModel`. The original banner-dismiss action and tooltip trigger/dismiss actions therefore depend on ViewModel state and observers. The local implementation previously substituted direct `View.GONE`/visibility changes and a hard-coded tooltip body for those original state transitions. Batch 67 removes those substitute listeners and marks the controls non-clickable/non-focusable until the original ViewModel and binding observer graph is integrated. The emulator smoke now verifies that boundary instead of claiming tooltip-open/close parity. The original event class-to-state transition for each of these controls is not yet fully mapped, so no exact local substitute is introduced.


## Batch 67 — exact VideoLanding control-to-event mapping

The binding constructor and click listeners now support a more exact event map:

| Original view ID | Original binding field | Source click listener | ViewModel event |
|---|---|---|---|
| `btnCloseInternModeBanner` | `buildAndPrepareSampleStreamWrappers.IconCompatParcelizer` | `setScrollPosition.java:2827–2831` | `TransformationChildCard.write.INSTANCE` |
| `ibTooltip` | `buildAndPrepareSampleStreamWrappers.MediaMetadataCompat` | `setScrollPosition.java:2838–2842` | `TransformationChildCard.AudioAttributesCompatParcelizer.INSTANCE` |
| `btnInternModeToolTipDone` | `buildAndPrepareSampleStreamWrappers.onPrepareFromUri.IconCompatParcelizer` | `setScrollPosition.java:2849–2853` | `TransformationChildCard.AudioAttributesImplApi21Parcelizer.INSTANCE` |
| `tvLearnMore` | `buildAndPrepareSampleStreamWrappers.onPrepareFromUri.RemoteActionCompatParcelizer` | `setScrollPosition.java:2794–2798` | `TransformationChildCard.AudioAttributesImplApi26Parcelizer.INSTANCE` |
| `switchInternMode` | `buildAndPrepareSampleStreamWrappers.onPlayFromSearch` | `setScrollPosition.java:2816–2821` | `TransformationChildCard.MediaBrowserCompatItemReceiver(checked)` |

The ViewModel handles these distinct events in `VideoLandingViewModel.java:2011–2038`: `write.INSTANCE` resets portions of `VideoLandingUIState` and launches a coroutine; `AudioAttributesCompatParcelizer.INSTANCE` launches a separate coroutine; `AudioAttributesImplApi21Parcelizer.INSTANCE` updates the `ExpandableBehavior` state to false; `AudioAttributesImplApi26Parcelizer.INSTANCE` resets the current `IntegrityManager` state. The exact downstream effects of the first two coroutine bodies and the Learn More destination are not fully recoverable from this decompiler output, so this table records the proven event path without inventing a local state transition. Batch 67 keeps these controls non-actionable rather than substituting direct visibility/navigation changes.


## Batch 68 — original VideoLandingViewModel factory and injected dependency trace

## Verified original dependency construction

The genuine decompiler archive contains the application ViewModel factory at `sources/kotlin/cloneWithUpdatedTimeline.java`. Its `read()` switch constructs the original `VideoLandingViewModel` at line 2066 (case 103) with these seven constructor arguments, in order:

| Constructor position | Exact factory argument | Original type / source evidence | Status in local replica |
|---:|---|---|---|
| 1 | `this.write.removeOnUserLeaveHintListener()` | Returns `isMediaStoreExternalContentUri`, the sole archive class implementing `isEncodingHighResolutionPcm`; its constructor takes original use-case/repository dependencies | Not integrated |
| 2 | `this.write.MediaBrowserCompatMediaItem.get()` | Factory provider supplies the original `LogLogLevel` implementation; archive class `kotlin.w` implements that interface | Not integrated |
| 3 | `this.write.setPositiveButton.get()` | Original `getDisplaySizeV17` implementation is `kotlin.getIntegerCodeForString` | Not integrated |
| 4 | `this.write.isEnabled.get()` | Original `binarySearchCeil` implementation is `kotlin.areEqual` | Not integrated |
| 5 | `removeEmbeddedStyling.AudioAttributesCompatParcelizer()` | `removeEmbeddedStyling` delegates to `AppModule.INSTANCE.IconCompatParcelizer()`; the module source delegates to `RtspHeadersBuilder.IconCompatParcelizer()`, returning `isSeekPending` | Not integrated |
| 6 | `this.write.setSessionImpl.get()` | Provider for the original `kotlin.Allocator` state container | Not integrated |
| 7 | `updateViewStates.IconCompatParcelizer()` | Delegates to `CoroutinesDispatchersModule.INSTANCE.read()`, returning the original coroutine dispatcher/context abstraction `getPlatform` | Not integrated |

The implementation class identities above are verified by scanning the supplied archive for `implements` declarations. The provider expressions are from the original factory source; this is not an inferred replacement graph. This factory is part of a broad app-wide dependency container and depends on numerous original providers and application repositories. The replica does not include that graph or the corresponding original ViewModelStore/factory wiring, so creating a standalone ViewModel or substituting locally written preferences would not be an exact integration.

### State/event implications

The original constructor initializes a state stream for `TransformationChildLayout` with defaults `null, false, false, false, 0, false` and a separate `ExpandableTransformationBehavior` stream. These constructor defaults are not evidence of the account/course-loaded state. In the original event dispatcher, `MediaBrowserCompatItemReceiver(checked)` updates the Intern Mode state and launches a coroutine; `write.INSTANCE` clears the banner-related state and launches another coroutine; `AudioAttributesCompatParcelizer.INSTANCE` launches a tooltip coroutine; `AudioAttributesImplApi21Parcelizer.INSTANCE` writes the tooltip state false; and `AudioAttributesImplApi26Parcelizer.INSTANCE` resets the Learn More-related state. Coroutine bodies that the decompiler explicitly omits remain unresolved. Batch 68 records the exact construction path but deliberately does not introduce a speculative local ViewModel.

### Original source fingerprints

Fingerprints were computed directly from entries in the uploaded `base.apk_Decompiler.com.zip`:

| Archive source | Bytes | SHA-256 |
|---|---:|---|
| `sources/kotlin/cloneWithUpdatedTimeline.java` | 384455 | `b8229271dbc27ff545421e4dc9ef67c66a96288089065269af14b5d9d63b928d` |
| `sources/com/marrow2/ui/video/landing/VideoLandingViewModel.java` | 199604 | `a57ae71953d5ca86534f5fbe8083930f38028891d9ace152b9ae22a8454a29cd` |
| `sources/kotlin/isMediaStoreExternalContentUri.java` | 56476 | `040bc15050bf66bbc0c16316deae5784f26a72cf62ac110181c00a87120ab704` |
| `sources/kotlin/w.java` | 60263 | `1be9120abacf8f0a160bfae38191f4f5941f2ad8875fe788e4032efc005cfbce` |
| `sources/kotlin/getIntegerCodeForString.java` | 135584 | `53f11363569cf03b444f973d4245eeabac47a33731c5983cbfcaeb31c7149e7a` |
| `sources/kotlin/areEqual.java` | 10985 | `67e781d5ba57f40ee662a06814fe31a3d70ba7b7c12ce70879caf2e805b1348d` |
| `sources/kotlin/maybeSetupTracks.java` | 10556 | `e15f9a28071ddab88c89b981ffb373dc09b3095715c6814fac7cb9cf77b37d41` |
| `sources/kotlin/Allocator.java` | 5149 | `e90d821bb1775baedf5432240985f29b1b7fc07bfd83909656f80f460f589884` |
| `sources/kotlin/getPlatform.java` | 6455 | `716d77e8ca930276b2014049b9a0489ddda35c50ad71421c761f90c56cb890a2` |


