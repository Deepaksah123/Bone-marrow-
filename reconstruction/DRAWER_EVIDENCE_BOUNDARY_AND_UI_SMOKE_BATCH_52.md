# Drawer Evidence Boundary + Emulator UI Smoke — Batch 52

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Source boundary:** original Marrow APK/decompiler evidence only; no external repository assets or implementation imported.

## Drawer decision

The original shell references `drawer_menu_revamp`, and source binding identifiers were recorded in Batch 42. The exact decoded binary XML tree for that layout is not present in the current checked-in source tree or available Library artifacts. The previous generic rows, labels and row click handlers were not source-exact.

- Replaced the speculative drawer row list with a neutral empty host that preserves the source shell's drawer include and open action.
- Removed the matching speculative row click handlers and unused row labels.
- Kept the menu icon's source-backed behavior: opening the start drawer.
- Added evidence-guard assertions to prevent speculative drawer rows/labels from silently returning before the original binary layout is recovered.

This is an evidence-boundary correction, **not** completion of the drawer. The correct next implementation step is to recover the original `drawer_menu_revamp` binary XML and trace its source-backed child hierarchy/routes. Do not infer destinations from names alone.

## Emulator QA infrastructure

Added `.github/workflows/android-ui-smoke.yml` to build the app, install it in an Android API 35 emulator, launch MainActivity, assert the four source-backed tab labels are present, tap each tab, assert the expected source-backed loading/root IDs and app-process survival, exercise the toolbar drawer-open action, capture each tab's screenshot/hierarchy, and relaunch under each system theme mode before capturing light/dark Home screenshots as a short-lived workflow artifact.

Screenshots are runtime QA evidence only; they are not implementation source and are not yet pixel-compared against the original APK. This smoke workflow does not prove full 1:1 parity.

## Validation

- Android build for app source commit `4c63633c0f1666887c2945ca33d7ec7ea9a3a71b`: **PASS**, [run 38078929016](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078929016).
- Evidence guard before this batch's added drawer assertions: **PASS**, [run 38079505213](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38079505213).
- Updated evidence guard with Batch 52 assertions: run is triggered by the current commit; final result must be checked before claiming validation.
- Emulator UI smoke: [run 38079901707](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38079901707) is running the latest smoke script; do not treat it as passed until screenshots/hierarchy artifact and all steps are confirmed. Do not treat it as passed until screenshots/hierarchy artifact and all steps are confirmed.

## Still open

- Original drawer binary XML and exact route bindings.
- Actual device visual comparison against the original APK in light/dark mode.
- Full navigation and live data-binding fidelity across Home, QBank, Tests and Videos.
- Source pattern-vector transfer for the Home Zen area; original vector files are not in the current repository tree or searchable Library results.
