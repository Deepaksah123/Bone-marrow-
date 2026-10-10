
# Source-Traced Better Search UI — Batch 56

**Repository:** `Deepaksah123/Bone-marrow-` only  
**Source:** SHA-verified original APK/decompiler archive plus source-trace evidence.  
**Scope:** source-backed search entry UI and navigation; no search result data or paid UI is fabricated.

## Source trace

- The original shell search icon opens `transformFutureAsync`, whose binding inflates `fragment_better_search`.
- The original navigation helper adds the destination to `R.id.fullContainer` and the back stack, using the source left/right slide animations.
- Non-monetization controls preserved: `llSearch`, `ivBack`, `ivSearch`, `etSearch`, `ivClose`, `tvInitMessage`, `tlFilters`, `llRecentSearch`, `rvResults`, `llError`, `imgError`, `tvNoResult`, `clProgress`, `pbMain`, `clEmpty`, and `tvClearAll`.
- Initial instruction: “Search MCQ IDs, Pearl IDs, topics from Qbank, Tests, Videos, Video Topics and Pearls”.
- Original search hint resource: “Try MB7831, PM4232”.
- Original `clProMain` / `btViewPlans` subtree is deliberately excluded under the no-monetization requirement.

## Changes

- Added a source-shaped Search overlay fragment and wired the toolbar search icon to open it in `fullContainer` with source slide animations and back-stack behavior.
- Added source UI assets, strings, dimensions, and the missing body-large typography attribute.
- Mapped light/dark status-bar color to the original theme's `?attr/colorPrimary`; status-bar icon contrast remains controlled by the source light/dark theme flags.
- Back and clear controls work. Search result/history adapters and API-backed behavior remain intentionally unimplemented; no questions or results are invented.

## Validation

- Android build PASS: [run 38086133865](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133865). Debug APK artifact ID `11682261632`, 8,269,398 bytes, SHA-256 `8aa289841eeb52239d3b069d329a909f76515ec33e059748512fa20d25d31d7f`.
- Evidence guard PASS: [run 38086133816](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133816).
- API 31 emulator smoke is in progress: [run 38086133823](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38086133823). It now exercises Search open/Back return and captures `search-open.png` plus the corresponding hierarchies; runtime QA is not yet claimed.
- Search data flow and original-APK pixel comparison remain open.
