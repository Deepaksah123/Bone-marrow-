# Original Drawer Binary XML Recovery — Batch 53

**Repository:** `Deepaksah123/Bone-marrow-`  
**Branch:** `main`  
**Source of truth:** the original APK and its verified decompiler archive; no other implementation repository was used.

## Source recovery

The original artifacts were recovered from the user's Library and verified by SHA-256:

- `base.apk`: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
- `base.apk_Decompiler.com.zip`: `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

The APK resource table maps `R.layout.drawer_menu_revamp` (`0x7f0d00b3`) to the obfuscated archive entry `On`. Its 10,056-byte binary XML was decoded from the verified APK, resolving the previously missing layout rather than guessing a replacement.

## Implemented in the app

- Reconstructed the original drawer view hierarchy and source binding IDs in `drawer_menu_empty_host_replica.xml`.
- Restored the profile image subtree (`profile_image_v2.xml`), hidden source `new_course_tag` include, source dimensions, source labels, and theme bindings for the drawer.
- Restored original APK drawable resources for the Settings icon, profile edit icon/background, footer Marrow wordmark, course arrow and hidden New badge.
- Added the original CircleImageView library family used by the APK's profile image view.
- Updated the evidence guard to require the source-derived drawer IDs and reject excluded purchase/upsell/referral/debug rows.

## Scope exclusions and remaining behavior

Removed from the reconstructed visible hierarchy: plan purchase, Buy Notes, Add Videos upsell, referral-coupon/extension, profile Pro badge, and debugging/logout rows. The menu icon still opens the drawer. Profile name, course title/detail and app version remain blank rather than being fabricated. The navigation rows whose source XML default is `gone` remain hidden until the original runtime visibility/data-binding flow is recovered.

The original decompiler's text for `ic_arrow_right` was rejected by the current Android vector resource compiler. Its path data was recovered directly from the verified APK's binary XML string pool and restored in the drawable.

## Validation status

- Evidence guard passed for commit `4222a0ffc863e75fdc04c7ae90130e22580f1fbf`: [run 38081056377](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38081056377). This was before the last resource additions and must not be treated as validation of current HEAD.
- Current Android build: [run 38081191407](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38081191407), in progress at report creation.
- Current evidence guard: [run 38081191405](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38081191405), in progress at report creation.
- Current emulator UI smoke: [run 38081191436](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38081191436), queued at report creation.

This batch advances the drawer substantially but does **not** claim the whole app is 1:1. Runtime drawer visibility, row destinations, profile/course data, original APK screenshot comparison and all four tabs' visual parity remain open.
