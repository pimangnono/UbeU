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
from ui.schema_config import SCENARIO_TEMPLATES, CCS_HIERARCHY


# Page configuration
st.set_page_config(
    page_title="UbeU V3 - AI Interview Platform",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide auto-generated page navigation from sidebar
st.markdown(
    "<style>[data-testid='stSidebarNav'] {display:none !important;}</style>",
    unsafe_allow_html=True,
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
        # Active modes configuration
        "active_modes": {"case": False, "group": True},  # Default: group only
        # Scenario selection for group discussion
        "selected_scenario": "product_team",
    }

    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


def render_sidebar():
    """Render the sidebar with navigation and status."""
    with st.sidebar:
        st.markdown("---")

        # Admin mode toggle at top
        admin_mode = st.toggle("🔐 Admin Mode", key="admin_toggle")
        if admin_mode and st.session_state.get("current_phase") != "admin":
            st.session_state.admin_mode = True
            st.rerun()
        elif not admin_mode and st.session_state.get("admin_mode"):
            st.session_state.admin_mode = False
            st.session_state.admin_authenticated = False
            st.rerun()

        st.markdown("---")

        # Mode configuration (only show before study starts)
        if not st.session_state.get("admin_mode"):
            if st.session_state.get("current_phase") == "consent":
                st.markdown("### Active Modes")

                case_active = st.toggle(
                    "Case Study",
                    value=st.session_state.active_modes.get("case", False),
                    key="case_mode_toggle",
                    help="1-on-1 logical assessment"
                )
                group_active = st.toggle(
                    "Group Discussion",
                    value=st.session_state.active_modes.get("group", True),
                    key="group_mode_toggle",
                    help="Personality assessment with AI team"
                )

                # Ensure at least one mode is active
                if not case_active and not group_active:
                    st.warning("At least one mode required")
                    group_active = True

                # Update session state if changed
                if (case_active != st.session_state.active_modes.get("case") or
                    group_active != st.session_state.active_modes.get("group")):
                    st.session_state.active_modes = {"case": case_active, "group": group_active}
                    st.rerun()

                # Scenario selection (only if group mode is active)
                if group_active:
                    st.markdown("---")
                    st.markdown("### Scenario")

                    scenario_options = {
                        "product_team": "Product Team",
                        "leadership": "Leadership",
                        "innovation": "Innovation"
                    }

                    current_scenario = st.session_state.get("selected_scenario", "product_team")
                    selected = st.selectbox(
                        "Discussion Topic",
                        options=list(scenario_options.keys()),
                        format_func=lambda x: scenario_options[x],
                        index=list(scenario_options.keys()).index(current_scenario),
                        key="scenario_select",
                        help="Choose the discussion scenario"
                    )

                    if selected != current_scenario:
                        st.session_state.selected_scenario = selected
                        st.rerun()

                    # Show focus skills for selected scenario
                    scenario = SCENARIO_TEMPLATES.get(selected, {})
                    if "focus_skills" in scenario:
                        st.caption("**Focus Skills:**")
                        for skill in scenario["focus_skills"]:
                            st.caption(f"• {skill}")

                st.markdown("---")

            st.markdown("### Study Progress")
            render_progress_tracker()

            # Participant ID at bottom
            if st.session_state.participant_id:
                st.divider()
                st.caption(f"ID: {st.session_state.participant_id}")

                # Demo mode indicator
                if st.session_state.get("demo_mode"):
                    st.caption("⚠️ Demo Mode")


def render_progress_tracker():
    """Render the study progress tracker based on active modes."""
    active_modes = st.session_state.get("active_modes", {"case": False, "group": True})
    case_active = active_modes.get("case", False)
    group_active = active_modes.get("group", True)

    # Build dynamic steps list
    steps_display = ["Consent", "Questionnaire"]
    step_map = {"consent": 0, "bfi44": 1}

    idx = 2
    if case_active:
        steps_display.append("Case Study")
        step_map["case"] = idx
        idx += 1
    if group_active:
        steps_display.append("Group Discussion")
        step_map["group"] = idx
        idx += 1

    steps_display.extend(["Survey", "Complete"])
    step_map["results"] = idx
    step_map["survey"] = idx
    step_map["complete"] = idx + 1

    current_phase = st.session_state.get("current_phase", "consent")
    current_idx = step_map.get(current_phase, 0)

    for i, step_name in enumerate(steps_display):
        if i < current_idx:
            # Completed - strikethrough
            st.markdown(f"~~{step_name}~~")
        elif i == current_idx:
            # Current - bold with arrow
            st.markdown(f"**> {step_name}**")
        else:
            # Future - indented
            st.markdown(f"&nbsp;&nbsp;{step_name}")


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
