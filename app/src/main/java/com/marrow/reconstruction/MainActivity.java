package com.marrow.reconstruction;

import android.app.Activity;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.view.View;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.widget.FrameLayout;
import android.widget.HorizontalScrollView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import com.google.android.material.tabs.TabLayout;

public final class MainActivity extends Activity {
    private TabLayout tabLayout;
    private static final int[] ICONS = { R.drawable.ic_home_tab_home, R.drawable.ic_home_tab_qbank, R.drawable.ic_home_tab_tests, R.drawable.ic_home_tab_videos };
    private static final int[] LABELS = { R.string.tab_home, R.string.tab_qbank, R.string.tab_tests, R.string.tab_video };
    private int selectedTab = 0;
    private FrameLayout content;
    private int selectedTestFilter = 0;

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
        content = findViewById(R.id.fullContainer);
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
        selectedTab=index;
        for(int i=0;i<tabLayout.getTabCount();i++) updateTabAppearance(tabLayout.getTabAt(i),i==index);
        content.removeAllViews();
        View screen = index==0 ? buildHome() : index==1 ? buildQbank() : index==2 ? buildTests() : buildVideos();
        content.addView(screen, new FrameLayout.LayoutParams(-1,-1));
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

    // Source-backed Home elements: module generation/completion, Zen area, and Share Marrow.
    // Dynamic user/course cards are intentionally omitted until actual account data is available.
    private View buildHome() {
        LinearLayout body=column();
        heading(body,"Home");
        LinearLayout progress=new LinearLayout(this); progress.setOrientation(LinearLayout.VERTICAL);
        progress.setPadding(dp(16),dp(16),dp(16),dp(16)); progress.setBackground(rounded(isDark()?Color.rgb(23,27,29):Color.rgb(248,250,250),isDark()?Color.rgb(48,54,56):Color.rgb(232,236,237)));
        progress.addView(text("Module completion",15,true,primaryText()));
        TextView amount=text("—",25,true,primaryText());
        LinearLayout.LayoutParams ap=new LinearLayout.LayoutParams(-1,-2);ap.topMargin=dp(10);progress.addView(amount,ap);
        progress.addView(text("Progress is not available without the original account data",12,false,secondaryText()));
        LinearLayout.LayoutParams pp=new LinearLayout.LayoutParams(-1,-2);pp.bottomMargin=dp(14);body.addView(progress,pp);
        sectionCard(body,"Zen Area","");
        sectionCard(body,"Share Marrow","");
        return scroll(body);
    }

    // Source trace resolves fragment_qbank_landing to a ConstraintLayout with
    // rvSubjectList and progressLoadList. Keep the real structure; do not invent subjects.
    private View buildQbank() {
        View root = LayoutInflater.from(this).inflate(R.layout.fragment_qbank_landing_replica, content, false);
        androidx.recyclerview.widget.RecyclerView subjects = root.findViewById(R.id.rvSubjectList);
        subjects.setLayoutManager(new androidx.recyclerview.widget.LinearLayoutManager(this));
        return root;
    }

    // Preserve existing test landing affordances while continuing to trace original strings/resources.
    private View buildTests() {
        LinearLayout body=column(); heading(body,"Tests");
        HorizontalScrollView hs=new HorizontalScrollView(this); hs.setHorizontalScrollBarEnabled(false);
        LinearLayout tabs=new LinearLayout(this); tabs.setOrientation(LinearLayout.HORIZONTAL);
        String[] names={"My Tests","Grand Tests","Previous Year"};
        for(int i=0;i<names.length;i++){
            TextView t=text(names[i],13,true,i==selectedTestFilter?Color.rgb(63,184,208):secondaryText());
            t.setGravity(Gravity.CENTER);t.setPadding(dp(14),dp(12),dp(14),dp(12));
            final int filter=i;
            t.setOnClickListener(v -> { selectedTestFilter=filter; renderTab(2); });
            tabs.addView(t,new LinearLayout.LayoutParams(-2,-2));
        }
        hs.addView(tabs);body.addView(hs);
        sectionCard(body,names[selectedTestFilter],"Test data is not connected to the recovered data layer.");
        return scroll(body);
    }

    // Source fragment is a scrollable landing with content sections; no fabricated lessons.
    private View buildVideos() {
        LinearLayout body=column(); heading(body,"Videos");
        sectionCard(body,"Revision","");
        sectionCard(body,"Sample Videos","");
        sectionCard(body,"Downloaded","");
        sectionCard(body,"Notes","");
        return scroll(body);
    }

    @Override protected void onSaveInstanceState(Bundle out) {
        out.putInt("selected_home_tab",selectedTab); super.onSaveInstanceState(out);
    }
}
