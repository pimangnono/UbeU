"""
V3 Main Application: Streamlit multi-page app for dual-mode interviews.

Run with: streamlit run ui/app.py
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="UbeU V3 - AI Interview Platform",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A5F;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-top: 0;
    }
    .mode-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .mode-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1E3A5F;
    }
    .trait-badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 15px;
        font-size: 0.85rem;
        margin: 2px;
    }
    .trait-O { background-color: #E8F5E9; color: #2E7D32; }
    .trait-C { background-color: #E3F2FD; color: #1565C0; }
    .trait-E { background-color: #FFF3E0; color: #E65100; }
    .trait-A { background-color: #FCE4EC; color: #C2185B; }
    .trait-N { background-color: #F3E5F5; color: #7B1FA2; }
</style>
""", unsafe_allow_html=True)


def main():
    """Main application entry point."""

    # Initialize session state
    if "participant_id" not in st.session_state:
        st.session_state.participant_id = None
    if "participant_name" not in st.session_state:
        st.session_state.participant_name = ""
    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = None
    if "session_active" not in st.session_state:
        st.session_state.session_active = False
    if "bfi44_completed" not in st.session_state:
        st.session_state.bfi44_completed = False

    # Sidebar navigation
    with st.sidebar:
        st.markdown("### Navigation")

        if st.session_state.participant_id:
            st.success(f"Participant: {st.session_state.participant_name}")

            if st.session_state.bfi44_completed:
                st.info("BFI-44: Completed")
            else:
                st.warning("BFI-44: Not completed")

            if st.session_state.selected_mode:
                mode_name = "Case Study" if st.session_state.selected_mode == "case" else "Group Discussion"
                st.info(f"Mode: {mode_name}")

        st.markdown("---")
        st.markdown("### About V3")
        st.markdown("""
        **Dual-Mode Assessment:**
        - **Mode 1**: Case Study (Logic)
        - **Mode 2**: Group Discussion (Personality)

        Each mode produces evidence-based reports with direct quotes from your responses.
        """)

    # Main content area
    st.markdown('<p class="main-header">UbeU V3</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Dual-Mode AI Interview Platform</p>', unsafe_allow_html=True)
    st.markdown("---")

    # Page routing based on state
    if not st.session_state.participant_id:
        show_registration_page()
    elif not st.session_state.bfi44_completed:
        show_bfi44_page()
    elif not st.session_state.selected_mode:
        show_mode_selection_page()
    elif st.session_state.session_active:
        if st.session_state.selected_mode == "case":
            show_case_interview_page()
        else:
            show_group_discussion_page()
    else:
        show_results_page()


def show_registration_page():
    """Registration and consent page."""
    st.header("Welcome")

    with st.form("registration_form"):
        st.markdown("### Participant Registration")

        name = st.text_input("Your Name", placeholder="Enter your full name")

        st.markdown("### Informed Consent")
        st.markdown("""
        By participating in this study, you agree that:
        - Your responses will be recorded and analyzed
        - Your personality profile will be assessed using AI
        - All data will be anonymized for research purposes
        - You can withdraw at any time

        This study is part of an NUS Final Year Thesis project.
        """)

        consent = st.checkbox("I have read and agree to the above terms")

        submitted = st.form_submit_button("Continue", use_container_width=True)

        if submitted:
            if not name:
                st.error("Please enter your name.")
            elif not consent:
                st.error("Please agree to the consent terms.")
            else:
                import uuid
                st.session_state.participant_id = f"P{str(uuid.uuid4())[:6].upper()}"
                st.session_state.participant_name = name
                st.rerun()


