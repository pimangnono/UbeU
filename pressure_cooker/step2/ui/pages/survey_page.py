"""
Page 4: Post-Session Experience Survey

5 Likert items + open text feedback.
"""

import httpx
import streamlit as st


API_BASE = "http://localhost:8000"

SURVEY_ITEMS = [
    ("naturalness", "How natural did the conversation feel?"),
    ("authenticity", "How authentic did the AI characters (Jordan and Sam) seem?"),
    ("realism", "How realistic was the business case scenario?"),
    ("engagement", "How engaged were you in the discussion?"),
    ("recommendation", "Would you recommend this experience to others?"),
]

LIKERT_LABELS = {
    1: "Strongly disagree",
    2: "Disagree",
    3: "Neutral",
    4: "Agree",
    5: "Strongly agree",
}


def render():
    pid = st.session_state.get("participant_id")
    if not pid:
        st.warning("Please complete the consent form first.")
        st.session_state.current_step = "consent"
        st.rerun()
        return

    st.header("Post-Discussion Survey")
    st.markdown(
        "Please rate your experience. Your feedback helps us improve the study."
    )
    st.markdown("---")

    with st.form("survey_form"):
        responses = {}

        for key, question in SURVEY_ITEMS:
            st.markdown(f"**{question}**")
            val = st.radio(
                question,
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: f"{x} - {LIKERT_LABELS[x]}",
                horizontal=True,
                key=f"survey_{key}",
                label_visibility="collapsed",
            )
            responses[key] = val
            st.markdown("")

        st.markdown("---")
        st.markdown("**Any additional feedback or comments?**")
        open_feedback = st.text_area(
            "Open feedback",
            placeholder="Share your thoughts about the experience...",
            key="survey_open_feedback",
            label_visibility="collapsed",
        )

        submitted = st.form_submit_button("Submit Survey", type="primary")

    if submitted:
        with st.spinner("Submitting survey..."):
            try:
                # Also end the session if not already ended
                sid = st.session_state.get("session_id")
                if sid:
                    try:
                        httpx.post(
                            f"{API_BASE}/session/{sid}/end",
                            timeout=30.0,
                        )
                    except httpx.HTTPError:
                        pass  # Session may already be ended

                resp = httpx.post(
                    f"{API_BASE}/participant/{pid}/survey",
                    json={
                        **responses,
                        "open_feedback": open_feedback,
                    },
                    timeout=10.0,
                )
                resp.raise_for_status()

                st.session_state.current_step = "thankyou"
                st.rerun()

            except httpx.HTTPError as e:
                st.error(f"Error submitting survey: {e}")
