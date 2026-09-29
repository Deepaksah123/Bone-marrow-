# Reconstruction batches

The supplied APK was successfully split locally into **52 batches** while preserving each file's original APK-relative path.

- 51 batches contain 100 files each.
- Batch 052 contains 16 files.
- Total extracted reconstruction files: 5,116.
- Total extracted bytes: 102,624,993.
- Payment/login/advertising exclusions were applied before batching.

The binary ZIP batch payloads themselves could not be transferred through the connected GitHub API because this GitHub connector accepts text blob content but has no local-file/binary upload handoff. The manifest records the verified batch structure so no files need to be randomly regrouped.

Local batch SHA-256 values are generated from the exact batch archives created from the supplied APK.
