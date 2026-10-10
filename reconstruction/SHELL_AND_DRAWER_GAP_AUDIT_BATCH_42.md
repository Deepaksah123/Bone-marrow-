# Main Shell and Drawer Gap Audit — Batch 42

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Source archive:** checksum-verified `base.apk_Decompiler.com.zip`  
**Original APK SHA-256:** `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`  
**Scope:** source-backed shell/drawer interaction audit; no unrelated repository or educational-content changes.

## Source evidence recovered

1. `sources/kotlin/parsePeriod.java:83` inflates `R.layout.activity_home_revamp`. Its generated binding requires `bottomNavigation` as a `TabLayout`, `drawerLayout`, `drawerMenu`, `upperContainer`, `fullContainer`, `iconMenu`, `iconBookmark`, `iconSearch`, and other shell views.
2. `sources/kotlin/zabz.java:1649–1668` sets the menu icon resource/tag and attaches click handlers to menu, search, and bookmark controls. The menu handler checks the `menu` tag and calls the drawer binding's action; this is not a decorative-only icon.
3. `sources/kotlin/copyToBuffer.java:163–192` confirms home-tab fragments are managed in `upperContainer` with `Home_<class>` tags. This is separate from full-screen routing through `fullContainer`.
4. `sources/kotlin/getSegmentIndex.java` is the generated view-binding class for `drawer_menu_revamp`. Its required IDs include `navigation_recycler_view`, `layoutProfilePicture`, `tvProfileName`, `yourCourseContainer`, `navYourCourse`, `tvSettings`, `navAboutUs`, `navFaq`, `navInvite`, `navContactUs`, `navRateUs`, `navReportCopyright`, `navTerms`, and additional rows. It also requires plan/buy/referral/debugging views that are explicitly outside the allowed scope.

## Current-replica comparison

- `activity_main.xml` retains the header, `TabLayout`, `upperContainer`, `fullContainer`, and a drawer child, so the overall shell host is present.
- `drawerMenu` currently includes `drawer_menu_empty_host_replica.xml`, which is only an empty `FrameLayout`. Therefore the menu content and menu-open interaction are not reconstructed.
- The visible search control has no click listener in `MainActivity.java`; the bookmark icon is currently hidden. The original source attaches handlers to these controls.
- The original drawer layout entry is referenced by `R.java` as `drawer_menu_revamp` (`0x7f0d00b3`), but that layout file is absent from the checksum-verified decompiler ZIP. The original APK has a resource table, but the working project does not yet have a decoded, verified XML tree for this drawer.

## Safe implementation decision

Do **not** fill the drawer with guessed rows, invented account details, fabricated click destinations, or a generic replacement that is claimed to be exact. Also do not restore plan purchase, upgrade, referral-coupon, subscription, renewal, checkout, or advertising surfaces. Next implementation must first recover the drawer's original binary XML / view hierarchy and trace its non-monetization click destinations. Then wire the menu icon to that verified drawer and implement only routes supported by source.

## Validation boundary

This is a static source audit. It does not claim the drawer is fixed or runtime-tested. Current Android build and evidence-guard status must be tracked separately from device-level QA.

## Resolution update — Batch 53

The decompiler ZIP still lacks a decoded file named `drawer_menu_revamp`, but the original APK itself was recovered and SHA-256 verified. Its resource table maps `R.layout.drawer_menu_revamp` (`0x7f0d00b3`) to obfuscated entry `On`; that 10,056-byte binary XML has now been decoded and used to reconstruct the drawer's source-backed view hierarchy. See [Drawer Binary XML Recovery — Batch 53](DRAWER_BINARY_XML_RECOVERY_BATCH_53.md). Runtime visibility/data binding and click destinations remain open; monetization/referral/debug rows stay excluded.
