"""
Pressure Cooker Annotation Tool
Streamlit-based UI for annotating personality simulation conversations.

Run with: streamlit run ui/app.py
"""

import json
import os
from datetime import datetime
from pathlib import Path

import streamlit as st

# Page config
st.set_page_config(
    page_title="Pressure Cooker Annotation Tool",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Constants
INTENT_OPTIONS = [
    "assertive",
    "cooperative",
    "avoidant",
    "aggressive",
    "anxious",
    "analytical",
    "creative",
    "empathetic",
    "defensive",
    "neutral"
]

CONFIDENCE_OPTIONS = ["Low", "Medium", "High"]

# Session state initialization
if "current_turn" not in st.session_state:
    st.session_state.current_turn = 0
if "session_data" not in st.session_state:
    st.session_state.session_data = None
if "annotations" not in st.session_state:
    st.session_state.annotations = {}
if "rater_id" not in st.session_state:
    st.session_state.rater_id = ""


def load_session(file_path: str) -> dict:
    """Load a session JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)


def get_available_sessions(sessions_dir: str = "outputs/sessions") -> list[str]:
    """Get list of available session files."""
    path = Path(sessions_dir)
    if not path.exists():
        return []
    return sorted([f.name for f in path.glob("*.json")])


def get_speaker_style(speaker: str) -> tuple[str, str]:
    """Get color and emoji for speaker role."""
    styles = {
        "candidate": ("#4CAF50", "🎯"),  # Green - target for annotation
        "provoker": ("#f44336", "😤"),   # Red
        "mediator": ("#2196F3", "🤝"),   # Blue
        "system": ("#9E9E9E", "📋"),     # Gray
    }
    return styles.get(speaker, ("#000000", "💬"))


def render_sidebar():
    """Render the sidebar with session selection and rater info."""
    st.sidebar.title("🔥 Pressure Cooker")
    st.sidebar.markdown("---")

    # Rater ID
    st.session_state.rater_id = st.sidebar.text_input(
        "Rater ID",
        value=st.session_state.rater_id,
        placeholder="Enter your ID (e.g., R01)"
    )

    st.sidebar.markdown("---")

    # Session selection
    st.sidebar.subheader("Session Selection")

    sessions = get_available_sessions()

    if not sessions:
        st.sidebar.warning("No sessions found in outputs/sessions/")
        st.sidebar.info("Run a simulation first:\n`python main.py simulate --mock -p balanced_leader -s resource_conflict`")
        return None

    selected_session = st.sidebar.selectbox(
        "Select Session",
        sessions,
        index=0
    )

    if st.sidebar.button("Load Session", type="primary"):
        file_path = f"outputs/sessions/{selected_session}"
        st.session_state.session_data = load_session(file_path)
        st.session_state.current_turn = 0
        st.session_state.annotations = {}
        st.rerun()

    # Session info
    if st.session_state.session_data:
        st.sidebar.markdown("---")
        st.sidebar.subheader("Session Info")
        data = st.session_state.session_data
        st.sidebar.text(f"ID: {data['metadata']['session_id']}")
        st.sidebar.text(f"Profile: {data['profile']['name']}")
        st.sidebar.text(f"Scenario: {data['scenario']['name']}")
        st.sidebar.text(f"Turns: {len(data['conversation'])}")

        # Progress
        total_candidate_turns = sum(
            1 for t in data['conversation']
            if t['speaker'] == 'candidate'
        )
        annotated = len(st.session_state.annotations)
        st.sidebar.progress(
            annotated / total_candidate_turns if total_candidate_turns > 0 else 0,
            text=f"Annotated: {annotated}/{total_candidate_turns}"
        )

    return selected_session


def render_conversation_panel():
    """Render the conversation display panel."""
    if not st.session_state.session_data:
        return

    conversation = st.session_state.session_data["conversation"]
    current = st.session_state.current_turn

    st.subheader("📜 Conversation")

    # Conversation container with scrolling
    conv_container = st.container(height=400)

    with conv_container:
        for i, turn in enumerate(conversation):
            speaker = turn["speaker"]
            color, emoji = get_speaker_style(speaker)

            # Highlight current turn
            is_current = i == current
            is_candidate = speaker == "candidate"

            # Build the turn display
            if is_current:
                st.markdown(
                    f"""<div style="background-color: #fff3cd; padding: 10px;
                    border-radius: 8px; margin: 5px 0; border-left: 4px solid {color};">
                    <strong>{emoji} {turn['speaker_name']}</strong>
                    <span style="color: #666;">(Turn {i+1})</span>
                    {"⭐ <em>Annotate this</em>" if is_candidate else ""}
                    <br/>{turn['content']}
                    </div>""",
                    unsafe_allow_html=True
                )
            else:
                opacity = "0.6" if i > current else "1.0"
                st.markdown(
                    f"""<div style="padding: 10px; border-radius: 8px; margin: 5px 0;
                    border-left: 4px solid {color}; opacity: {opacity};">
                    <strong>{emoji} {turn['speaker_name']}</strong>
                    <span style="color: #666;">(Turn {i+1})</span>
                    <br/>{turn['content']}
                    </div>""",
                    unsafe_allow_html=True
                )


def render_annotation_panel():
    """Render the annotation panel for candidate turns."""
    if not st.session_state.session_data:
        return

    conversation = st.session_state.session_data["conversation"]
    current = st.session_state.current_turn

    if current >= len(conversation):
        st.success("🎉 All turns reviewed!")
        return

    turn = conversation[current]

    st.subheader("✏️ Annotation Panel")

    # Only show annotation for candidate turns
    if turn["speaker"] == "candidate":
        st.markdown(f"**Turn {current + 1}:** {turn['speaker_name']}")
        st.info(f'"{turn["content"]}"')

        # Get existing annotation if any
        existing = st.session_state.annotations.get(current, {})

        col1, col2 = st.columns(2)

        with col1:
            # Intent selection
            current_intent = existing.get("intent", turn.get("intent", "neutral"))
            intent_idx = INTENT_OPTIONS.index(current_intent) if current_intent in INTENT_OPTIONS else 0

            selected_intent = st.selectbox(
                "Intent Category",
                INTENT_OPTIONS,
                index=intent_idx,
                key=f"intent_{current}"
            )

        with col2:
            # Confidence
            current_conf = existing.get("confidence", "Medium")
            conf_idx = CONFIDENCE_OPTIONS.index(current_conf) if current_conf in CONFIDENCE_OPTIONS else 1

            selected_confidence = st.radio(
                "Confidence",
                CONFIDENCE_OPTIONS,
                index=conf_idx,
                horizontal=True,
                key=f"conf_{current}"
            )

        # Notes
        notes = st.text_area(
            "Notes (optional)",
            value=existing.get("notes", ""),
            height=80,
            key=f"notes_{current}"
        )

        # Save annotation
        st.session_state.annotations[current] = {
            "turn_number": current,
            "intent": selected_intent,
            "confidence": selected_confidence,
            "notes": notes,
            "original_intent": turn.get("intent"),
            "timestamp": datetime.now().isoformat()
        }

    else:
        st.markdown(f"**Turn {current + 1}:** {turn['speaker_name']} ({turn['speaker']})")
        st.markdown(f'> {turn["content"]}')
        st.caption("ℹ️ Non-candidate turn - no annotation needed. Click Next to continue.")


def render_navigation():
    """Render navigation buttons."""
    if not st.session_state.session_data:
        return

    conversation = st.session_state.session_data["conversation"]
    current = st.session_state.current_turn
    total = len(conversation)

    st.markdown("---")

    col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])

    with col1:
        if st.button("⏮️ First", disabled=current == 0):
            st.session_state.current_turn = 0
            st.rerun()

    with col2:
        if st.button("◀️ Prev", disabled=current == 0):
            st.session_state.current_turn = max(0, current - 1)
            st.rerun()

    with col3:
        st.markdown(
            f"<div style='text-align: center; padding: 8px;'>"
            f"<strong>Turn {current + 1} / {total}</strong></div>",
            unsafe_allow_html=True
        )

    with col4:
        if st.button("Next ▶️", disabled=current >= total - 1, type="primary"):
            st.session_state.current_turn = min(total - 1, current + 1)
            st.rerun()

    with col5:
        if st.button("Last ⏭️", disabled=current >= total - 1):
            st.session_state.current_turn = total - 1
            st.rerun()


def render_export_panel():
    """Render export/save functionality."""
    if not st.session_state.session_data:
        return

    if not st.session_state.annotations:
        return

    st.markdown("---")
    st.subheader("💾 Export Annotations")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Save Annotations"):
            save_annotations()
            st.success("Annotations saved!")

    with col2:
        # Download button
        export_data = {
            "session_id": st.session_state.session_data["metadata"]["session_id"],
            "rater_id": st.session_state.rater_id,
            "timestamp": datetime.now().isoformat(),
            "annotations": list(st.session_state.annotations.values()),
            "ground_truth": st.session_state.session_data["profile"]["vector"]
        }

        st.download_button(
            "Download JSON",
            data=json.dumps(export_data, indent=2),
            file_name=f"annotation_{export_data['session_id']}_{st.session_state.rater_id}.json",
            mime="application/json"
        )


def save_annotations():
    """Save annotations to file."""
    if not st.session_state.session_data or not st.session_state.annotations:
        return

    output_dir = Path("outputs/annotations")
    output_dir.mkdir(parents=True, exist_ok=True)

    session_id = st.session_state.session_data["metadata"]["session_id"]
    rater_id = st.session_state.rater_id or "anonymous"

    export_data = {
        "session_id": session_id,
        "rater_id": rater_id,
        "timestamp": datetime.now().isoformat(),
        "annotations": list(st.session_state.annotations.values()),
        "ground_truth": st.session_state.session_data["profile"]["vector"]
    }

    filename = f"annotation_{session_id}_{rater_id}.json"
    with open(output_dir / filename, "w") as f:
        json.dump(export_data, f, indent=2)


def render_meeting_scene():
    """Render a simple 2D meeting scene visualization."""
    if not st.session_state.session_data:
        return

    conversation = st.session_state.session_data["conversation"]
    current = st.session_state.current_turn

    if current >= len(conversation):
        return

    turn = conversation[current]
    speaker = turn["speaker"]

    # Simple ASCII-style meeting scene
    scene = """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 20px; border-radius: 12px; text-align: center; color: white;">
        <div style="font-size: 14px; margin-bottom: 10px;">Meeting Room</div>
        <div style="display: flex; justify-content: center; gap: 40px; margin: 20px 0;">
            <div style="opacity: {provoker_opacity};">
                <div style="font-size: 40px;">😤</div>
                <div>Jordan</div>
                <div style="font-size: 10px;">(Provoker)</div>
            </div>
            <div style="opacity: {candidate_opacity};">
                <div style="font-size: 40px;">🎯</div>
                <div>Alex</div>
                <div style="font-size: 10px;">(Candidate)</div>
            </div>
            <div style="opacity: {mediator_opacity};">
                <div style="font-size: 40px;">🤝</div>
                <div>Sam</div>
                <div style="font-size: 10px;">(Mediator)</div>
            </div>
        </div>
        <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px; margin-top: 10px;">
            <strong>{speaker_name}</strong>: "{content}"
        </div>
    </div>
    """.format(
        provoker_opacity="1.0" if speaker == "provoker" else "0.5",
        candidate_opacity="1.0" if speaker == "candidate" else "0.5",
        mediator_opacity="1.0" if speaker == "mediator" else "0.5",
        speaker_name=turn["speaker_name"],
        content=turn["content"][:100] + "..." if len(turn["content"]) > 100 else turn["content"]
    )

    st.markdown(scene, unsafe_allow_html=True)


def main():
    """Main application."""
    # Sidebar
    render_sidebar()

    # Main content
    st.title("🔥 Pressure Cooker Annotation Tool")

    if not st.session_state.session_data:
        st.info("👈 Select and load a session from the sidebar to begin annotation.")

        st.markdown("### Quick Start")
        st.markdown("""
        1. Enter your Rater ID in the sidebar
        2. Select a session file from the dropdown
        3. Click **Load Session**
        4. Navigate through turns using Next/Prev buttons
        5. Annotate candidate (🎯 Alex) turns with intent labels
        6. Export your annotations when done
        """)
        return

    # Two column layout
    col_left, col_right = st.columns([1, 1])

    with col_left:
        render_meeting_scene()
        st.markdown("")
        render_conversation_panel()

    with col_right:
        render_annotation_panel()
        render_navigation()
        render_export_panel()


if __name__ == "__main__":
    main()
