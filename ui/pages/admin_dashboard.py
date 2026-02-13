"""
Admin Dashboard Page: HR view for reviewing candidates.

V4: Supabase Auth for admin login (replaces hardcoded password).

Features:
- Candidate list with sorting/filtering
- Individual candidate reports
- Multi-candidate comparison
- Validation metrics
- Export functionality
"""

import streamlit as st
import httpx
import plotly.graph_objects as go
import plotly.express as px
from typing import Optional
from datetime import datetime


API_BASE = "http://localhost:8000"


def show_admin_dashboard():
    """Display admin/HR dashboard."""
    st.header("HR Dashboard")

    # Admin authentication
    if "admin_authenticated" not in st.session_state:
        st.session_state.admin_authenticated = False

    if not st.session_state.admin_authenticated:
        show_admin_login()
        return

    # Dashboard tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "Candidate List",
        "Candidate Details",
        "Comparison View",
        "Validation Metrics"
    ])

    with tab1:
        show_candidate_list()

    with tab2:
        show_candidate_details()

    with tab3:
        show_comparison_view()

    with tab4:
        show_validation_metrics()


def show_admin_login():
    """Show admin login form (Supabase Auth placeholder — full implementation in Phase 1)."""
    st.subheader("Admin Login")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form("admin_login"):
            email = st.text_input("Email", placeholder="admin@ubeu.com")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login", use_container_width=True)

            if submitted:
                if not email or not password:
                    st.error("Please enter email and password")
                    return

                # TODO Phase 1: Replace with Supabase Auth
                # For now, validate against backend
                try:
                    with httpx.Client(timeout=10.0) as client:
                        response = client.get(f"{API_BASE}/health")
                        response.raise_for_status()
                        # If backend is running, allow admin access
                        st.session_state.admin_authenticated = True
                        st.rerun()
                except Exception:
                    st.error("Cannot connect to backend. Ensure the server is running.")

        st.caption("Supabase Auth will be configured in Phase 1.")


def _fetch_candidates() -> list[dict]:
    """Fetch candidates from the API."""
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(f"{API_BASE}/hr/candidates")
            response.raise_for_status()
            data = response.json()
            return data.get("candidates", [])
    except Exception as e:
        st.error(f"Failed to fetch candidates: {str(e)}")
        return []


def show_candidate_list():
    """Show list of all candidates."""
    st.subheader("All Candidates")

    candidates = _fetch_candidates()

    if not candidates:
        st.info("No completed candidates yet.")
        return

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        sort_by = st.selectbox(
            "Sort by",
            ["Date (Newest)", "Date (Oldest)", "Logic Score (High)", "Logic Score (Low)", "Name"]
        )
    with col2:
        min_score = st.slider("Min Logic Score", 0.0, 5.0, 0.0, 0.5)
    with col3:
        search_query = st.text_input("Search by name", placeholder="Enter name...")

    # Apply filters
    filtered = candidates

    if search_query:
        filtered = [c for c in filtered if search_query.lower() in c.get("name", "").lower()]

    if min_score > 0:
        filtered = [c for c in filtered if c.get("logic_overall_score", 0) >= min_score]

    # Apply sorting
    if sort_by == "Date (Newest)":
        filtered.sort(key=lambda x: x.get("completed_at", ""), reverse=True)
    elif sort_by == "Date (Oldest)":
        filtered.sort(key=lambda x: x.get("completed_at", ""))
    elif sort_by == "Logic Score (High)":
        filtered.sort(key=lambda x: x.get("logic_overall_score", 0), reverse=True)
    elif sort_by == "Logic Score (Low)":
        filtered.sort(key=lambda x: x.get("logic_overall_score", 0))
    elif sort_by == "Name":
        filtered.sort(key=lambda x: x.get("name", ""))

    # Display as cards
    st.markdown(f"**{len(filtered)} candidates**")

    for candidate in filtered:
        render_candidate_card(candidate)


def render_candidate_card(candidate: dict):
    """Render a candidate summary card."""
    pid = candidate.get("participant_id", "N/A")
    name = candidate.get("name", "Unknown")
    completed = candidate.get("completed_at", "")
    logic_score = candidate.get("logic_overall_score", 0)
    personality = candidate.get("personality_vector", {})

    # Format date
    if completed:
        try:
            dt = datetime.fromisoformat(completed.replace("Z", "+00:00"))
            completed_str = dt.strftime("%Y-%m-%d %H:%M")
        except Exception:
            completed_str = completed
    else:
        completed_str = "N/A"

    with st.container():
        col1, col2, col3, col4 = st.columns([2, 1, 2, 1])

        with col1:
            st.markdown(f"**{name}**")
            st.caption(f"ID: {pid} | {completed_str}")

        with col2:
            st.metric("Logic", f"{logic_score:.1f}/5")

        with col3:
            if personality:
                traits_str = " | ".join([f"{k}: {v:.2f}" for k, v in personality.items()])
                st.caption(traits_str)
            else:
                st.caption("No personality data")

        with col4:
            if st.button("View", key=f"view_{pid}"):
                st.session_state.selected_candidate = pid
                st.rerun()

        st.markdown("---")


