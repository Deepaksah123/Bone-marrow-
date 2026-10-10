# QBank Root and Spinner Fidelity — Batch 51

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Source evidence:** checksum-verified `base.apk_Decompiler.com.zip`, `resources/res/layout/fragment_qbank_landing`, and `resources/res/drawable/rotate_progress_drawable_blue.xml`.

## Verified source behavior

- The original QBank root uses `?attr/backgroundColor`.
- The subject RecyclerView uses match-parent width, 0dp constrained height, nested scrolling disabled, and a LinearLayoutManager declared in XML.
- The centered loading ProgressBar uses the original `rotate_progress_drawable_blue` animated drawable.
- The replica had no root background, used 0dp width for the RecyclerView, lacked the source nested-scrolling/layout-manager attributes, and used the platform default spinner.

## Implemented

- Restored the theme-aware root background and source RecyclerView attributes.
- Added the original blue sweep-ring progress drawable directly from the verified decompiler resource.
- Connected `progressLoadList` to that drawable and added targeted evidence-guard checks.
- No subject names, modules, question counts, or QBank data were invented.

## Validation

**Validated:** Android build [38078412747](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078412747) passed, and evidence guard [38078412756](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078412756) passed. Artifact ID `11678498594`, size `8,196,390` bytes, SHA-256 `b8cc5a081cc906855a361d34f60dc8acca950bc851b67cdee28a468cef6b175b`.
