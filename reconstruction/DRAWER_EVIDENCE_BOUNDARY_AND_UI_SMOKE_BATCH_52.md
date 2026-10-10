# Drawer Evidence Boundary + Emulator UI Smoke — Batch 52

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Source boundary:** original Marrow APK/decompiler evidence only; no external repository implementation was imported.

## Drawer evidence correction

The first part of this batch removed the speculative generic drawer rows and handlers because the named `drawer_menu_revamp` XML was absent from the checked-in decompiler ZIP. The original APK was then recovered from the user's Library and verified against the project SHA-256 records. Batch 53 decodes the actual binary XML and reconstructs the source-backed drawer hierarchy. See [Drawer Binary XML Recovery — Batch 53](DRAWER_BINARY_XML_RECOVERY_BATCH_53.md).

The current drawer is no longer an empty placeholder. Purchase/upsell/referral/debug rows are excluded by project scope. Profile name, course detail and app version remain blank until their real data bindings are recovered; source rows whose original XML default is `gone` are not made visible by guesswork.

## Emulator QA infrastructure

Added `.github/workflows/android-ui-smoke.yml` to build the app, install it in an Android API 35 emulator, launch MainActivity, assert the four source-backed tab labels and loading/root IDs, tap each tab, verify app-process survival, open the toolbar drawer and assert the source-backed `Your Course` and `Settings` labels. It captures each tab's UI hierarchy/screenshot plus drawer-open and light/dark Home screenshots as a short-lived workflow artifact.

The app is relaunched under each theme mode before light/dark capture. Screenshots are runtime QA evidence only; they are not implementation source and are not yet pixel-compared against the original APK.

## Validation

- Source-backed drawer IDs and scope exclusions are guarded by CI.
- Android build: **PASS**, [run 38081191407](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38081191407).
- Evidence guard: **PASS**, [run 38081191405](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38081191405).
- Emulator UI smoke: [run 38081191436](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38081191436) is still running; its final result and screenshot artifact must be inspected.

## Still open

- Trace original drawer row visibility/data-binding flow and source click destinations.
- Inspect the emulator screenshots and fix any runtime failures.
- Do original-APK screenshot/pixel comparison in light/dark mode.
- Complete full navigation and live data-binding fidelity across Home, QBank, Tests and Videos.
- Recover the original Home Zen pattern vector family into build-ready resources; the verified vector aliases still need a clean transfer into the app.
