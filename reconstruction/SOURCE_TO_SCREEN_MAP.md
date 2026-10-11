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

The referenced layout files exist in `resources/res/layout/` in the decompiler archive, but they are binary XML rather than readable text XML in this dump. The uploaded original APK contains `resources.arsc`; decoding its resource table and binary XML is the next required gate. The current runtime route from the genuine launcher activity through these generated bindings is not yet proven. The exact screen tree remains unresolved until that trace is complete. Screenshots remain QA only; no XML or tree will be fabricated.

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

Source inventory and six explicit generated inflater-to-layout references are verified. The original APK's `resources.arsc` is present, but this environment has no `aapt`, `aapt2`, `apktool`, or `jadx` executable, and external package installation is unavailable. Do **not** claim the exact screen tree is resolved or change runtime UI based on guesses. Next gate: use an available Android resource decoder against the checksum-verified APK, resolve binary XML/resource IDs, then trace the genuine launcher/navigation path to Home before any UI integration.
