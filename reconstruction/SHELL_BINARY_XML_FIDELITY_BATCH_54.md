# Main Shell Binary XML Fidelity Corrections — Batch 54

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Evidence:** SHA-verified original APK and its decompiler archive only.

## Source recovery

The original APK resource table maps `R.layout.activity_home_revamp` (`0x7f0d0033`) to obfuscated APK entry `zZ`. The original binary XML is 16,022 bytes and was decoded directly from the verified APK. This is a source-level check, not screenshot-derived implementation.

## Implemented shell corrections

- `screen_blocker` now uses the source black color and 8dp elevation.
- `homeAppBar`, `lytContent`, `upperContainer`, and the popup container restore the source orientation/clipping flags.
- The toolbar restores its clickable surface and centers the branding container.
- Bookmark and search actions are grouped in the source-style trailing LinearLayout, with the source 8dp outer spacing and horizontal-only icon padding.
- Bottom navigation restores the source 16dp horizontal margins and weighted 56dp tab row.
- `fullContainer` now uses the source 8dp elevation and no longer has the previously misinterpreted 8dp outer margin.
- The drawer include inherits its width/height/gravity from the recovered drawer root, instead of overriding those source layout parameters in the activity.

This corrects the earlier Batch 30 interpretation that `fullContainer` had an outer margin. The evidence guard now asserts elevation rather than margin.

## Scope and validation

- Monetization/plan banners remain empty/hidden hosts; no purchase, upgrade, checkout or subscription UI was added.
- Android build passed for the shell correction and drawer batch: [run 38082219855](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082219855).
- Evidence guard for the subsequent documentation/guard correction: [run 38082293980](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082293980), in progress at report creation.
- Emulator UI smoke and screenshots: [run 38082219825](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38082219825), in progress at report creation.

No original-APK pixel-diff or whole-app 1:1 claim is made. Main screen data bindings, drawer row visibility/destinations, full Home/QBank/Test/Video parity and source screenshot comparison remain open.
