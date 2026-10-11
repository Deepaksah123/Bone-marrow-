package com.marrow.reconstruction;

import androidx.fragment.app.FragmentActivity;
import android.content.res.Configuration;
import android.content.res.ColorStateList;
import android.graphics.Rect;
import android.graphics.BitmapFactory;
import android.util.Base64;
import android.util.TypedValue;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.LayoutInflater;
import android.widget.ImageView;
import android.widget.TextView;
import com.google.android.material.tabs.TabLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import java.util.Locale;

public final class MainActivity extends FragmentActivity {
    private TabLayout tabLayout;
    private ImageView bookmarkIcon;
    private TextView textBranding;
    private TextView textPageTitle;
    private androidx.drawerlayout.widget.DrawerLayout drawerLayout;
    private static final int[] ICONS = { R.drawable.ic_home_tab_home, R.drawable.ic_home_tab_qbank, R.drawable.ic_home_tab_tests, R.drawable.ic_home_tab_videos };
    private static final int[] LABELS = { R.string.tab_home, R.string.tab_qbank, R.string.tab_tests, R.string.tab_video };
    private int selectedTab = 0;

    private int dp(float value) { return (int)(value * getResources().getDisplayMetrics().density + 0.5f); }
    private int color(int id) { return getColor(id); }

    // Mirrors the original Google Play Services DeviceProperties.isTablet(Resources) test.
    private boolean isSourceTablet() {
        Configuration configuration = getResources().getConfiguration();
        int screenSize = configuration.screenLayout & Configuration.SCREENLAYOUT_SIZE_MASK;
        return screenSize > Configuration.SCREENLAYOUT_SIZE_LARGE
                || (screenSize <= Configuration.SCREENLAYOUT_SIZE_LARGE
                && configuration.smallestScreenWidthDp >= 600);
    }

    private int themeColor(int attribute, int fallbackColor) {
        TypedValue value = new TypedValue();
        if (getTheme().resolveAttribute(attribute, value, true)) {
            if (value.resourceId != 0) return getColor(value.resourceId);
            if (value.type >= TypedValue.TYPE_FIRST_COLOR_INT
                    && value.type <= TypedValue.TYPE_LAST_COLOR_INT) return value.data;
        }
        return color(fallbackColor);
    }

