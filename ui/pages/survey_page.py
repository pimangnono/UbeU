"""
Survey Page: Post-study feedback survey.

Collects:
- Mode-specific experience ratings
- Overall recommendations
- Preferred mode (if both modes active)
- Open-ended feedback
"""

import streamlit as st
import httpx


API_BASE = "http://localhost:8000"

# Survey questions
LIKERT_OPTIONS = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
LIKERT_VALUES = {opt: i + 1 for i, opt in enumerate(LIKERT_OPTIONS)}


def show_survey_page():
    """Display post-study survey with dynamic content based on active modes."""
    st.header("Study Feedback Survey")

    active_modes = st.session_state.get("active_modes", {"case": False, "group": True})
    case_active = active_modes.get("case", False)
    group_active = active_modes.get("group", True)

    # Dynamic intro
    if case_active and group_active:
        st.markdown("""
        Thank you for completing both assessment modes! Your feedback is valuable for improving
        this AI interview platform. Please take a few minutes to share your experience.
        """)
    else:
        st.markdown("""
        Thank you for completing the assessment! Your feedback is valuable for improving
        this AI interview platform. Please take a few minutes to share your experience.
        """)

    st.markdown("---")

    with st.form("survey_form"):
        # Initialize variables for all possible fields
        case_naturalness = None
        case_challenge = None
        case_fairness = None
        group_naturalness = None
        group_authenticity = None
        group_engagement = None
        preferred_mode = None

        # Case Study feedback (only if case mode active)
        if case_active:
            st.subheader("Case Study Interview Experience")

            case_naturalness = st.radio(
                "The conversation with the AI facilitator felt natural",
                options=LIKERT_OPTIONS,
                horizontal=True,
                key="case_naturalness"
            )

            case_challenge = st.radio(
                "The case study was appropriately challenging",
                options=LIKERT_OPTIONS,
                horizontal=True,
                key="case_challenge"
            )

            case_fairness = st.radio(
                "I felt the assessment was fair and unbiased",
                options=LIKERT_OPTIONS,
                horizontal=True,
                key="case_fairness"
            )

            st.markdown("---")

        # Group Discussion feedback (only if group mode active)
        if group_active:
            st.subheader("Group Discussion Experience")

            group_naturalness = st.radio(
                "The AI team members felt like realistic colleagues",
                options=LIKERT_OPTIONS,
                horizontal=True,
                key="group_naturalness"
            )

            group_authenticity = st.radio(
                "I could behave naturally during the group discussion",
                options=LIKERT_OPTIONS,
                horizontal=True,
                key="group_authenticity"
            )

            group_engagement = st.radio(
                "The discussion was engaging and kept my attention",
                options=LIKERT_OPTIONS,
                horizontal=True,
                key="group_engagement"
            )

            st.markdown("---")

        # Overall feedback
        st.subheader("Overall Assessment")

        overall_recommendation = st.radio(
            "I would recommend this type of AI assessment to others",
            options=LIKERT_OPTIONS,
            horizontal=True,
            key="overall_recommendation"
        )

        # Preferred mode question (only if both modes active)
        if case_active and group_active:
            preferred_mode = st.radio(
                "Which assessment mode did you prefer?",
                options=[
                    "Case Study (1-on-1 with AI facilitator)",
                    "Group Discussion (with AI team members)",
                    "Both equally",
                    "Neither"
                ],
                key="preferred_mode"
            )

        would_recommend = st.radio(
            "Would you use this type of AI assessment again?",
            options=["Yes, definitely", "Maybe", "No"],
            horizontal=True,
            key="would_recommend"
        )

        st.markdown("---")

        # Open-ended feedback
        st.subheader("Additional Comments")

        open_feedback = st.text_area(
            "Please share any additional thoughts, suggestions, or concerns about your experience:",
            placeholder="What worked well? What could be improved? Any technical issues?",
            height=150,
            key="open_feedback"
        )

        st.markdown("---")

        # Submit
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button(
                "Submit Survey",
                use_container_width=True,
                type="primary"
            )

        if submitted:
            # Build required fields list dynamically
            required_fields = [overall_recommendation, would_recommend]

            if case_active:
                required_fields.extend([case_naturalness, case_challenge, case_fairness])
            if group_active:
                required_fields.extend([group_naturalness, group_authenticity, group_engagement])
            if case_active and group_active:
                required_fields.append(preferred_mode)

            if any(f is None for f in required_fields):
                st.error("Please answer all required questions.")
                return

            # Build survey data dynamically
            survey_data = {
                "overall_recommendation": LIKERT_VALUES[overall_recommendation],
                "would_recommend": would_recommend,
                "open_feedback": open_feedback.strip() if open_feedback else None,
            }

            if case_active:
                survey_data["case_naturalness"] = LIKERT_VALUES[case_naturalness]
                survey_data["case_challenge"] = LIKERT_VALUES[case_challenge]
                survey_data["case_fairness"] = LIKERT_VALUES[case_fairness]

            if group_active:
                survey_data["group_naturalness"] = LIKERT_VALUES[group_naturalness]
                survey_data["group_authenticity"] = LIKERT_VALUES[group_authenticity]
                survey_data["group_engagement"] = LIKERT_VALUES[group_engagement]

            if case_active and group_active:
                preferred_mode_map = {
                    "Case Study (1-on-1 with AI facilitator)": "case",
                    "Group Discussion (with AI team members)": "group",
                    "Both equally": "both",
                    "Neither": "neither",
                }
                survey_data["preferred_mode"] = preferred_mode_map.get(preferred_mode, "both")

            if st.session_state.get("demo_mode"):
                # Demo mode: store locally
                st.session_state.survey_completed = True
                st.session_state.survey_data = survey_data
                st.session_state.current_phase = "complete"
                st.success("Survey submitted! Thank you for your participation.")
                st.rerun()
            else:
                # Call API
                try:
                    with httpx.Client(timeout=30.0) as client:
                        response = client.post(
                            f"{API_BASE}/participant/{st.session_state.participant_id}/survey",
                            json=survey_data
                        )
                        response.raise_for_status()

                        st.session_state.survey_completed = True
                        st.session_state.current_phase = "complete"
                        st.success("Survey submitted! Thank you for your participation.")
                        st.rerun()

                except httpx.HTTPError as e:
                    st.error(f"Survey submission failed: {str(e)}")
                except Exception as e:
                    st.error(f"Unexpected error: {str(e)}")


