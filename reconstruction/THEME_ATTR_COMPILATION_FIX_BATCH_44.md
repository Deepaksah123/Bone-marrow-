# Theme Attribute Compilation Fix — Batch 44

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Trigger:** Batch 43 Android build failed at `MainActivity.java` because this app module uses non-transitive `R` classes and does not declare `colorPrimary` in its own `R.attr` namespace.

## Failure evidence

Android build run [38076798674](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38076798674) failed in `compileDebugJavaWithJavac` with:

`cannot find symbol: variable colorPrimary, location: class attr`

The evidence guard passed, but a passing grep-based guard did not establish Java compilation.

## Corrective change

- Changed the selected-tab tint resolver to reference `com.google.android.material.R.attr.colorPrimary`, which is provided by the Material dependency in `app/build.gradle`.
- Kept `R.color.colorPrimary` as the exact fallback and retained the app-owned `R.attr.onBackgroundSurface3` for the unselected state.
- Updated the evidence guard to check the compiled-resource namespace actually used by the app.

## Validation status

The new Android build and evidence guard must pass for this correction to be considered complete. No APK success or artifact is claimed in this report before those runs finish.
