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

## Source-bound ID reconciliation

- Home binding source: sources/kotlin/getNextSegmentHolder.java references 22 IDs. The current Home replica contains 17/22. The five omitted IDs are cvGoPro, goProEd5Ed6, shimmerGoPro, spacePro, and tvGoPro; their names identify the Pro/upsell surface, which remains intentionally excluded by the frozen scope. The core Home IDs (rvHomeCard, shimmerMain, layoutDynamicZenArea, pbModuleCompletion, zenAreaContainer, etc.) are present.
- QBank binding source: sources/kotlin/HlsMediaChunk.java references 2 IDs. The current QBank replica contains 2/2: rvSubjectList (0x7f0a0759) and progressLoadList (0x7f0a06d6).
- Tests binding source: sources/kotlin/getNextMediaSequenceAndPartIndex.java references 9 IDs. The current Tests replica contains 9/9: appbarGTa, collapsing_toolbar, composeGta, emptyLayout, loadingContainer, parent, rvMainList, tabs, and toolbar.
- Videos binding source: sources/kotlin/buildAndPrepareSampleStreamWrappers.java references 43 IDs. The current Videos replica contains all 43 source binding IDs plus the original root ID `parentFrame`, which is present in the genuine binary layout even though it is not a field in the generated binding class. The source IDs include bottomNudgeContainer, clInternModeBanner, btnCloseInternModeBanner, ibTooltip, switchInternMode, tooltipInternModeInfo, and tvInternModeStatus.
- Shell binding source: sources/kotlin/parsePeriod.java references 24 IDs. The current shell contains 22/24; the omitted proCard and tvGoPro IDs are the excluded Pro/upsell surface. The extra non-source shell_root ID was removed.
- Bottom tab item: the original custom_home_tab layout and its inflation/binding references agree on icon, indicator, and title. The separate upperContainer ID belongs to the shell layout, not the tab item.

## Tooltip correction grounded in source

The original tooltip binding in sources/kotlin/getEndTimeUs.java requires btnInternModeToolTipDone, cardInternModeTooltip, container, ivTooltip, tvLearnMore, and txtToolTipBody. The prior replica's tvInternModeTooltipTitle, btnCloseInternModeTooltip, and tvInternModeTooltipDescription IDs do not exist in the original R.java. Batch 59 replaces those invented IDs and the title/close-card structure with the source-bound tooltip hierarchy and original strings/resources.

The original tooltip layout's default body string is text_concise_tooltip_description. Its updated text_concise_tooltip_description_updated is applied by the original state flow; it is not the static default. The original Done label is got_it, the Learn More label is nav_learn_more, and the arrow drawable is tooltip_arrow_v1.

## Limits and acceptance gates

- The layout entries in the decompiler ZIP are Android binary XML, not plain-text XML. A decoded view hierarchy and resource references are evidence; they are not by themselves proof of pixel parity.
- The source references and binding IDs are verified. Full navigation parity, all layout attributes, data-bound list states, screenshot comparison, and emulator runtime pass are still separate gates.
- No educational questions, account state, ads, payment, checkout, subscription, or upsell content is fabricated.

## Result

Core layout/resource references cross-check successfully. Tooltip IDs, hierarchy, text resources, dimensions, and arrow asset have been aligned to the genuine source evidence. Runtime verification remains pending.

## Follow-up source fidelity and CI guard — Batch 60

- Parsed the original binary XML attributes for `tooltip_intern_mode_info`, including its resource-map attribute names and resolved `R.java` symbols, rather than relying only on the layout's tag names.
- Corrected the replica root attributes to match the original resource-map values: `focusable=true`, `focusableInTouchMode=true`, visible state, clickable root, `fillViewport=true`, match-parent dimensions, and `margin_50` horizontal padding. Removed the unsupported `fitsSystemWindows` attribute.
- Restored the original `container` clipping flags, CardView clickability, nested action-row `layout_gravity=end`, and the Learn More end margin. The arrow vector was compared with the archive's actual `tooltip_arrow_v1.xml` and matches its original path.
- Added `.github/scripts/verify_source_bound_layouts.py` and wired it before the Android build. It enforces the exact expected ID set for Home/QBank/Tests/Videos/shell/tab item/tooltip, separately reports explicit Pro exclusions, rejects unknown IDs, parses XML for well-formedness, and checks tooltip string/dimension/drawable references.
- Independent content-level checks against the current GitHub files report all expected required IDs present, no excluded IDs reintroduced, and no unresolved tooltip strings or dimensions.
- Further binary-XML comparisons restored the original Video root ID `parentFrame`, added QBank's original 16dp horizontal RecyclerView margins, aligned the Tests root background/orientation, layout gravity and parent width, and restored the original bottom-tab clipping flags and FrameLayout layout gravity.
- The static regression check is now part of CI. The actual Android build/emulator job still needs to finish successfully before runtime QA can be called PASS.


## Intern Mode fallback colors — Batch 64

- Compared the Intern Mode OFF/ON state branches in the original `sources/kotlin/setScrollPosition.java` against the canonical decompiler archive's `resources/res/values/colors.xml`.
- Original OFF background uses `?attr/backgroundColor`, falling back to `@color/bg_no_guess` (`#f5f5f5`); ON uses `?attr/colorSurfaceVariant13`, falling back to `@color/sepia80` (`#fce795`).
- Restored those exact fallback resources and used them in `MainActivity.updateInternModeVisualState` instead of transparent fallback values. Added a regression assertion to the source-bound verifier.
- This is a narrowly scoped source-evidence correction, not a claim of complete 1:1 parity. Runtime screenshot verification and remaining screen/data/interactions are still outstanding.


## Toolbar bookmark action evidence boundary — Batch 65

- Searched the canonical decompiler archive `base.apk_Decompiler.com.zip` for the exact symbols `iconBookmark` and `R.id.iconBookmark`.
- The only Java/Kotlin occurrences of `iconBookmark` are in `sources/kotlin/parsePeriod.java` (the generated `activity_home_revamp` view-binding class) and the resource symbol declaration in `sources/com/marrow/R.java`. No separate Java/Kotlin click-listener reference to this toolbar view was found by that exact-symbol scan.
- Therefore, the toolbar bookmark's click destination/behavior remains **unverified**. Keep its source-backed visual control, but do not invent a destination, overlay, or navigation action. A broader call-path trace is required before wiring behavior.
- This is a source-evidence boundary, not proof that the original app has no bookmark behavior; obfuscated or indirect binding paths may require further tracing.


## Intern Mode banner event reconciliation — Batch 66

- Traced the original Video landing listener in `sources/kotlin/setScrollPosition.java`: the `ibTooltip` view dispatches `TransformationChildCard.write.INSTANCE`.
- Traced that event in `sources/com/marrow2/ui/video/landing/VideoLandingViewModel.java`: it preserves the Intern Mode flags and clears `showPytBanner`. The source state observer in `sources/kotlin/setScrollPosition.java` applies that state to the bound `clInternModeBanner` view.
- Corrected the replica so `ibTooltip` dismisses `clInternModeBanner` rather than inventing a tooltip-toggle action. The smoke test now checks this source-traced banner dismissal and no longer claims that tapping `ibTooltip` opens the tooltip.
- The tooltip include and Done control remain present, but its exact opening/visibility flow is still unverified. No guessed trigger was added.
- Artifact review of run `38120225475` also found Android ANR dialogs in the screenshots despite the job's green conclusion. Batch 66 expanded the QA guard to reject generic ANR dialogs, and the next run must be reviewed before runtime QA is considered valid.
