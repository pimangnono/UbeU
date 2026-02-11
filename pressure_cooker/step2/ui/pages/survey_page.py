"""
Page 4: Post-Session Experience Survey

5 Likert items + open text feedback.
"""

import httpx
import streamlit as st
import streamlit.components.v1 as components
import time


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
        # Set loading state and rerun to show loading screen
        st.session_state.survey_submitting = True
        st.session_state.survey_responses = responses
        st.session_state.survey_feedback = open_feedback
        st.rerun()

    # Handle submission in a separate check (after rerun)
    if st.session_state.get("survey_submitting"):
        # Show full-screen loading overlay using components.html
        components.html(
            """
            <style>
                body { margin: 0; padding: 0; overflow: hidden; }
                .loading-container {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%);
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    z-index: 999999;
                }
                .spinner {
                    width: 100px;
                    height: 100px;
                    border: 8px solid rgba(255,255,255,0.2);
                    border-top: 8px solid #3b82f6;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                    margin-bottom: 32px;
                }
                @keyframes spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
                .loading-text {
                    color: white;
                    font-size: 28px;
                    font-weight: 700;
                    margin-bottom: 16px;
                    text-align: center;
                }
                .loading-subtext {
                    color: #94a3b8;
                    font-size: 18px;
                    margin-bottom: 40px;
                }
                .loading-steps {
                    color: #cbd5e1;
                    font-size: 16px;
                    text-align: center;
                    line-height: 2.2;
                }
                .loading-steps span {
                    display: block;
                    opacity: 0;
                    animation: fadeIn 0.5s ease forwards;
                }
                .loading-steps span:nth-child(1) { animation-delay: 0.5s; }
                .loading-steps span:nth-child(2) { animation-delay: 1.5s; }
                .loading-steps span:nth-child(3) { animation-delay: 2.5s; }
                @keyframes fadeIn {
                    to { opacity: 1; }
                }
                .warning-text {
                    position: absolute;
                    bottom: 40px;
                    color: #fbbf24;
                    font-size: 14px;
                    font-weight: 500;
                }
            </style>
            <div class="loading-container">
                <div class="spinner"></div>
                <div class="loading-text">Submitting Your Feedback</div>
                <div class="loading-subtext">Please wait while we process your session...</div>
                <div class="loading-steps">
                    <span>✓ Saving survey responses...</span>
                    <span>✓ Running personality assessment...</span>
                    <span>✓ Generating your report...</span>
                </div>
                <div class="warning-text">⚠️ Please do not close this window</div>
            </div>
            """,
            height=800,
        )

        # Actually submit
        responses = st.session_state.get("survey_responses", {})
        open_feedback = st.session_state.get("survey_feedback", "")

        try:
            # End the session (triggers personality inference)
            sid = st.session_state.get("session_id")
            if sid:
                try:
                    httpx.post(
                        f"{API_BASE}/session/{sid}/end",
                        timeout=120.0,  # Longer timeout for personality inference
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

            # Clear submission state and go to thank you
            st.session_state.survey_submitting = False
            st.session_state.current_step = "thankyou"
            st.rerun()

        except httpx.HTTPError as e:
            st.session_state.survey_submitting = False
            st.error(f"Error submitting survey: {e}")
            st.rerun()
