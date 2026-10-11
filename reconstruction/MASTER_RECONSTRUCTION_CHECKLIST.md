# Reconstruction Master Checklist

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Updated:** 2026-10-11  
**Status:** Home, Tests, Video-root and shell hierarchy batches compile and pass the evidence guard; included subtrees, runtime behavior and visual parity remain incomplete.

## Verified completed

- [x] Batch 56: wired the source-bound Video Intern Mode banner-close and tooltip affordances from the original binding/event trace; ViewModel state and persistence remain incomplete. Details: `reconstruction/VIDEO_LANDING_SOURCE_INTERACTION_BINDINGS_BATCH_56.md`. Build, guard and emulator verification are tracked separately.


- [x] Original source evidence inventory and binary-layout decode report recorded in `reconstruction/EXACT_SOURCE_UI_INDEX.md` and `reconstruction/VERIFIED_BINARY_LAYOUT_BATCH_3.md`.
- [x] Evidence guard now verifies SHA-256 for the exact source Lottie JSON, mdpi logo WebP and dark Zen gradient, checks the layout references and source-qualified 4dp/28dp dimensions, and fails if the incorrect pattern-gradient substitute is reintroduced.
- [x] Four top-level tabs and source-backed order recorded: HOME → QBANK → TESTS → VIDEOS.
- [x] Batch 30: existing selected-tab save/restore verified; optional RecyclerView roots null-checked before layout-manager setup. Details: `reconstruction/TAB_STATE_AND_OPTIONAL_VIEW_GUARDS_BATCH_30.md`; build run `38075394178` passed, guard run `38075448081` passed, artifact `11678014087`, ZIP SHA-256 `ba1d4d81b109dc4e1aa8d6a75ec231129df8f78968378c706a2a46296e344de5`.
- [x] Batch 40: six shell/Home backgrounds changed to source `?attr/backgroundColor` using verified light/dark mappings. Details: `reconstruction/HOME_THEME_BACKGROUND_ATTR_BATCH_40.md`; build run `38075586947` passed, latest guard run `38075758945` passed, artifact `11677674404`, artifact ZIP SHA-256 `5880ced6c26df6bdc6650a4e328e6aaeff87b9a7bf161e631d47eb538ad65236`; embedded APK ZIP/signature checks passed, APK SHA-256 `b43993b0b7b3ce2c2d7e06c4ef93bf4526a9c4f10984cac02537bc2d13958f7e`. Device installation and visual QA remain pending.
- [x] Batch 41: downloaded the build artifact and verified ZIP integrity, APK ZIP integrity, debug signing, and distinct application ID `com.marrow.reconstruction.replica` vs. original `com.marrow`. Details: `reconstruction/APK_INSTALLABILITY_PREFLIGHT_BATCH_41.md`; actual device installation and first-launch QA remain pending.
- [x] Tab destination/root-layout mappings documented in `reconstruction/HOME_TAB_TO_ROOT_LAYOUT_MAP_BATCH_9.md`.
- [x] QBank landing replica has the verified `ConstraintLayout` root and source-bound IDs `rvSubjectList`, `progressLoadList`.
- [x] Test landing replica includes source-bound `test_tab_toolbar`, `loader_empty_layout`, and `loading_layout` containers.
- [x] Video landing replica includes several source-bound view IDs, including `clMain`, `epoxyRVSubject`, and the documented deck/bookmark/sample-video containers.
- [x] Navigation batch commit `7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b` replaces the prior per-tab `replace()` flow with separate tagged tab fragments and add/show/hide behavior: [commit](https://github.com/Deepaksah123/Bone-marrow-/commit/7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b).
- [x] Navigation follow-up commit `1ef4db62408ad188f2a760eda92d5d2b4ba85f45` aligned tags with the decompiler's destination class aliases; Batch 65 corrects those runtime tags to raw DEX `o.*` names (`Home_o.*`) because `copyToBuffer.write(Class)` uses `Class.getName()`. Local wrapper Fragment classes remain a reconstruction boundary, not original implementations.
- [x] Tests layout follow-up commits `871337b330bde3dc132f9c9587be9fe092cab08f`, `9b4b8102686733c4ce44d664bacfc60561b476aa`, and `7f5b27b778e77bdfc6c19ffccb06b1894d1103aa` align the app-bar ID to source-bound `appbarGTa`, repair its constraint references, and add source-bound `collapsing_toolbar`; wrapper class/attributes remain unverified.
- [x] Recovered `base.apk` and `base.apk_Decompiler.com.zip` from the Library in this session; verified SHA-256 values against the original evidence record. The original APK contains `resources.arsc`; the decompiler ZIP still omits that table.
- [x] Added `reconstruction/DECODED_CORE_LAYOUT_HIERARCHY_BATCH_20.md` with decoded IDs and include trees for Home, shell, Tests, QBank and Videos.
- [x] Rebuilt the Tests root hierarchy around source-backed `toolbar`, `tabs`, `parent`, `appbarGTa`, `collapsing_toolbar`, `composeGta`, `emptyLayout`, `loadingContainer`, and `rvMainList`; copied original text-based vector assets and added the Compose UI dependency required by the source ComposeView.
- [x] Replaced generic hand-built Home cards with `fragment_home_replica.xml`, based on the decoded original Home hierarchy. Original source-derived strings/icons are used; account progress and lesson data remain unpopulated.
- [x] Home module-completion widget geometry/style corrected from the verified original binary XML: bottom badge margin, 70dp autosizing number, 90dp progress ring, 24dp top margin, 100/100 progress, and source Headline1/Headline5 styles. Details: [Batch 24](HOME_COMPLETION_WIDGET_BATCH_24.md). Fresh CI validation pending.
- [x] Restored the original Home shimmer include tree (one cards skeleton, six Edition-2 lesson skeletons and six legacy lesson skeletons), source colors/dimensions, rounded card background and two source icon vectors. No lesson/account content is populated. Details: [Batch 25](HOME_SHIMMER_SUBTREE_BATCH_25.md). Build passed for commit `2151f4e6ded5`: [run 38072310626](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072310626). Artifact ID `11676808919`, digest `sha256:f50ed94b1ce4e509c3df4883c58a4d96af0a0dc867863ff11bca3bae786c9f49`. Source evidence guard passed: [run 38072310571](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072310571).
- [x] Tests landing geometry corrected from decoded source: fixed 48dp tabs, source light/dark tab surface colors, AppBar padding/elevation, CollapsingToolbar margins, ComposeView spacing, list height/bottom padding, and toolbar icon/title sizing. Details: [Batch 26](TESTS_LANDING_GEOMETRY_BATCH_26.md). Evidence guard passed [run 38072602160](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072602160); Android build passed for `6bc87b41ed7d` [run 38072593877](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072593877). Artifact ID `11677153986`, digest `sha256:57f7d93793e5713bf45c6e3e1143fc291aa3deeb8e948b76f36a766bf56a0933`.
- [x] Video landing visible controls aligned to source: Intern Mode theme/spacing, switch/tooltip tints, subject header, sort controls, 14dp grid padding and centered piracy footer. Details: [Batch 27](VIDEO_VISIBLE_CONTROLS_BATCH_27.md). Evidence guard passed [run 38072839299](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072839299); Android build passed [run 38072831065](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38072831065). Artifact ID `11677224204`, digest `sha256:1bec4f25351f16041d658dfc74e4d7a911c10c50469020e4218e80c8e0c5465e`.
- [x] Corrected Video landing include mapping: continue-watching ID now includes its resume/progress card; watch-next ID now includes the separate watch-next card. Scroll content uses theme background. Details: [Batch 28](VIDEO_CARD_INCLUDE_MAPPING_BATCH_28.md). Android build passed [run 38074064454](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074064454), artifact ID `11677922158`, digest `sha256:7944050e0eb69336c69ef5736850f1972ca60f972e95e6756b2daad83b64b30a`. Evidence guard passed [run 38074106241](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074106241).
- [x] Switched all four home tabs from synthetic programmatic screens to their source-shaped XML root layouts; existing shell header and bottom navigation are preserved. Missing adapters/Compose bindings remain explicit gaps; no fake educational data is generated. Details: [Batch 29](ALL_HOME_TABS_SOURCE_ROOTS_BATCH_29.md). Evidence guard passed [run 38074219308](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074219308); Android build passed [run 38074210922](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074210922). Artifact ID `11678411729`, digest `sha256:e28b72976cc7360079706b7dcf1a01b7256371ecc51151c4026d16b188a89821`.
- [x] Restored a dedicated source-shaped Continue Watching card layout and five exact source drawables (thumbnail logo, play icon/circle, dismiss icon and progress drawable). The main `layoutVideoWatchNextCard` now points to the dedicated source layout. Details: [Batch 36](VIDEO_CONTINUE_WATCHING_CARD_BATCH_36.md).
- [x] Restored the distinct bottom-nudge Watch Next card, exact source placeholder vector and right-arrow PNG, and mapped the source Watch Next string/theme. The two source include IDs now map to separate layouts. Details: [Batch 37](VIDEO_WATCH_NEXT_BOTTOM_NUDGE_BATCH_37.md). Both remain hidden until runtime data/visibility binding is reconstructed. Evidence guard passed [run 38073315067](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38073315067); Android compile and APK upload passed [run 38073302955](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38073302955). Artifact ID `11678100530`, digest `sha256:84ea7c9f6a3732e522460ffe94479e3888954a3653d1a03313d252c3329f44ab`.
- [x] Main shell toolbar and bottom navigation aligned to source: theme backgrounds, action-bar sizing, menu/search/bookmark dimensions, centered page title, Headline5/4 styles, divider color, scrollable tab configuration and 8dp full-container margin. Details: [Batch 30](SHELL_TOOLBAR_BOTTOM_NAV_BATCH_30.md). Build passed [run 38074210922](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074210922), artifact ID `11678411729`; guard passed [run 38074219308](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074219308).
- [x] Custom Home tab item now follows decoded `custom_home_tab` structure: 20dp icon/indicator overlay, source `icon`/`indicator`/`title` IDs, source text style and spacing. Build passed [run 38074210922](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074210922), artifact ID `11678411729`; guard passed [run 38074219308](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074219308). Details: [Batch 31](CUSTOM_HOME_TAB_BATCH_31.md).
- [x] Added CI guards for all four decoded root classes and direct-ID counts: Home 17 non-monetization IDs, QBank 2, Tests 9, Videos 44. Details: [Batch 32](FOUR_TAB_ROOT_ID_AUDIT_BATCH_32.md). Evidence guard passed [run 38074402816](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074402816); implementation build remains validated by [run 38074210922](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074210922).
- [x] Removed dormant synthetic screen builders from `MainActivity`; active tabs now use only source-shaped XML roots, with source-backed list layout managers retained. CI guard also prevents reintroduction of synthetic builders. Details: [Batch 33](REMOVE_SYNTHETIC_TAB_BUILDERS_BATCH_33.md). Android build passed [run 38074469213](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074469213), artifact ID `11678407183`; corrected evidence guard passed [run 38074557943](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074557943).
- [x] Restored source AppThemeV2 semantic attribute mappings for light/dark palettes, text styles and video progress style. Light build passed [run 38074564411](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074564411); dark build passed [run 38074568348](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074568348), artifact ID `11677648227`, digest `sha256:731fef107ec8d86bd51611272684921ec3486c39e1e32e3def74edbba58f1ac2`. Details: [Batch 34](APPTHEMEV2_LIGHT_DARK_MAPPING_BATCH_34.md).
- [x] Updated home-tab transactions to remove inactive `Home_` fragments and add/show the selected destination in `upperContainer`, matching the source helper trace. Details: [Batch 35](HOME_FRAGMENT_TRANSACTION_FIDELITY_BATCH_35.md). Build/guard pending.
- [x] Corrected Video Intern Mode to source `colorSurfaceVariant13` with exact light/dark colors, restored `SwitchTheme`, and added source watch-next top/gone margins. Details: [Batch 36](VIDEO_INTERN_MODE_SOURCE_VALUES_BATCH_36.md). Build/guard pending.
- [x] Home dynamic Zen include now references the exact source Lottie JSON, mdpi circle-logo WebP and source gradient XML; the completion label's sibling position, 21dp bottom padding, 4dp progress-label top margin, vertically centered title, and source-qualified 4dp / API 35 28dp content top margin were corrected from binary XML. The distinct 296,606-byte pattern vector remains a documented transfer gap and is not replaced with another image. Full asset hashes and limitations are recorded in [Batch 23](HOME_DYNAMIC_ZEN_EXACT_ASSET_BATCH_23.md). A temporary unverified raster substitute was removed before finalizing source assets.
- [x] The previous code build at `ed1d2c860f38` passed: [run 38057383849](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057383849), artifact ID `11671933327` (8,180,745 bytes; digest `sha256:071fb864cfda06ecd2cd11bb22e82497f55aa44c0fcfeebcacb283fe2d18acf6`). The latest Body2 style update is commit `5da1cbc59a53`; its evidence guard passed [run 38057531575](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057531575) and Android build passed [run 38057531540](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38057531540). Latest debug APK artifact ID `11672053446`, size 8,179,949 bytes, digest `sha256:d6b32d8e40dd64ed150d9f76a002e18c424d89bf0aaafbe571fb7068ce9e15ad`. The Zen content top-margin dimension, 21dp bottom padding and 4dp label top margin now use the exact source attributes; the guard checks these placements. Layout commit `3d8bc391738c` build passed: [run 38071524241](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38071524241). Evidence guard passed for the top-margin correction [run 38071531370](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38071531370) and checklist follow-up [run 38071542304](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38071542304). The original decompiler ZIP and APK are now recovered from the Library and checksum-verified. The light/dark pattern vectors are confirmed at 296,606 / 298,407 bytes, but the generated drawable aliases they reference must be resolved before safe integration. No substitute pattern artwork is used. Original Roboto font files remain absent from the app resources.
- [x] Home hierarchy build and evidence guard passed for commit `8bf4caa70cf08324b5f9a990b9a524b7a98edbee`: [build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054999183), [guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38054999216). Artifact ID `11670879127`, digest `sha256:b4c12d6cd93b238595002705c60b73fb5d71dcec36f1c1d24c81c146ba793f24`.
- [x] Shell hierarchy commits `28059ddbdacc840e44f06c78a14f3b14dde144cc` and `6f491199731a710661bb9e16d2ee8553611ded7a` separate `upperContainer` and `fullContainer`, restore source-bound shell IDs and render the original menu PNG at runtime. The selected-tab indicator and light/dark divider/elevation attributes are also source-derived.
- [x] Video landing root rebuilt from decoded source with **44/44 source-bound IDs**; uses `EpoxyRecyclerView`, responsive 2-column phone / 3-column tablet grid, original source-derived labels/icons, and empty hosts instead of invented lessons: [Video batch report](VIDEO_LANDING_ROOT_RECONSTRUCTION_BATCH_21.md).
- [x] Shell source hierarchy and theme behavior recorded in [Batch 22 report](SHELL_ROOT_RECONSTRUCTION_BATCH_22.md); shell ID coverage is 22/22 non-monetization IDs. Drawer menu content remains unimplemented because its source layout file is absent from the decompiler ZIP.
- [x] Latest combined Home/Tests/Video/shell code build succeeded for commit `2d9b435299fa`: [Android build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616041), [evidence guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38055616024).
- [x] Latest debug APK artifact uploaded: `marrow-reconstruction-debug`, artifact ID `11671950435`, SHA-256 `f732ff3b05304e31c82db01e3bda0e96a71fd1befb7a69cf8a1608622ab6576f`.
- [x] Android debug build compiled and assembled successfully for navigation commit `7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b`: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38052847889).
- [x] Evidence guard passed for navigation commit `7ff041d7c84a4d7b8a4cfc095e2322ad11c4296b`: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38052847844).
- [x] Debug APK artifact uploaded: `marrow-reconstruction-debug`, artifact ID `11669882167`, SHA-256 digest `f8adf9e46a32741851a59563ed3cb61e192c08e7248257a342c8dab1e773d921` (artifact is available from the build run above).
- [x] Existing app-bar title/header restored in commit `84d79c004840ddcae485ce61c5ba171ce50547ae`; do not remove existing UI merely because a detail is not yet verified.
- [x] Android debug build succeeded for commit `84d79c004840ddcae485ce61c5ba171ce50547ae`: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38029001898).
- [x] Reconstruction evidence guard succeeded for the same commit: [GitHub Actions run](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38029001876).
- [x] Ads, subscriptions, upgrades, renewals, payment/checkout and upsell interfaces are explicitly out of scope.
- [x] No invented question banks, subjects, lessons, or user-account progress are populated.

