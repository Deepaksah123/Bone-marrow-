# Video Landing Source Interaction Bindings — Batch 56

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Source of truth:** verified original Marrow decompiler archive and its `VideoLandingFragment` view-binding/event trace.

## Implemented

- Bound `btnCloseInternModeBanner` to dismiss its own `clInternModeBanner` container.
- Bound `ibTooltip` to toggle the source-bound `tooltipInternModeInfo` include; tapping the tooltip closes it.
- Preserved the existing 2/3-column tablet-aware subject grid and all source-backed root IDs.
- No lesson rows, subject data, account progress, ads, or monetization behavior were fabricated.

## Evidence and limits

The original binding class `sources/kotlin/buildAndPrepareSampleStreamWrappers.java` resolves both the banner close button/container and tooltip trigger/include. The original `sources/kotlin/setScrollPosition.java` registers a dedicated click handler for the close control and an event for the tooltip trigger. This batch wires the local visible affordances; it does not claim to restore the original ViewModel, persistence, or account-backed Intern Mode state.

## Validation

Build, evidence guard and emulator screenshot results must be checked against the exact commit that includes this batch. Overall 1:1 readiness remains **PARTIAL**.
