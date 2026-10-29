# Original ViewModel Factory Trace — Batch 71

**Scope:** source-only dependency wiring audit for the existing Home-shell and Video landing ViewModels. This is evidence, not a replacement implementation.

## Verified factory call sites

Source archive: user-supplied `base.apk_Decompiler.com.zip`.

1. `sources/kotlin/cloneWithUpdatedTimeline.java`, factory switch case **79** constructs `RevampHomeActivityViewModel` with seven provider expressions:
   `setPositiveButton.get()`, `r8lambdah6vvr6zUWA2U1fE0KsKpOgpr28.get()`, `addOnPictureInPictureModeChangedListener()`, `getSavedStateRegistryControllerannotations()`, `ActivityResult.get()`, `MediaSessionCompatResultReceiverWrapper()`, and `updateViewStates.IconCompatParcelizer()`.
2. The original `RevampHomeActivityViewModel` constructor accepts, in order: `getDisplaySizeV17`, `readSynchSafeInt`, `readTimestamp`, `ParsableNalUnitBitArray`, `crc32`, `NetworkTypeObserverApi31DisplayInfoCallback`, `getPlatform`.
3. The same factory file, switch case **103**, constructs `VideoLandingViewModel` with seven provider expressions:
   `removeOnUserLeaveHintListener()`, `MediaBrowserCompatMediaItem.get()`, `setPositiveButton.get()`, `isEnabled.get()`, `AudioAttributesCompatParcelizer()`, `setSessionImpl.get()`, and `updateViewStates.IconCompatParcelizer()`.
4. The original `VideoLandingViewModel` constructor accepts, in order: `isEncodingHighResolutionPcm`, `LogLogLevel`, `getDisplaySizeV17`, `binarySearchCeil`, `isSeekPending`, `Allocator`, `getPlatform`.

## Integration decision

The factory call sites establish the constructor/provider boundary, but do not alone establish a buildable graph. Several types are decompiler aliases for obfuscated runtime classes, and the factory's owning component, provider implementations, module bindings, scopes, inherited lifecycle, and transitively required services must all be available and type-compatible. Do not wire local substitutes or guess what any alias means.

## Next source-verification targets

- Trace the factory's enclosing class and constructor/provider field initialization.
- Resolve each of the fourteen provider expressions to its exact provider declaration and binding module.
- Trace the two ViewModels' actual fragment creation and lifecycle owners back to original shell navigation.
- Mark a dependency as integration-ready only after both provider binding and all transitive constructor dependencies are verified from original source.

## Validation status

- Factory/constructor signatures: verified against the original decompiler archive.
- Runtime DI graph: **unresolved**.
- Native original Fragment integration: **unresolved**.
- Buildable original UI integration and runtime parity: **not complete**.
- No UI, placeholder data, or substitute dependency implementation was added by this audit.