- [x] Corrected bottom-navigation `SmallText2` to the source Caption inheritance (10sp text, 12sp line height, medium weight). Details: [Batch 39](TYPOGRAPHY_CAPTION_BATCH_39.md). Guard passed [run 38074841342](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074841342); Android build passed [run 38074833753](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074833753), artifact ID `11678038295`, digest `sha256:c189dfa232bf9bd857b8cf60ef61a9919145b7b58aa97486b54eb320355e3936`.

## Remaining work — do not mark complete until verified

- [x] Decoded and resolved the original APK `resources.arsc` (3,327,896 bytes; package `com.marrow`) and cross-checked source `colors.xml`, `dimens.xml`, `attrs.xml`, and `styles.xml`. Source palette, key light/dark theme mappings and typography metrics are restored. Details: [Batch 38](RESOURCE_TABLE_RESOLUTION_BATCH_38.md). Build passed [run 38074568348](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074568348), artifact ID `11677648227`, digest `sha256:731fef107ec8d86bd51611272684921ec3486c39e1e32e3def74edbba58f1ac2`; latest guard passed [run 38074590738](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074590738). Source font binaries and per-activity theme selection remain pending.
- [ ] Complete Home hierarchy fidelity: main view tree and direct IDs are source-derived, and shared palette/dimensions now resolve from the original resource table. Included Zen pattern asset transfer, exact constraints, per-activity theme selection and runtime visibility still need work. Keep monetization UI excluded and do not fabricate account progress.
- [ ] Finish the `activity_home_revamp` shell hierarchy: the main container relationship and source IDs are restored, but drawer content, exact header/action sizing, toolbar state, dimensions/styles and original runtime navigation remain incomplete.
- [ ] Compare every implemented screen against the original APK on a device/emulator. Current build success is **not** proof of visual parity.
- [x] Root ID coverage audit completed: Home non-monetization IDs 17/17, QBank 2/2, Tests 9/9, Videos 44/44, shell 22/22 non-monetization IDs.
- [ ] Complete included-layout subtree, attribute, drawable and configuration-qualifier audits against the original archive.
- [ ] Finish exact navigation fidelity: current implementation uses local wrapper fragment classes and source-shaped add/show/hide transactions; it is not yet proven equivalent to the original obfuscated destination classes, saved state, back-stack, or all transitions.
- [ ] Trace and implement source-backed loading/empty states, back navigation, saved selection, and screen transitions from decompiled source.
- [ ] Run build + evidence guard after every implementation batch and inspect the latest artifact.
- [ ] Verify the APK installs and opens on the target Android version/device; record the result and artifact checksum.
- [ ] Update this checklist with commit links and QA evidence after each completed batch.


