# Home Zen Pattern Drawable Dependency Audit — Batch 50

**Repository boundary:** `Deepaksah123/Bone-marrow-` only  
**Branch:** `main`  
**Audit date:** 11 Oct 2026  
**Source archive:** `base.apk_Decompiler.com.zip`  
**Verified archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Scope

Investigated the unresolved transfer/alias gap for the original light and dark Home Zen pattern vectors. The source archive hash was recomputed and matches the established evidence record.

## Exact findings

- Light vector: `resources/res/drawable/ic_practical_corner_zen_are_pattern.xml`, 296,606 bytes.
- Dark vector: `resources/res/drawable/ic_practical_corner_zen_are_pattern_dark.xml`, 298,407 bytes.
- Each vector references 360 distinct generated drawable aliases.
- All 720 alias references resolve to files in the verified archive; zero missing references were found.
- Every alias file has the same SHA-256: `4e97644184ec5bdbbf46d83155bf86b85329a4fd7870f5f42bdc298d7716afa6`.
- The aliases are byte-identical standalone gradient resources; they contain no further drawable or color resource references.
- The exact alias gradient is white at offset 0 fading to transparent white at offset 1, with the source coordinates and orientation preserved.

## Safe next implementation

The evidence supports a source-equivalent resource reduction: retain both original vector path geometries and dimensions, replace the 360 light alias references and 360 dark alias references with one shared drawable containing the exact byte-identical gradient definition, then wire the original light/dark vectors to the source-backed Home Zen background view using the verified theme/configuration behavior.

This is a resource-name normalization, not permission to redraw or rasterize the pattern. Do not substitute a screenshot, generated artwork, or approximate gradient.

## Not yet done / validation gate

- The two large vectors and the shared gradient have **not** been added to app resources by this audit.
- No layout wiring change is claimed.
- Build and evidence guard must pass after implementation.
- Android device light/dark rendering and visual comparison remain pending.
- The Home account/progress values and click/data bindings remain unimplemented; do not fabricate them.

## Repository comparison note

The current Home replica contains 17 non-monetization IDs. The five decoded original IDs `cvGoPro`, `tvGoPro`, `shimmerGoPro`, `spacePro`, and `goProEd5Ed6` remain intentionally excluded as monetization-related. This omission is policy-driven and must not be misreported as an accidental loss of an in-scope control.
