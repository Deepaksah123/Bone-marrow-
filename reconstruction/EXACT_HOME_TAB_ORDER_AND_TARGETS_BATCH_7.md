# Exact Home Tab Order & Fragment Targets — Evidence Batch 7

## Direct source-of-truth: tab model enum

File: `sources/kotlin/DataBuffer.java`, static initializer at lines 106–123. The original source defines exactly four tab models and their ordering:

| Index | Model name | String resource | Icon resource | Fragment class passed in model | Analytics/state key |
|---:|---|---|---|---|---|
| 0 | `HOME` | `R.string.tab_home` | `R.drawable.ic_home_tab_home` | `makeGooglePlayServicesAvailable.class` | `home` |
| 1 | `QBANK` | `R.string.tab_qbank` | `R.drawable.ic_home_tab_qbank` | `ResidentKeyRequirementUnsupportedResidentKeyRequirementException.class` | `qbank` |
| 2 | `TESTS` | `R.string.tab_tests` | `R.drawable.ic_home_tab_tests` | `WalletConstantsCardNetwork.class` | `test` |
| 3 | `VIDEOS` | `R.string.tab_video` | `R.drawable.ic_home_tab_videos` | `setScrollPosition.class` | `video` |

Evidence:
- `DataBuffer.java:108`: HOME model and fragment class.
- `DataBuffer.java:114`: QBANK model and fragment class.
- `DataBuffer.java:115`: TESTS model and fragment class.
- `DataBuffer.java:116`: VIDEOS model and fragment class.
- `DataBuffer.java:122`: enum/list order is `HOME, QBANK, TESTS, VIDEOS`.

## Tab selection event path confirmed

- `sources/kotlin/zabz.java:2936–2944` emits the selected index.
- `sources/com/marrow2/ui/main/viewmodel/HomeUIActivityViewModel.java:1207–1215` stores the selected index against a list of `DataBuffer` models.
- `sources/kotlin/DataBuffer.java:44–52, 59–85` shows each model stores its resource ID, icon ID, destination `Class<?>`, state key and flags.

This closes the exact tab order and the destination class values recorded in the source model. The classes' human-readable screen semantics are supported by their surrounding source references, not their obfuscated class names alone.

## Remaining route mechanics

The exact list and target classes are now known. The next step is to verify how the base activity observes the view-model selection and performs fragment operations, including saved state and back-stack behavior. Do not replace this with a guessed navigation implementation.

## Fidelity and validation limits

- This is static decompiled-source evidence.
- It does not prove that every destination fragment renders correctly after reconstruction.
- No Android project build, APK installation, or runtime screenshot validation is claimed.
- Payment, subscription, renewal, checkout, upsell and advertising UI remain excluded.
- Overall readiness remains **PARTIAL, NOT RESOLVED**.
