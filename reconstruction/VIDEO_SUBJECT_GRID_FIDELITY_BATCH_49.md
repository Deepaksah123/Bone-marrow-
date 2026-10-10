# Video Subject Grid Fidelity — Batch 49

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Evidence source:** checksum-verified `base.apk_Decompiler.com.zip`, `sources/kotlin/setScrollPosition.java`, `sources/kotlin/setAnimateOnTouchUp.java`, and `sources/com/google/android/gms/common/util/DeviceProperties.java`.

## Verified original behavior

- `VideoLandingFragment.initView()` uses a `GridLayoutManager` with 3 columns when `DeviceProperties.isTablet(context)` is true, otherwise 2.
- Its anonymous `GridLayoutManager` overrides predictive-item animations to return false.
- It adds `setAnimateOnTouchUp(margin_6dp, margin_4dp)`. The original decoration sets top/bottom offsets to the first dimension (6dp) and left/right offsets to the second (4dp).
- The replica previously used only `smallestScreenWidthDp >= 600`, did not disable predictive animations, and had no equivalent item decoration.

## Implemented

- Added `isSourceTablet()` matching the verified `DeviceProperties.isTablet(Resources)` condition: screen size greater than LARGE, or smallest width at least 600dp when screen size is not greater than LARGE.
- Matched 2/3-column selection and disabled predictive item animations.
- Added the exact 6dp vertical and 4dp horizontal item offsets, including the missing source-backed `margin_6dp` dimension.
- Added evidence-guard assertions. No video subjects, lesson cards, or progress data were fabricated.

## Validation

Validation (11 Oct 2026):

- Android reconstruction build passed: [run 38078006253](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006253), commit `884aaf01821899e0c5fd7c7dcc0f7b22f74a4b8e`.
- Reconstruction evidence guard passed: [run 38078006278](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38078006278), same commit.
- Debug artifact: `marrow-reconstruction-debug`, artifact ID `11678864090`, ZIP size `8,195,237` bytes, artifact ZIP SHA-256 `fadbe68bceb34a26f8db64c07e519067ab0e1073f50f7ca0b8fe924230911fb7`.
- These CI checks establish compile/assembly and evidence-guard success only. Device install, launch, layout rendering, and phone/tablet visual QA remain pending.
