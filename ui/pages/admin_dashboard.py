"""
Admin Dashboard Page: HR view for reviewing candidates.

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

# Demo candidates for testing
DEMO_CANDIDATES = [
    {
        "participant_id": "P001",
        "name": "Alice Chen",
        "completed_at": "2024-01-15T14:30:00",
        "logic_overall_score": 4.2,
        "logic_strengths": ["Strong problem structuring", "Clear communication"],
        "personality_vector": {"O": 0.72, "C": 0.68, "E": 0.75, "A": 0.82, "N": 0.28},
    },
    {
        "participant_id": "P002",
        "name": "Bob Smith",
        "completed_at": "2024-01-16T10:15:00",
        "logic_overall_score": 3.8,
        "logic_strengths": ["Good quantitative reasoning", "Thorough analysis"],
        "personality_vector": {"O": 0.58, "C": 0.85, "E": 0.45, "A": 0.72, "N": 0.35},
    },
    {
        "participant_id": "P003",
        "name": "Carol Davis",
        "completed_at": "2024-01-17T16:45:00",
        "logic_overall_score": 4.5,
        "logic_strengths": ["Excellent hypothesis thinking", "Strong recommendations"],
        "personality_vector": {"O": 0.88, "C": 0.65, "E": 0.82, "A": 0.58, "N": 0.22},
    },
]


def show_admin_dashboard():
    """Display admin/HR dashboard."""
    st.header("HR Dashboard")

    # Admin authentication (simplified)
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
    """Show admin login form."""
    st.subheader("Admin Login")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form("admin_login"):
            password = st.text_input("Admin Password", type="password")
            submitted = st.form_submit_button("Login", use_container_width=True)

            if submitted:
                # Simple password check (in production, use proper auth)
                if password == "admin123":
                    st.session_state.admin_authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid password")

        st.info("Demo password: admin123")


def show_candidate_list():
    """Show list of all candidates."""
    st.subheader("All Candidates")

    # Fetch candidates
    if st.session_state.get("demo_mode"):
        candidates = DEMO_CANDIDATES
    else:
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get(f"{API_BASE}/hr/candidates")
                response.raise_for_status()
                data = response.json()
                candidates = data.get("candidates", [])
        except Exception as e:
            st.error(f"Failed to fetch candidates: {str(e)}")
            candidates = []

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
        except:
            completed_str = completed
    else:
        completed_str = "N/A"

    # Score color
    if logic_score >= 4:
        score_color = "#22C55E"
    elif logic_score >= 3:
        score_color = "#F97316"
    else:
        score_color = "#EF4444"

    with st.container():
        col1, col2, col3, col4 = st.columns([2, 1, 2, 1])

        with col1:
            st.markdown(f"**{name}**")
            st.caption(f"ID: {pid} | {completed_str}")

        with col2:
            st.metric("Logic", f"{logic_score:.1f}/5")

        with col3:
            if personality:
                # Mini trait display
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

    # Candidate selector
    if st.session_state.get("demo_mode"):
        candidates = DEMO_CANDIDATES
    else:
        # Fetch from API
        candidates = []
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get(f"{API_BASE}/hr/candidates")
                response.raise_for_status()
                data = response.json()
                candidates = data.get("candidates", [])
        except:
            pass

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

    if st.session_state.get("demo_mode"):
        candidates = DEMO_CANDIDATES
    else:
        candidates = []
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get(f"{API_BASE}/hr/candidates")
                response.raise_for_status()
                data = response.json()
                candidates = data.get("candidates", [])
        except:
            pass

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
    """Show validation metrics for the assessment system."""
    st.subheader("Validation Metrics")

    st.info("These metrics show how well the AI assessments correlate with ground truth (BFI-44).")

    # Demo validation data
    validation_data = {
        "n_participants": 50,
        "convergent_validity": {
            "overall_correlation": 0.72,
            "overall_mae": 0.12,
            "trait_validations": {
                "O": {"correlation": 0.68, "mae": 0.14, "bias": -0.05},
                "C": {"correlation": 0.75, "mae": 0.10, "bias": 0.02},
                "E": {"correlation": 0.78, "mae": 0.11, "bias": -0.03},
                "A": {"correlation": 0.70, "mae": 0.13, "bias": 0.01},
                "N": {"correlation": 0.65, "mae": 0.15, "bias": 0.04},
            }
        },
        "discriminant_validity": {
            "logic_personality_correlation": 0.18,
            "constructs_independent": True,
        },
        "ensemble_agreement": {
            "mean_confidence": 0.82,
            "agreement_rate": 0.76,
        }
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Overall Correlation",
            f"{validation_data['convergent_validity']['overall_correlation']:.2f}",
            help="Correlation between AI-inferred and BFI-44 self-reported personality"
        )

    with col2:
        st.metric(
            "Mean Absolute Error",
            f"{validation_data['convergent_validity']['overall_mae']:.3f}",
            help="Average absolute difference between inferred and ground truth scores"
        )

    with col3:
        st.metric(
            "N Participants",
            validation_data["n_participants"],
            help="Number of participants in validation dataset"
        )

    st.markdown("---")

    # Trait-level validation
    st.markdown("### Trait-Level Validation")

    trait_data = validation_data["convergent_validity"]["trait_validations"]
    table_rows = []

    trait_names = {"O": "Openness", "C": "Conscientiousness", "E": "Extraversion", "A": "Agreeableness", "N": "Neuroticism"}

    for trait, data in trait_data.items():
        table_rows.append({
            "Trait": trait_names[trait],
            "Correlation": f"{data['correlation']:.2f}",
            "MAE": f"{data['mae']:.3f}",
            "Bias": f"{data['bias']:+.3f}",
            "Status": "Good" if data['correlation'] > 0.5 else "Fair",
        })

    st.dataframe(table_rows, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Discriminant validity
    st.markdown("### Discriminant Validity")

    col1, col2 = st.columns(2)

    with col1:
        dv = validation_data["discriminant_validity"]
        st.metric(
            "Logic-Personality Correlation",
            f"{dv['logic_personality_correlation']:.2f}",
            help="Low correlation indicates Mode 1 and Mode 2 measure different constructs"
        )

    with col2:
        status = "Pass" if dv["constructs_independent"] else "Fail"
        st.metric("Construct Independence", status)

    st.markdown("---")

    # Ensemble agreement
    st.markdown("### Ensemble Agreement")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Mean Confidence",
            f"{validation_data['ensemble_agreement']['mean_confidence']:.2f}",
            help="Average confidence across 3-model ensemble"
        )

    with col2:
        st.metric(
            "High Agreement Rate",
            f"{validation_data['ensemble_agreement']['agreement_rate']:.0%}",
            help="% of traits where all 3 models agreed (confidence > 0.7)"
        )
