"""
Consent Page: Participant registration and informed consent.
"""

import streamlit as st
import httpx
from datetime import datetime


API_BASE = "http://localhost:8000"


def show_consent_page():
    """Display registration and consent form."""
    st.header("Participant Registration")

    # Study information
    st.markdown("""
    ### About This Study

    Welcome to the **UbeU V3 Dual-Mode AI Interview Platform**. This system is part of an
    NUS Final Year Thesis project exploring AI-based candidate assessment methods.

    You will complete:
    1. **BFI-44 Questionnaire** - Standard personality assessment (~5 min)
    2. **Two Interview Modes** - Each approximately 15 minutes
       - **Case Study Interview** - Problem-solving with an AI facilitator
       - **Group Discussion** - Collaboration with AI team members
    3. **Brief Survey** - Your feedback on the experience (~2 min)

    Total estimated time: **35-45 minutes**
    """)

    st.markdown("---")

    # Demo mode toggle
    demo_mode = st.checkbox(
        "Demo Mode (skip API calls)",
        help="Enable for testing without backend server"
    )

    if demo_mode:
        st.session_state.demo_mode = True
        st.info("Demo mode enabled. Responses will be simulated locally.")

    # Registration form
    with st.form("registration_form"):
        st.markdown("### Your Information")

        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(
                "Full Name *",
                placeholder="Enter your full name",
                help="This will be used to personalize your experience"
            )
        with col2:
            email = st.text_input(
                "Email (optional)",
                placeholder="your.email@example.com",
                help="For receiving your assessment report"
            )

        st.markdown("---")
        st.markdown("### Informed Consent")

        st.markdown("""
        **Please read carefully before proceeding:**

        By participating in this study, you understand and agree that:

        1. **Data Collection**: Your text responses and interaction patterns will be recorded
           and analyzed by AI systems to generate personality and logical assessment reports.

        2. **Assessment Nature**: This is a research platform, not a validated employment
           assessment tool. Results are for research purposes only.

        3. **Privacy**: Your data will be anonymized using a participant ID. Your name
           will only appear in your personal report.

        4. **Voluntary Participation**: You may withdraw at any time by closing the browser.
           Incomplete data will not be used in analysis.

        5. **Research Use**: Aggregated, anonymized findings may be published in academic
           contexts (thesis, papers) without identifying individual participants.

        6. **Data Retention**: Your data will be retained for the duration of the research
           project (approximately 6 months) and then securely deleted.
        """)

        consent_understand = st.checkbox(
            "I have read and understood the above information"
        )
        consent_participate = st.checkbox(
            "I voluntarily agree to participate in this study"
        )
        consent_data = st.checkbox(
            "I consent to my responses being recorded and analyzed"
        )

        st.markdown("---")

        submitted = st.form_submit_button(
            "Continue to Questionnaire",
            use_container_width=True,
            type="primary"
        )

        if submitted:
            # Validate inputs
            if not name or len(name.strip()) < 2:
                st.error("Please enter your full name (at least 2 characters).")
                return

            if not (consent_understand and consent_participate and consent_data):
                st.error("Please agree to all consent items to continue.")
                return

            # Create participant
            if demo_mode or st.session_state.get("demo_mode"):
                # Demo mode: generate local ID
                import uuid
                pid = f"P{str(uuid.uuid4())[:6].upper()}"
                st.session_state.participant_id = pid
                st.session_state.participant_name = name.strip()
                st.session_state.participant_email = email.strip() if email else None
                st.session_state.condition = "case_first"  # Default for demo
                st.session_state.first_mode = "case"
                st.session_state.consent_given = True
                st.session_state.current_phase = "bfi44"
                st.success(f"Registered as participant {pid}")
                st.rerun()
            else:
                # Call API
                try:
                    with httpx.Client(timeout=30.0) as client:
                        # Create participant
                        response = client.post(
                            f"{API_BASE}/participant",
                            json={"name": name.strip(), "email": email.strip() if email else None}
                        )
                        response.raise_for_status()
                        data = response.json()

                        pid = data["participant_id"]

                        # Record consent
                        consent_response = client.post(
                            f"{API_BASE}/participant/{pid}/consent",
                            json={"consent": True}
                        )
                        consent_response.raise_for_status()

                        # Store in session
                        st.session_state.participant_id = pid
                        st.session_state.participant_name = name.strip()
                        st.session_state.participant_email = email.strip() if email else None
                        st.session_state.condition = data.get("condition", "case_first")
                        st.session_state.first_mode = data.get("first_mode", "case")
                        st.session_state.consent_given = True
                        st.session_state.current_phase = "bfi44"

                        st.success(f"Registered as participant {pid}")
                        st.rerun()

                except httpx.HTTPError as e:
                    st.error(f"Registration failed: {str(e)}")
                except Exception as e:
                    st.error(f"Unexpected error: {str(e)}")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.85em;">
        <p>Questions or concerns? Contact the research team.</p>
        <p>NUS School of Computing | Final Year Thesis Project</p>
    </div>
    """, unsafe_allow_html=True)
