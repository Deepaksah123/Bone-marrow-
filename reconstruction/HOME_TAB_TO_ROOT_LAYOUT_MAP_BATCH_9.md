# Home Tab → Root Fragment Layout Mapping — Evidence Batch 9

This batch connects each tab's destination class to the actual layout binding used by that fragment's `onCreateView`.

| Tab | Fragment destination class from `DataBuffer` | Direct `onCreateView` binding call | Resolved root layout | Root type |
|---|---|---|---|---|
| HOME | `makeGooglePlayServicesAvailable` | `getNextSegmentHolder.RemoteActionCompatParcelizer(inflater, container)` | `fragment_home` | `ConstraintLayout` |
| QBANK | `ResidentKeyRequirementUnsupportedResidentKeyRequirementException` | `HlsMediaChunk.read(inflater, container)` | `fragment_qbank_landing` | `ConstraintLayout` |
| TESTS | `WalletConstantsCardNetwork` | `getNextMediaSequenceAndPartIndex.AudioAttributesCompatParcelizer(inflater, container)` | `fragment_home_test` | `ConstraintLayout` |
| VIDEOS | `setScrollPosition` | `buildAndPrepareSampleStreamWrappers.AudioAttributesCompatParcelizer(inflater, container)` | `fragment_video_landing` | `FrameLayout` |

## Source evidence

- HOME: `sources/kotlin/makeGooglePlayServicesAvailable.java:457–464` calls `getNextSegmentHolder.RemoteActionCompatParcelizer`; binding source `sources/kotlin/getNextSegmentHolder.java:79` inflates `R.layout.fragment_home`.
- QBANK: `sources/kotlin/ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java:92–99` calls `HlsMediaChunk.read`; binding source `sources/kotlin/HlsMediaChunk.java:30` inflates `R.layout.fragment_qbank_landing`.
- TESTS: `sources/kotlin/WalletConstantsCardNetwork.java:114–126` calls `getNextMediaSequenceAndPartIndex.AudioAttributesCompatParcelizer`; binding source `sources/kotlin/getNextMediaSequenceAndPartIndex.java:48` inflates `R.layout.fragment_home_test`.
- VIDEOS: `sources/kotlin/setScrollPosition.java:250–265` calls `buildAndPrepareSampleStreamWrappers.AudioAttributesCompatParcelizer`; binding source `sources/kotlin/buildAndPrepareSampleStreamWrappers.java:126` inflates `R.layout.fragment_video_landing`.

## What is now mapped

The four top-level home tabs, their order, destination fragment classes, root view types, and root layout resource names are directly linked by source. This gives an implementation-grade starting point for recreating the home shell and tab switching without guessing.

## Remaining fidelity work

1. Resolve view attributes/styles/dimensions/colors and drawable/string resources against the original APK's resource table.
2. Trace each fragment's internal navigation to QBank play/score, tests, video lesson/player, bookmarks, search and profile/settings.
3. Establish original app build configuration and create a real Android Gradle project before claiming installable output.
4. Verify on device/emulator after a build; static resource trees are not runtime QA.

No APK build/install/runtime QA is claimed. Overall readiness remains **PARTIAL, NOT RESOLVED**. Excluded payment, subscription, renewal, checkout, upsell and advertising interfaces remain excluded.
