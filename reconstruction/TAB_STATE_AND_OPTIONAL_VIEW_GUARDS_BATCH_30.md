# Tab State and Optional View Guards — Batch 30

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Scope:** Main activity lifecycle safety only; no unrelated repositories or educational content.

## Changes

1. Confirmed the existing `onSaveInstanceState(Bundle)` already persists `selected_home_tab`; retained that original method without duplication.
2. Added null checks before setting layout managers on the four tab RecyclerView roots (`rvHomeCard`, `rvSubjectList`, `rvMainList`, `epoxyRVSubject`). Source/layout variants that omit an optional list root no longer cause a null dereference during tab creation.
3. No layout XML, source assets, tab order, header, bottom navigation, content, monetization surface, or fragment destination names were changed.

## Validation boundary

- The first build caught a duplicate `onSaveInstanceState(Bundle)` override because the original implementation was already present. The duplicate was removed immediately; the existing method is retained. A fresh Android build is pending.
- The repository evidence guard passed on the documentation commit; the corrected code commit triggers a fresh guard run.
- This is not a claim of full UI parity or device-level rotation QA.
- No fake subjects, lessons, scores, account data, or other educational content were added.
- Source evidence remains the only implementation authority; screenshots remain QA-only.
