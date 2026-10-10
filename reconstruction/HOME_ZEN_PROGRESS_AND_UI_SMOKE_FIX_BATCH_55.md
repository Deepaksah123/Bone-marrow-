# Home Zen Progress Integrity + Emulator Smoke Fix — Batch 55

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Scope:** source-faithful Home UI and reliable emulator QA only. No other repository or content source was used.

## Source findings

- `reconstruction/DECODED_CORE_LAYOUT_HIERARCHY_BATCH_20.md` records that `tvZenCompletedModules` is a data-bound account-progress field and that the literal `9/35 modules` is placeholder/account-progress content, not a valid hard-coded default.
- The current replica had accidentally reintroduced `android:text="9/35 modules"` into `layout_dynamic_zen_area_replica.xml`, while the evidence guard required that fabricated value. This contradicted the documented source-state rule.

## Changes made

1. Removed the hard-coded `9/35 modules` text from `app/src/main/res/layout/layout_dynamic_zen_area_replica.xml`. The label now stays empty until its original account-data binding is recovered; no fake progress is shown.
2. Updated `.github/workflows/reconstruction-evidence-guard.yml` to fail if the static `9/35 modules` value is reintroduced.
3. Fixed the emulator runner's shell bootstrap in `.github/workflows/android-ui-smoke.yml`: its runner invokes the script through POSIX `sh`, where `set -euo pipefail` fails immediately. Replaced it with portable `set -eu`.

## Validation

- Workflow fix commit: `bab1f04f4e9eda2d654ba73ddbf54520a2f48910`.
- Evidence guard for that commit passed: [run 38084717980](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38084717980).
- Emulator UI smoke for that commit was running at the start of this batch: [run 38084717984](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38084717984). It predates the Home XML correction below and must not be treated as validation of the final batch.
- Home XML correction commit: `a23376ba2368d52cf05898b3f95e6d0b3781d575`.
- Evidence guard correction commit: `9e0f51e0ceb3b3ae1c39e681fbfd8c0b61f771d9`.
- Build and guard for the final batch are pending CI; emulator screenshots, runtime hierarchy, and original-APK pixel comparison are not yet verified.

## Remaining fidelity gaps

- Account-backed progress and lesson values remain unbound by design.
- The original Practical Corner pattern resource family is still not restored as native drawable resources.
- Search/bookmark destination flows and drawer row destinations remain unresolved; no guessed destinations were added.
- Passing static checks or the emulator smoke does not establish 1:1 visual fidelity.
