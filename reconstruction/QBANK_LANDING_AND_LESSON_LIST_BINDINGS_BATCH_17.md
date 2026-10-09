# QBank Landing and Lesson-List View Binding Map — Batch 17

## QBank subject landing

- `sources/kotlin/HlsMediaChunk.java:30–38` inflates `R.layout.fragment_qbank_landing` and binds:
  - `progressLoadList` — ProgressBar
  - `rvSubjectList` — RecyclerView
- The owning fragment `ResidentKeyRequirementUnsupportedResidentKeyRequirementException` attaches its adapter at lines 116–117, observes subject/list models at 130–141, and toggles list/progress visibility at 408–415.
- The source-backed subject item route into the lesson-list host remains Batch 10.

## QBank lesson-list

`sources/kotlin/buildDataSource.java:68–128` inflates `R.layout.fragment_qbank_lesson_list` and binds:
- `clMain`, `clSort`
- `ivBack`, `ivEmptyState`, `ivIndex`
- `lblSortBy`, `llIndex`, `lytQbankSuggestion`
- `progressLoadList`
- `rvLessonFilter`, `rvLessonList`, `rvLessonSortFilter`
- `tabs` (TabLayout), `toolbar`
- `tvEmptyState`, `tvIndex`, `tvSortItemTitle`, `tvSubjectTitle`
- `viewDark`

These names/types are direct view-binding evidence. They do not establish dimensions, colors, typography, sorting order, or click behavior by themselves.

## QBank play and score host boundary

- `sources/kotlin/getAllAppIds.java:140` supplies `R.layout.activity_qbank_play` to the QBank play activity base.
- `sources/kotlin/AbstractActivityC0270zzbj.java:129` supplies `R.layout.activity_qbank_score` to the score activity base.
- The direct play completion → score Intent route is in Batch 12.

The actual binary layout files and resource table must still be resolved for pixel-accurate implementation; this binding map is not a replacement for the original XML/resource rendering.

## Validation and scope

Static source mapping only; no Android build, installation, or runtime QA is claimed. Keep payment, plan upgrade, subscription, renewal, checkout, upsell, and advertising surfaces excluded. Overall readiness remains **PARTIAL, NOT RESOLVED**.
