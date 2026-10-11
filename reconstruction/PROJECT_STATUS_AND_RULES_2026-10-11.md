# Bone Marrow Android UI Reconstruction — Status & Rules

**Updated:** 2026-10-11 (UTC)  
**Repository boundary:** `Deepaksah123/Bone-marrow-` only  
**Active branch:** `source-fidelity/intern-mode-colors`  
**PR:** [#1 — Match original Intern Mode fallback colors](https://github.com/Deepaksah123/Bone-marrow-/pull/1) — open, not confirmed merged.

## 1. Current status

- Original APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- Canonical decompiler ZIP SHA-256: `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`
- Latest observed evidence guard: run `38122563135` — **success**.
- Latest observed Android build: run `38122563138` — **in progress** at snapshot.
- Latest observed UI smoke: run `38122563080` — **in progress**, no artifact available at snapshot.
- Full-app 1:1 status: **not complete; no pixel-perfect claim is justified yet**.

A prior smoke run (`38120225475`) was marked successful but its screenshots contained Android “isn't responding” dialogs. It is not accepted as valid visual QA. The smoke guard was expanded to reject generic ANR dialogs; the new run and screenshots must be inspected before runtime QA passes.

## 2. Completed work

### Source inventory and trace
- Original APK/decompiler inputs are identified by recorded hashes.
- The decompiler archive has 26,825 entries, 20,526 Java/Kotlin source files and 578 direct layout entries.
- Core shell, Home, QBank, Tests, Videos and Intern Mode tooltip IDs were cross-checked against original resource symbols and source/binding references.
- The original drawer binary XML hierarchy was reconstructed and documented.
- Source-to-screen inventory and a readiness audit distinguish verified facts from unresolved candidates.

### Implemented source-bound areas
- Main shell with Material TabLayout, source-derived tab order/resources and core shell IDs.
- Home, QBank, Tests and Videos landing replicas with source-bound IDs/hierarchies, though their runtime data/state flows remain incomplete.
- Recovered drawer hierarchy.
- Source-traced Better Search entry/initial overlay; query/results/history behavior remains incomplete.
- Intern Mode fallback colors: ON fallback `sepia80 #fce795`, OFF fallback `bg_no_guess #f5f5f5`.
- Intern Mode tooltip/banner event mapping corrected using original binding/ViewModel evidence: the banner-close control dismisses the banner; `ibTooltip` opens the tooltip. The default original tooltip description is used; the current-edition/ED6 variant remains unbound, so Learn More is not fabricated.
- Evidence guard and emulator screenshot QA scripts/workflows exist; evidence notes track unresolved gaps.

## 3. Remaining work

1. Finish current Android build and emulator smoke run; review the screenshot artifact and reject OS prompts, ANR overlays or contaminated captures.
2. Validate the latest Intern Mode tooltip/banner interaction on emulator.
3. Compare replica screenshots against a genuine original-app reference under the same viewport, density, theme and state.
4. Finish decoding/cross-referencing binary XML/resource table for unresolved screens and variants.
5. Trace all navigation, back-stack/deeplink behavior, listeners, ViewModel events and observer-driven UI states.
6. Replace provisional/loading-only screen bodies with only source-verified content/state behavior.
7. Complete QBank: landing, intro, lesson list, play/MCQ, tracker, score/review/search.
8. Complete Tests: landing, intro, play/timer/submit, review, score and analytics.
9. Complete Videos: landing, lesson list, player boundary, revision, downloads, notes and sample flows.
10. Trace and implement supporting screens (bookmark, settings/profile, custom module, pearl, feedback, recent updates, theme).
11. Run final screen-by-screen visual and interaction parity checks; update the readiness audit.

**Frozen exclusions:** no educational/content data until the user supplies it after UI fidelity is reached; no advertising, payment, checkout, subscription or monetization/upsell UI.

## 4. Non-negotiable project rules

1. **Single repo:** all project work stays inside `Deepaksah123/Bone-marrow-`. Do not work in another repository.
2. **No contamination:** do not mix another app's UI, code, assets, content, assumptions or design patterns.
3. **Genuine sources only:** the original APK and checksum-identified decompiler/source artifacts are authoritative.
4. **No fabrication:** never invent a screen, destination, string, icon, data, state, asset or interaction. Mark it unresolved and trace it.
5. **Evidence before implementation:** resource names alone do not prove navigation or layout selection. Cross-reference resource ID, binary XML, binding/listener and ViewModel/observer flow.
6. **Screenshots are QA, not implementation authority:** use screenshots to test fidelity, not to invent missing UI.
7. **Do not overclaim:** a compile or static evidence guard is not proof of visual parity. Only claim runtime QA after reviewing valid screenshots.
8. **Do not remove existing UI just because a search did not find its source string:** trace the original resource first.
9. **Keep scope frozen:** no educational content insertion, ads or monetization/payment interfaces.
10. **Track gaps:** record source paths/symbols and distinguish verified facts from candidates.
11. **Work in coherent batches:** parallelize related tasks where practical, but verify every batch.
12. **CI honesty:** an ANR, immersive prompt, OS overlay, failed launch or missing screenshot artifact invalidates visual QA even if a job reports success.

## 5. How the workflow operates

1. Verify canonical APK/decompiler hashes.
2. Trace original layout/resource IDs, binary XML, generated bindings, click listeners, ViewModel events, observer state, strings, dimensions, styles and assets.
3. Record source-to-screen evidence and unresolved questions.
4. Implement only source-supported behavior inside this repository.
5. Run source-bound layout/evidence guard.
6. Build the debug APK.
7. Run emulator navigation and interaction smoke tests.
8. Capture screenshots and interaction evidence.
9. Inspect screenshots for the real app screen, expected state and absence of ANR/OS overlays.
10. Update the readiness audit and report only what has passed.

## 6. Important repository files

- `app/src/main/java/com/marrow/reconstruction/MainActivity.java` — shell/navigation and traced interactions
- `app/src/main/res/layout/fragment_home_replica.xml`
- `app/src/main/res/layout/fragment_qbank_landing_replica.xml`
- `app/src/main/res/layout/fragment_home_test_replica.xml`
- `app/src/main/res/layout/fragment_video_landing_replica.xml`
- `app/src/main/res/layout/tooltip_intern_mode_info_replica.xml`
- `app/src/main/res/layout/drawer_menu_empty_host_replica.xml`
- `.github/scripts/verify_source_bound_layouts.py` — static/source-bound verifier
- `.github/scripts/run_android_ui_smoke.py` — emulator smoke/screenshot QA
- `.github/workflows/android-ui-smoke.yml` — Android build and emulator QA
- `.github/workflows/reconstruction-evidence-guard.yml` — evidence-boundary regression checks
- `reconstruction/ORIGINAL_UI_SOURCE_TRACE_BATCH_59.md` — source trace notes
- `reconstruction/1TO1_READINESS_AUDIT.md` — verified status and remaining gaps
- `reconstruction/EXACT_SOURCE_UI_INDEX.md` — source archive inventory
- `reconstruction/SOURCE_TO_SCREEN_MAP.md` — source domains and screen map

## 7. Definition of done for “1:1”

- Every included screen/state has direct source/resource evidence.
- Layout hierarchy, dimensions, typography, colors, icons, strings, theme and assets match the original evidence.
- Loading, empty, error and state-dependent variants are traced and implemented where present.
- Navigation and interactions match source behavior.
- Screenshots are captured under controlled conditions and compared with genuine original-app references.
- No OS prompts, ANR dialogs, immersive confirmations or unrelated UI appear in QA captures.
- Evidence guard and build pass on the final commit; QA artifacts are reviewed.
- The readiness audit is updated, and unknowns are not described as complete.

## Current conclusion

The project has a verified source inventory, core source-bound landing replicas, recovered drawer structure, a source-traced search entry, and ongoing Intern Mode fidelity/QA corrections. The evidence guard passed in the latest observed run, while the latest build and smoke run were still in progress at the snapshot. The full application is not yet verified as 1:1. Immediate next gate: finish CI and inspect the fresh screenshots, then continue tracing and implementing remaining screen/state flows.