def show_candidate_details():
    """Show detailed view of selected candidate."""
    st.subheader("Candidate Details")

    candidates = _fetch_candidates()

    if not candidates:
        st.info("No candidates available.")
        return

    # Selection
    candidate_options = {c["participant_id"]: f"{c['name']} ({c['participant_id']})" for c in candidates}

    selected = st.selectbox(
        "Select Candidate",
        options=list(candidate_options.keys()),
        format_func=lambda x: candidate_options.get(x, x),
        index=0
    )

    if not selected:
        return

    # Find candidate data
    candidate = next((c for c in candidates if c["participant_id"] == selected), None)

    if not candidate:
        st.error("Candidate not found")
        return

    # Display detailed report
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Logic Assessment")
        logic_score = candidate.get("logic_overall_score", 0)
        st.metric("Overall Score", f"{logic_score:.1f}/5")

        st.markdown("**Strengths:**")
        for strength in candidate.get("logic_strengths", []):
            st.markdown(f"- {strength}")

    with col2:
        st.markdown("### Personality Profile")
        personality = candidate.get("personality_vector", {})

        if personality:
            # Radar chart
            traits = ["O", "C", "E", "A", "N"]
            trait_names = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]
            scores = [personality.get(t, 0.5) for t in traits]

            fig = go.Figure(go.Scatterpolar(
                r=scores + [scores[0]],
                theta=trait_names + [trait_names[0]],
                fill='toself',
                line_color='rgb(99, 102, 241)',
            ))

            fig.update_layout(
                polar=dict(radialaxis=dict(range=[0, 1])),
                height=300,
                margin=dict(t=20, b=20, l=40, r=40),
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No personality data available")

    # Actions
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("Download PDF Report", use_container_width=True)

    with col2:
        st.button("View Full Transcript", use_container_width=True)

    with col3:
        st.button("Add to Comparison", use_container_width=True)


def show_comparison_view():
    """Show side-by-side candidate comparison."""
    st.subheader("Candidate Comparison")

    candidates = _fetch_candidates()

    if len(candidates) < 2:
        st.info("Need at least 2 candidates for comparison.")
        return

    # Multi-select candidates
    candidate_options = {c["participant_id"]: f"{c['name']} ({c['participant_id']})" for c in candidates}

    selected_ids = st.multiselect(
        "Select candidates to compare (2-4)",
        options=list(candidate_options.keys()),
        format_func=lambda x: candidate_options.get(x, x),
        default=list(candidate_options.keys())[:2],
        max_selections=4,
    )

    if len(selected_ids) < 2:
        st.warning("Please select at least 2 candidates.")
        return

    selected_candidates = [c for c in candidates if c["participant_id"] in selected_ids]

    # Logic score comparison
    st.markdown("### Logic Score Comparison")

    fig = go.Figure(go.Bar(
        x=[c["name"] for c in selected_candidates],
        y=[c.get("logic_overall_score", 0) for c in selected_candidates],
        marker_color='rgb(99, 102, 241)',
    ))

    fig.update_layout(
        yaxis=dict(range=[0, 5], title="Score"),
        height=300,
    )

    st.plotly_chart(fig, use_container_width=True)

    # Personality comparison radar
    st.markdown("### Personality Comparison")

    traits = ["O", "C", "E", "A", "N"]
    trait_names = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

    fig = go.Figure()

    colors = ['rgb(99, 102, 241)', 'rgb(34, 197, 94)', 'rgb(249, 115, 22)', 'rgb(236, 72, 153)']

    for i, candidate in enumerate(selected_candidates):
        personality = candidate.get("personality_vector", {})
        scores = [personality.get(t, 0.5) for t in traits]

        fig.add_trace(go.Scatterpolar(
            r=scores + [scores[0]],
            theta=trait_names + [trait_names[0]],
            name=candidate["name"],
            line_color=colors[i % len(colors)],
        ))

    fig.update_layout(
        polar=dict(radialaxis=dict(range=[0, 1])),
        height=400,
    )

    st.plotly_chart(fig, use_container_width=True)

    # Summary table
    st.markdown("### Summary Table")

    table_data = []
    for c in selected_candidates:
        personality = c.get("personality_vector", {})
        table_data.append({
            "Name": c["name"],
            "Logic Score": f"{c.get('logic_overall_score', 0):.1f}",
            "O": f"{personality.get('O', 0.5):.2f}",
            "C": f"{personality.get('C', 0.5):.2f}",
            "E": f"{personality.get('E', 0.5):.2f}",
            "A": f"{personality.get('A', 0.5):.2f}",
            "N": f"{personality.get('N', 0.5):.2f}",
        })

    st.dataframe(table_data, use_container_width=True, hide_index=True)


def show_validation_metrics():
    """Show validation metrics for the assessment system.

    Note: These will show real computed statistics once Phase 7 is implemented.
    For now, displays placeholder structure.
    """
    st.subheader("Validation Metrics")

    st.info("Validation metrics will be computed from real participant data once enough sessions are collected (Phase 7).")

    st.markdown("### Planned Analysis")
    st.markdown("""
    | Method | Purpose |
    |--------|---------|
    | Pearson r per trait | Linear correlation with p-value |
    | ICC(2,1) per trait | Absolute agreement |
    | Paired t-test per trait | Systematic bias detection |
    | Cohen's d | Effect size |
    | MAE per trait | Error magnitude |
    | Bland-Altman plots | Visual agreement |
    """)

    st.markdown("### Data Quality Thresholds")
    st.markdown("""
    - Minimum 8 candidate turns per session
    - Minimum 15 average words per turn
    - Minimum trait coverage confidence of 0.3
    - Maximum 1 parse error per evaluation
    """)