def get_completion_summary():
    """Generate completion summary based on active modes."""
    active_modes = st.session_state.get("active_modes", {"case": False, "group": True})
    case_active = active_modes.get("case", False)
    group_active = active_modes.get("group", True)

    steps = ["1. BFI-44 Personality Questionnaire"]
    step_num = 2

    if case_active:
        steps.append(f"{step_num}. Case Study Interview with AI Facilitator")
        step_num += 1
    if group_active:
        steps.append(f"{step_num}. Group Discussion with AI Team Members")
        step_num += 1

    steps.append(f"{step_num}. Feedback Survey")

    return "\n    ".join(steps)


def show_completion_page():
    """Display study completion page with dynamic content."""
    st.header("Study Complete!")

    st.markdown("""
    <div style="text-align: center; padding: 40px;">
        <h2 style="color: #22C55E;">Thank you for your participation!</h2>
    </div>
    """, unsafe_allow_html=True)

    completion_summary = get_completion_summary()

    st.success(f"""
    **Participant ID:** {st.session_state.get('participant_id', 'N/A')}

    Your assessment has been completed and recorded. Here's a summary of what you completed:

    {completion_summary}

    Thank you for helping with this research!
    """)

    st.markdown("---")

    # Final actions
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("View Results Again", use_container_width=True):
            st.session_state.current_phase = "results"
            st.rerun()

    with col2:
        if st.button("Download Report (PDF)", use_container_width=True):
            st.info("PDF download requires backend connection")

    with col3:
        if st.button("Start New Session", use_container_width=True):
            # Clear session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.markdown("---")

    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        <p><strong>Research Contact:</strong> For questions about this study, please contact the research team.</p>
        <p>NTU College of Computing | Final Year Thesis Project</p>
        <p style="margin-top: 20px; color: #999;">
            UbeU V3 - Dual-Mode AI Interview Platform
        </p>
    </div>
    """, unsafe_allow_html=True)
