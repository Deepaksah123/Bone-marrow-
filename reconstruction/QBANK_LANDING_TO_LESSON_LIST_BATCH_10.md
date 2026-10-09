# QBank Landing → Lesson List Route — Evidence Batch 10

## Verified QBank landing structure

- Tab model index 1 is `QBANK`, with destination class `ResidentKeyRequirementUnsupportedResidentKeyRequirementException` (Batch 7).
- `sources/kotlin/ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:92–99` creates the fragment view through `HlsMediaChunk.read(inflater, container)`.
- `sources/kotlin/HlsMediaChunk.java:30–38` inflates `R.layout.fragment_qbank_landing` and binds `progressLoadList` and `rvSubjectList`.
- `ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:116–117` attaches the fragment's adapter to the bound RecyclerView.
- `ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:130–141` observes a list of QBank subject/domain model items and forwards it to the adapter.
- `ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:408–415` switches the subject RecyclerView and progress indicator visibility based on the loading state.

## Verified subject-to-lesson-list navigation call

- `ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:427–433` constructs an Intent through `ActivityC0259zzaz.Companion.RemoteActionCompatParcelizer(...)`, passing an `isCompatible` model containing two strings and a numeric value.
- The destination class `sources/kotlin/ActivityC0259zzaz.java:31` declares `ActivityC0259zzaz extends AbstractActivityC0258zzay`.
- The source-to-layout index records `AbstractActivityC0258zzay.java:150` as a direct reference to `R.layout.activity_qbank_lesson_list`; the corresponding resource is `0x7f0d0052`.
- Therefore, a QBank landing action can route into the QBank lesson-list activity hierarchy, whose source superclass references the `activity_qbank_lesson_list` layout. The exact display text and all payload semantics still require tracing the `isCompatible` model and destination's argument consumers.

## Excluded behavior

The QBank fragment also has a separate plan-upgrade route in `ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:490–496`. Renewal, subscription, upgrade, payment, checkout, upsell and advertising UI must remain excluded from the reconstructed interface. Documenting the original route is not permission to implement it.

## Next trace

Trace the lesson-list activity's argument handling and the selected lesson action toward QBank introduction/play, then verify score/tracker transitions from source and layout IDs.

## Validation boundary

Static source only. No Android project build, install or runtime QA is claimed. Readiness remains **PARTIAL, NOT RESOLVED**.
