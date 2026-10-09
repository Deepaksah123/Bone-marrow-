# Verified Layout Inflation & View-Binding Evidence — Batch 2

This batch records only direct references found in the user-provided decompiler ZIP for the original APK. It does not infer a full navigation graph or claim that an Android project has been built.

## Source identity

- Target repository: `Deepaksah123/Bone-marrow-` only.
- Original APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`.
- Evidence archive: `base.apk_Decompiler.com.zip`.
- Resource caveat: the decompiler ZIP has decoded-resource files but does not include `resources.arsc`; original APK resource-table cross-resolution and complete binary-XML decoding remain pending.

## Direct layout inflation references

| Layout | Direct source reference | Exact evidence | What is established |
|---|---|---|---|
| `activity_home_revamp` | `sources/kotlin/parsePeriod.java:83` | `layoutInflater.inflate(R.layout.activity_home_revamp, (ViewGroup) null, false)` | A generated binding/helper inflates this layout. |
| `fragment_home` | `sources/kotlin/getNextSegmentHolder.java:79` | `layoutInflater.inflate(R.layout.fragment_home, viewGroup, false)` | A generated binding/helper inflates the home fragment layout. |
| `fragment_home_test` | `sources/kotlin/getNextMediaSequenceAndPartIndex.java:48` | `layoutInflater.inflate(R.layout.fragment_home_test, viewGroup, false)` | A generated binding/helper inflates the test-home fragment layout. |
| `fragment_qbank_landing` | `sources/kotlin/HlsMediaChunk.java:30` | `layoutInflater.inflate(R.layout.fragment_qbank_landing, viewGroup, false)` | Binding helper directly references the QBank landing layout. |
| `activity_qbank_play` | `sources/kotlin/getAllAppIds.java:140` | `super(R.layout.activity_qbank_play)` | An activity base constructor is given this layout resource. |
| `fragment_video_landing` | `sources/kotlin/buildAndPrepareSampleStreamWrappers.java:126` | `layoutInflater.inflate(R.layout.fragment_video_landing, viewGroup, false)` | A generated binding/helper inflates the video landing fragment layout. |
| `activity_lesson_video` | `sources/com/marrow/ui/activities/learn/video/LessonVideoActivity.java:11080` | Returns `Integer.valueOf(R.layout.activity_lesson_video)` | The named lesson-video activity references this layout ID in its source. |

These source paths include obfuscated/generated class names. A direct resource reference proves the reference exists; it does not, by itself, establish the user-facing route or lifecycle owner.

## View-binding evidence

| Layout | Directly bound view IDs found in source | Evidence |
|---|---|---|
| `activity_home_revamp` | `bottomNavigation`, `collegeYearUpdateBanner` | `parsePeriod.java:87-96` begins binding these IDs from the inflated root. |
| `fragment_home` | `barrier`, `clMainInfo` | `getNextSegmentHolder.java:83-88` begins binding these IDs. |
| `fragment_home_test` | `appbarGTa`, `collapsing_toolbar` | `getNextMediaSequenceAndPartIndex.java:49-54` begins binding these IDs. |
| `fragment_qbank_landing` | `progressLoadList`, `rvSubjectList` | `HlsMediaChunk.java:67-72` binds a progress bar and a RecyclerView. |
| `fragment_video_landing` | `bottomNudgeContainer`, `btnCloseInternModeBanner` | `buildAndPrepareSampleStreamWrappers.java:103-108` binds a container and an image button. |

The IDs above are source-backed. Their exact visual styling, constraints, text, colors, drawable resolution, and device-configuration variants require decoded layout/resource evidence.

## Important unresolved items

1. Decode the original APK's binary layout XML and resource table. The decompiler ZIP alone is insufficient to resolve every resource ID and theme/style value.
2. Trace actual activity/fragment transactions, bottom-tab destinations, deep-link routing, and back-stack behavior from source call sites before implementing navigation.
3. Build the Android project skeleton only after the original app module/build configuration and resource dependencies are sufficiently identified.
4. Keep payment, subscription, renewal, checkout, upsell, and advertising interfaces excluded from the reconstruction as already specified.

## Validation status

- Evidence in this batch was checked directly against ZIP source lines.
- No binary XML decode was claimed.
- No APK build or runtime QA was claimed.
- Reconstruction readiness remains **PARTIAL, NOT RESOLVED** until source/resource mapping and the Android project/build are established.
