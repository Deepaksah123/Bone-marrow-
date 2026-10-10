# APK Installability Preflight — Batch 41

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Build artifact:** `marrow-reconstruction-debug`, artifact ID `11677674404`.

## Checks actually completed

- Downloaded artifact ZIP; `unzip -t` passed.
- Extracted `app-debug.apk`; APK ZIP integrity passed.
- `jarsigner -verify -verbose -certs` reported `jar verified`; signer shown as Android Debug.
- APK SHA-256: `b43993b0b7b3ce2c2d7e06c4ef93bf4526a9c4f10984cac02537bc2d13958f7e`.
- Gradle config declares `applicationId 'com.marrow.reconstruction.replica'`, distinct from the original resource package `com.marrow`. This avoids a package-name collision with the original installation.

## Not yet verified

- No Android device/emulator is connected to this workflow, so actual installation, first launch, rotation, dark-mode switching and on-device visual QA are **not** claimed.
- The APK is debug-signed; do not treat it as a production/release-signed package.

## Source/contamination boundary

This audit concerns only the APK built by this repository's GitHub Actions workflow. No external repository assets or educational content were introduced.