## Batch 47 — Tests initial loading state

- [x] Implemented source-backed initial Test landing loading presentation: hide the empty test list, show the original loading container, and keep the empty-state host hidden until real data state is available. No test cards or results were invented. Details: [Batch 47](TESTS_INITIAL_LOADING_STATE_BATCH_47.md).
- [x] Android build [38077629617](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077629617) and evidence guard [38077629680](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077629680) passed for code commit `53ce875754dc`. Artifact ID `11679262916`, size `8,194,557` bytes, SHA-256 `3802fc314cb80fc843bde0bd2a76cd451dc958bcdbc12461941306cb9da59b59`. Device-level QA remains pending.


## Batch 48 — Video scroll content theme correction

- [x] Fixed a nested background mismatch missed by the broad theme guard: `clMain` inside the Video landing scroll view now resolves `?attr/backgroundColor` instead of hard-coded `@color/shell_background`. Details: [Batch 48](VIDEO_SCROLL_CONTENT_THEME_BACKGROUND_BATCH_48.md).
- [x] Android build [38078006253](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006253) and evidence guard [38078006278](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006278) passed on commit `884aaf01821899e0c5fd7c7dcc0f7b22f74a4b8e`. Artifact ID `11678864090`, size `8,195,237` bytes, artifact ZIP SHA-256 `fadbe68bceb34a26f8db64c07e519067ab0e1073f50f7ca0b8fe924230911fb7`. Device-level light/dark screenshots and pixel comparison remain pending.

