# Video Intern Mode + Watch-Next Exact Values — Batch 36

**Source:** checksum-verified original `base.apk` SHA-256 `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`; decoded resource archive `base.apk_Decompiler.com.zip` SHA-256 `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`.

## Source-backed corrections

- The Intern Mode row uses `?attr/colorSurfaceVariant13`, not `backgroundVariant2`.
- Original AppThemeV2 maps `colorSurfaceVariant13` to `@color/sepia85` in light mode and `@color/brown13` in dark mode. Exact colors restored: `sepia85=#fbe795`, `brown13=#584b19`.
- The Intern Mode switch uses source `@style/SwitchTheme`, restored with its original foreground, activated-color and normal-thumb values.
- The watch-next include restores the original 4dp top margin and 20dp gone-margin-top. Existing continue-watching and watch-next IDs remain mapped to their corresponding source layouts.

## Validation

CI now checks the source attribute, light/dark mappings, exact colors, switch style and watch-next margins. Build/guard outcomes are pending after this commit. This does not claim full video landing parity; the original font assets, hidden video component sublayouts and runtime bindings remain incomplete.
