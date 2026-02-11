"""
Streamlit entry point for Step 2 Live Interview Platform.

Multi-page app with:
  1. Consent
  2. BFI-44 Questionnaire
  3. Live Interview
  4. Post-Session Survey
  5. Thank You / Debrief

Run from pressure_cooker/:
    streamlit run step2/ui/app.py
"""

import sys
from pathlib import Path

# Ensure pressure_cooker/ is on sys.path for all imports
_root = str(Path(__file__).parent.parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

import streamlit as st

st.set_page_config(
    page_title="Workplace Discussion Study",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide auto-generated page navigation from sidebar
st.markdown(
    "<style>[data-testid='stSidebarNav'] {display:none !important;}</style>",
    unsafe_allow_html=True,
)

# Initialize session state defaults
if "participant_id" not in st.session_state:
    st.session_state.participant_id = None
if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "current_step" not in st.session_state:
    st.session_state.current_step = "consent"
if "api_base" not in st.session_state:
    st.session_state.api_base = "http://localhost:8000"

# Navigation
STEPS = {
    "consent": "1_consent",
    "bfi44": "2_bfi44",
    "interview": "3_interview",
    "survey": "4_survey",
    "thankyou": "5_thankyou",
}


def main():
    # Sidebar with minimal info
    with st.sidebar:
        # Admin toggle at top
        st.markdown("---")
        admin_mode = st.toggle("🔐 Admin Mode", key="admin_toggle")
        if admin_mode and st.session_state.current_step != "admin":
            st.session_state.current_step = "admin"
            st.rerun()
        elif not admin_mode and st.session_state.current_step == "admin":
            st.session_state.current_step = "consent"
            st.rerun()
        st.markdown("---")

        if st.session_state.current_step != "admin":
            st.markdown("### Study Progress")
            steps_display = ["Consent", "Questionnaire", "Interview", "Survey", "Complete"]
            step_map = {"consent": 0, "bfi44": 1, "interview": 2, "survey": 3, "thankyou": 4}
            current_idx = step_map.get(st.session_state.current_step, 0)

            for i, step_name in enumerate(steps_display):
                if i < current_idx:
                    st.markdown(f"~~{step_name}~~")
                elif i == current_idx:
                    st.markdown(f"**> {step_name}**")
                else:
                    st.markdown(f"  {step_name}")

            if st.session_state.participant_id:
                st.divider()
                st.caption(f"ID: {st.session_state.participant_id}")

    # Title (hidden on interview and admin pages for compact layout)
    if st.session_state.current_step not in ("interview", "admin"):
        st.title("Workplace Discussion Study")
        st.markdown("---")

    # Route to current step
    step = st.session_state.current_step

    if step == "admin":
        from step2.ui.pages import admin_page
        admin_page.render()
    elif step == "consent":
        from step2.ui.pages import consent_page
        consent_page.render()
    elif step == "bfi44":
        from step2.ui.pages import bfi44_page
        bfi44_page.render()
    elif step == "interview":
        from step2.ui.pages import interview_page
        interview_page.render()
    elif step == "survey":
        from step2.ui.pages import survey_page
        survey_page.render()
    elif step == "thankyou":
        from step2.ui.pages import thankyou_page
        thankyou_page.render()


if __name__ == "__main__":
    main()
