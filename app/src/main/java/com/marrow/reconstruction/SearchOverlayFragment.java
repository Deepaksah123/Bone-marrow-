package com.marrow.reconstruction;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

/**
 * Source-shaped overlay for the original Better Search surface.
 * Search result data is intentionally not fabricated; only the verified initial UI is rendered.
 */
public final class SearchOverlayFragment extends Fragment {
    public static final String TAG = "SearchOverlayFragment";

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
            @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_better_search_replica, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        ImageView back = view.findViewById(R.id.ivBack);
        ImageView close = view.findViewById(R.id.ivClose);
        EditText query = view.findViewById(R.id.etSearch);
        TextView initialMessage = view.findViewById(R.id.tvInitMessage);

        back.setOnClickListener(v -> {
            FragmentManager manager = getParentFragmentManager();
            if (manager.getBackStackEntryCount() > 0) {
                manager.popBackStack();
            } else {
                manager.beginTransaction().remove(this).commit();
            }
        });
        close.setOnClickListener(v -> query.setText(""));
        query.addTextChangedListener(new TextWatcher() {
            @Override public void beforeTextChanged(CharSequence s, int start, int count, int after) { }
            @Override public void onTextChanged(CharSequence s, int start, int before, int count) {
                boolean empty = s == null || s.length() == 0;
                close.setVisibility(empty ? View.GONE : View.VISIBLE);
                initialMessage.setVisibility(empty ? View.VISIBLE : View.GONE);
            }
            @Override public void afterTextChanged(Editable s) { }
        });
    }
}
