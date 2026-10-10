# Tab State and Optional View Guards — Batch 30

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Scope:** Main activity lifecycle safety only; no unrelated repositories or educational content.

## Changes

1. Persisted the selected top-level tab using `onSaveInstanceState(Bundle)` with the existing `selected_home_tab` key already read during `onCreate`. This closes the save/restore asymmetry for activity recreation.
2. Added null checks before setting layout managers on the four tab RecyclerView roots (`rvHomeCard`, `rvSubjectList`, `rvMainList`, `epoxyRVSubject`). Source/layout variants that omit an optional list root no longer cause a null dereference during tab creation.
3. No layout XML, source assets, tab order, header, bottom navigation, content, monetization surface, or fragment destination names were changed.

## Validation boundary

- This change is committed to `main`; CI must confirm Android compilation and the repository evidence guard before it is considered build-verified.
- This is not a claim of full UI parity or device-level rotation QA.
- No fake subjects, lessons, scores, account data, or other educational content were added.
- Source evidence remains the only implementation authority; screenshots remain QA-only.