    @Override protected void onCreate(Bundle state) {
        super.onCreate(state);
        setContentView(R.layout.activity_main);
        ImageView menuIcon = findViewById(R.id.iconMenu);
        drawerLayout = findViewById(R.id.drawerLayout);
        menuIcon.setOnClickListener(v -> drawerLayout.openDrawer(android.view.Gravity.START));
        ImageView searchIcon = findViewById(R.id.iconSearch);
        searchIcon.setOnClickListener(v -> {
            FragmentManager manager = getSupportFragmentManager();
            if (manager.findFragmentByTag(SearchOverlayFragment.TAG) == null) {
                manager.beginTransaction()
                        .setCustomAnimations(R.anim.trans_left_in, R.anim.trans_left_out,
                                R.anim.trans_right_in, R.anim.trans_right_out)
                        .add(R.id.fullContainer, new SearchOverlayFragment(), SearchOverlayFragment.TAG)
                        .addToBackStack(SearchOverlayFragment.TAG)
                        .commit();
            }
        });
        // The drawer's source-backed non-monetization hierarchy is reconstructed.
        // Keep account data and row destinations unbound until their original flows are traced.
        bookmarkIcon = findViewById(R.id.iconBookmark);
        textBranding = findViewById(R.id.textBranding);
        textPageTitle = findViewById(R.id.textPageTitle);
        byte[] menuIconBytes = Base64.decode(getString(R.string.source_menu_icon_png_base64), Base64.DEFAULT);
        menuIcon.setImageBitmap(BitmapFactory.decodeByteArray(menuIconBytes, 0, menuIconBytes.length));
        tabLayout = findViewById(R.id.bottomNavigation);
        tabLayout.setTabMode(TabLayout.MODE_SCROLLABLE);
        tabLayout.setTabGravity(TabLayout.GRAVITY_FILL);
        tabLayout.setSelectedTabIndicator(R.drawable.ic_tab_indicator);
        tabLayout.setSelectedTabIndicatorHeight(dp(4));
        tabLayout.setTabIndicatorFullWidth(true);
        for (int i=0;i<4;i++) {
            TabLayout.Tab tab=tabLayout.newTab().setCustomView(R.layout.item_home_tab);
            View custom=tab.getCustomView();
            ImageView icon=custom.findViewById(R.id.icon);
            TextView label=custom.findViewById(R.id.title);
            icon.setImageResource(ICONS[i]);
            label.setText(LABELS[i]);
            custom.setContentDescription(getString(LABELS[i]));
            tabLayout.addTab(tab,false);
        }
        tabLayout.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override public void onTabSelected(TabLayout.Tab tab) { renderTab(tab.getPosition()); }
            @Override public void onTabUnselected(TabLayout.Tab tab) { updateTabAppearance(tab,false); }
            @Override public void onTabReselected(TabLayout.Tab tab) { renderTab(tab.getPosition()); }
        });
        if (state != null) selectedTab = state.getInt("selected_home_tab", 0);
        selectedTab = Math.max(0, Math.min(selectedTab, 3));
        tabLayout.selectTab(tabLayout.getTabAt(selectedTab));
    }

    private void updateToolbarTitle(int index) {
        if (textBranding == null || textPageTitle == null) return;
        if (index == 0) {
            textBranding.setVisibility(View.VISIBLE);
            textPageTitle.setVisibility(View.GONE);
            return;
        }
        textBranding.setVisibility(View.GONE);
        textPageTitle.setVisibility(View.VISIBLE);
        switch (index) {
            case 1:
                textPageTitle.setText(R.string.replica_tab_title_qbank_edition_85);
                break;
            case 2:
                textPageTitle.setText(R.string.replica_tab_title_tests);
                break;
            case 3:
                textPageTitle.setText(R.string.replica_tab_title_videos_edition_85);
                break;
            default:
                textBranding.setVisibility(View.VISIBLE);
                textPageTitle.setVisibility(View.GONE);
        }
    }

    private void updateTabAppearance(TabLayout.Tab tab, boolean selected) {
        if (tab == null || tab.getCustomView() == null) return;
        View custom=tab.getCustomView();
        TextView label=custom.findViewById(R.id.title);
        ImageView icon=custom.findViewById(R.id.icon);
        int tint = selected
                ? themeColor(com.google.android.material.R.attr.colorPrimary, R.color.colorPrimary)
                : themeColor(R.attr.onBackgroundSurface3, R.color.n_40);
        label.setTextColor(tint);
        icon.setColorFilter(tint);
        custom.setSelected(selected);
    }

    private void renderTab(int index) {
        selectedTab = Math.max(0, Math.min(index, 3));
        updateToolbarTitle(selectedTab);
        // The source DataBuffer exposes the bookmark action on HOME only.
        if (bookmarkIcon != null) {
            bookmarkIcon.setVisibility(selectedTab == 0 ? View.VISIBLE : View.GONE);
        }
        for (int i = 0; i < tabLayout.getTabCount(); i++) {
            updateTabAppearance(tabLayout.getTabAt(i), i == selectedTab);
        }

        FragmentManager manager = getSupportFragmentManager();
        String destinationTag = sourceDestinationTagFor(selectedTab);
        Fragment destination = manager.findFragmentByTag(destinationTag);
        androidx.fragment.app.FragmentTransaction transaction = manager.beginTransaction();

        // Match the verified source helper: remove inactive Home_ destinations, preserve the
        // selected instance if present, then add it if absent or show it if already managed.
        for (Fragment fragment : manager.getFragments()) {
            if (fragment != null && fragment.isAdded()
                    && fragment.getTag() != null
                    && fragment.getTag().startsWith("Home_")
                    && fragment != destination) {
                transaction.remove(fragment);
            }
        }

        if (destination == null) {
            destination = newTabFragment(selectedTab);
            transaction.add(R.id.upperContainer, destination, destinationTag);
        } else {
            transaction.show(destination);
        }
        transaction.commit();
    }

    // These destination names are verified in the original DataBuffer model.
    // Local wrapper Fragments keep reconstruction classes separate from source names.
    private static String sourceDestinationTagFor(int index) {
        switch (index) {
            case 1: return "Home_kotlin.ResidentKeyRequirementUnsupportedResidentKeyRequirementException";
            case 2: return "Home_kotlin.WalletConstantsCardNetwork";
            case 3: return "Home_kotlin.setScrollPosition";
            default: return "Home_kotlin.makeGooglePlayServicesAvailable";
        }
    }

    private static TabContentFragment newTabFragment(int index) {
        TabContentFragment fragment;
        switch (index) {
            case 1: fragment = new QBankTabFragment(); break;
            case 2: fragment = new TestsTabFragment(); break;
            case 3: fragment = new VideosTabFragment(); break;
            default: fragment = new HomeTabFragment(); break;
        }
        Bundle args = new Bundle();
        args.putInt(TabContentFragment.ARG_TAB_INDEX, Math.max(0, Math.min(index, 3)));
        fragment.setArguments(args);
        return fragment;
    }

    private void configureInternModeSwitch(View root) {
        com.google.android.material.switchmaterial.SwitchMaterial modeSwitch =
                root.findViewById(R.id.switchInternMode);
        TextView modeStatus = root.findViewById(R.id.tvInternModeStatus);
        if (modeSwitch == null || modeStatus == null) return;

        // The original XML defines the initial switch state as unchecked and the
        // OFF colors through its theme attributes. The original event -> ViewModel
        // -> observer transition has not yet been traced end-to-end here. Do not
        // fake an ON/OFF transition by changing only the label and colors.
        modeStatus.setText(String.format(Locale.ROOT,
                getString(R.string.concise_mode), modeSwitch.isChecked() ? "ON" : "OFF"));
        modeSwitch.setClickable(false);
        modeSwitch.setFocusable(false);
    }

    private int resolveThemeColor(int attribute, int fallback) {
        TypedValue value = new TypedValue();
        if (getTheme().resolveAttribute(attribute, value, true)) {
            if (value.resourceId != 0) {
                return androidx.core.content.ContextCompat.getColor(this, value.resourceId);
            }
            return value.data;
        }
        return fallback;
    }

    private View createTabContent(int index, ViewGroup parent) {
        // Inflate the source-shaped resource hierarchy instead of synthesizing screen content.
        // Lists/Compose surfaces remain empty until their original adapters/data bindings are recovered.
        int layout;
        switch (index) {
            case 1: layout = R.layout.fragment_qbank_landing_replica; break;
            case 2: layout = R.layout.fragment_home_test_replica; break;
            case 3: layout = R.layout.fragment_video_landing_replica; break;
            default: layout = R.layout.fragment_home_replica; break;
        }
        View root = LayoutInflater.from(this).inflate(layout, parent, false);
        if (index == 0) {
            androidx.recyclerview.widget.RecyclerView cards = root.findViewById(R.id.rvHomeCard);
            if (cards != null) {
                cards.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
                // Source HomeViewModelV2 starts in loading state; its fragment hides the empty
                // RecyclerView and shows shimmerMain until real home-card data arrives.
                cards.setVisibility(View.GONE);
            }
            com.facebook.shimmer.ShimmerFrameLayout shimmer = root.findViewById(R.id.shimmerMain);
            if (shimmer != null) shimmer.setVisibility(View.VISIBLE);
        } else if (index == 1) {
            androidx.recyclerview.widget.RecyclerView subjects = root.findViewById(R.id.rvSubjectList);
            if (subjects != null) {
                subjects.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
                // Source QBankLandingViewModel enters loading before the first real subject list arrives.
                subjects.setVisibility(View.GONE);
            }
            View progress = root.findViewById(R.id.progressLoadList);
            if (progress != null) progress.setVisibility(View.VISIBLE);
        } else if (index == 2) {
            androidx.recyclerview.widget.RecyclerView list = root.findViewById(R.id.rvMainList);
            if (list != null) {
                list.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
                // The source Test landing fragment has explicit showLoading/hideLoading states.
                // Keep the empty list hidden while its original test adapter/data flow is absent.
                list.setVisibility(View.GONE);
            }
            View loading = root.findViewById(R.id.loadingContainer);
            if (loading != null) loading.setVisibility(View.VISIBLE);
            View empty = root.findViewById(R.id.emptyLayout);
            if (empty != null) empty.setVisibility(View.GONE);
        } else {
            configureInternModeSwitch(root);
            androidx.recyclerview.widget.RecyclerView subjects = root.findViewById(R.id.epoxyRVSubject);
            int spanCount = isSourceTablet() ? 3 : 2;
            if (subjects != null) {
                subjects.setLayoutManager(new androidx.recyclerview.widget.GridLayoutManager(this, spanCount) {
                    @Override
                    public boolean supportsPredictiveItemAnimations() {
                        return false;
                    }
                });
                final int verticalSpacing = getResources().getDimensionPixelSize(R.dimen.margin_6dp);
                final int horizontalSpacing = getResources().getDimensionPixelSize(R.dimen.margin_4dp);
                subjects.addItemDecoration(new androidx.recyclerview.widget.RecyclerView.ItemDecoration() {
                    @Override
                    public void getItemOffsets(Rect outRect, View view,
                            androidx.recyclerview.widget.RecyclerView parent,
                            androidx.recyclerview.widget.RecyclerView.State state) {
                        outRect.top = verticalSpacing;
                        outRect.bottom = verticalSpacing;
                        outRect.left = horizontalSpacing;
                        outRect.right = horizontalSpacing;
                    }
                });
            }

            // These controls are bound by the original VideoLandingFragment view binding.
            // The original close action dispatches a dedicated banner-dismiss event.
            View internModeBanner = root.findViewById(R.id.clInternModeBanner);
            View closeInternModeBanner = root.findViewById(R.id.btnCloseInternModeBanner);
            if (internModeBanner != null && closeInternModeBanner != null) {
                closeInternModeBanner.setOnClickListener(v ->
                        internModeBanner.setVisibility(View.GONE));
            }

            // The original second ImageButton (ibTooltip) dispatches the event that opens
            // InternModeTooltipState. The current-edition flag is not data-bound in this replica,
            // so keep the verified default tooltip text and do not invent the ED6 Learn More state.
            View internModeTooltip = root.findViewById(R.id.tooltipInternModeInfo);
            View internModeTooltipTrigger = root.findViewById(R.id.ibTooltip);
            if (internModeTooltip != null && internModeTooltipTrigger != null) {
                internModeTooltipTrigger.setOnClickListener(v -> {
                    TextView tooltipBody = root.findViewById(R.id.txtToolTipBody);
                    View learnMore = root.findViewById(R.id.tvLearnMore);
                    if (tooltipBody != null) {
                        tooltipBody.setText(R.string.text_concise_tooltip_description);
                    }
                    if (learnMore != null) learnMore.setVisibility(View.GONE);
                    internModeTooltip.setVisibility(View.VISIBLE);
                });
                View doneInternModeTooltip = root.findViewById(R.id.btnInternModeToolTipDone);
                if (doneInternModeTooltip != null) {
                    doneInternModeTooltip.setOnClickListener(v ->
                            internModeTooltip.setVisibility(View.GONE));
                }
            }
        }
        return root;
    }

    public static class TabContentFragment extends Fragment {
        private static final String ARG_TAB_INDEX = "tab_index";

        static TabContentFragment newInstance(int index) {
            TabContentFragment fragment = new TabContentFragment();
            Bundle args = new Bundle();
            args.putInt(ARG_TAB_INDEX, index);
            fragment.setArguments(args);
            return fragment;
        }

        @Override public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle state) {
            int index = getArguments() == null ? 0 : getArguments().getInt(ARG_TAB_INDEX, 0);
            if (!(requireActivity() instanceof MainActivity)) {
                return new View(requireContext());
            }
            return ((MainActivity) requireActivity()).createTabContent(
                    Math.max(0, Math.min(index, 3)), container);
        }
    }

    public static final class HomeTabFragment extends TabContentFragment { }
    public static final class QBankTabFragment extends TabContentFragment { }
    public static final class TestsTabFragment extends TabContentFragment { }
    public static final class VideosTabFragment extends TabContentFragment { }

    @Override public void onBackPressed() {
        // Preserve the original shell when Android BACK is pressed over the
        // navigation drawer. FragmentActivity handles the Search back stack
        // after the drawer is closed.
        if (drawerLayout != null
                && drawerLayout.isDrawerOpen(android.view.Gravity.START)) {
            drawerLayout.closeDrawer(android.view.Gravity.START);
            return;
        }
        super.onBackPressed();
    }

    @Override protected void onSaveInstanceState(Bundle out) {
        out.putInt("selected_home_tab",selectedTab); super.onSaveInstanceState(out);
    }
}
