"""
BFI-44 Page: Full 44-item Big Five Inventory questionnaire.
"""

import streamlit as st
import httpx
import time


API_BASE = "http://localhost:8000"

# Full BFI-44 items
BFI44_ITEMS = [
    (1, "I see myself as someone who is talkative", "E"),
    (2, "I see myself as someone who tends to find fault with others", "A"),
    (3, "I see myself as someone who does a thorough job", "C"),
    (4, "I see myself as someone who is depressed, blue", "N"),
    (5, "I see myself as someone who is original, comes up with new ideas", "O"),
    (6, "I see myself as someone who is reserved", "E"),
    (7, "I see myself as someone who is helpful and unselfish with others", "A"),
    (8, "I see myself as someone who can be somewhat careless", "C"),
    (9, "I see myself as someone who is relaxed, handles stress well", "N"),
    (10, "I see myself as someone who is curious about many different things", "O"),
    (11, "I see myself as someone who is full of energy", "E"),
    (12, "I see myself as someone who starts quarrels with others", "A"),
    (13, "I see myself as someone who is a reliable worker", "C"),
    (14, "I see myself as someone who can be tense", "N"),
    (15, "I see myself as someone who is ingenious, a deep thinker", "O"),
    (16, "I see myself as someone who generates a lot of enthusiasm", "E"),
    (17, "I see myself as someone who has a forgiving nature", "A"),
    (18, "I see myself as someone who tends to be disorganized", "C"),
    (19, "I see myself as someone who worries a lot", "N"),
    (20, "I see myself as someone who has an active imagination", "O"),
    (21, "I see myself as someone who tends to be quiet", "E"),
    (22, "I see myself as someone who is generally trusting", "A"),
    (23, "I see myself as someone who tends to be lazy", "C"),
    (24, "I see myself as someone who is emotionally stable, not easily upset", "N"),
    (25, "I see myself as someone who is inventive", "O"),
    (26, "I see myself as someone who has an assertive personality", "E"),
    (27, "I see myself as someone who can be cold and aloof", "A"),
    (28, "I see myself as someone who perseveres until the task is finished", "C"),
    (29, "I see myself as someone who can be moody", "N"),
    (30, "I see myself as someone who values artistic, aesthetic experiences", "O"),
    (31, "I see myself as someone who is sometimes shy, inhibited", "E"),
    (32, "I see myself as someone who is considerate and kind to almost everyone", "A"),
    (33, "I see myself as someone who does things efficiently", "C"),
    (34, "I see myself as someone who remains calm in tense situations", "N"),
    (35, "I see myself as someone who prefers work that is routine", "O"),
    (36, "I see myself as someone who is outgoing, sociable", "E"),
    (37, "I see myself as someone who is sometimes rude to others", "A"),
    (38, "I see myself as someone who makes plans and follows through with them", "C"),
    (39, "I see myself as someone who gets nervous easily", "N"),
    (40, "I see myself as someone who likes to reflect, play with ideas", "O"),
    (41, "I see myself as someone who has few artistic interests", "O"),
    (42, "I see myself as someone who likes to cooperate with others", "A"),
    (43, "I see myself as someone who is easily distracted", "C"),
    (44, "I see myself as someone who is sophisticated in art, music, or literature", "O"),
]

LIKERT_OPTIONS = [
    "Disagree strongly",
    "Disagree a little",
    "Neither agree nor disagree",
    "Agree a little",
    "Agree strongly",
]

# Trait colors for visualization
TRAIT_COLORS = {
    "O": "#8B5CF6",  # Purple - Openness
    "C": "#3B82F6",  # Blue - Conscientiousness
    "E": "#F97316",  # Orange - Extraversion
    "A": "#EC4899",  # Pink - Agreeableness
    "N": "#6366F1",  # Indigo - Neuroticism
}

TRAIT_NAMES = {
    "O": "Openness",
    "C": "Conscientiousness",
    "E": "Extraversion",
    "A": "Agreeableness",
    "N": "Neuroticism",
}


def show_bfi44_page():
    """Display full BFI-44 questionnaire."""
    st.header("Personality Questionnaire (BFI-44)")

    # Initialize timer if not set
    if "bfi44_start_time" not in st.session_state:
        st.session_state.bfi44_start_time = time.time()

    # Initialize responses if not set
    if "bfi44_responses" not in st.session_state:
        st.session_state.bfi44_responses = {}

    # Progress tracking
    answered = len([k for k, v in st.session_state.bfi44_responses.items() if v is not None])
    progress = answered / 44

    col1, col2 = st.columns([3, 1])
    with col1:
        st.progress(progress, text=f"Progress: {answered}/44 questions answered")
    with col2:
        elapsed = int(time.time() - st.session_state.bfi44_start_time)
        st.metric("Time Elapsed", f"{elapsed // 60}:{elapsed % 60:02d}")

    st.markdown("""
    **Instructions:** Please rate how much you agree with each statement about yourself.
    There are no right or wrong answers. Answer honestly based on how you generally see yourself.
    """)

    st.markdown("---")

    # Display questions in sections
    sections = [
        ("Questions 1-11", BFI44_ITEMS[0:11]),
        ("Questions 12-22", BFI44_ITEMS[11:22]),
        ("Questions 23-33", BFI44_ITEMS[22:33]),
        ("Questions 34-44", BFI44_ITEMS[33:44]),
    ]

    with st.form("bfi44_form"):
        for section_name, items in sections:
            st.subheader(section_name)

            for item_num, text, trait in items:
                # Create unique key
                key = f"bfi_{item_num}"

                # Get current value from session state
                current_val = st.session_state.bfi44_responses.get(item_num, None)
                default_idx = LIKERT_OPTIONS.index(current_val) if current_val in LIKERT_OPTIONS else None

                response = st.radio(
                    f"**{item_num}.** {text}",
                    options=LIKERT_OPTIONS,
                    horizontal=True,
                    key=key,
                    index=default_idx,
                )

                if response:
                    st.session_state.bfi44_responses[item_num] = response

            st.markdown("---")

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
                    # Convert Likert to 1-5 score
                    score = LIKERT_OPTIONS.index(response) + 1
                    responses_dict[item_num] = score

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
                st.session_state.current_phase = st.session_state.get("first_mode", "case")

                # Show results briefly
                st.success("Questionnaire completed!")
                display_bfi44_results(scores)
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
                        data = response.json()

                        st.session_state.bfi44_completed = True
                        st.session_state.bfi44_duration = duration
                        st.session_state.current_phase = data.get("next_phase", "case")

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


def display_bfi44_results(scores: dict):
    """Display BFI-44 results briefly."""
    st.markdown("### Your Personality Profile (Ground Truth)")

    cols = st.columns(5)
    for i, (trait, score) in enumerate(scores.items()):
        with cols[i]:
            st.metric(
                TRAIT_NAMES[trait],
                f"{score:.2f}",
            )
