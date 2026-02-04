"""
Page 2: BFI-44 Questionnaire

44 items in st.form() with Likert radio buttons (1-5).
Single submit to avoid 44 reruns.
"""

import time

import httpx
import streamlit as st


API_BASE = "http://localhost:8000"

# All 44 items in order. (Matches step2/bfi44.py)
BFI44_ITEMS = [
    (1,  "Is talkative"),
    (2,  "Tends to find fault with others"),
    (3,  "Does a thorough job"),
    (4,  "Is depressed, blue"),
    (5,  "Is original, comes up with new ideas"),
    (6,  "Is reserved"),
    (7,  "Is helpful and unselfish with others"),
    (8,  "Can be somewhat careless"),
    (9,  "Is relaxed, handles stress well"),
    (10, "Is curious about many different things"),
    (11, "Is full of energy"),
    (12, "Starts quarrels with others"),
    (13, "Is a reliable worker"),
    (14, "Can be tense"),
    (15, "Is ingenious, a deep thinker"),
    (16, "Generates a lot of enthusiasm"),
    (17, "Has a forgiving nature"),
    (18, "Tends to be disorganized"),
    (19, "Worries a lot"),
    (20, "Has an active imagination"),
    (21, "Tends to be quiet"),
    (22, "Is generally trusting"),
    (23, "Tends to be lazy"),
    (24, "Is emotionally stable, not easily upset"),
    (25, "Is inventive"),
    (26, "Has an assertive personality"),
    (27, "Can be cold and aloof"),
    (28, "Perseveres until the task is finished"),
    (29, "Can be moody"),
    (30, "Values artistic, aesthetic experiences"),
    (31, "Is sometimes shy, inhibited"),
    (32, "Is considerate and kind to almost everyone"),
    (33, "Does things efficiently"),
    (34, "Remains calm in tense situations"),
    (35, "Prefers work that is routine"),
    (36, "Is outgoing, sociable"),
    (37, "Is sometimes rude to others"),
    (38, "Makes plans and follows through with them"),
    (39, "Gets nervous easily"),
    (40, "Likes to reflect, play with ideas"),
    (41, "Has few artistic interests"),
    (42, "Likes to cooperate with others"),
    (43, "Is easily distracted"),
    (44, "Is sophisticated in art, music, or literature"),
]

LIKERT_OPTIONS = {
    1: "Disagree strongly",
    2: "Disagree a little",
    3: "Neither agree nor disagree",
    4: "Agree a little",
    5: "Agree strongly",
}


def render():
    pid = st.session_state.get("participant_id")
    if not pid:
        st.warning("Please complete the consent form first.")
        st.session_state.current_step = "consent"
        st.rerun()
        return

    st.header("Personality Questionnaire")
    st.markdown(
        "Please indicate how much you agree or disagree with each statement. "
        "**\"I see myself as someone who...\"**"
    )
    st.markdown("---")

    # Track start time
    if "bfi44_start_time" not in st.session_state:
        st.session_state.bfi44_start_time = time.time()

    with st.form("bfi44_form"):
        responses = {}

        for idx, (item_num, item_text) in enumerate(BFI44_ITEMS):
            col1, col2 = st.columns([3, 5])
            with col1:
                st.markdown(f"**{item_num}.** ...{item_text}")
            with col2:
                val = st.radio(
                    f"Item {item_num}",
                    options=[1, 2, 3, 4, 5],
                    format_func=lambda x: LIKERT_OPTIONS[x],
                    horizontal=True,
                    key=f"bfi44_item_{item_num}",
                    label_visibility="collapsed",
                )
                responses[item_num] = val

            # Add visual separator every 11 items
            if (idx + 1) % 11 == 0 and idx < len(BFI44_ITEMS) - 1:
                st.markdown("---")

        st.markdown("---")
        submitted = st.form_submit_button("Submit Questionnaire", type="primary")

    if submitted:
        duration = time.time() - st.session_state.bfi44_start_time

        with st.spinner("Scoring your responses..."):
            try:
                resp = httpx.post(
                    f"{API_BASE}/participant/{pid}/bfi44",
                    json={
                        "responses": {str(k): v for k, v in responses.items()},
                        "duration_seconds": duration,
                    },
                    timeout=10.0,
                )
                resp.raise_for_status()

                st.session_state.current_step = "interview"
                st.rerun()

            except httpx.HTTPError as e:
                st.error(f"Error submitting questionnaire: {e}")
