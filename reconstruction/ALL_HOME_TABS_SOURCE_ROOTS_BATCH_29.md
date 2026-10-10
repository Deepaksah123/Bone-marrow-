# All Four Home Tabs Inflate Source-Shaped Roots — Batch 29

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`.

## Change

The four top-level tabs now inflate their existing source-shaped XML hierarchies from `createTabContent()`:
- HOME → `fragment_home_replica.xml`
- QBANK → `fragment_qbank_landing_replica.xml`
- TESTS → `fragment_home_test_replica.xml`
- VIDEOS → `fragment_video_landing_replica.xml`

Previously, the fragment wrapper called programmatic `buildHome()`, `buildQbank()`, `buildTests()`, and `buildVideos()` methods. Those synthetic views could diverge from the decoded original hierarchy and show invented values. They are no longer the active tab render path. The existing top-level activity header and bottom navigation remain unchanged.

## Scope / limitations

This makes the verified XML trees the active UI roots, but does **not** implement missing adapters, Compose content, network/data binding, click handlers, or original custom view classes. Lists and Compose surfaces may remain empty; that is preferable to invented subjects, scores, lesson names or account data. Hidden monetization surfaces remain excluded. Exact visual parity still requires on-device comparison.

## Validation

The evidence guard passed: [run 38074219308](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074219308). Android build passed for code commit `47d71eef4352`: [run 38074210922](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074210922). Debug APK artifact ID `11678411729`, size `8,196,583` bytes, digest `sha256:e28b72976cc7360079706b7dcf1a01b7256371ecc51151c4026d16b188a89821`.