## Guardrails

1. Only use this repository for implementation: `https://github.com/Deepaksah123/Bone-marrow-`.
2. Original APK resources and decompiled source are the source of truth. Screenshots are QA references, not implementation evidence.
3. Preserve existing UI and functionality unless direct source evidence establishes the correct change. **Unknown means investigate, not delete.**
4. Do not claim 1:1 completion without original-resource comparison and runtime visual QA.
5. Do not fabricate educational content, account data, screen labels, or interactions to fill empty space.
6. Keep excluded monetization and advertising UI out of the reconstruction.


## Batch 42 — shell/drawer audit

- [x] Audited original shell/drawer behavior against the checksum-verified decompiled source. Confirmed the current drawer include is an empty host, and menu/search/bookmark handlers are incomplete. Recorded exact source classes, binding IDs, exclusions, and safe next steps in [Batch 42](SHELL_AND_DRAWER_GAP_AUDIT_BATCH_42.md). No guessed drawer rows or destinations were added. Original drawer XML is missing from the decompiler dump; recover it from verified binary resources before implementing the drawer. Static audit only; no runtime behavior is claimed.


## Batch 43 — source tab appearance

- [x] Recovered the HOME-only bookmark visibility flag and theme-aware selected/unselected tab tint from the original `DataBuffer.java` / `zabz.java` source. Implemented the visual state and added guard assertions in [Batch 43](HOME_TAB_TINT_AND_BOOKMARK_VISIBILITY_BATCH_43.md). Bookmark click routing remains a documented gap; this batch does not claim full toolbar functionality.


