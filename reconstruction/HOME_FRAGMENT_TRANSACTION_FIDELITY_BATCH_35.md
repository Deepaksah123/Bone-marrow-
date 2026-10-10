# Home Tab Fragment Transaction Fidelity — Batch 35

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Source evidence:** `reconstruction/HOME_FRAGMENT_TRANSACTION_TRACE_BATCH_8.md`.

## Change

The tab handler now removes inactive fragments whose tags begin with `Home_` instead of hiding them. It preserves the currently selected destination if it already exists, adds a new destination to `R.id.upperContainer` when absent, or shows the existing destination when present. The source tag family remains `Home_<fully-qualified destination class>`.

## Guard

CI now asserts:
- inactive Home fragments use `transaction.remove(fragment)`;
- the previous hide-based behavior is not reintroduced;
- selected destination lookup, add to `upperContainer`, and show-existing paths remain present;
- all four exact source tag strings (`Home_kotlin.makeGooglePlayServicesAvailable`, `Home_kotlin.ResidentKeyRequirementUnsupportedResidentKeyRequirementException`, `Home_kotlin.WalletConstantsCardNetwork`, `Home_kotlin.setScrollPosition`) remain unchanged.

## Limits

The local wrapper fragment classes still stand in for the original obfuscated destination classes, and exact animations/back-stack/state-restoration semantics are not yet runtime-proven. This batch aligns the transaction operation sequence with the documented decompiled helper; it does not claim complete navigation parity.

## Validation

Build and evidence guard must pass after this commit. Runtime testing on a device remains pending.
