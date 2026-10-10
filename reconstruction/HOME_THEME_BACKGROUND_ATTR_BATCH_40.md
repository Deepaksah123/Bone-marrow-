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

Android build passed for the Home/shell code commit: [run 38075586947](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38075586947). Evidence guard passed on the latest checklist commit: [run 38075606322](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38075606322). Debug APK artifact ID `11677674404`, size `8,193,923` bytes, digest `sha256:5880ced6c26df6bdc6650a4e328e6aaeff87b9a7bf161e631d47eb538ad65236`. Runtime screenshot/pixel parity remains pending.
