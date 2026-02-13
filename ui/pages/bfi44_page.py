"""
BFI-44 Page: Full 44-item Big Five Inventory questionnaire.
Redesigned for better UX with cleaner, more intuitive layout.
"""

import streamlit as st
import httpx
import time


API_BASE = "http://localhost:8000"


def get_next_phase_after_bfi44():
    """Determine next phase based on active modes."""
    active_modes = st.session_state.get("active_modes", {"case": False, "group": True})
    if active_modes.get("case", False):
        return "case"
    elif active_modes.get("group", True):
        return "group"
    else:
        return "results"


# Shortened BFI-44 items (removed repetitive prefix)
BFI44_ITEMS = [
    (1, "Talkative", "E"),
    (2, "Tends to find fault with others", "A"),
    (3, "Does a thorough job", "C"),
    (4, "Depressed, blue", "N"),
    (5, "Original, comes up with new ideas", "O"),
    (6, "Reserved", "E"),
    (7, "Helpful and unselfish with others", "A"),
    (8, "Can be somewhat careless", "C"),
    (9, "Relaxed, handles stress well", "N"),
    (10, "Curious about many different things", "O"),
    (11, "Full of energy", "E"),
    (12, "Starts quarrels with others", "A"),
    (13, "A reliable worker", "C"),
    (14, "Can be tense", "N"),
    (15, "Ingenious, a deep thinker", "O"),
    (16, "Generates a lot of enthusiasm", "E"),
    (17, "Has a forgiving nature", "A"),
    (18, "Tends to be disorganized", "C"),
    (19, "Worries a lot", "N"),
    (20, "Has an active imagination", "O"),
    (21, "Tends to be quiet", "E"),
    (22, "Generally trusting", "A"),
    (23, "Tends to be lazy", "C"),
    (24, "Emotionally stable, not easily upset", "N"),
    (25, "Inventive", "O"),
    (26, "Has an assertive personality", "E"),
    (27, "Can be cold and aloof", "A"),
    (28, "Perseveres until the task is finished", "C"),
    (29, "Can be moody", "N"),
    (30, "Values artistic, aesthetic experiences", "O"),
    (31, "Sometimes shy, inhibited", "E"),
    (32, "Considerate and kind to almost everyone", "A"),
    (33, "Does things efficiently", "C"),
    (34, "Remains calm in tense situations", "N"),
    (35, "Prefers work that is routine", "O"),
    (36, "Outgoing, sociable", "E"),
    (37, "Sometimes rude to others", "A"),
    (38, "Makes plans and follows through with them", "C"),
    (39, "Gets nervous easily", "N"),
    (40, "Likes to reflect, play with ideas", "O"),
    (41, "Has few artistic interests", "O"),
    (42, "Likes to cooperate with others", "A"),
    (43, "Easily distracted", "C"),
    (44, "Sophisticated in art, music, or literature", "O"),
]

LIKERT_LABELS = ["1", "2", "3", "4", "5"]
LIKERT_HELP = "1 = Disagree strongly, 5 = Agree strongly"


