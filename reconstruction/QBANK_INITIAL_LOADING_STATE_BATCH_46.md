# QBank Initial Loading State — Batch 46

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.  
**Source evidence:** `sources/com/marrow2/ui/qbank/landing/QBankLandingViewModel.java` and `sources/kotlin/ResidentKeyRequirementUnsupportedResidentKeyRequirementException.java` from the checksum-verified decompiler source.

## Verified source behavior

- `QBankLandingViewModel` starts its subject-list fetch during initialization. Its fetch coroutine sets the loading flag to true before obtaining the real list and resets it after the fetch result is delivered.
- `QBankLandingFragment` observes the flag. Its `RemoteActionCompatParcelizer(boolean)` method hides `rvSubjectList` and shows `progressLoadList` while loading, then reverses them.
- The replica had the empty RecyclerView visible and the progress indicator gone despite having no original QBank data adapter.

## Implemented

- Keep the source-backed RecyclerView layout manager.
- Hide the empty subject RecyclerView and show `progressLoadList` in the initial state.
- Added guard checks for the loading-state mapping.
- Did not fabricate subject names, module counts, completion data, or question content.

## Runtime limitation

The replica still lacks the original QBank ViewModel and data fetch/observer. The progress indicator therefore remains visible until the verified subject-list binding is reconstructed. This deliberately avoids showing invented QBank content.

**Validated:** Android build [38077287838](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077287838) passed, and evidence guard [38077287841](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38077287841) passed. Artifact ID `11678636989`, size `8,194,476` bytes, SHA-256 `7f3b2663e1b48aa9aa145795457e3eea770c357730245a53e8554a192dbe9fbe`.
