# 1:1 Reconstruction Readiness Audit

Source boundary: `Deepaksah123/Bone-marrow-` only.

## Verified available in the working reconstruction environment

- Original `base.apk`
- Original APK SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- Original APK inventory: 5,128 entries
- Decompiled ZIP: 26,825 entries
- Java/Kotlin source: 20,526 files
- Smali: 817 files
- XML: 2,371 files
- `com/marrow2` source: 401 files
- `com/marrow2/ui` source: 233 files
- Decoded Android resources including layouts, drawables, colors, fonts and values
- Existing APK path/batch inventory and exclusion documentation in the repository

## Previous blockers — status

1. ~~Original `base.apk` unavailable~~ — **RESOLVED**; uploaded and verified.
2. ~~Verified decompiled Java/Kotlin unavailable~~ — **RESOLVED**; uploaded decompiler dump verified.
3. ~~Verified Smali unavailable~~ — **RESOLVED**.
4. ~~Decoded resource/XML source unavailable~~ — **RESOLVED**.
5. Source-to-screen/behavior map missing — **ACTIVE NEXT TASK**.

## Scope exclusions

- Educational/content data: intentionally deferred; user will provide it after the UI is 1:1.
- Advertising UI: excluded.
- Payment/checkout/subscription/monetization UI: excluded.

## Non-negotiable reconstruction rules

- Original APK/decompiler evidence is the source of truth.
- Screenshots are visual QA/reference only, never implementation source.
- Do not fabricate missing UI or behavior.
- Do not import code, content, assets, UI or assumptions from Marrow or any unrelated repository.
- Keep unresolved evidence gaps explicitly tracked.

## Current state

The project has moved from **evidence acquisition** to **actual reconstruction**.

## Next large batch

1. Trace Home, QBank, Test and Video source-to-screen relationships.
2. Map resource IDs, layouts, themes, dimensions, colors, strings and drawables.
3. Establish navigation/state boundaries.
4. Build the first complete evidence-backed Android UI/navigation batch in the Bone-marrow repository.
5. Build/QA and iterate from verified failures rather than creating a prototype.
