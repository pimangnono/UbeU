"""
V3 Main Application: Streamlit multi-page app for dual-mode interviews.

Run with: streamlit run ui/app.py
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import page modules
from ui.pages.consent_page import show_consent_page
from ui.pages.bfi44_page import show_bfi44_page
from ui.pages.case_interview_page import show_case_interview_page
from ui.pages.group_discussion_page import show_group_discussion_page
from ui.pages.results_page import show_results_page
from ui.pages.survey_page import show_survey_page, show_completion_page
from ui.pages.admin_dashboard import show_admin_dashboard


# Page configuration
st.set_page_config(
    page_title="UbeU V3 - AI Interview Platform",
    page_icon=":material/psychology:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Custom CSS
def apply_custom_css():
    st.markdown("""
    <style>
        /* Main header styling */
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

        /* Mode cards */
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

        /* Trait badges */
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

        /* Chat styling */
        .stChatMessage {
            padding: 10px 15px;
        }

        /* Progress indicators */
        .phase-indicator {
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 500;
        }
        .phase-active {
            background-color: #E8F5E9;
            color: #2E7D32;
        }
        .phase-pending {
            background-color: #F5F5F5;
            color: #666;
        }
        .phase-complete {
            background-color: #E3F2FD;
            color: #1565C0;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #F8FAFC;
        }

        /* Evidence quotes */
        .evidence-quote {
            padding: 12px;
            background-color: #F8F9FA;
            border-left: 3px solid #6366F1;
            border-radius: 4px;
            margin: 8px 0;
            font-style: italic;
        }
    </style>
    """, unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables."""
    defaults = {
        "participant_id": None,
        "participant_name": "",
        "participant_email": None,
        "consent_given": False,
        "bfi44_completed": False,
        "bfi44_scores": None,
        "case_completed": False,
        "case_assessment": None,
        "group_completed": False,
        "group_assessment": None,
        "survey_completed": False,
        "current_phase": "consent",  # consent, bfi44, case, group, results, survey, complete
        "first_mode": None,  # case or group (counterbalanced)
        "condition": None,  # case_first or group_first
        "demo_mode": False,
    }

    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


def render_sidebar():
    """Render the sidebar with navigation and status."""
    with st.sidebar:
        st.markdown("### UbeU V3")
        st.caption("Dual-Mode AI Interview Platform")

        st.markdown("---")

        # Admin mode toggle
        if st.session_state.get("admin_mode"):
            st.success("Admin Mode Active")
            if st.button("Exit Admin Mode"):
                st.session_state.admin_mode = False
                st.session_state.admin_authenticated = False
                st.rerun()
        else:
            if st.button("Admin Dashboard"):
                st.session_state.admin_mode = True
                st.rerun()

        if st.session_state.get("admin_mode"):
            return

        st.markdown("---")

        # Participant info
        if st.session_state.participant_id:
            st.markdown("**Participant**")
            st.info(f"{st.session_state.participant_name}")
            st.caption(f"ID: {st.session_state.participant_id}")

            st.markdown("---")

            # Progress tracker
            st.markdown("**Progress**")
            render_progress_tracker()

            st.markdown("---")

            # Demo mode indicator
            if st.session_state.get("demo_mode"):
                st.warning("Demo Mode Active")

        else:
            st.markdown("### About")
            st.markdown("""
            **Dual-Mode Assessment:**

            **Mode 1:** Case Study Interview
            - 1-on-1 with AI facilitator
            - Tests logical reasoning

            **Mode 2:** Group Discussion
            - 1-to-3 with AI team members
            - Assesses personality traits

            Each mode generates evidence-based reports.
            """)


def render_progress_tracker():
    """Render the study progress tracker."""
    phases = [
        ("consent", "Consent", st.session_state.consent_given),
        ("bfi44", "BFI-44", st.session_state.bfi44_completed),
    ]

    # Add interview modes in correct order
    if st.session_state.get("first_mode") == "case":
        phases.extend([
            ("case", "Case Study", st.session_state.case_completed),
            ("group", "Group Discussion", st.session_state.group_completed),
        ])
    else:
        phases.extend([
            ("group", "Group Discussion", st.session_state.group_completed),
            ("case", "Case Study", st.session_state.case_completed),
        ])

    phases.extend([
        ("survey", "Survey", st.session_state.survey_completed),
    ])

    current = st.session_state.current_phase

    for phase_id, phase_name, completed in phases:
        if completed:
            icon = ":material/check_circle:"
            color = "#22C55E"
        elif phase_id == current:
            icon = ":material/radio_button_checked:"
            color = "#3B82F6"
        else:
            icon = ":material/radio_button_unchecked:"
            color = "#9CA3AF"

        st.markdown(f"<span style='color: {color};'>{icon} {phase_name}</span>", unsafe_allow_html=True)


def route_to_page():
    """Route to the appropriate page based on current phase."""
    # Admin mode takes precedence
    if st.session_state.get("admin_mode"):
        show_admin_dashboard()
        return

    phase = st.session_state.get("current_phase", "consent")

    if phase == "consent" or not st.session_state.participant_id:
        show_consent_page()

    elif phase == "bfi44":
        show_bfi44_page()

    elif phase == "case":
        show_case_interview_page()

    elif phase == "group":
        show_group_discussion_page()

    elif phase == "results":
        show_results_page()

    elif phase == "survey":
        show_survey_page()

    elif phase == "complete":
        show_completion_page()

    else:
        # Fallback
        st.error(f"Unknown phase: {phase}")
        if st.button("Reset"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


def main():
    """Main application entry point."""
    # Apply custom CSS
    apply_custom_css()

    # Initialize session state
    init_session_state()

    # Render sidebar
    render_sidebar()

    # Route to appropriate page
    route_to_page()


if __name__ == "__main__":
    main()