def show_bfi44_page():
    """Display full BFI-44 questionnaire with improved UX."""

    # Initialize timer if not set
    if "bfi44_start_time" not in st.session_state:
        st.session_state.bfi44_start_time = time.time()

    # Initialize responses if not set
    if "bfi44_responses" not in st.session_state:
        st.session_state.bfi44_responses = {}

    # Header
    st.markdown("## Personality Questionnaire")

    # Disclaimer
    st.warning("**Note:** This questionnaire is for research purposes only. Your responses here will **not** affect your interview assessment results.")

    # Instructions
    st.markdown("**I see myself as someone who is...**")
    st.caption("Rate each trait from 1 (Disagree strongly) to 5 (Agree strongly)")

    st.markdown("---")

    # Custom CSS for cleaner question cards
    st.markdown("""
    <style>
        .question-card {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 12px 16px;
            margin-bottom: 8px;
            border-left: 4px solid #6366f1;
        }
        .question-num {
            font-weight: 600;
            color: #6366f1;
            margin-right: 8px;
        }
        .question-text {
            font-size: 1.05rem;
            color: #1f2937;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.form("bfi44_form"):
        # Display questions in a cleaner format
        for item_num, text, trait in BFI44_ITEMS:
            key = f"bfi_{item_num}"

            # Question with number
            col_q, col_r = st.columns([3, 2])

            with col_q:
                st.markdown(f"**{item_num}.** {text}")

            with col_r:
                # Get current value
                current_val = st.session_state.bfi44_responses.get(item_num)
                default_idx = current_val - 1 if current_val else None

                response = st.radio(
                    f"q{item_num}",
                    options=[1, 2, 3, 4, 5],
                    horizontal=True,
                    key=key,
                    index=default_idx,
                    label_visibility="collapsed"
                )

                if response:
                    st.session_state.bfi44_responses[item_num] = response

            # Subtle divider every 11 questions
            if item_num in [11, 22, 33]:
                st.markdown("---")

        st.markdown("---")

        # Scale reminder
        st.caption("**Scale:** 1 = Disagree strongly | 2 = Disagree a little | 3 = Neutral | 4 = Agree a little | 5 = Agree strongly")

        # Submit button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button(
                "Submit Questionnaire",
                use_container_width=True,
                type="primary"
            )

        if submitted:
            # Validate all questions answered
            missing = []
            responses_dict = {}

            for item_num, text, trait in BFI44_ITEMS:
                key = f"bfi_{item_num}"
                response = st.session_state.get(key)

                if response is None:
                    missing.append(item_num)
                else:
                    responses_dict[item_num] = response

            if missing:
                st.error(f"Please answer all questions. Missing: {missing[:5]}{'...' if len(missing) > 5 else ''}")
                return

            # Calculate duration
            duration = int(time.time() - st.session_state.bfi44_start_time)

            # Submit to API or process locally
            if st.session_state.get("demo_mode"):
                # Demo mode: compute scores locally
                scores = compute_bfi44_scores_local(responses_dict)
                st.session_state.bfi44_scores = scores
                st.session_state.bfi44_completed = True
                st.session_state.bfi44_duration = duration
                st.session_state.current_phase = get_next_phase_after_bfi44()

                st.success("Questionnaire completed!")
                st.rerun()
            else:
                # Call API
                try:
                    with httpx.Client(timeout=30.0) as client:
                        response = client.post(
                            f"{API_BASE}/participant/{st.session_state.participant_id}/bfi44",
                            json={
                                "responses": {str(k): v for k, v in responses_dict.items()},
                                "duration_seconds": duration,
                            }
                        )
                        response.raise_for_status()

                        st.session_state.bfi44_completed = True
                        st.session_state.bfi44_duration = duration
                        st.session_state.current_phase = get_next_phase_after_bfi44()

                        st.success("Questionnaire completed!")
                        st.rerun()

                except httpx.HTTPError as e:
                    st.error(f"Submission failed: {str(e)}")
                except Exception as e:
                    st.error(f"Unexpected error: {str(e)}")


def compute_bfi44_scores_local(responses: dict[int, int]) -> dict:
    """Compute BFI-44 scores locally for demo mode."""
    # Reverse-scored items
    reverse_items = {2, 6, 8, 9, 12, 18, 21, 23, 24, 27, 31, 34, 35, 37, 41, 43}

    trait_sums = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}
    trait_counts = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}

    trait_map = {
        1: "E", 2: "A", 3: "C", 4: "N", 5: "O",
        6: "E", 7: "A", 8: "C", 9: "N", 10: "O",
        11: "E", 12: "A", 13: "C", 14: "N", 15: "O",
        16: "E", 17: "A", 18: "C", 19: "N", 20: "O",
        21: "E", 22: "A", 23: "C", 24: "N", 25: "O",
        26: "E", 27: "A", 28: "C", 29: "N", 30: "O",
        31: "E", 32: "A", 33: "C", 34: "N", 35: "O",
        36: "E", 37: "A", 38: "C", 39: "N", 40: "O",
        41: "O", 42: "A", 43: "C", 44: "O",
    }

    for item_num, score in responses.items():
        trait = trait_map[item_num]
        if item_num in reverse_items:
            score = 6 - score
        trait_sums[trait] += score
        trait_counts[trait] += 1

    scores = {}
    for trait in ["O", "C", "E", "A", "N"]:
        avg = trait_sums[trait] / trait_counts[trait]
        scores[trait] = round((avg - 1) / 4, 3)  # Normalize to 0-1

    return scores