def show_bfi44_page():
    """BFI-44 personality questionnaire page."""
    st.header("Personality Questionnaire (BFI-44)")

    st.markdown("""
    Please rate how much you agree with each statement about yourself.
    Answer honestly - there are no right or wrong answers.
    """)

    # For demo, show abbreviated version
    st.info("This is a demo version with selected questions. Full version has 44 items.")

    with st.form("bfi44_form"):
        # Sample questions (in production, all 44)
        sample_questions = [
            ("I see myself as someone who is talkative", "E"),
            ("I see myself as someone who is reserved", "E_r"),
            ("I see myself as someone who is original, comes up with new ideas", "O"),
            ("I see myself as someone who is helpful and unselfish with others", "A"),
            ("I see myself as someone who does a thorough job", "C"),
            ("I see myself as someone who is relaxed, handles stress well", "N_r"),
        ]

        responses = {}
        for i, (question, trait) in enumerate(sample_questions):
            responses[i] = st.radio(
                question,
                options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                horizontal=True,
                key=f"bfi_{i}",
            )

        submitted = st.form_submit_button("Submit Questionnaire", use_container_width=True)

        if submitted:
            st.session_state.bfi44_completed = True
            st.session_state.bfi44_responses = responses
            st.success("Questionnaire submitted!")
            st.rerun()


