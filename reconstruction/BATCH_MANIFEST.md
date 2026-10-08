# Reconstruction batches

The supplied APK was successfully split locally into **51 batches** while preserving each file's original APK-relative path.

- 50 batches contain 100 files each.
- Batch 051 contains 77 files.
- Total extracted reconstruction files: 5,077.
- Payment/login/advertising exclusions were applied before batching.

The binary ZIP batch payloads themselves could not be transferred through the connected GitHub API because this GitHub connector accepts text blob content but has no local-file/binary upload handoff. The manifest records the verified batch structure so no files need to be randomly regrouped.

Local batch SHA-256 values are generated from the exact batch archives created from the supplied APK.
