"""
Results Page: Display assessment results with evidence expanders.

Shows:
- Mode 1 (Case Study): 6-dimension logic scores with evidence quotes
- Mode 2 (Group Discussion): Big Five personality profile with behavioral evidence
- Comparison with BFI-44 ground truth (if available)
"""

import streamlit as st
import httpx
import plotly.graph_objects as go
from typing import Optional


API_BASE = "http://localhost:8000"

# Dimension labels for Mode 1
LOGIC_DIMENSIONS = {
    "problem_structuring": "Problem Structuring",
    "hypothesis_thinking": "Hypothesis-Driven Thinking",
    "quantitative_reasoning": "Quantitative Reasoning",
    "data_synthesis": "Data Synthesis",
    "recommendation_quality": "Recommendation Quality",
    "communication_clarity": "Communication Clarity",
}

# Trait labels for Mode 2
TRAIT_INFO = {
    "O": {"name": "Openness", "description": "Creativity, curiosity, openness to new ideas", "color": "#8B5CF6"},
    "C": {"name": "Conscientiousness", "description": "Organization, dependability, self-discipline", "color": "#3B82F6"},
    "E": {"name": "Extraversion", "description": "Sociability, assertiveness, positive emotions", "color": "#F97316"},
    "A": {"name": "Agreeableness", "description": "Cooperation, trust, helpfulness", "color": "#EC4899"},
    "N": {"name": "Neuroticism", "description": "Emotional instability, anxiety, moodiness", "color": "#6366F1"},
}


def show_results_page():
    """Display assessment results."""
    st.header("Your Assessment Results")

    # Check what's completed
    case_completed = st.session_state.get("case_completed", False)
    group_completed = st.session_state.get("group_completed", False)

    if not case_completed and not group_completed:
        st.warning("No assessments completed yet.")
        return

    # Tabs for each mode
    if case_completed and group_completed:
        tab1, tab2, tab3 = st.tabs(["Case Study Results", "Group Discussion Results", "Combined Profile"])

        with tab1:
            render_case_results()
        with tab2:
            render_group_results()
        with tab3:
            render_combined_profile()
    elif case_completed:
        render_case_results()
        st.info("Complete the Group Discussion to see your full personality profile.")
    else:
        render_group_results()
        st.info("Complete the Case Study to see your logical assessment results.")

    st.markdown("---")

    # Navigation
    col1, col2, col3 = st.columns(3)

    with col1:
        # Check if other mode needs to be done
        if case_completed and not group_completed:
            if st.button("Continue to Group Discussion", type="primary", use_container_width=True):
                st.session_state.current_phase = "group"
                st.rerun()
        elif group_completed and not case_completed:
            if st.button("Continue to Case Study", type="primary", use_container_width=True):
                st.session_state.current_phase = "case"
                st.rerun()

    with col2:
        if case_completed and group_completed:
            if st.button("Continue to Survey", type="primary", use_container_width=True):
                st.session_state.current_phase = "survey"
                st.rerun()

    with col3:
        if st.button("Download Report (PDF)"):
            st.info("PDF download functionality - requires backend connection")


def render_case_results():
    """Render Mode 1 (Case Study) results."""
    st.subheader("Case Study Assessment")

    assessment = st.session_state.get("case_assessment", {})

    if not assessment:
        st.info("Case study assessment not available.")
        return

    # Overall score
    overall_score = assessment.get("overall_score", 0)
    st.metric("Overall Score", f"{overall_score:.1f} / 5.0")

    st.markdown("---")

    # Dimension scores with evidence
    st.markdown("### Dimension Scores")

    col1, col2 = st.columns(2)
    dimensions = list(LOGIC_DIMENSIONS.items())

    for i, (dim_key, dim_label) in enumerate(dimensions):
        col = col1 if i < 3 else col2
        dim_data = assessment.get(dim_key, {})

        with col:
            score = dim_data.get("score", 0) if isinstance(dim_data, dict) else 0
            render_dimension_card(dim_key, dim_label, score, dim_data)

    # Strengths and development areas
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Strengths")
        strengths = assessment.get("strengths", [])
        if strengths:
            for strength in strengths:
                st.markdown(f"- {strength}")
        else:
            st.info("No strengths identified yet.")

    with col2:
        st.markdown("### Development Areas")
        dev_areas = assessment.get("development_areas", [])
        if dev_areas:
            for area in dev_areas:
                st.markdown(f"- {area}")
        else:
            st.info("No development areas identified.")


