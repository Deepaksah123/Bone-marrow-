# Source Theme Background Mapping — Shell + Home (Batch 40)

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Source authority:** original APK resource-table/theme resolution recorded in `reconstruction/RESOURCE_TABLE_RESOLUTION_BATCH_38.md` and shell geometry in `reconstruction/SHELL_TOOLBAR_BOTTOM_NAV_BATCH_30.md`.

## Change

Replaced six hardcoded `@color/shell_background` assignments with the source theme attribute `?attr/backgroundColor`:

- `activity_main.xml`: `homeAppBar` and `upperContainer`
- `fragment_home_replica.xml`: root, `nestedScrollView`, `clMainInfo`, and `rvHomeCard`

The verified source theme maps `backgroundColor` to `n_05 (#F5F5F5)` in light mode and `n_85 (#252727)` in dark mode. The shell's separate `shell_background` token is white/near-black and does not match those source theme values. This mismatch made the Home surface diverge from the original theme and from the already source-themed Video/Test surfaces.

## Guardrails

- No view IDs, dimensions, hierarchy, visibility, text, content, or navigation behavior changed.
- No account data, subject/lesson content, or monetization UI was added.
- The evidence guard now asserts these source theme attributes and rejects reintroduction of the hardcoded background token in the two layouts.

## Validation status

Android build and evidence guard are triggered by these commits. Mark this batch build-verified only after both runs pass. Runtime screenshot/pixel parity remains pending.
