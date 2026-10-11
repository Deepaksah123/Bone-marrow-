# Original Marrow UI Source Trace — Batch 59

This is a source-evidence report for the existing Bone-marrow- reconstruction. It does not infer routes from obfuscated names and does not generate content.

## Verified input identity

- Original base.apk SHA-256: e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3
- Decompiler ZIP SHA-256: 92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685
- Decompiler ZIP entries: 26,825
- Java/Kotlin source entries: 20,526
- Resource layout entries: 578
- The APK hash matches the source hash already recorded by the project.

## Source-to-layout map

| Surface | Original layout | Resource ID | Source reference |
|---|---|---:|---|
| Shell | activity_home_revamp | 0x7f0d0033 | sources/kotlin/parsePeriod.java:83 |
| Bottom tab item | custom_home_tab | 0x7f0d0079 | sources/kotlin/zabz.java:2434 |
| Home | fragment_home | 0x7f0d00d9 | sources/kotlin/getNextSegmentHolder.java:79 |
| QBank | fragment_qbank_landing | 0x7f0d00f6 | sources/kotlin/HlsMediaChunk.java:30 |
| Tests host | activity_home_test | 0x7f0d0034 | sources/kotlin/parseLabel.java:30 |
| Tests | fragment_home_test | 0x7f0d00da | sources/kotlin/getNextMediaSequenceAndPartIndex.java:48 |
| Videos | fragment_video_landing | 0x7f0d0106 | sources/kotlin/buildAndPrepareSampleStreamWrappers.java:126 |
| Intern Mode tooltip | tooltip_intern_mode_info | 0x7f0d0227 | resources/res/values/public.xml and sources/kotlin/getEndTimeUs.java binding |

Every listed layout symbol exists in sources/com/marrow/R.java and resources/res/values/public.xml with the same ID, and its binary layout entry exists under resources/res/layout/.

## Source-bound IDs for the four tab surfaces

- Home binding source: sources/kotlin/getNextSegmentHolder.java. It references 22 IDs, including rvHomeCard, shimmerMain, shimmerGoPro, layoutDynamicZenArea, pbModuleCompletion, and zenAreaContainer.
- QBank binding source: sources/kotlin/HlsMediaChunk.java. It references rvSubjectList (0x7f0a0759) and progressLoadList (0x7f0a06d6).
- Tests binding source: sources/kotlin/getNextMediaSequenceAndPartIndex.java. It references appbarGTa, collapsing_toolbar, composeGta, emptyLayout, loadingContainer, rvMainList, tabs, and toolbar.
- Videos binding source: sources/kotlin/buildAndPrepareSampleStreamWrappers.java. It references 43 IDs, including bottomNudgeContainer, clInternModeBanner, btnCloseInternModeBanner, ibTooltip, switchInternMode, tooltipInternModeInfo, and tvInternModeStatus.

## Tooltip correction grounded in source

The original tooltip binding in sources/kotlin/getEndTimeUs.java requires btnInternModeToolTipDone, cardInternModeTooltip, container, ivTooltip, tvLearnMore, and txtToolTipBody. The prior replica's tvInternModeTooltipTitle, btnCloseInternModeTooltip, and tvInternModeTooltipDescription IDs do not exist in the original R.java. Batch 59 replaces those invented IDs and the title/close-card structure with the source-bound tooltip hierarchy and original strings/resources.

The original tooltip layout's default body string is text_concise_tooltip_description. Its updated text_concise_tooltip_description_updated is applied by the original state flow; it is not the static default. The original Done label is got_it, the Learn More label is nav_learn_more, and the arrow drawable is tooltip_arrow_v1.

## Limits and acceptance gates

- The layout entries in the decompiler ZIP are Android binary XML, not plain-text XML. A decoded view hierarchy and resource references are evidence; they are not by themselves proof of pixel parity.
- The source references and binding IDs are verified. Full navigation parity, all layout attributes, data-bound list states, screenshot comparison, and emulator runtime pass are still separate gates.
- No educational questions, account state, ads, payment, checkout, subscription, or upsell content is fabricated.

## Result

Core layout/resource references cross-check successfully. Tooltip IDs, hierarchy, text resources, dimensions, and arrow asset have been aligned to the genuine source evidence. Runtime verification remains pending.