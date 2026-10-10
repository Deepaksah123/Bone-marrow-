package com.marrow.reconstruction;

import androidx.fragment.app.FragmentActivity;
import android.graphics.Color;
import android.graphics.BitmapFactory;
import android.util.Base64;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.widget.FrameLayout;
import android.widget.HorizontalScrollView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import com.google.android.material.tabs.TabLayout;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

public final class MainActivity extends FragmentActivity {
    private TabLayout tabLayout;
    private static final int[] ICONS = { R.drawable.ic_home_tab_home, R.drawable.ic_home_tab_qbank, R.drawable.ic_home_tab_tests, R.drawable.ic_home_tab_videos };
    private static final int[] LABELS = { R.string.tab_home, R.string.tab_qbank, R.string.tab_tests, R.string.tab_video };
    private int selectedTab = 0;
    private FrameLayout content;

    private int dp(float value) { return (int)(value * getResources().getDisplayMetrics().density + 0.5f); }
    private int color(int id) { return getColor(id); }
    private boolean isDark() { return (getResources().getConfiguration().uiMode & android.content.res.Configuration.UI_MODE_NIGHT_MASK) == android.content.res.Configuration.UI_MODE_NIGHT_YES; }
    private int pageColor() { return isDark() ? Color.rgb(16,19,20) : Color.WHITE; }
    private int cardColor() { return isDark() ? Color.rgb(23,27,29) : Color.WHITE; }
    private int primaryText() { return isDark() ? Color.rgb(242,244,244) : Color.rgb(34,39,41); }
    private int secondaryText() { return isDark() ? Color.rgb(157,165,167) : Color.rgb(125,132,135); }

    @Override protected void onCreate(Bundle state) {
        super.onCreate(state);
        setContentView(R.layout.activity_main);
        ImageView menuIcon = findViewById(R.id.iconMenu);
        byte[] menuIconBytes = Base64.decode(getString(R.string.source_menu_icon_png_base64), Base64.DEFAULT);
        menuIcon.setImageBitmap(BitmapFactory.decodeByteArray(menuIconBytes, 0, menuIconBytes.length));
        content = findViewById(R.id.upperContainer);
        tabLayout = findViewById(R.id.bottomNavigation);
        tabLayout.setTabMode(TabLayout.MODE_FIXED);
        tabLayout.setTabGravity(TabLayout.GRAVITY_FILL);
        tabLayout.setSelectedTabIndicator(null);
        tabLayout.setTabRippleColor(null);
        for (int i=0;i<4;i++) {
            TabLayout.Tab tab=tabLayout.newTab().setCustomView(R.layout.item_home_tab);
            View custom=tab.getCustomView();
            ImageView icon=custom.findViewById(R.id.tab_icon);
            TextView label=custom.findViewById(R.id.tab_label);
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
        TextView label=custom.findViewById(R.id.tab_label);
        ImageView icon=custom.findViewById(R.id.tab_icon);
        label.setTextColor(selected?color(R.color.shell_selected):color(R.color.shell_muted));
        icon.setAlpha(selected?1f:.72f);
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

    private LinearLayout column() {
        LinearLayout v=new LinearLayout(this); v.setOrientation(LinearLayout.VERTICAL);
        v.setPadding(dp(18),dp(16),dp(18),dp(20)); v.setBackgroundColor(pageColor()); return v;
    }
    private TextView text(String value, int size, boolean bold, int textColor) {
        TextView t=new TextView(this); t.setText(value); t.setTextSize(size); t.setTextColor(textColor);
        if(bold)t.setTypeface(Typeface.DEFAULT,Typeface.BOLD); return t;
    }
    private GradientDrawable rounded(int fill, int stroke) {
        GradientDrawable d=new GradientDrawable(); d.setColor(fill); d.setCornerRadius(dp(12));
        if(stroke!=0)d.setStroke(dp(1),stroke); return d;
    }
    private void heading(LinearLayout root,String value) {
        TextView t=text(value,18,true,primaryText());
        LinearLayout.LayoutParams p=new LinearLayout.LayoutParams(-1,-2); p.bottomMargin=dp(12); root.addView(t,p);
    }
    private void sectionCard(LinearLayout root, String title, String subtitle) {
        LinearLayout card=new LinearLayout(this); card.setOrientation(LinearLayout.VERTICAL);
        card.setPadding(dp(16),dp(14),dp(16),dp(14)); card.setBackground(rounded(cardColor(),isDark()?Color.rgb(48,54,56):Color.rgb(230,233,235)));
        TextView a=text(title,15,true,primaryText()); card.addView(a);
        if(subtitle!=null&&!subtitle.isEmpty()){
            TextView b=text(subtitle,13,false,secondaryText());
            LinearLayout.LayoutParams p=new LinearLayout.LayoutParams(-1,-2);p.topMargin=dp(6);card.addView(b,p);
        }
        LinearLayout.LayoutParams cp=new LinearLayout.LayoutParams(-1,-2); cp.bottomMargin=dp(12); root.addView(card,cp);
    }
    private View scroll(LinearLayout body) {
        ScrollView s=new ScrollView(this); s.setFillViewport(true); s.setBackgroundColor(pageColor()); s.addView(body); return s;
    }

    // Home hierarchy and IDs were decoded from the original fragment_home binary XML.
    // User/account progress is intentionally left empty until its original data flow is reconstructed.
    private View buildHome() {
        View root = LayoutInflater.from(this).inflate(R.layout.fragment_home_replica, content, false);
        androidx.recyclerview.widget.RecyclerView cards = root.findViewById(R.id.rvHomeCard);
        cards.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        return root;
    }

    // Source trace resolves fragment_qbank_landing to a ConstraintLayout with
    // rvSubjectList and progressLoadList. Keep the real structure; do not invent subjects.
    private View buildQbank() {
        View root = LayoutInflater.from(this).inflate(R.layout.fragment_qbank_landing_replica, content, false);
        androidx.recyclerview.widget.RecyclerView subjects = root.findViewById(R.id.rvSubjectList);
        subjects.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        return root;
    }

    // Original test landing is a ConstraintLayout with a collapsing app bar,
    // Material TabLayout, RecyclerView, empty/loading containers. Keep existing filter labels pending trace.
    private View buildTests() {
        View root = LayoutInflater.from(this).inflate(R.layout.fragment_home_test_replica, content, false);
        // These IDs and the root hierarchy are taken from the decoded original fragment_home_test.
        // Tabs/categories remain unpopulated until their source-backed data flow is implemented.
        com.google.android.material.tabs.TabLayout tabs = root.findViewById(R.id.tabs);
        androidx.recyclerview.widget.RecyclerView list = root.findViewById(R.id.rvMainList);
        list.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        return root;
    }

    // Source trace maps Videos to fragment_video_landing (FrameLayout), with a
    // nested scroll area, subject EpoxyRecyclerView and video/banner containers.
    // Do not populate invented lessons or recreate excluded upsell/advertising UI.
    private View buildVideos() {
        View root = LayoutInflater.from(this).inflate(R.layout.fragment_video_landing_replica, content, false);
        androidx.recyclerview.widget.RecyclerView subjects = root.findViewById(R.id.epoxyRVSubject);
        subjects.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        return root;
    }

    private View createTabContent(int index, ViewGroup parent) {
        content = (FrameLayout) parent;
        return index==0 ? buildHome() : index==1 ? buildQbank() : index==2 ? buildTests() : buildVideos();
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