## Batch 44 — compile-failure correction

- [x] Fixed Batch 43's Java compilation failure by resolving `colorPrimary` through the Material library's non-transitive R namespace; updated the guard to match. Failure and fix recorded in [Batch 44](THEME_ATTR_COMPILATION_FIX_BATCH_44.md). Build passed in [run 38076939681](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38076939681); evidence guard passed in [run 38076939536](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38076939536). Artifact ID `11678571578`, size `8,194,359` bytes, SHA-256 `beef4e4bb441851130b8c5804b2651dbfbfe26ac34315f098dd17836d70801c47`.


## Batch 45 — Home initial loading state

- [x] Restored the source-backed Home initial loading state: hide the empty home-card RecyclerView and show the original shimmer skeleton while real card data/adapters remain unrecovered. Source trace is recorded in [Batch 45](HOME_INITIAL_LOADING_STATE_BATCH_45.md). Android build [38077165155](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077165155) and evidence guard [38077165079](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077165079) passed. Artifact ID `11678926576`, size `8,194,419` bytes, SHA-256 `e74a9aa88d29536871dfce5578df4c9590d0b896d825f19e04e1bfb37d4a735a`. This is not a claim of live data loading; the skeleton remains visible until real source-backed binding is implemented.


## Batch 46 — QBank initial loading state

