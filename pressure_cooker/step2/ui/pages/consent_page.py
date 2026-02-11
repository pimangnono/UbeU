"""
Page 1: Consent Form

- Study description, what to expect, data usage
- Name input for the interview
- Checkbox consent + submit
- Demo Mode: Watch AI personas go through the interview
"""

import httpx
import streamlit as st


API_BASE = "http://localhost:8000"

# AI Test Personas for Demo Mode
DEMO_PERSONAS = {
    "fluent_expert": {
        "name": "Fluent Expert",
        "display_name": "Morgan",
        "description": "Final-year business student, knows frameworks, comfortable typing",
        "icon": "🎓",
    },
    "reluctant_expert": {
        "name": "Reluctant Expert",
        "display_name": "Alex",
        "description": "Final-year business student, knows frameworks, uncomfortable typing (short responses)",
        "icon": "😓",
    },
    "novice_learner": {
        "name": "Novice Learner",
        "display_name": "Riley",
        "description": "Year 1 student, no case study experience, doesn't know frameworks",
        "icon": "🌱",
    },
}


def _generate_demo_bfi44(persona_id: str) -> dict:
    """Generate BFI-44 responses based on persona personality."""
    import random

    # Persona personality vectors (O, C, E, A, N)
    vectors = {
        "fluent_expert": (0.7, 0.85, 0.7, 0.6, 0.25),
        "reluctant_expert": (0.6, 0.8, 0.3, 0.5, 0.4),
        "novice_learner": (0.6, 0.5, 0.5, 0.7, 0.5),
    }

    # BFI-44 item trait mappings (simplified)
    trait_items = {
        "E": [1, 6, 11, 16, 21, 26, 31, 36],
        "A": [2, 7, 12, 17, 22, 27, 32, 37, 42],
        "C": [3, 8, 13, 18, 23, 28, 33, 38, 43],
        "N": [4, 9, 14, 19, 24, 29, 34, 39],
        "O": [5, 10, 15, 20, 25, 30, 35, 40, 41, 44],
    }
    reversed_items = {6, 21, 31, 2, 12, 27, 37, 8, 18, 23, 43, 9, 24, 34, 35, 41}

    o, c, e, a, n = vectors.get(persona_id, (0.5, 0.5, 0.5, 0.5, 0.5))
    trait_values = {"O": o, "C": c, "E": e, "A": a, "N": n}

    responses = {}
    for trait, items in trait_items.items():
        base_value = trait_values[trait]
        for item in items:
            if item in reversed_items:
                score = int(5 - (base_value * 4) + 0.5)
            else:
                score = int(1 + (base_value * 4) + 0.5)
            noise = random.choice([-1, 0, 0, 0, 1])
            score = max(1, min(5, score + noise))
            responses[str(item)] = score

    return responses


def render():
    st.header("Study Consent Form")

    # Demo Mode Section (collapsible at top)
    with st.expander("🤖 **Demo Mode** — Watch an AI candidate", expanded=False):
        st.markdown("""
        **Watch an AI persona go through the interview automatically.**

        This is useful for testing and seeing how different types of candidates
        approach the case study.
        """)

        col1, col2 = st.columns([2, 1])
        with col1:
            selected_persona = st.selectbox(
                "Select AI Persona:",
                options=list(DEMO_PERSONAS.keys()),
                format_func=lambda x: f"{DEMO_PERSONAS[x]['icon']} {DEMO_PERSONAS[x]['name']}",
            )

        persona = DEMO_PERSONAS[selected_persona]
        st.caption(f"**{persona['name']}**: {persona['description']}")

        if st.button("🚀 Start Demo", type="primary"):
            with st.spinner("Setting up AI demo session..."):
                try:
                    # Create participant with AI name
                    resp = httpx.post(
                        f"{API_BASE}/participant",
                        json={"name": f"AI_{persona['display_name']}"},
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

                    # Auto-submit BFI-44 based on persona
                    bfi_responses = _generate_demo_bfi44(selected_persona)
                    resp3 = httpx.post(
                        f"{API_BASE}/participant/{pid}/bfi44",
                        json={"responses": bfi_responses, "duration_seconds": 60},
                        timeout=10.0,
                    )
                    resp3.raise_for_status()

                    # Store demo mode settings
                    st.session_state.participant_id = pid
                    st.session_state.participant_name = persona["display_name"]
                    st.session_state.demo_mode = True
                    st.session_state.demo_persona = selected_persona
                    st.session_state.current_step = "interview"
                    st.rerun()

                except httpx.HTTPError as e:
                    st.error(f"Connection error: {e}. Is the backend running?")

        st.markdown("---")

    st.markdown("""
    ### About This Study

    You are invited to participate in a research study on analytical discussion
    and personality expression. The study involves:

    1. **Personality Questionnaire** (~5 min): A standard 44-item personality
       questionnaire (BFI-44).
    2. **Case Study Discussion** (~15 min): A business case study discussion with
       AI-powered colleagues about a realistic business problem. You will
       participate as yourself.
    3. **Brief Survey** (~2 min): A short survey about your experience.

    ### What to Expect

    During the case study discussion, you will interact with two AI colleagues
    (Jordan and Sam) and a facilitator in a consulting-style scenario involving
    business problem analysis. You'll be presented with a company and its
    challenge, and can ask for data to support your analysis. Please respond
    naturally as you would in a real team discussion.

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