def render_dimension_card(dim_key: str, dim_label: str, score: int, dim_data: dict):
    """Render a dimension score card with evidence expander."""
    # Score color based on value
    if score >= 4:
        color = "#22C55E"  # Green
        rating = "Strong"
    elif score >= 3:
        color = "#F97316"  # Orange
        rating = "Meets Expectations"
    else:
        color = "#EF4444"  # Red
        rating = "Needs Development"

    st.markdown(f"""
    <div style="padding: 15px; background-color: {color}22; border-left: 4px solid {color}; border-radius: 4px; margin-bottom: 10px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <strong>{dim_label}</strong>
            <span style="font-size: 1.2em; font-weight: bold;">{score}/5</span>
        </div>
        <div style="font-size: 0.85em; color: #666;">{rating}</div>
    </div>
    """, unsafe_allow_html=True)

    # Evidence expander
    evidence = dim_data.get("evidence", []) if isinstance(dim_data, dict) else []
    if evidence:
        with st.expander(f"View evidence for {dim_label}"):
            for i, quote in enumerate(evidence):
                st.markdown(f"""
                <div style="padding: 10px; background-color: #f5f5f5; border-radius: 4px; margin-bottom: 8px;">
                    <em>"{quote}"</em>
                </div>
                """, unsafe_allow_html=True)


def render_group_results():
    """Render Mode 2 (Group Discussion) results."""
    st.subheader("Personality Assessment")

    assessment = st.session_state.get("group_assessment", {})

    if not assessment:
        st.info("Group discussion assessment not available.")
        return

    # Personality vector
    personality_vector = {}
    for trait_key, trait_info in TRAIT_INFO.items():
        trait_name = trait_info["name"].lower()
        trait_data = assessment.get(trait_name, {})
        if isinstance(trait_data, dict):
            personality_vector[trait_key] = trait_data.get("score", 0.5)
        else:
            personality_vector[trait_key] = 0.5

    # Radar chart
    render_personality_radar(personality_vector)

    st.markdown("---")

    # Trait details with evidence
    st.markdown("### Trait Analysis")

    col1, col2 = st.columns(2)
    traits = list(TRAIT_INFO.items())

    for i, (trait_key, trait_info) in enumerate(traits):
        col = col1 if i % 2 == 0 else col2
        trait_name = trait_info["name"].lower()
        trait_data = assessment.get(trait_name, {})

        with col:
            score = trait_data.get("score", 0.5) if isinstance(trait_data, dict) else 0.5
            render_trait_card(trait_key, trait_info, score, trait_data)

    # Strengths and development areas
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Behavioral Strengths")
        strengths = assessment.get("strengths", [])
        if strengths:
            for strength in strengths:
                st.markdown(f"- {strength}")
        else:
            st.info("No strengths identified yet.")

    with col2:
        st.markdown("### Areas for Growth")
        dev_areas = assessment.get("development_areas", [])
        if dev_areas:
            for area in dev_areas:
                st.markdown(f"- {area}")
        else:
            st.info("No development areas identified.")


def render_personality_radar(personality_vector: dict):
    """Render a radar chart for personality traits."""
    traits = ["O", "C", "E", "A", "N"]
    trait_names = [TRAIT_INFO[t]["name"] for t in traits]
    scores = [personality_vector.get(t, 0.5) for t in traits]

    # Close the radar by repeating the first value
    trait_names_closed = trait_names + [trait_names[0]]
    scores_closed = scores + [scores[0]]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=scores_closed,
        theta=trait_names_closed,
        fill='toself',
        fillcolor='rgba(99, 102, 241, 0.3)',
        line=dict(color='rgb(99, 102, 241)', width=2),
        name='Your Profile'
    ))

    # Add BFI-44 ground truth if available
    bfi44_scores = st.session_state.get("bfi44_scores", {})
    if bfi44_scores:
        gt_scores = [bfi44_scores.get(t, 0.5) for t in traits]
        gt_scores_closed = gt_scores + [gt_scores[0]]

        fig.add_trace(go.Scatterpolar(
            r=gt_scores_closed,
            theta=trait_names_closed,
            fill='toself',
            fillcolor='rgba(34, 197, 94, 0.2)',
            line=dict(color='rgb(34, 197, 94)', width=2, dash='dot'),
            name='BFI-44 Ground Truth'
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                tickvals=[0.25, 0.5, 0.75, 1.0],
            )
        ),
        showlegend=True,
        height=400,
        margin=dict(t=20, b=20, l=60, r=60),
    )

    st.plotly_chart(fig, use_container_width=True)