- [x] Matched the original QBank loading observer: hide the empty subject RecyclerView and show `progressLoadList` until the real subject list arrives. Evidence: [Batch 46](QBANK_INITIAL_LOADING_STATE_BATCH_46.md). Android build [38077287838](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077287838) and evidence guard [38077287841](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077287841) passed. Artifact ID `11678636989`, size `8,194,476` bytes, SHA-256 `7f3b2663e1b48aa9aa145795457e3eea770c357730245a53e8554a192dbe9fbe`. No subject data was fabricated.


## Batch 49 — Video subject grid fidelity

- [x] Matched the original Video landing grid behavior from `setScrollPosition.java`: exact tablet detection semantics, 2/3-column grid, predictive animations disabled, and 6dp vertical / 4dp horizontal item offsets. Added the source-backed `margin_6dp` dimension and guard checks. Details: [Batch 49](VIDEO_SUBJECT_GRID_FIDELITY_BATCH_49.md). Android build [38078006253](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006253) and evidence guard [38078006278](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006278) passed. Artifact ID `11678864090`, size `8,195,237` bytes, artifact ZIP SHA-256 `fadbe68bceb34a26f8db64c07e519067ab0e1073f50f7ca0b8fe924230911fb7`. Device-level phone/tablet visual QA remains pending.


## Batch 50 — Home Zen pattern dependency audit

- [x] Verified the original source archive SHA-256 and audited both pattern vectors. Each has 360 alias references; all 720 references resolve, and every alias file is byte-identical (SHA-256 `4e97644184ec5bdbbf46d83155bf86b85329a4fd7870f5f42bdc298d7716afa6`). Details: [Batch 50](HOME_ZEN_PATTERN_DRAWABLE_DEPENDENCY_AUDIT_BATCH_50.md).
- [ ] Implement the source-equivalent vector/gradient resource reduction and wire the original light/dark pattern. The audit did not change app resources; build/guard and device visual QA are still required.


## Batch 51 — QBank root and spinner fidelity

- [x] Restored the original QBank root's theme-aware background, match-parent subject-list width, disabled nested scrolling, source LinearLayoutManager XML attribute, and original `rotate_progress_drawable_blue` spinner drawable from the verified source archive. Targeted guard added. Details: [Batch 51](QBANK_ROOT_AND_SPINNER_FIDELITY_BATCH_51.md). Android build [38078412747](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078412747) and evidence guard [38078412756](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078412756) passed. Artifact ID `11678498594`, size `8,196,390` bytes, SHA-256 `b8cc5a081cc906855a361d34f60dc8acca950bc851b67cdee28a468cef6b175b`.


## Batch 52 — drawer evidence boundary + emulator UI smoke

- [x] Removed speculative drawer rows, then recovered the original `drawer_menu_revamp` binary XML from the SHA-verified original APK and reconstructed the source-backed hierarchy. Details: [Batch 52](DRAWER_EVIDENCE_BOUNDARY_AND_UI_SMOKE_BATCH_52.md) and [Batch 53](DRAWER_BINARY_XML_RECOVERY_BATCH_53.md).
- [x] Added CI evidence-guard checks to prevent the speculative drawer rows/labels from returning before source recovery. Updated guard result must be checked on the current HEAD.
- [x] Added an Android API 34 emulator smoke workflow to launch the app, verify HOME/QBANK/TESTS/VIDEOS labels and source-backed root/loading IDs, tap through tabs, verify app-process survival, exercise the drawer-open action, and capture per-tab UI hierarchy dumps/screenshots plus light/dark Home screenshots for QA. Workflow: [Android UI smoke](../.github/workflows/android-ui-smoke.yml).
- [ ] Confirm the latest emulator smoke run, inspect all four screenshots and hierarchy dumps, and fix any runtime failures. Latest smoke run [38082552298](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082552298) is the current tab/drawer/theme QA run; inspect its final result and screenshot artifact.
- [ ] Do original-APK screenshot/pixel comparison after source-exact UI is recovered; CI screenshots alone do not prove 1:1 fidelity.

