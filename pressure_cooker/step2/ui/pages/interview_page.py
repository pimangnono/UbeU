"""
Page 3: Live Interview Chat Interface

- st.chat_message for conversation display
- st.chat_input for human input
- Speaker names: "Jordan", "Sam", "Facilitator"
- st.spinner as typing indicator during backend call
- Timer display (countdown from 15 min)
"""

import time

import httpx
import streamlit as st


API_BASE = "http://localhost:8000"

# Map speaker names to chat avatars/icons
SPEAKER_AVATARS = {
    "Jordan": "🔴",
    "Sam": "🟢",
    "Facilitator": "⚙️",
}


def render():
    pid = st.session_state.get("participant_id")
    if not pid:
        st.warning("Please complete the consent form first.")
        st.session_state.current_step = "consent"
        st.rerun()
        return

    st.header("Workplace Discussion")

    # --- Session initialization ---
    if "session_id" not in st.session_state or st.session_state.session_id is None:
        _initialize_session(pid)
        return

    sid = st.session_state.session_id

    # --- Timer display ---
    if "interview_start" in st.session_state:
        elapsed = time.time() - st.session_state.interview_start
        remaining = max(0, 15 * 60 - elapsed)
        mins, secs = divmod(int(remaining), 60)

        timer_col, status_col = st.columns([1, 3])
        with timer_col:
            if remaining <= 60:
                st.markdown(f"**:red[{mins:02d}:{secs:02d}]**")
            elif remaining <= 180:
                st.markdown(f"**:orange[{mins:02d}:{secs:02d}]**")
            else:
                st.markdown(f"**{mins:02d}:{secs:02d}** remaining")
        with status_col:
            session_state = st.session_state.get("session_state", "active")
            if session_state == "ended":
                st.info("Discussion has ended.")

    st.markdown("---")

    # --- Chat history display ---
    messages = st.session_state.get("messages", [])
    participant_name = st.session_state.get("participant_name", "You")

    for msg in messages:
        speaker = msg["speaker"]
        content = msg["content"]

        if speaker == participant_name:
            with st.chat_message("user"):
                st.markdown(content)
        else:
            avatar = SPEAKER_AVATARS.get(speaker, "💬")
            with st.chat_message("assistant", avatar=avatar):
                st.markdown(f"**{speaker}:** {content}")

    # --- Check if session ended ---
    session_state = st.session_state.get("session_state", "active")
    if session_state == "ended":
        st.markdown("---")
        if st.button("Continue to Survey", type="primary"):
            st.session_state.current_step = "survey"
            st.rerun()
        return

    # --- Chat input ---
    user_input = st.chat_input("Type your response...")

    if user_input:
        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(user_input)

        # Add to history
        messages.append({"speaker": participant_name, "content": user_input})
        st.session_state.messages = messages

        # Send to backend and get AI responses
        with st.spinner("Others are responding..."):
            try:
                resp = httpx.post(
                    f"{API_BASE}/session/{sid}/message",
                    json={"content": user_input},
                    timeout=60.0,
                )
                resp.raise_for_status()
                data = resp.json()

                # Display AI turns
                for ai_turn in data["ai_turns"]:
                    speaker = ai_turn["speaker"]
                    content = ai_turn["content"]
                    messages.append({"speaker": speaker, "content": content})

                    avatar = SPEAKER_AVATARS.get(speaker, "💬")
                    with st.chat_message("assistant", avatar=avatar):
                        st.markdown(f"**{speaker}:** {content}")

                st.session_state.messages = messages
                st.session_state.session_state = data["session_state"]

                # If session ended, show continue button on next rerun
                if data["session_state"] == "ended":
                    st.rerun()

            except httpx.HTTPError as e:
                st.error(f"Connection error: {e}")


def _initialize_session(pid: str):
    """Create a new session via the backend."""
    st.info("Starting the discussion...")

    with st.spinner("Setting up the discussion..."):
        try:
            resp = httpx.post(
                f"{API_BASE}/session/create",
                json={"participant_id": pid},
                timeout=60.0,
            )
            resp.raise_for_status()
            data = resp.json()

            st.session_state.session_id = data["session_id"]
            st.session_state.interview_start = time.time()
            st.session_state.messages = [
                {"speaker": m["speaker"], "content": m["content"]}
                for m in data["opening_messages"]
            ]
            st.session_state.session_state = "active"
            st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to start session: {e}. Is the backend running?")
