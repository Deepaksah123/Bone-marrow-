# Tab State and Optional View Guards — Batch 30

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Scope:** Main activity lifecycle safety only; no unrelated repositories or educational content.

## Changes

1. Confirmed the existing `onSaveInstanceState(Bundle)` already persists `selected_home_tab`; retained that original method without duplication.
2. Added null checks before setting layout managers on the four tab RecyclerView roots (`rvHomeCard`, `rvSubjectList`, `rvMainList`, `epoxyRVSubject`). Source/layout variants that omit an optional list root no longer cause a null dereference during tab creation.
3. No layout XML, source assets, tab order, header, bottom navigation, content, monetization surface, or fragment destination names were changed.

## Validation boundary

- The first build caught a duplicate `onSaveInstanceState(Bundle)` override because the original implementation was already present. The duplicate was removed immediately; the existing method is retained.
- Corrected Android build passed: [run 38075394178](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38075394178).
- Evidence guard passed with lifecycle/optional-root assertions: [run 38075448081](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38075448081).
- Debug APK artifact ID `11678014087`, size `8,193,935` bytes, digest `sha256:ba1d4d81b109dc4e1aa8d6a75ec231129df8f78968378c706a2a46296e344de5`.
- This is not a claim of full UI parity or device-level rotation QA.
- No fake subjects, lessons, scores, account data, or other educational content were added.
- Source evidence remains the only implementation authority; screenshots remain QA-only.