## Batch 53 — original drawer binary XML recovery

- [x] Retrieved and SHA-256 verified the original APK and decompiler ZIP against the recorded hashes.
- [x] Mapped `R.layout.drawer_menu_revamp` (`0x7f0d00b3`) to the original obfuscated APK entry and decoded its 10,056-byte binary XML.
- [x] Reconstructed source-backed drawer IDs, profile/course header, footer and non-monetization rows; restored the original small drawer assets and required theme/dimension/string resources.
- [x] Kept purchase, Buy Notes, Add Videos, referral-coupon/extension, Pro badge, and debugging/logout UI excluded.
- [x] Current Android build passed: [run 38082219855](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082219855); current evidence guard passed: [run 38082552280](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082552280).
- [ ] Finish emulator smoke [run 38082552298](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082552298), inspect screenshot artifacts, and resolve any runtime failures. Source-row visibility/data-binding and click destinations remain open.
- [ ] Recover the original Practical Corner landing pattern resource family into build-ready resources; no vector data was fabricated. Source tracing shows this pattern is applied by PracticalCornerLandingFragment, not the Home root's hidden ivEd6background.


## Batch 56 — source-traced Better Search overlay

- [x] Recovered the original search route: toolbar `iconSearch` opens the Better Search fragment in `fullContainer` with back-stack navigation and source slide animations.
- [x] Added the source-shaped search UI and source drawable/animation resources; back and clear controls work, and the initial message/hint use source strings.
- [x] Excluded the source `clProMain` / `btViewPlans` monetization subtree.
- [x] Status bar uses source `?attr/colorPrimary`; light/dark icon contrast follows the source theme flags.
- [x] Android build PASS: [run 38086133865](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133865); evidence guard PASS: [run 38086133816](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133816).
- [x] Debug APK Actions artifact ZIP: ID `11682261632`, ZIP size `8,269,398` bytes, SHA-256 `8aa289841eeb52239d3b069d329a909f76515ec33e059748512fa20d25d31d7f`.
- [ ] API 31 emulator smoke [run 38086133823](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133823) is still running; Search open/Back screenshot QA remains pending.
- [ ] Search data adapter, query API, recent-search history and original-APK pixel comparison remain open.
- Details: [Batch 56 report](SEARCH_OVERLAY_SOURCE_UI_BATCH_56.md).

## Batch 55 — Home Zen progress integrity + emulator smoke fix

- [x] Removed the hard-coded `9/35 modules` value from `layout_dynamic_zen_area_replica.xml`; source account progress remains empty until its real data binding is recovered.
- [x] Updated the evidence guard to reject a static `9/35 modules` value.
- [x] Fixed emulator-runner POSIX shell startup: `set -euo pipefail` failed because the action runs scripts through `sh`; now uses portable `set -eu`.
- [x] Evidence guard passed for the workflow-fix commit: [run 38084717980](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38084717980).
- [ ] Confirm build + evidence guard for the Home XML/guard correction commits `a23376b` / `9e0f51e`, then inspect the newest emulator smoke run and its screenshot/hierarchy artifact.
- [ ] Original-APK pixel comparison and search/bookmark/drawer destination fidelity remain open.
- Details: [Batch 55 report](HOME_ZEN_PROGRESS_AND_UI_SMOKE_FIX_BATCH_55.md).


## Batch 54 — original shell binary XML geometry

- [x] Decoded `activity_home_revamp` (`0x7f0d0033`) directly from the verified original APK.
- [x] Corrected source-backed shell clipping, toolbar action grouping/padding, bottom-nav horizontal margins, blocker elevation and `fullContainer` elevation.
- [x] Updated the evidence guard to assert the original `fullContainer` elevation instead of the earlier incorrect margin assumption.
- [x] Android build passed: [run 38082219855](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082219855).
- [ ] Finish emulator UI smoke and inspect screenshots: [run 38082552298](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082552298).
- [ ] Full source-state visibility/navigation trace and original-APK pixel comparison remain open.


## Parallel batch execution — 2026-10-11

- [x] Added static regression assertions for source-backed initial states and video subject-grid behavior in the source-bound layout verifier. This protects Home shimmer vs empty list, QBank spinner vs empty subject list, Tests loading vs empty list, and Videos 2/3-column layout/spacing behavior.
- [x] Toolbar title/branding states are guarded against resource and Java-binding regressions.
- [ ] Current-head emulator run must finish with screenshots/diagnostics uploaded before runtime QA can be marked PASS.
- [ ] Reconstruct original ViewModel/adapter/data bindings and perform pixel comparison; do not fabricate rows to make loading states disappear.

