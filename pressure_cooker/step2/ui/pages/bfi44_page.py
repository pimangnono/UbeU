"""
Page 2: BFI-44 Questionnaire

44 items with horizontal dot scale (1-5).
Uses clickable dots in a row per item via st.columns + st.button.
Labels: "Strongly Disagree" on left, "Strongly Agree" on right.
Selected dot highlighted with CSS (filled circle vs hollow).
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

# CSS for the horizontal dot scale
DOT_SCALE_CSS = """
<style>
.dot-scale-container {
    display: flex;
    align-items: center;
    gap: 0;
    padding: 4px 0;
}
.dot-scale-labels {
    display: flex;
    justify-content: space-between;
    width: 100%;
    font-size: 0.75rem;
    color: #888;
    margin-top: 2px;
}
.dot-btn {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    border: 2px solid #666;
    background: transparent;
    cursor: pointer;
    margin: 0 6px;
    padding: 0;
    transition: all 0.15s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
.dot-btn:hover {
    border-color: #4A90D9;
    background: rgba(74, 144, 217, 0.1);
}
.dot-btn.selected {
    background: #4A90D9;
    border-color: #4A90D9;
}
.bfi-item-row {
    display: flex;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid #f0f0f0;
}
.bfi-item-text {
    flex: 0 0 45%;
    font-size: 0.95rem;
}
.bfi-item-scale {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
"""


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

    # Inject dot scale CSS
    st.markdown(DOT_SCALE_CSS, unsafe_allow_html=True)

    st.markdown("---")

    # Track start time
    if "bfi44_start_time" not in st.session_state:
        st.session_state.bfi44_start_time = time.time()

    # Initialize responses in session state if needed
    if "bfi44_responses" not in st.session_state:
        st.session_state.bfi44_responses = {num: 3 for num, _ in BFI44_ITEMS}

    # Scale labels header
    label_cols = st.columns([4, 1, 1, 1, 1, 1])
    with label_cols[0]:
        st.markdown("")
    with label_cols[1]:
        st.caption("Strongly Disagree")
    with label_cols[3]:
        st.caption("Neutral")
    with label_cols[5]:
        st.caption("Strongly Agree")

    st.markdown("---")

    for idx, (item_num, item_text) in enumerate(BFI44_ITEMS):
        cols = st.columns([4, 1, 1, 1, 1, 1])

        with cols[0]:
            st.markdown(f"**{item_num}.** ...{item_text}")

        current_val = st.session_state.bfi44_responses.get(item_num, 3)

        for dot_idx, value in enumerate([1, 2, 3, 4, 5]):
            with cols[dot_idx + 1]:
                # Use filled/hollow circle based on selection
                is_selected = current_val == value
                label = "\u25CF" if is_selected else "\u25CB"  # Filled vs hollow circle
                if st.button(
                    label,
                    key=f"dot_{item_num}_{value}",
                    help=f"{value}",
                    use_container_width=True,
                ):
                    st.session_state.bfi44_responses[item_num] = value
                    st.rerun()

        # Add visual separator every 11 items
        if (idx + 1) % 11 == 0 and idx < len(BFI44_ITEMS) - 1:
            st.markdown("---")

    st.markdown("---")

    # Check all items answered (they default to 3, so always answered)
    if st.button("Submit Questionnaire", type="primary"):
        duration = time.time() - st.session_state.bfi44_start_time
        responses = st.session_state.bfi44_responses

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
