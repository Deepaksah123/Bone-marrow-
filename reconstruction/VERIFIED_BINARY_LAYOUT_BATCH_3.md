# Verified Binary Layout XML Decode — Batch 3

## Scope and method

- Target repository: `Deepaksah123/Bone-marrow-` only.
- Source archive: user-provided `base.apk_Decompiler.com.zip`.
- Original APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`.
- A local binary-XML chunk parser decoded **616 layout resource files** under `resources/res/layout*` without parser errors. This includes configuration variants and subdirectories; repeated layout names can occur across qualifiers.
- Layout resource IDs were cross-referenced against `sources/com/marrow/R.java`. Direct view IDs and include-layout references were extracted from decoded element trees.
- This is resource evidence, not a completed Android app or runtime validation.

## Core screen layout evidence

| Layout | Resource ID | Root widget | Direct view IDs decoded | Included layouts |
|---|---|---|---|---|
| `activity_home_revamp` | `0x7f0d0033` | `FrameLayout` | 24 | `banner_renew_plan`, `banner_update_college_year_revamp`, `banner_kyc_verify_revamp`, `drawer_menu_revamp` |
| `fragment_home` | `0x7f0d00d9` | `ConstraintLayout` | 22 | `layout_dynamic_zen_area`, `layout_home_cards_shimmer_m2`, `layout_home_lesson_shimmer_m2` (repeated), `layout_home_lesson_shimmer` (repeated) |
| `custom_home_tab` | `0x7f0d0079` | `LinearLayout` | 3 | none |
| `activity_home_test` | `0x7f0d0034` | `FrameLayout` | 1 | none |
| `fragment_home_test` | `0x7f0d00da` | `ConstraintLayout` | 9 | `test_tab_toolbar`, `loader_empty_layout`, `loading_layout` |
| `fragment_qbank_landing` | `0x7f0d00f6` | `ConstraintLayout` | 2 | none |
| `fragment_qbank_introduction_marrow2` | `0x7f0d00f5` | `LinearLayout` | 41 | none |
| `activity_qbank_lesson_list` | `0x7f0d0052` | `FrameLayout` | 1 | none |
| `fragment_qbank_lesson_list` | `0x7f0d00f7` | `ConstraintLayout` | 19 | `item_type_qbank_progress` |
| `activity_qbank_play` | `0x7f0d0053` | `FrameLayout` | 1 | none |
| `activity_qbank_score` | `0x7f0d0054` | `FrameLayout` | 1 | none |
| `fragment_qbank_tracker` | `0x7f0d00f8` | `LinearLayout` | 23 | none |
| `activity_qbank_tracker` | `0x7f0d0055` | `FrameLayout` | 1 | none |
| `activity_test_introduction_marrow2` | `0x7f0d0065` | `FrameLayout` | 1 | none |
| `fragment_test_introduction_marrow2` | `0x7f0d0102` | `FrameLayout` | 20 | `layout_test_instruction` |
| `fragment_test_score` | `0x7f0d0103` | `CoordinatorLayout` | 20 | score/rank, time, guess, answer-change and previous-NEET analytics layouts |
| `fragment_test_analytics` | `0x7f0d0101` | `CoordinatorLayout` | 14 | `view_rank_details_analytics`, `view_score_card_analytics` |
| `activity_gt_analytics` | `0x7f0d0032` | `FrameLayout` | 1 | none |
| `fragment_video_landing` | `0x7f0d0106` | `FrameLayout` | 44 | continue-watching, horizontal video components, watch-next and intern-mode tooltip layouts |
| `fragment_video_lesson_list` | `0x7f0d0107` | `ConstraintLayout` | 16 | none |
| `activity_lesson_video` | `0x7f0d003b` | `ConstraintLayout` | 25 | `layout_lesson_video_bottom` |
| `fragment_video` | `0x7f0d0105` | `ConstraintLayout` | 38 | interactive-video orientation switch and options feature-discovery layouts |
| `fragment_downloaded_video_list` | `0x7f0d00d7` | `ConstraintLayout` | 18 | none |
| `fragment_video_notes` | `0x7f0d0108` | `FrameLayout` | 5 | none |
| `sample_videos` | `0x7f0d0212` | `LinearLayout` | 8 | none |
| `activity_bookmark_landing` | `0x7f0d0022` | `FrameLayout` | 1 | none |
| `activity_custom_module_creation` | `0x7f0d0027` | `FrameLayout` | 1 | none |
| `activity_theme_selection` | `0x7f0d0067` | `FrameLayout` | 1 | none |
| `activity_main_settings` | `0x7f0d003c` | `FrameLayout` | 1 | none |
| `fragment_profile_landing` | `0x7f0d00f3` | `ConstraintLayout` | 38 | `profile_image_v2`, `plan_upgrade_card` |
| `fragment_better_search` | `0x7f0d00c7` | `ConstraintLayout` | 18 | none |

## Source-backed findings

- `activity_home_revamp` is inflated through `R.layout.activity_home_revamp` at `sources/kotlin/parsePeriod.java:83`.
- Its binding helper directly looks up `bottomNavigation`, `collegeYearUpdateBanner`, `cvBottomNavigationContainer`, `drawerLayout`, `drawerMenu`, `fullContainer`, `homeAppBar`, and other IDs at `parsePeriod.java:87-125`.
- The binding helper casts `bottomNavigation` to **`TabLayout`**. Do not replace it with a `BottomNavigationView` based on assumption.
- `fragment_qbank_landing` contains `rvSubjectList` and `progressLoadList`; binding references are present in `sources/kotlin/HlsMediaChunk.java:34-38` and `sources/kotlin/deriveAudioFormat.java:92-93`.
- `activity_qbank_play` is a `FrameLayout` host; the layout alone does not establish its question-play behavior.
- `fragment_video_landing` contains both standard Android views and a ComposeView in its decoded tree.
- `activity_lesson_video` is referenced in `com.marrow.ui.activities.learn.video.LessonVideoActivity.java:11080`.

## Exclusion and fidelity guardrails

The original home shell references renewal and plan-related banner resources. These are evidence of original resource composition, **not permission to reproduce excluded interfaces**. Renewal, payment, subscription, checkout, upsell, and advertising interfaces remain excluded from the reconstruction as previously specified.

## Limits and next work

1. The resource hierarchy and view IDs are decoded; theme/style/dimension/color values still require authoritative framework attribute and configuration-aware resource-table resolution.
2. The decompiler ZIP does not include `resources.arsc`; the original APK does. No Android build tools or offline AXML/ARSC library are installed, and package installation failed because DNS/network access is unavailable in this environment.
3. Actual activity/fragment transitions, deep links, and back-stack behavior still need source-call tracing before implementation.
4. No Gradle Android project was added, no APK was built, and no runtime screenshot QA was claimed. Readiness remains **PARTIAL, NOT RESOLVED**.
