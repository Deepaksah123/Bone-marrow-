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

The inspected `base.apk_Decompiler.com.zip` contains 26,825 entries and 2,371 `.xml`-suffixed entries overall, but **zero paths under `res/` and no Android layout XML inventory**. Therefore earlier counts of 578 layout XML, 16 landscape layouts, 7 `sw600dp` layouts, 2,210 drawables, 216 colors and 7 fonts are not substantiated by this archive and must not be used as implementation evidence until independently matched to the original APK/resource table.

Names in the domain table above are candidates, not verified resource paths. `reconstruction/EXACT_SOURCE_UI_INDEX.md` records exact source paths and the verified archive boundary. The exact screen tree remains blocked on decoding the original APK's `resources.arsc` and binary XML or acquiring a checksum-verified decoded-resource dump. Screenshots are QA only; no XML or tree will be fabricated.

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

Source class inventory is available, but exact resource/layout evidence is not yet complete. Do **not** claim the exact screen tree is resolved or start fabricating UI. Next gate: decode and cross-reference original `resources.arsc`/binary XML; then trace shell/navigation and Home with source-line evidence before implementation.
