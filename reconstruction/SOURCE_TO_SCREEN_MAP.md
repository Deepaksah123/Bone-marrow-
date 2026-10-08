# Bone-marrow — Source-to-Screen Reconstruction Map

Generated from the uploaded original APK/decompiler workspace. This is an implementation map, not a prototype specification.

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

## Resource evidence

The decompiler contains:
- 578 layout XML entries
- 16 landscape layout entries
- 7 sw600dp layout entries
- 2,210 drawable entries
- 216 color entries
- 7 font entries
- values and values-night resources

The resource files in the dump are compiled/binary resource representations in several cases. They are therefore treated as evidence until decoded/converted into build-ready Android source. We will not hand-invent XML from screenshots.

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

Evidence acquisition is complete. The project is now in source-to-screen reconstruction. The next implementation unit is **Batch A (shell/navigation + Home)** followed immediately by build/verification before moving to Batch B.
