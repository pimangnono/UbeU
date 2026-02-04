"""
Page 1: Consent Form

- Study description, what to expect, data usage
- Name input for the interview
- Checkbox consent + submit
"""

import httpx
import streamlit as st


API_BASE = "http://localhost:8000"


def render():
    st.header("Study Consent Form")

    st.markdown("""
    ### About This Study

    You are invited to participate in a research study on workplace communication
    and personality expression. The study involves:

    1. **Personality Questionnaire** (~5 min): A standard 44-item personality
       questionnaire (BFI-44).
    2. **Group Discussion** (~15 min): A simulated workplace discussion with
       AI-powered colleagues about a realistic workplace scenario. You will
       participate as yourself.
    3. **Brief Survey** (~2 min): A short survey about your experience.

    ### What to Expect

    During the group discussion, you will interact with two AI colleagues
    (Jordan and Sam) and a facilitator in a workplace scenario involving a
    team decision. Please respond naturally as you would in a real workplace
    discussion.

    ### Data Usage

    - Your responses will be used for academic research on personality
      assessment and AI-mediated communication.
    - All data is stored securely and identified only by a participant ID.
    - Your name is used only during the interview for natural conversation.
    - You may withdraw at any time.

    ### Confidentiality

    Your individual responses will not be shared. Only aggregated,
    anonymized results will be reported.
    """)

    st.markdown("---")

    # Name input
    name = st.text_input(
        "Your first name (used during the discussion):",
        placeholder="e.g., Alex",
        key="consent_name",
    )

    # Consent checkbox
    consent = st.checkbox(
        "I have read the above information and voluntarily agree to participate "
        "in this study. I understand I can withdraw at any time.",
        key="consent_checkbox",
    )

    # Submit
    if st.button("Continue", type="primary", disabled=not (consent and name)):
        with st.spinner("Setting up your session..."):
            try:
                # Create participant
                resp = httpx.post(
                    f"{API_BASE}/participant",
                    json={"name": name},
                    timeout=10.0,
                )
                resp.raise_for_status()
                data = resp.json()
                pid = data["participant_id"]

                # Record consent
                resp2 = httpx.post(
                    f"{API_BASE}/participant/{pid}/consent",
                    json={"consent": True},
                    timeout=10.0,
                )
                resp2.raise_for_status()

                # Store in session state
                st.session_state.participant_id = pid
                st.session_state.participant_name = name
                st.session_state.current_step = "bfi44"
                st.rerun()

            except httpx.HTTPError as e:
                st.error(f"Connection error: {e}. Is the backend running?")
