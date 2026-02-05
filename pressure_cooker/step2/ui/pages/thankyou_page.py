"""
Page 5: Thank You / Debrief
"""

import streamlit as st


def render():
    st.header("Thank You!")

    st.markdown("""
    ### Your participation is complete.

    Thank you for taking part in this study on analytical discussion
    and personality expression.

    ### What was this about?

    This study investigates how personality traits are expressed during
    group discussions. During the discussion, you interacted with AI-powered
    colleagues in a consulting-style case study scenario. The AI characters
    ("Jordan" and "Sam") were designed to create a natural group dynamic
    with different analytical perspectives.

    Your conversation will be analyzed (anonymously) to understand how
    personality is expressed in analytical discussion and problem-solving.
    The BFI-44 questionnaire you completed provides a baseline measure of
    your personality traits, which we compare against what observers can
    infer from the conversation alone.

    ### Key points:

    - Your data is identified only by your participant ID
    - Individual results will not be shared publicly
    - Only aggregated findings will be reported

    ### Questions?

    If you have any questions about this study, please contact the
    research team.
    """)

    st.markdown("---")

    pid = st.session_state.get("participant_id", "N/A")
    st.info(f"Your participant ID for reference: **{pid}**")

    st.balloons()
