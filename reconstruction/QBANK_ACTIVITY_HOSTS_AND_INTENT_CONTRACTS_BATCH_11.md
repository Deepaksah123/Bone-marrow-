# QBank Activity Host & Intent Contracts — Evidence Batch 11

## Concrete activity subclasses and root layouts

The decompiled source ties these concrete activity classes to QBank screen host layouts:

| User-facing role suggested by resource | Concrete class | Superclass / host constructor | Exact layout evidence |
|---|---|---|---|
| QBank lesson list | `kotlin.ActivityC0259zzaz` | extends `AbstractActivityC0258zzay` | superclass constructor `AbstractActivityC0258zzay.java:150` supplies `R.layout.activity_qbank_lesson_list` |
| QBank question play | `kotlin.setAppId` | extends `getAllAppIds` | `getAllAppIds.java:140` supplies `R.layout.activity_qbank_play` |
| QBank introduction | `kotlin.setTokenBinding` | extends `getAuthenticatorSelection` | `getAuthenticatorSelection.java:199` supplies `R.layout.activity_qbank_introduction_marrow2` |
| QBank score | `kotlin.ActivityC0274zzbn` | extends `AbstractActivityC0270zzbj` | `AbstractActivityC0270zzbj.java:129` supplies `R.layout.activity_qbank_score` |
| QBank tracker | `kotlin.zzel` | extends `zzeg` | `zzeg.java:151` supplies `R.layout.activity_qbank_tracker` |

The table establishes class inheritance and layout assignment. It does not assert a complete transition sequence among these screens.

## Direct Intent contracts found in concrete hosts

### QBank play

`sources/kotlin/setAppId.java:193–205` defines an Intent builder that targets `setAppId.class` and sets:
- `step_id` (String)
- `lesson_title` (String)
- `McqActivityPlayContract_Parent_Type` (enum/model `readBlockToCache`)
- `bookmarkStartIndex` (integer)
- `bookmarkStartMcqId` (String)

This is a source-backed launch contract for the QBank play host. The exact click path that supplies every value still needs a caller trace.

### QBank introduction

`sources/kotlin/setTokenBinding.java:214–219` defines an Intent builder that targets `setTokenBinding.class` and sets:
- `test_id` (String)
- `qbank_source` (integer)
- `analytics_source` (String)

`setTokenBinding.java:442–445` reads these three values in `onCreate`. This establishes the argument contract, not the exact origin of every invocation.

### QBank score

`sources/kotlin/ActivityC0274zzbn.java:206–210` defines an Intent builder targeting `ActivityC0274zzbn.class`, taking a `C0272zzbl` argument model and passing it through that model's Intent serialization method.

### QBank tracker

`sources/kotlin/zzel.java:204–206` defines an Intent factory returning an Intent to `zzel.class`.

## Decompiler limitation that blocks a stronger claim

The decompiler explicitly marks several activity lifecycle methods as failed/skipped decompilation stubs, including:
- `ActivityC0259zzaz.onCreate`
- `setAppId.onCreate`
- `getAllAppIds.onCreate`
- `ActivityC0274zzbn` has a recovered `onCreate` body but its superclass's core lifecycle is partially stubbed.

Because these lifecycle bodies and some click listeners are incomplete, this batch does **not** claim the full sequence lesson list → introduction → play → score → tracker. Those transitions must be confirmed from recovered call sites or smali, not guessed from screen names.

## Fidelity exclusions and validation

Plan upgrade/renewal/payment/checkout/upsell/advertising paths remain excluded from the reconstructed UI.

Static source evidence only; no Android build, installation, or runtime QA is claimed. Overall readiness remains **PARTIAL, NOT RESOLVED**.