def render_trait_card(trait_key: str, trait_info: dict, score: float, trait_data: dict):
    """Render a personality trait card with evidence expander."""
    name = trait_info["name"]
    description = trait_info["description"]
    color = trait_info["color"]

    # Level description
    if score < 0.3:
        level = "Low"
    elif score < 0.5:
        level = "Moderately Low"
    elif score < 0.7:
        level = "Moderate"
    elif score < 0.85:
        level = "Moderately High"
    else:
        level = "High"

    st.markdown(f"""
    <div style="padding: 15px; background-color: {color}22; border-left: 4px solid {color}; border-radius: 4px; margin-bottom: 10px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <strong>{name}</strong>
            <span style="font-size: 1.2em; font-weight: bold;">{score:.2f}</span>
        </div>
        <div style="font-size: 0.85em; color: #666;">{level} - {description}</div>
    </div>
    """, unsafe_allow_html=True)

    # Evidence expander
    evidence = trait_data.get("evidence", []) if isinstance(trait_data, dict) else []
    if evidence:
        with st.expander(f"View evidence for {name}"):
            for quote in evidence:
                st.markdown(f"""
                <div style="padding: 10px; background-color: #f5f5f5; border-radius: 4px; margin-bottom: 8px;">
                    <em>"{quote}"</em>
                </div>
                """, unsafe_allow_html=True)


def render_combined_profile():
    """Render combined profile comparing both assessments."""
    st.subheader("Combined Assessment Profile")

    case_assessment = st.session_state.get("case_assessment", {})
    group_assessment = st.session_state.get("group_assessment", {})
    bfi44_scores = st.session_state.get("bfi44_scores", {})

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Logical Assessment Summary")
        overall_score = case_assessment.get("overall_score", 0)

        # Summary metrics
        st.metric("Overall Logic Score", f"{overall_score:.1f} / 5.0")

        st.markdown("**Key Strengths:**")
        for strength in case_assessment.get("strengths", [])[:3]:
            st.markdown(f"- {strength}")

    with col2:
        st.markdown("### Personality Profile Summary")

        # Top traits
        traits = []
        for trait_key, trait_info in TRAIT_INFO.items():
            trait_name = trait_info["name"].lower()
            trait_data = group_assessment.get(trait_name, {})
            if isinstance(trait_data, dict):
                score = trait_data.get("score", 0.5)
                traits.append((trait_key, trait_info["name"], score))

        traits.sort(key=lambda x: x[2], reverse=True)

        st.markdown("**Top Traits:**")
        for trait_key, trait_name, score in traits[:3]:
            st.markdown(f"- {trait_name}: {score:.2f}")

    # Ground truth comparison
    if bfi44_scores:
        st.markdown("---")
        st.markdown("### Personality Inference Accuracy")
        st.info("Comparing AI-inferred personality (from group discussion) with BFI-44 self-report ground truth.")

        accuracy_data = []
        for trait_key, trait_info in TRAIT_INFO.items():
            trait_name = trait_info["name"].lower()
            trait_data = group_assessment.get(trait_name, {})

            gt_score = bfi44_scores.get(trait_key, 0.5)
            inferred_score = trait_data.get("score", 0.5) if isinstance(trait_data, dict) else 0.5
            diff = abs(gt_score - inferred_score)

            accuracy_data.append({
                "Trait": trait_info["name"],
                "Ground Truth": f"{gt_score:.2f}",
                "Inferred": f"{inferred_score:.2f}",
                "Difference": f"{diff:.2f}",
                "Match": "Good" if diff < 0.15 else ("Fair" if diff < 0.25 else "Poor"),
            })

        st.dataframe(accuracy_data, use_container_width=True, hide_index=True)

        # Calculate overall MAE
        total_diff = sum(
            abs(bfi44_scores.get(t, 0.5) - group_assessment.get(TRAIT_INFO[t]["name"].lower(), {}).get("score", 0.5))
            for t in TRAIT_INFO
        )
        mae = total_diff / 5

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Mean Absolute Error", f"{mae:.3f}", help="Lower is better. <0.15 is excellent, <0.25 is good.")
        with col2:
            accuracy_level = "Excellent" if mae < 0.15 else ("Good" if mae < 0.25 else "Fair")
            st.metric("Accuracy Level", accuracy_level)
