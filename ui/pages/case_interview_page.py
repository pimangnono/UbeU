"""
Case Interview Page: Mode 1 - One-on-one case study interview with AI facilitator.
"""

import streamlit as st
import httpx
import time
from typing import Optional


API_BASE = "http://localhost:8000"


def get_next_phase_after_case():
    """Determine next phase based on active modes and completion status."""
    active_modes = st.session_state.get("active_modes", {"case": False, "group": True})

    # If group is active and not yet completed, go to group
    if active_modes.get("group", True) and not st.session_state.get("group_completed", False):
        return "group"

    # Otherwise go to results
    return "results"

# Interview duration in seconds (15 minutes)
INTERVIEW_DURATION = 15 * 60


def show_case_instruction_page():
    """Show immersive loading page before starting the case study interview."""

    # Navy background interview room
    st.markdown("""
<div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            padding: 50px 30px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;">
    <div style="font-size: 0.85rem; opacity: 0.7; margin-bottom: 8px; letter-spacing: 3px; text-transform: uppercase;">
        Interview Room
    </div>
    <div style="font-size: 2.2rem; font-weight: 700; margin-bottom: 30px;">
        Case Study Interview
    </div>

    <div style="display: flex; justify-content: center; gap: 100px; margin: 40px 0;">
        <div style="text-align: center;">
            <div style="font-size: 48px; margin-bottom: 10px;">🎯</div>
            <div style="font-weight: 600; font-size: 1.1rem;">Facilitator</div>
            <div style="font-size: 0.8rem; opacity: 0.7;">Your interviewer</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 48px; margin-bottom: 10px;">👤</div>
            <div style="font-weight: 600; font-size: 1.1rem;">You</div>
            <div style="font-size: 0.8rem; opacity: 0.7;">Candidate</div>
        </div>
    </div>
</div>
    """, unsafe_allow_html=True)

    # Instructions
    st.markdown("### What to Expect")
    st.markdown("""
You'll analyze a business problem with an AI facilitator.
Ask for data, structure your thinking, and develop recommendations.
Think of this as a consulting case interview.
    """)

    st.markdown("### Tips")
    st.markdown("""
- Structure your approach before diving in
- Ask for specific data to test your hypotheses
- Think out loud — share your reasoning
- Be clear and concise in your recommendations
    """)

    st.markdown("")

    # Start button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start Interview", type="primary", use_container_width=True):
            st.session_state.case_ready_to_start = True
            st.rerun()


def show_case_interview_page():
    """Display case study interview interface."""
    # Initialize session state
    if "case_session_id" not in st.session_state:
        st.session_state.case_session_id = None
    if "case_messages" not in st.session_state:
        st.session_state.case_messages = []
    if "case_start_time" not in st.session_state:
        st.session_state.case_start_time = None
    if "revealed_data" not in st.session_state:
        st.session_state.revealed_data = set()
    if "case_ended" not in st.session_state:
        st.session_state.case_ended = False
    if "case_ready_to_start" not in st.session_state:
        st.session_state.case_ready_to_start = False

    # Show instructions first if not ready to start
    if not st.session_state.case_ready_to_start and st.session_state.case_session_id is None:
        show_case_instruction_page()
        return

    # Start session if not started
    if st.session_state.case_session_id is None and not st.session_state.case_ended:
        start_case_session()
        return

    # Header with timer
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.header("Case Study Interview")
    with col2:
        if st.session_state.case_start_time:
            elapsed = int(time.time() - st.session_state.case_start_time)
            remaining = max(0, INTERVIEW_DURATION - elapsed)
            mins, secs = divmod(remaining, 60)

            if remaining < 300:  # Less than 5 minutes
                st.warning(f"Time: {mins}:{secs:02d}")
            else:
                st.info(f"Time: {mins}:{secs:02d}")
    with col3:
        if st.button("End Interview", type="secondary"):
            end_case_session()
            return

    st.markdown("---")

    # Layout: Chat on left, Data panel on right
    chat_col, data_col = st.columns([3, 2])

    with data_col:
        render_data_panel()

    with chat_col:
        render_chat_interface()


def start_case_session():
    """Initialize the case study session."""
    st.info("Starting case study session...")

    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(
                f"{API_BASE}/session/create",
                json={
                    "participant_id": st.session_state.participant_id,
                    "mode": "case_study",
                }
            )
            response.raise_for_status()
            data = response.json()

            st.session_state.case_session_id = data["session_id"]
            st.session_state.case_start_time = time.time()
            st.session_state.case_company = data.get("company_name", "Company")
            st.session_state.case_problem = data.get("problem_statement", "")

            # Convert opening messages
            st.session_state.case_messages = [
                {"role": "facilitator", "content": msg["content"]}
                for msg in data.get("opening_messages", [])
            ]
            st.rerun()

    except httpx.HTTPError as e:
        st.error(f"Failed to start session: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")


def render_chat_interface():
    """Render the main chat interface."""
    st.subheader("Conversation")

    # Chat container with scrolling
    chat_container = st.container()

    with chat_container:
        for msg in st.session_state.case_messages:
            if msg["role"] == "facilitator":
                with st.chat_message("assistant", avatar=":material/description:"):
                    st.markdown(msg["content"])
            else:
                with st.chat_message("user", avatar=":material/person:"):
                    st.markdown(msg["content"])

    # Input area
    if not st.session_state.case_ended:
        user_input = st.chat_input(
            "Type your response...",
            key="case_input"
        )

        if user_input:
            handle_user_message(user_input)


def handle_user_message(content: str):
    """Handle user message submission."""
    # Add user message
    st.session_state.case_messages.append({
        "role": "candidate",
        "content": content
    })

    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(
                f"{API_BASE}/session/{st.session_state.case_session_id}/message",
                json={"content": content}
            )
            response.raise_for_status()
            data = response.json()

            # Add AI responses
            for turn in data.get("ai_turns", []):
                st.session_state.case_messages.append({
                    "role": "facilitator",
                    "content": turn["content"]
                })

            # Check if session should end
            if data.get("session_state") == "ended":
                st.session_state.case_ended = True

            st.rerun()

    except httpx.HTTPError as e:
        st.error(f"Message failed: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")


def render_data_panel():
    """Render the data panel showing revealed information."""
    st.subheader("Data Panel")

    if not st.session_state.revealed_data:
        st.info("""
        **No data revealed yet.**

        Ask the facilitator for specific data to analyze.
        Data will appear here as it's revealed during the interview.
        """)
        return

    data_gates = st.session_state.get("case_data_gates", {})

    for data_key in st.session_state.revealed_data:
        if data_key in data_gates:
            data = data_gates[data_key]
            with st.expander(f"**{data['title']}**", expanded=True):
                st.markdown(data["content"])


def end_case_session():
    """End the case study session and run evaluation."""
    st.session_state.case_ended = True

    try:
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                f"{API_BASE}/session/{st.session_state.case_session_id}/end"
            )
            response.raise_for_status()
            data = response.json()

            st.session_state.case_assessment = data.get("summary", {})
            st.session_state.case_completed = True
            st.session_state.current_phase = get_next_phase_after_case()

            st.rerun()

    except httpx.HTTPError as e:
        st.error(f"Failed to end session: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
