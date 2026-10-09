package com.marrow.reconstruction;

import android.app.Activity;
import android.content.res.Configuration;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.marrow.reconstruction.R;

/**
 * First native implementation slice: source-verified app shell and four-tab selection.
 * Screen bodies are deliberately not fabricated while their exact view/data wiring is incomplete.
 */
public final class MainActivity extends Activity {
    private static final int[] TAB_IDS = {
        R.id.home_tab, R.id.qbank_tab, R.id.tests_tab, R.id.videos_tab
    };
    private static final int[] ICONS = {
        R.drawable.ic_home_tab_home,
        R.drawable.ic_home_tab_qbank,
        R.drawable.ic_home_tab_tests,
        R.drawable.ic_home_tab_videos
    };
    private static final int[] LABELS = {
        R.string.tab_home, R.string.tab_qbank, R.string.tab_tests, R.string.tab_video
    };

    private int selectedTab = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if (savedInstanceState != null) {
            selectedTab = savedInstanceState.getInt("selected_home_tab", 0);
        }
        selectedTab = Math.max(0, Math.min(selectedTab, TAB_IDS.length - 1));
        bindTabs();
        selectTab(selectedTab);
    }

    private void bindTabs() {
        for (int index = 0; index < TAB_IDS.length; index++) {
            final int destination = index;
            View tab = findViewById(TAB_IDS[index]);
            ImageView icon = tab.findViewById(R.id.tab_icon);
            TextView label = tab.findViewById(R.id.tab_label);
            icon.setImageResource(ICONS[index]);
            label.setText(LABELS[index]);
            tab.setContentDescription(getString(LABELS[index]));
            tab.setOnClickListener(view -> selectTab(destination));
        }
    }

    private void selectTab(int index) {
        selectedTab = index;
        int muted = getColor(R.color.shell_muted);
        int selected = getColor(R.color.shell_selected);
        for (int i = 0; i < TAB_IDS.length; i++) {
            View tab = findViewById(TAB_IDS[i]);
            ImageView icon = tab.findViewById(R.id.tab_icon);
            TextView label = tab.findViewById(R.id.tab_label);
            boolean active = i == selectedTab;
            tab.setSelected(active);
            label.setTextColor(active ? selected : muted);
            icon.setAlpha(active ? 1.0f : 0.78f);
        }
        // Body fragments are intentionally not replaced with guessed placeholder content.
        // The exact Home/QBank/Test/Video destination classes and root layouts are recorded
        // in reconstruction/EXACT_SOURCE_UI_INDEX.md and will be wired as their resources
        // and dependencies are recovered into this standalone Android module.
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        outState.putInt("selected_home_tab", selectedTab);
        super.onSaveInstanceState(outState);
    }
}
