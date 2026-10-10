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

A fresh Android build and evidence guard are required before this batch is considered validated.