## Raw runtime class identity and title-binding cleanup — Batches 63–65

- Removed the three static toolbar title strings previously transcribed from screenshots. Original DEX calls `CourseConfigV2.CourseStrings.getQbankHeaderTitle()`, `getTestHeaderTitle()`, and `getVideoHeaderTitle()` and passes those values to `DataBuffer.read(String)`. The local title stays blank until the original config/ViewModel flow is integrated.
- Matched the local app label to original source string `Marrow` while retaining a separate application ID.
- Corrected source-runtime package identity: raw APK manifest/DEX uses `o.zadb`, `o._coerceBooleanFromInt`, and tab Fragment classes in `o.*`; the decompiler archive remaps these to `kotlin.*`. Local source-tab tags now use `Home_o.*`, matching the original `Home_ + Class.getName()` convention.
- Added source guard assertions against screenshot-title regressions and decompiler-alias runtime tags.
- Validation on intermediate commit `f01bdaeb83eea470a224cab0fb6c2cbfddbb73c7`: Android build, evidence guard, and source layout audit tests passed. Emulator smoke QA was still running at that checkpoint; it must be inspected separately. The combined raw-package correction/guard commit still requires a fresh build and CI validation after it is pushed to the working branch.
- Full source-native Fragment/Application/Activity integration and 1:1 parity remain incomplete; no manifest-only launcher swap was made.


## Batch 66 — Intern Mode event/state trace

- [x] Traced the original Videos fragment switch listener through `o.setScrollPosition`, the checked-boolean event `TransformationChildCard.MediaBrowserCompatItemReceiver`, and `VideoLandingViewModel.IconCompatParcelizer` state update.
- [x] Verified original state observer owns ON/OFF label, checked state, theme tints, banners, and transition/loading labels; the behavior is not a cosmetic toggle.
- [x] Kept the local switch non-clickable/non-focusable because the original ViewModel/repository/use-case graph is not integrated. Updated smoke comments and added a regression test to reject a local listener before source integration.
- [ ] Full original Videos ViewModel and data/repository dependency integration remains unresolved; this batch does not claim Intern Mode parity.


## Batch 67 — VideoLanding event fidelity boundary

- [x] Removed locally invented direct visibility changes for the Intern Mode banner dismiss and tooltip trigger/dismiss controls.
- [x] Verified original binding-to-event mapping for banner dismiss, tooltip open, tooltip Done, Learn More, and the Intern Mode switch from `setScrollPosition.java`, `buildAndPrepareSampleStreamWrappers.java`, and `VideoLandingViewModel.java`.
- [x] Kept banner dismiss, tooltip open/Done, Learn More, and switch controls non-clickable/non-focusable until the original ViewModel event/state pipeline is integrated.
- [x] Updated emulator smoke expectations, source-evidence guard, and regression tests to reject local direct visibility/navigation substitutes.
- [x] Recomputed the SHA-256 fingerprints for eight original Intern Mode source/dependency files directly from the supplied decompiler archive.
- [ ] Integrate the original VideoLanding ViewModel, event classes, observer, and injected dependencies before enabling these actions. Do not claim tooltip/banner interaction parity yet.
- [ ] Latest Android build and emulator smoke results must be checked on the final batch commit; earlier smoke runs were cancelled when the branch was advanced.


## Batch 68 — original VideoLanding dependency graph

- [x] Traced the original `VideoLandingViewModel` factory callsite and recorded its seven constructor providers in source order.
- [x] Verified archive implementation classes for the first four injected interfaces and the AppModule/coroutine-dispatcher provider paths.
- [x] Preserved source fingerprints for the factory, ViewModel, and dependency implementations.
- [ ] Integrate the original application provider graph and ViewModel lifecycle before enabling VideoLanding event controls; several coroutine bodies remain decompiler-unresolved.
- [ ] Re-run build, evidence guard, layout/unit tests, and emulator smoke QA on the final PR head. Prior emulator smoke run was cancelled when branch commits advanced.


## Batch 69 — transition resources and state binding

- [x] Restored the four source-backed Intern Mode transition strings verbatim from the original archive.
- [x] Added regression tests for exact transition and tooltip resource values.
- [x] Recorded original loading-state message selection and tooltip-copy selection from the original fragment observer.
- [x] Kept the loading overlay and tooltip hidden until their original state streams are integrated; the state-dependent message remains unpopulated.
- [ ] Integrate the original app-scoped ViewModel/provider graph and lifecycle/observer collection. Several decompiler bodies remain unresolved.