def show_mode_selection_page():
    """Mode selection page - choose between Case Study or Group Discussion."""
    st.header("Select Interview Mode")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="mode-card">
            <p class="mode-title">Mode 1: Case Study</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        **Format:** 1-on-1 with AI Facilitator

        **Duration:** ~15 minutes

        **What's Assessed:**
        - Problem Structuring
        - Hypothesis-Driven Thinking
        - Quantitative Reasoning
        - Data Synthesis
        - Recommendation Quality
        - Communication Clarity

        **Style:** Management consulting case interview.
        You'll analyze a business problem and develop recommendations.
        """)

        if st.button("Start Case Study", key="start_case", use_container_width=True):
            st.session_state.selected_mode = "case"
            st.session_state.session_active = True
            st.rerun()

    with col2:
        st.markdown("""
        <div class="mode-card">
            <p class="mode-title">Mode 2: Group Discussion</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        **Format:** 1-to-3 with AI Team Members

        **Duration:** ~15 minutes

        **What's Assessed:**
        - Openness (creativity, curiosity)
        - Conscientiousness (organization)
        - Extraversion (engagement)
        - Agreeableness (collaboration)
        - Neuroticism (stress response)

        **Style:** Leaderless group discussion.
        You'll discuss a workplace scenario with AI colleagues.
        """)

        if st.button("Start Group Discussion", key="start_group", use_container_width=True):
            st.session_state.selected_mode = "group"
            st.session_state.session_active = True
            st.rerun()


def show_case_interview_page():
    """Case study interview interface (Mode 1)."""
    st.header("Case Study Interview")

    # Demo interface
    st.info("This is a demo interface. In production, this connects to the CaseEngine.")

    # Timer
    col1, col2 = st.columns([3, 1])
    with col2:
        st.metric("Time Remaining", "14:32")

    # Chat interface
    st.markdown("### Conversation")

    # Demo messages
    if "case_messages" not in st.session_state:
        st.session_state.case_messages = [
            {"role": "facilitator", "content": "TechFlow Solutions is an enterprise SaaS company. Their profit margins have declined 15% over the past two years despite revenue growth of 25%. The CEO wants to understand why profitability is declining and what actions to take."},
        ]

    for msg in st.session_state.case_messages:
        if msg["role"] == "facilitator":
            with st.chat_message("assistant", avatar="📋"):
                st.write(msg["content"])
        else:
            with st.chat_message("user", avatar="👤"):
                st.write(msg["content"])

    # Input
    user_input = st.chat_input("Your response...")

    if user_input:
        st.session_state.case_messages.append({"role": "user", "content": user_input})

        # Demo: Add facilitator response
        demo_response = "I have data on revenue breakdown, cost structure, customer metrics, and market data. What specific information would you like?"
        st.session_state.case_messages.append({"role": "facilitator", "content": demo_response})
        st.rerun()

    # End session button
    if st.button("End Interview", type="secondary"):
        st.session_state.session_active = False
        st.rerun()


def show_group_discussion_page():
    """Group discussion interface (Mode 2)."""
    st.header("Group Discussion")

    # Demo interface
    st.info("This is a demo interface. In production, this connects to the GroupEngine.")

    # Participant avatars
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**Alex** (Challenger)")
    with col2:
        st.markdown("**Jordan** (Supporter)")
    with col3:
        st.markdown("**Riley** (Skeptic)")
    with col4:
        st.markdown(f"**{st.session_state.participant_name}** (You)")

    # Timer
    st.metric("Time Remaining", "14:15")

    # Chat interface
    st.markdown("### Discussion")

    if "group_messages" not in st.session_state:
        st.session_state.group_messages = [
            {"role": "jordan", "content": "Welcome everyone! We need to decide how to allocate resources for this 3-week project. We can only build 2 out of 4 features. What do you all think we should prioritize?"},
        ]

    for msg in st.session_state.group_messages:
        avatar_map = {"jordan": "🤝", "alex": "💪", "riley": "🤔", "user": "👤"}
        name_map = {"jordan": "Jordan", "alex": "Alex", "riley": "Riley", "user": st.session_state.participant_name}

        avatar = avatar_map.get(msg["role"], "👤")
        name = name_map.get(msg["role"], msg["role"])

        if msg["role"] == "user":
            with st.chat_message("user", avatar=avatar):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant", avatar=avatar):
                st.markdown(f"**{name}:** {msg['content']}")

    # Input
    user_input = st.chat_input("Your response...")

    if user_input:
        st.session_state.group_messages.append({"role": "user", "content": user_input})

        # Demo: Add AI responses
        demo_responses = [
            {"role": "alex", "content": "I'm not sure I agree with that approach. We need to focus on the features that will have the biggest impact, not just the easiest ones to build."},
        ]
        st.session_state.group_messages.extend(demo_responses)
        st.rerun()

    # End session button
    if st.button("End Discussion", type="secondary"):
        st.session_state.session_active = False
        st.rerun()


def show_results_page():
    """Results dashboard page."""
    st.header("Assessment Results")

    mode_name = "Case Study" if st.session_state.selected_mode == "case" else "Group Discussion"
    st.subheader(f"Mode: {mode_name}")

    if st.session_state.selected_mode == "case":
        # Logic assessment results
        st.markdown("### Logical Assessment Scores")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Problem Structuring", "4/5", help="Strong framework usage")
            st.metric("Hypothesis Thinking", "4/5", help="Good hypothesis formation")
            st.metric("Quantitative Reasoning", "3/5", help="Some calculation errors")

        with col2:
            st.metric("Data Synthesis", "4/5", help="Good connections made")
            st.metric("Recommendation Quality", "3/5", help="Could be more specific")
            st.metric("Communication Clarity", "5/5", help="Excellent clarity")

        st.markdown("### Evidence Highlights")
        with st.expander("Problem Structuring Evidence"):
            st.markdown("""
            **Turn 3:** "Let me structure this as a profitability problem — I want to look at revenue drivers and cost drivers separately."
            > *Demonstrates: Explicit framework articulation*
            """)

    else:
        # Personality assessment results
        st.markdown("### Personality Profile")

        # Radar chart placeholder
        st.markdown("*(Radar chart would go here)*")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Openness", "0.72", help="Engaged with creative ideas")
            st.metric("Conscientiousness", "0.58", help="Moderate organization")
            st.metric("Extraversion", "0.75", help="Active participation")

        with col2:
            st.metric("Agreeableness", "0.82", help="Collaborative approach")
            st.metric("Neuroticism", "0.28", help="Calm under pressure")

        st.markdown("### Behavioral Summary")
        st.info("Collaborative communicator with strong engagement. Maintained composure during disagreements and actively included all team members.")

    # Actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Do Other Mode"):
            other_mode = "group" if st.session_state.selected_mode == "case" else "case"
            st.session_state.selected_mode = other_mode
            st.session_state.session_active = True
            st.rerun()
    with col2:
        st.button("Download Report")
    with col3:
        if st.button("Exit"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


if __name__ == "__main__":
    main()
