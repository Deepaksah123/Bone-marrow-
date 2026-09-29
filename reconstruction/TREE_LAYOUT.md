# Reconstruction tree layout

Source: `base.apk`
SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`

## Placement rule

Do not rename or randomly regroup APK entries. When an entry is materialized, preserve its original APK path.

### Core application layers

- `AndroidManifest.xml` — original binary manifest; decode before editing.
- `resources.arsc` — original resource table; decode with an Android resource decoder.
- `classes.dex` ... `classes5.dex` — application/dependency bytecode; keep one-to-one with original DEX names.
- `lib/<abi>/*.so` — native libraries; preserve ABI directories exactly.
- `assets/lottie/**` — application UI animations.
- `assets/css/**` — application/web-content styling.
- `assets/font/**`, `assets/fonts/**`, `assets/*.ttf` — application typography.
- other `assets/**` — preserve original relative path unless explicitly excluded.
- `META-INF/**` — APK signing/build metadata; not UI code.

### Obfuscated root resources

The APK contains hundreds of root-level entries with short/obfuscated names such as `A`, `A.xml`, `BA`, etc. These are NOT safe to relocate based on filename alone. They must remain at their original APK path until `resources.arsc` is decoded and the resource IDs are resolved.

### Explicitly excluded

Payment/Juspay/Razorpay/PhonePe assets, login/auth-specific resources, and advertising-specific resources are excluded from the reconstruction payload. See `reconstruction/EXCLUDED_INTERFACES.txt`.

### Important bytecode caveat

The DEX files contain both app code and third-party SDK code. It is not safe to remove payment/login/ad classes from raw DEX by string matching: that would corrupt bytecode. Those UI/features should be removed at the decoded source/resource layer after proper DEX/resource decompilation.
