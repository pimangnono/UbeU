"""
Admin Dashboard: View participant reports and session results.

Protected by login (id: ubeutest, password: ubeutest)
"""

import json
from pathlib import Path

import streamlit as st


# Admin credentials
ADMIN_ID = "ubeutest"
ADMIN_PASSWORD = "ubeutest"

# Data directories
PARTICIPANTS_DIR = Path("outputs/step2/participants")
SESSIONS_DIR = Path("outputs/step2/sessions")


def render():
    """Render the admin dashboard."""
    # Check if logged in
    if not st.session_state.get("admin_logged_in"):
        _render_login()
        return

    _render_dashboard()


def _render_login():
    """Render the login form."""
    st.markdown(
        """
        <style>
        .admin-login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 40px;
            background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%);
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🔐 Admin Login")
        st.markdown("Enter credentials to access the dashboard.")
        st.markdown("---")

        with st.form("admin_login"):
            user_id = st.text_input("User ID", placeholder="Enter user ID")
            password = st.text_input("Password", type="password", placeholder="Enter password")
            submitted = st.form_submit_button("Login", type="primary", use_container_width=True)

        if submitted:
            if user_id == ADMIN_ID and password == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")

        st.markdown("---")
        if st.button("← Back to Study", use_container_width=True):
            st.session_state.current_step = "consent"
            st.rerun()


def _render_dashboard():
    """Render the main dashboard."""
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("## 📊 Admin Dashboard")
    with col2:
        if st.button("🚪 Logout"):
            st.session_state.admin_logged_in = False
            st.rerun()

    st.markdown("---")

    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_pid = st.text_input(
            "🔍 Search Participant ID",
            placeholder="e.g., P051",
            key="admin_search",
        )
    with col2:
        st.markdown("")  # Spacer
        refresh = st.button("🔄 Refresh Data")
    with col3:
        st.markdown("")
        show_all = st.checkbox("Show all details", value=False)

    if refresh:
        st.rerun()

    st.markdown("---")

    # Load all participants
    participants = _load_all_participants()

    if not participants:
        st.warning("No participants found.")
        return

    # Filter by search
    if search_pid:
        participants = {
            pid: data for pid, data in participants.items()
            if search_pid.upper() in pid.upper()
        }

    if not participants:
        st.info(f"No participants matching '{search_pid}'")
        return

    # Summary stats
    total = len(participants)
    completed = sum(1 for p in participants.values() if p.get("session_output"))
    with_survey = sum(1 for p in participants.values() if p.get("record", {}).get("survey"))

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Participants", total)
    with col2:
        st.metric("Sessions Completed", completed)
    with col3:
        st.metric("Surveys Submitted", with_survey)
    with col4:
        st.metric("Completion Rate", f"{100*completed/total:.0f}%" if total else "0%")

    st.markdown("---")

    # Participant list
    for pid in sorted(participants.keys(), reverse=True):
        data = participants[pid]
        _render_participant_card(pid, data, expanded=show_all or bool(search_pid))


def _load_all_participants() -> dict:
    """Load all participant data."""
    participants = {}

    if not PARTICIPANTS_DIR.exists():
        return participants

    for pdir in sorted(PARTICIPANTS_DIR.iterdir()):
        if not pdir.is_dir() or not pdir.name.startswith("P"):
            continue

        pid = pdir.name
        data = {"pid": pid}

        # Load record.json
        record_path = pdir / "record.json"
        if record_path.exists():
            with open(record_path) as f:
                data["record"] = json.load(f)

        # Load session_output.json
        session_output_path = pdir / "session_output.json"
        if session_output_path.exists():
            with open(session_output_path) as f:
                data["session_output"] = json.load(f)

        # Load logic_validation.json
        logic_path = pdir / "logic_validation.json"
        if logic_path.exists():
            with open(logic_path) as f:
                data["logic_validation"] = json.load(f)

        participants[pid] = data

    return participants


def _render_participant_card(pid: str, data: dict, expanded: bool = False):
    """Render a participant card with expandable details."""
    record = data.get("record", {})
    session_output = data.get("session_output")
    logic_validation = data.get("logic_validation")

    # Status indicators
    has_consent = record.get("consent_given", False)
    has_bfi44 = record.get("bfi44_scores") is not None
    has_session = session_output is not None
    has_survey = record.get("survey") is not None

    status_icons = []
    if has_consent:
        status_icons.append("✅ Consent")
    if has_bfi44:
        status_icons.append("📝 BFI-44")
    if has_session:
        status_icons.append("💬 Session")
    if has_survey:
        status_icons.append("📊 Survey")

    status_text = " | ".join(status_icons) if status_icons else "⏳ Started"

    with st.expander(f"**{pid}** - {record.get('name', 'Unknown')} | {status_text}", expanded=expanded):
        tabs = st.tabs(["📋 Overview", "🧠 Personality", "💬 Conversation", "📊 Assessment"])

        with tabs[0]:
            _render_overview_tab(record, session_output)

        with tabs[1]:
            _render_personality_tab(record, session_output)

        with tabs[2]:
            _render_conversation_tab(session_output)

        with tabs[3]:
            _render_assessment_tab(session_output, logic_validation)


def _render_overview_tab(record: dict, session_output: dict):
    """Render overview tab."""
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Participant Info**")
        st.write(f"- **Name:** {record.get('name', 'N/A')}")
        st.write(f"- **ID:** {record.get('participant_id', 'N/A')}")
        st.write(f"- **Scenario:** {record.get('assigned_scenario', 'N/A')}")
        st.write(f"- **Created:** {record.get('created_at', 'N/A')[:19] if record.get('created_at') else 'N/A'}")

    with col2:
        st.markdown("**Session Info**")
        if session_output:
            meta = session_output.get("metadata", {})
            st.write(f"- **Session ID:** {meta.get('session_id', 'N/A')}")
            st.write(f"- **Total Turns:** {meta.get('total_turns', 0)}")
            duration = meta.get('duration_seconds', 0)
            st.write(f"- **Duration:** {duration/60:.1f} minutes")
            st.write(f"- **Model:** {meta.get('model_used', 'N/A')}")
        else:
            st.info("No session data yet.")

    # Survey results
    if record.get("survey"):
        st.markdown("---")
        st.markdown("**Post-Session Survey**")
        survey = record["survey"]
        survey_items = [
            ("Naturalness", survey.get("naturalness")),
            ("Authenticity", survey.get("authenticity")),
            ("Realism", survey.get("realism")),
            ("Engagement", survey.get("engagement")),
            ("Recommendation", survey.get("recommendation")),
        ]
        cols = st.columns(5)
        for i, (label, score) in enumerate(survey_items):
            with cols[i]:
                st.metric(label, f"{score}/5" if score else "N/A")

        if survey.get("open_feedback"):
            st.markdown(f"**Feedback:** {survey['open_feedback']}")


def _render_personality_tab(record: dict, session_output: dict):
    """Render personality comparison tab."""
    # Guard against None record
    if record is None:
        record = {}

    # Ground truth (BFI-44) - handle None explicitly
    bfi44_raw = record.get("bfi44_scores")
    bfi44 = bfi44_raw if isinstance(bfi44_raw, dict) else {}

    # Inferred (from session)
    inferred = {}
    inference_data = {}
    if session_output and isinstance(session_output, dict):
        inference_data = session_output.get("personality_inference") or {}
        if isinstance(inference_data, dict):
            inferred = inference_data.get("average_ocean") or {}
        else:
            inference_data = {}

    st.markdown("**OCEAN Personality Comparison**")

    # Create comparison table
    traits = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]

    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.markdown("**Trait**")
    with col2:
        st.markdown("**Ground Truth (BFI-44)**")
    with col3:
        st.markdown("**Inferred (Ensemble)**")
    with col4:
        st.markdown("**Difference**")

    for trait in traits:
        gt = bfi44.get(trait, 0.5) if bfi44 else 0.5
        inf = inferred.get(trait, 0.5) if inferred else 0.5
        diff = inf - gt

        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        with col1:
            st.write(trait.capitalize())
        with col2:
            st.write(f"{gt:.2f}")
        with col3:
            st.write(f"{inf:.2f}")
        with col4:
            color = "green" if abs(diff) < 0.1 else "orange" if abs(diff) < 0.2 else "red"
            st.markdown(f":{color}[{diff:+.2f}]")

    # Evidence section - show quotes supporting each trait
    if inference_data and inference_data.get("model_results"):
        st.markdown("---")
        st.markdown("**📝 Evidence from Conversation**")

        # Collect all evidence from all models
        all_evidence = []
        for mr in inference_data.get("model_results", []):
            if mr.get("success") and mr.get("evidence"):
                for ev in mr["evidence"]:
                    all_evidence.append(ev)

        if all_evidence:
            # Group evidence by trait
            trait_evidence = {t: [] for t in traits}
            for ev in all_evidence:
                facet = ev.get("facet", "").lower()
                quote = ev.get("quote", "")
                signal = ev.get("signal", "")

                # Map facet to OCEAN trait
                facet_to_trait = {
                    "fantasy": "openness", "aesthetics": "openness", "feelings": "openness",
                    "actions": "openness", "ideas": "openness", "values": "openness",
                    "competence": "conscientiousness", "order": "conscientiousness",
                    "dutifulness": "conscientiousness", "achievement_striving": "conscientiousness",
                    "self_discipline": "conscientiousness", "deliberation": "conscientiousness",
                    "warmth": "extraversion", "gregariousness": "extraversion",
                    "assertiveness": "extraversion", "activity": "extraversion",
                    "excitement_seeking": "extraversion", "positive_emotions": "extraversion",
                    "trust": "agreeableness", "straightforwardness": "agreeableness",
                    "altruism": "agreeableness", "compliance": "agreeableness",
                    "modesty": "agreeableness", "tender_mindedness": "agreeableness",
                    "anxiety": "neuroticism", "angry_hostility": "neuroticism",
                    "depression": "neuroticism", "self_consciousness": "neuroticism",
                    "impulsiveness": "neuroticism", "vulnerability": "neuroticism",
                }
                trait_for_facet = facet_to_trait.get(facet, "")
                if trait_for_facet and quote:
                    trait_evidence[trait_for_facet].append({
                        "quote": quote,
                        "facet": facet,
                        "signal": signal
                    })

            # Display evidence per trait
            for trait in traits:
                evidences = trait_evidence.get(trait, [])
                if evidences:
                    with st.expander(f"{trait.capitalize()} ({len(evidences)} evidence items)"):
                        for i, ev in enumerate(evidences[:5]):  # Show max 5
                            signal_icon = "🔺" if ev["signal"] == "high" else "🔻" if ev["signal"] == "low" else "➖"
                            st.markdown(f"{signal_icon} **{ev['facet']}**: \"{ev['quote']}\"")
                        if len(evidences) > 5:
                            st.caption(f"... and {len(evidences) - 5} more")
        else:
            st.info("No evidence quotes available.")

    # Model breakdown
    if inference_data and inference_data.get("model_results"):
        st.markdown("---")
        st.markdown("**Individual Model Results**")

        for mr in inference_data.get("model_results", []):
            model_name = mr.get("model", "unknown").split("/")[-1]
            if mr.get("success"):
                scores = mr.get("ocean_scores", {})
                evidence_count = mr.get("evidence_count", 0)
                st.write(f"**{model_name}** ({evidence_count} evidence items)")
                score_str = " | ".join([
                    f"O:{scores.get('openness', 0.5):.2f}",
                    f"C:{scores.get('conscientiousness', 0.5):.2f}",
                    f"E:{scores.get('extraversion', 0.5):.2f}",
                    f"A:{scores.get('agreeableness', 0.5):.2f}",
                    f"N:{scores.get('neuroticism', 0.5):.2f}",
                ])
                st.caption(score_str)
            else:
                st.write(f"**{model_name}**: ❌ Failed - {mr.get('error', 'Unknown error')[:50]}")

    # Strengths and weaknesses
    if inference_data:
        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**💪 Strengths**")
            strengths = inference_data.get("strengths", [])
            if strengths:
                for s in strengths:
                    trait_name = s.get('trait', 'unknown')
                    description = s.get('description', '')
                    st.success(f"**{trait_name.capitalize()}**: {description}")
                    evidence_list = s.get("evidence", [])
                    if evidence_list:
                        quote = evidence_list[0].get('quote', '') if isinstance(evidence_list[0], dict) else ''
                        if quote:
                            st.caption(f"Evidence: \"{quote[:100]}{'...' if len(quote) > 100 else ''}\"")
            else:
                st.info("No significant strengths identified (scores near neutral)")

        with col2:
            st.markdown("**⚠️ Areas for Development**")
            weaknesses = inference_data.get("weaknesses", [])
            if weaknesses:
                for w in weaknesses:
                    trait_name = w.get('trait', 'unknown')
                    description = w.get('description', '')
                    st.warning(f"**{trait_name.capitalize()}**: {description}")
                    evidence_list = w.get("evidence", [])
                    if evidence_list:
                        quote = evidence_list[0].get('quote', '') if isinstance(evidence_list[0], dict) else ''
                        if quote:
                            st.caption(f"Evidence: \"{quote[:100]}{'...' if len(quote) > 100 else ''}\"")
            else:
                st.info("No significant weaknesses identified (scores near neutral)")


def _render_conversation_tab(session_output: dict):
    """Render conversation transcript."""
    if not session_output:
        st.info("No session data available.")
        return

    conversation = session_output.get("conversation", [])
    if not conversation:
        st.info("No conversation recorded.")
        return

    st.markdown(f"**Conversation Transcript** ({len(conversation)} turns)")
    st.markdown("---")

    for turn in conversation:
        speaker = turn.get("speaker_name", turn.get("speaker", "Unknown"))
        content = turn.get("content", "")
        role = turn.get("speaker", "")

        # Color coding by role
        if role == "candidate":
            st.markdown(f"**🧑 {speaker}:** {content}")
        elif role == "provoker":
            st.markdown(f"**🔴 {speaker}:** {content}")
        elif role == "mediator":
            st.markdown(f"**🟢 {speaker}:** {content}")
        else:
            st.markdown(f"**📋 {speaker}:** {content}")


def _render_assessment_tab(session_output: dict, logic_validation: dict):
    """Render assessment and validation results."""
    if not session_output and not logic_validation:
        st.info("No assessment data available.")
        return

    # Competency scores
    if session_output and session_output.get("assessment_mapping"):
        st.markdown("**Competency Assessment**")
        mapping = session_output["assessment_mapping"]

        cols = st.columns(5)
        competencies = [
            ("Collaboration", mapping.get("collaboration_score", 0)),
            ("Leadership", mapping.get("leadership_score", 0)),
            ("Stress Mgmt", mapping.get("stress_management_score", 0)),
            ("Communication", mapping.get("communication_score", 0)),
            ("Problem Solving", mapping.get("problem_solving_score", 0)),
        ]
        for i, (name, score) in enumerate(competencies):
            with cols[i]:
                pct = score * 100 if score <= 1 else score
                st.metric(name, f"{pct:.0f}%")

    # Logic validation
    if logic_validation:
        st.markdown("---")
        st.markdown("**Analytical Assessment (Senior Analyst)**")

        col1, col2 = st.columns(2)
        with col1:
            depth = logic_validation.get("analytical_depth", 0)
            st.metric("Analytical Depth", f"{depth}/5")
        with col2:
            rec = logic_validation.get("recommendation_quality", 0)
            st.metric("Recommendation Quality", f"{rec}/5")

        # Summary
        if logic_validation.get("summary"):
            st.markdown("**Summary:**")
            st.info(logic_validation["summary"])

        # Logical gaps
        gaps = logic_validation.get("logical_gaps", [])
        if gaps:
            with st.expander(f"Logical Gaps ({len(gaps)} identified)"):
                for gap in gaps[:10]:
                    st.write(f"• {gap}")
                if len(gaps) > 10:
                    st.caption(f"... and {len(gaps) - 10} more")

        # Assumptions
        assumptions = logic_validation.get("assumptions_made", [])
        if assumptions:
            valid = [a for a in assumptions if a.get("valid")]
            invalid = [a for a in assumptions if not a.get("valid")]

            with st.expander(f"Assumptions ({len(valid)} valid, {len(invalid)} invalid)"):
                for a in assumptions[:8]:
                    icon = "✅" if a.get("valid") else "❌"
                    st.write(f"{icon} **{a.get('assumption', 'N/A')}**")
                    st.caption(a.get("explanation", ""))
