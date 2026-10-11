# Video Landing Source Interaction Bindings — Batch 56

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Source of truth:** verified original Marrow decompiler archive and its `VideoLandingFragment` view-binding/event trace.

## Implemented

- Bound `btnCloseInternModeBanner` to dismiss its own `clInternModeBanner` container.
- Bound `ibTooltip` to toggle the source-bound `tooltipInternModeInfo` include. Batch 59 then replaced the guessed tooltip card with the original binding structure and wired the source-bound `btnInternModeToolTipDone` button to dismiss it.
- Preserved the existing 2/3-column tablet-aware subject grid and all source-backed root IDs.
- No lesson rows, subject data, account progress, ads, or monetization behavior were fabricated.

## Evidence and limits

The original binding class `sources/kotlin/buildAndPrepareSampleStreamWrappers.java` resolves the banner close button/container and tooltip trigger/include. The tooltip's nested binding `sources/kotlin/getEndTimeUs.java` requires `btnInternModeToolTipDone`, `cardInternModeTooltip`, `container`, `ivTooltip`, `tvLearnMore`, and `txtToolTipBody`. Batch 59 verified the original resource IDs and default text/drawable references. The local Done action hides the tooltip, but the original ViewModel event flow, persistence, Learn More destination, and account-backed Intern Mode state remain unimplemented.

## Validation

Build, evidence guard and emulator screenshot results must be checked against the exact commit that includes this batch. Overall 1:1 readiness remains **PARTIAL**.


## Batch 59 correction

See [ORIGINAL_UI_SOURCE_TRACE_BATCH_59.md](ORIGINAL_UI_SOURCE_TRACE_BATCH_59.md) for the verified source/resource map and explicit per-surface ID reconciliation. The Home Pro IDs remain omitted because the frozen scope excludes Pro/upsell UI; this is not counted as a completed Home 1:1 screen.
