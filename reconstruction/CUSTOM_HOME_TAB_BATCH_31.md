# Custom Home Tab Item — Source Hierarchy Batch 31

**Repository:** `Deepaksah123/Bone-marrow-`, branch `main`  
**Verified source archive SHA-256:** `92fa24c6d91faafa61e3317adcb5c7c10384eea437fa6b7f99c09ac372ab8685`

## Restored source custom tab layout

The previous `item_home_tab.xml` had a different hierarchy and different IDs (`tab_icon`, `tab_label`), fixed icon dimensions, and no source indicator overlay. It now follows the decoded `custom_home_tab` hierarchy:

- root LinearLayout with weight 1, centered vertical orientation and wrap-content height;
- 20dp × 20dp FrameLayout with 8dp top margin;
- AppCompatImageView `icon` and source ImageView `indicator` overlaid in the same FrameLayout;
- TextView `title` with source `smallText2` style, 3dp top margin, 10dp bottom margin and `colorPrimary` default;
- exact source `ic_home_indicator.xml` restored and SHA-256 guarded.

`MainActivity` now binds the source IDs `icon` and `title` and tints icon/text with source primary blue when selected and neutral `n_40` when unselected. The indicator stays gone by default because the original per-tab indicator flag/data model is not reconstructed; no unread/new-state badge is invented.

## Validation

The evidence guard passed for the source custom-tab hierarchy: [run 38074219308](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074219308). Android build passed for commit `47d71eef4352`: [run 38074210922](https://github.com/Deepaksah123/Bone-marrow-/actions/runs/38074210922), artifact ID `11678411729`, digest `sha256:e28b72976cc7360079706b7dcf1a01b7256371ecc51151c4026d16b188a89821`. This is source-layout alignment, not on-device pixel-diff QA.
