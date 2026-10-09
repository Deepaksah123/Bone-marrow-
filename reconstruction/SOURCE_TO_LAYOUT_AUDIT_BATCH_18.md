# Source-to-layout audit — Batch 18

## Reproducible scan

A standard-library Python audit script has been added at `tools/audit_source_layouts.py`. It scans a decompiler ZIP, collects literal `R.layout.*` references and source line locations, cross-references the decompiled `R.java` layout IDs, checks matching layout entries, and records unresolved symbols. It explicitly avoids inferring screen routes from resource names.

Run it locally in an environment where the decompiler ZIP is available:

```bash
python tools/audit_source_layouts.py base.apk_Decompiler.com.zip --json-out layout-audit.json --markdown-out layout-audit.md
```

## Verified output for the supplied archive

- Archive SHA-256: `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`
- Archive entries: **26,825**
- Java/Kotlin source files scanned: **20,526**
- Layout entries across resource variants: **616**
- Distinct literal `R.layout.*` symbols: **314**
- Literal reference sites: **342**
- `resources.arsc` in this decompiler ZIP: **absent**
- Source symbols with no same-named layout entry: **10**

## Core resource cross-check

| Symbol | ID in decompiled R.java | Matching layout entry |
|---|---|---|
| `activity_home_revamp` | `0x7f0d0033` | Present |
| `fragment_home` | `0x7f0d00d9` | Present |
| `custom_home_tab` | `0x7f0d0079` | Present |
| `fragment_home_test` | `0x7f0d00da` | Present |
| `fragment_qbank_landing` | `0x7f0d00f6` | Present |
| `activity_qbank_lesson_list` | `0x7f0d0052` | Present |
| `fragment_qbank_lesson_list` | `0x7f0d00f7` | Present |
| `activity_qbank_play` | `0x7f0d0053` | Present |
| `activity_qbank_score` | `0x7f0d0054` | Present |
| `activity_qbank_introduction_marrow2` | `0x7f0d0051` | **No same-named layout entry in dump** |
| `fragment_qbank_introduction_marrow2` | `0x7f0d00f5` | Present |
| `activity_test_introduction_marrow2` | `0x7f0d0065` | Present |
| `fragment_video_landing` | `0x7f0d0106` | Present |
| `fragment_video_lesson_list` | `0x7f0d0107` | Present |
| `activity_lesson_video` | `0x7f0d003b` | Present |

## Interpretation and next dependency

The audit confirms the known decompiler archive gap: the QBank introduction activity has an `R.layout` symbol and ID, but its same-named layout file is missing from the dump. The original APK contains `resources.arsc`; this dump does not. The original resource table and compiled binary XML must be decoded to resolve this accurately.

This is a reproducible source-audit tool and verified report, **not an Android UI implementation or build**. No missing screen is fabricated, and excluded ads/upgrade/payment/checkout/subscription/upsell surfaces remain out of scope. Overall readiness remains **PARTIAL, NOT RESOLVED**.
