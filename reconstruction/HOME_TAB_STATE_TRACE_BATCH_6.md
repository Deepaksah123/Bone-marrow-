# Home Tab Index → ViewModel State Trace — Evidence Batch 6

## Verified event path

1. `sources/kotlin/zabz.java:2936–2944`: the TabLayout selected callback obtains the selected tab position with `mediaBrowserCompatCustomActionResultReceiver.RemoteActionCompatParcelizer()` and sends `new setTempDir.MediaBrowserCompatItemReceiver(position)` to the Home UI view model.
2. `sources/kotlin/setTempDir.java:34–45`: this event stores the selected integer position and exposes it through `RemoteActionCompatParcelizer()`.
3. `sources/com/marrow2/ui/main/viewmodel/HomeUIActivityViewModel.java:488–500`: the view model recognizes the selected-position event and calls `AudioAttributesCompatParcelizer(position)`.
4. `HomeUIActivityViewModel.java:1207–1215`: when a tab position differs from the current selection, the view model updates its selected `Pair<List<DataBuffer>, Integer>` state and records the selected tab item's `getMediaBrowserCompatItemReceiver()` value through `getSelectedIndexInTrackGroup.Companion.read(...)`.
5. `sources/kotlin/zabz.java:2572–2593`: the UI iterates tab items as `DataBuffer`, reads each item's icon resource, and registers the activity as a TabLayout listener.

## What this proves

- Tab selection is index-driven and flows through a typed event into `HomeUIActivityViewModel`.
- The view model's current tab collection is represented as a list of `DataBuffer` items plus a selected index.
- The selected tab's associated value is stored in state. This is stronger than inferring navigation from layout or screenshot appearance.

## Still not proven

- The exact user-facing tab labels and stable order.
- Which fragment/screen is shown for each selected item, and whether all items replace fragments or some trigger other actions.
- Full back-stack restoration, process recreation, deep-link selection and runtime behavior. These require tracing the consumers of `getSelectedIndexInTrackGroup` and the view-model state collectors in the base activity; the base `onCreate` decompilation is incomplete.

## Validation boundary

Static source inspection only; no build, install or runtime UI validation is claimed. Readiness remains **PARTIAL, NOT RESOLVED**. Payment, subscription, renewal, checkout, upsell and advertising interfaces remain excluded.
