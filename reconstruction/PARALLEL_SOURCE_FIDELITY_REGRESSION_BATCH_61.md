# Parallel Source-Fidelity Regression Batch — 2026-10-11

Repository boundary: `Deepaksah123/Bone-marrow-` only  
Branch: `source-fidelity/intern-mode-colors`  
Acceptance target: original Marrow UI 1:1, backed by the checksum-verified original APK/decompiler and supplied screenshot references.

## Parallel workstreams completed in this batch

### 1. Source-bound structure and first-frame states
Added static regression assertions to `.github/scripts/verify_source_bound_layouts.py` for:
- Home: empty `rvHomeCard` stays hidden while original `shimmerMain` is visible in the initial loading state.
- QBank: empty `rvSubjectList` stays hidden while original `progressLoadList` is visible.
- Tests: empty `rvMainList` and `emptyLayout` stay hidden while `loadingContainer` is visible.
- Videos: 2 columns on phone / 3 on tablet, predictive item animations disabled, source-backed 6dp vertical / 4dp horizontal spacing.

These assertions protect the already implemented source-backed initial states; they do not claim that the missing original ViewModels, adapters or network-backed data have been reconstructed.

### 2. Toolbar and shell fidelity
Guarded the screenshot-evidenced toolbar states and their resource bindings:
- Home retains Marrow branding and hides the centered page title.
- QBank: `QBank Edition 8.5`.
- Tests: `Tests`.
- Videos: `Videos Edition 8.5`.

### 3. Verified Videos interactions
Added static checks for the existing source-bound banner and tooltip wiring:
- `btnCloseInternModeBanner` dismisses `clInternModeBanner`.
- `ibTooltip` reveals `tooltipInternModeInfo`.
- `btnInternModeToolTipDone` dismisses the tooltip.
- The tooltip default body uses verified resource `text_concise_tooltip_description`.

This does not claim the original ViewModel event flow, persistence, Learn More destination or account-backed Intern Mode state is complete.

### 4. CI / runtime QA isolation
- The smoke workflow now uses API 35, 4 GiB RAM and 4 CPU cores following evidence of a visible System UI ANR on the earlier API 30 / 2 GiB / 2-core environment.
- A concurrency guard keeps only the latest smoke run active per ref, reducing competing cold boots.
- The workflow retains bounded execution and unconditional upload of screenshots and diagnostics.

## Current validation boundary

- Android build for commit `d121fd69ceabc347166d6bd5444c64ff36e09a4d`: PASS, run [38151799238](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38151799238).
- Source-evidence guard for that commit: PASS, run [38151799222](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38151799222).
- The expanded guard passed for commit `e123343cf14cb6dab30de3c11e86840e7bdbe639`, run [38152286752](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38152286752).
- Latest expanded guard, build and emulator smoke for commit `5f4982b111ac618536d355f214c7946cdd6b831b` are queued/in progress at report time:
  - [Source-evidence guard](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38152331536)
  - [Android build](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38152331606)
  - [Emulator screenshot QA](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38152331542)

## Open acceptance blockers

1. Emulator navigation/screenshot QA must finish and upload current-head evidence without a system/app ANR.
2. Original Home/QBank/Tests/Videos child hierarchies and all relevant binary XML/resource attributes must be compared against the actual APK resources.
3. Original runtime data/view-model bindings and click destinations are incomplete. Until recovered, source-backed loading states remain visible rather than showing fabricated lesson, subject, test, account or progress content.
4. Compare emulator screenshots to the original supplied reference screenshots and resolve measured mismatches.

**Status: PARTIAL. Build/guard PASS is not a full visual-parity pass. FAT PASS is not claimed.** No unrelated app/repository assets or fabricated educational content were added.
