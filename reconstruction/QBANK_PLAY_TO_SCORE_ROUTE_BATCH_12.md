# QBank Play → Score/Review Route Evidence — Batch 12

## Direct QBank play-to-score transition

The source contains a direct path from a QBank play view-model completion action to the QBank score activity:

- `sources/kotlin/RequestParams.java:5216–5220` constructs a `C0272zzbl` score/analytics model from the active QBank result, calls `ActivityC0274zzbn.Companion.IconCompatParcelizer(context, model)`, adds `key_override_transition=false`, starts the resulting activity, then dispatches a completion/reset event to `QBankPlayViewModel`.
- `sources/kotlin/ActivityC0274zzbn.java:206–210` confirms that the Intent builder targets `ActivityC0274zzbn.class`.
- `sources/kotlin/ActivityC0274zzbn.java:36` establishes that this class extends `AbstractActivityC0270zzbj`.
- `sources/kotlin/AbstractActivityC0270zzbj.java:129` establishes that the superclass constructor supplies `R.layout.activity_qbank_score`.

This confirms a source-backed QBank play completion → score screen launch path. The exact presentation of each score field still requires resource/theme resolution and full model-field tracing.

## Other verified QBank route contracts

- The concrete play activity is `setAppId`, which extends `getAllAppIds`; its base constructor supplies `activity_qbank_play`.
- The play Intent builder in `setAppId.java:193–205` carries `step_id`, `lesson_title`, `McqActivityPlayContract_Parent_Type`, `bookmarkStartIndex`, and `bookmarkStartMcqId`.
- The QBank introduction concrete activity is `setTokenBinding`, which extends `getAuthenticatorSelection`; the host layout is `activity_qbank_introduction_marrow2`.
- Its Intent contract in `setTokenBinding.java:214–219` carries `test_id`, `qbank_source`, and `analytics_source`; `setTokenBinding.java:442–445` reads these arguments.
- The lesson-list activity host `ActivityC0259zzaz` receives an `isCompatible` argument via `ActivityC0259zzaz.Companion.RemoteActionCompatParcelizer`, called by the QBank landing fragment at `ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:427–433`.

## Remaining gaps

The decompiler skips or stubs several core lifecycle methods, including the concrete QBank play host's `onCreate`. Therefore, this batch does not claim the full lesson-list → introduction → play sequence or all back/exit behavior. Those must be recovered from call sites or smali. The play-to-score route above is directly visible.

## Scope and validation

Only the target Bone-marrow repository is updated. Renewal, subscription, payment, checkout, upsell, and advertising UI remains excluded. Static-source tracing only; no Android project build, APK install, or runtime QA is claimed. Readiness remains **PARTIAL, NOT RESOLVED**.
