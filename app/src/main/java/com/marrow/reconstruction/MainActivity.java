package com.marrow.reconstruction;

import androidx.fragment.app.FragmentActivity;
import android.graphics.BitmapFactory;
import android.util.Base64;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.LayoutInflater;
import android.widget.ImageView;
import android.widget.TextView;
import com.google.android.material.tabs.TabLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

public final class MainActivity extends FragmentActivity {
    private TabLayout tabLayout;
    private static final int[] ICONS = { R.drawable.ic_home_tab_home, R.drawable.ic_home_tab_qbank, R.drawable.ic_home_tab_tests, R.drawable.ic_home_tab_videos };
    private static final int[] LABELS = { R.string.tab_home, R.string.tab_qbank, R.string.tab_tests, R.string.tab_video };
    private int selectedTab = 0;

    private int dp(float value) { return (int)(value * getResources().getDisplayMetrics().density + 0.5f); }
    private int color(int id) { return getColor(id); }

    @Override protected void onCreate(Bundle state) {
        super.onCreate(state);
        setContentView(R.layout.activity_main);
        ImageView menuIcon = findViewById(R.id.iconMenu);
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

    private void updateTabAppearance(TabLayout.Tab tab, boolean selected) {
        if (tab == null || tab.getCustomView() == null) return;
        View custom=tab.getCustomView();
        TextView label=custom.findViewById(R.id.title);
        ImageView icon=custom.findViewById(R.id.icon);
        int tint = selected ? color(R.color.mb_50) : color(R.color.n_40);
        label.setTextColor(tint);
        icon.setColorFilter(tint);
        custom.setSelected(selected);
    }

    private void renderTab(int index) {
        selectedTab = Math.max(0, Math.min(index, 3));
        for (int i = 0; i < tabLayout.getTabCount(); i++) {
            updateTabAppearance(tabLayout.getTabAt(i), i == selectedTab);
        }

        FragmentManager manager = getSupportFragmentManager();
        String destinationTag = sourceDestinationTagFor(selectedTab);
        Fragment destination = manager.findFragmentByTag(destinationTag);
        androidx.fragment.app.FragmentTransaction transaction = manager.beginTransaction();

        // Match the verified source's Home_<fully-qualified-class> tag family:
        // keep prior destinations managed, hide inactive ones, and show the selected destination.
        for (Fragment fragment : manager.getFragments()) {
            if (fragment != null && fragment.isAdded()
                    && fragment.getTag() != null
                    && fragment.getTag().startsWith("Home_")
                    && fragment != destination) {
                transaction.hide(fragment);
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
            cards.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        } else if (index == 1) {
            androidx.recyclerview.widget.RecyclerView subjects = root.findViewById(R.id.rvSubjectList);
            subjects.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        } else if (index == 2) {
            androidx.recyclerview.widget.RecyclerView list = root.findViewById(R.id.rvMainList);
            list.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        } else {
            androidx.recyclerview.widget.RecyclerView subjects = root.findViewById(R.id.epoxyRVSubject);
            int spanCount = getResources().getConfiguration().smallestScreenWidthDp >= 600 ? 3 : 2;
            subjects.setLayoutManager(new androidx.recyclerview.widget.GridLayoutManager(this, spanCount));
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

    @Override protected void onSaveInstanceState(Bundle out) {
        out.putInt("selected_home_tab",selectedTab); super.onSaveInstanceState(out);
    }
}
