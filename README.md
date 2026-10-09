# Marrow Reconstruction Workspace

This repository is the single-source reconstruction workspace for the supplied original APK. It now contains the first native Android implementation slice as well as the source-evidence inventory.

## Android app module

- Module: `:app`
- Launcher: `com.marrow.reconstruction.MainActivity`
- Application ID: `com.marrow.reconstruction.replica` (separate from the original app so both can be installed side by side)
- Four source-verified tabs: Home, QBank, Tests, Videos
- Original APK vector assets imported for the four tab icons
- Tab selection state is interactive and survives activity recreation
- Light/night resource palettes and a dedicated GitHub Actions APK build workflow are configured

**Current limit:** this is the shell/navigation implementation slice, not a 1:1 reconstruction yet. The body screens are intentionally not populated with guessed UI or fabricated educational content. Exact Home/QBank/Test/Video destination layouts, their data wiring, and unresolved resource-table gaps still need to be integrated and runtime-verified.

## Source evidence

- Original APK size: 72,425,656 bytes
- Original APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- Decompiled archive: 26,825 entries, 20,526 Java/Kotlin files
- See [analysis/STATIC_EXTRACTION_SUMMARY.md](analysis/STATIC_EXTRACTION_SUMMARY.md) and [reconstruction/EXACT_SOURCE_UI_INDEX.md](reconstruction/EXACT_SOURCE_UI_INDEX.md).

## Build

GitHub Actions workflow: [Android reconstruction build](.github/workflows/android-reconstruction-build.yml). A successful run publishes a `marrow-reconstruction-debug` APK artifact.

No build or runtime result should be assumed from the existence of the workflow; check its latest run.

## Fidelity constraints

- Original APK and verified decompiler resources are the source of truth.
- Screenshots are QA/reference only.
- Do not fabricate missing UI or behavior.
- No educational content is included until the user supplies it.
- Ads, subscriptions, plan upgrades, renewals, payment, checkout, and upsell UI remain excluded.
- Do not import code, assets, content, dependencies, or assumptions from other Marrow-related or unrelated repositories.
