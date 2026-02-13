"""
Group Discussion Page: Mode 2 - Group discussion with three AI agents.

Agents configured via CCS (Critical Core Skills) schema:
- Alex: Team Lead (high E, low A) - Focus: Decision Making, Influence
- Jordan: Product Manager (high A, high E) - Focus: Collaboration, Communication
- Riley: Senior Engineer (low E, moderate A) - Focus: Sense Making, Adaptability
"""

import streamlit as st
import httpx
import time
from typing import Optional

# Import CCS schema
from ui.schema_config import (
    CCS_HIERARCHY,
    DEFAULT_AGENT_CONFIGS,
    SCENARIO_TEMPLATES,
    ALL_SKILLS,
)


API_BASE = "http://localhost:8000"


def get_next_phase_after_group():
    """Determine next phase based on active modes and completion status."""
    active_modes = st.session_state.get("active_modes", {"case": False, "group": True})

    # If case is active and not yet completed, go to case
    if active_modes.get("case", False) and not st.session_state.get("case_completed", False):
        return "case"

    # Otherwise go to results
    return "results"


# Discussion duration in seconds (15 minutes)
DISCUSSION_DURATION = 15 * 60


def get_active_agents():
    """Get agent configurations (from session state or defaults)."""
    return st.session_state.get("agent_configs", DEFAULT_AGENT_CONFIGS)


def get_active_scenario():
    """Get active scenario (from session state or default)."""
    scenario_key = st.session_state.get("selected_scenario", "product_team")
    return SCENARIO_TEMPLATES.get(scenario_key, SCENARIO_TEMPLATES["product_team"])


# Keep AGENTS as a computed property for backward compatibility
AGENTS = DEFAULT_AGENT_CONFIGS

# Demo agent responses for different scenarios
DEMO_RESPONSES = {
    "opening": [
        {
            "speaker": "jordan",
            "content": "Thanks for joining everyone! So we've got a tough decision ahead. I think we should start by understanding what each of us thinks is most important. What are your initial thoughts?",
        },
    ],
    "generic_alex": [
        "I don't think that's quite right. We need to think about what actually moves the needle here. Let's focus on impact.",
        "Let's be realistic about this. Sounds exciting, but do we have the resources to execute well? I'm skeptical.",
        "I hear what you're saying, but I think you're underweighting the risks. We need to consider the downside.",
    ],
    "generic_jordan": [
        "That's a great point! I can see how that would benefit our users. How do you think we could build on that idea?",
        "I like where this is going. What if we combined elements of both approaches? Maybe we could find a middle ground?",
        "You both make valid points. It seems like we all agree on the core priorities. Can we find common ground there?",
    ],
    "generic_riley": [
        "...I've been thinking about this. Has anyone considered what happens if we choose wrong? What's our fallback?",
        "I'm not sure I agree with the assumptions here. Have we actually validated that with data?",
        "Something doesn't add up. If this is that critical, why wasn't it already prioritized?",
    ],
}


def show_instruction_page():
    """Show immersive loading page before starting the group discussion."""
    agents = get_active_agents()
    scenario = get_active_scenario()

    # Build agent HTML dynamically
    agent_html = ""
    emojis = {"alex": "👔", "jordan": "👩‍💼", "riley": "👨‍💻"}
    for agent_id, agent in agents.items():
        emoji = emojis.get(agent_id, "👤")
        agent_html += f"""
        <div style="text-align: center;">
            <div style="font-size: 48px; margin-bottom: 10px;">{emoji}</div>
            <div style="font-weight: 600; font-size: 1.1rem;">{agent['name']}</div>
            <div style="font-size: 0.8rem; opacity: 0.7;">{agent['role']}</div>
        </div>
        """

    # Navy background meeting room - pressure-cooker style
    st.markdown(f"""
<div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            padding: 50px 30px; border-radius: 20px; text-align: center; color: white; margin-bottom: 30px;">
    <div style="font-size: 0.85rem; opacity: 0.7; margin-bottom: 8px; letter-spacing: 3px; text-transform: uppercase;">
        Virtual Meeting Room
    </div>
    <div style="font-size: 2.2rem; font-weight: 700; margin-bottom: 30px;">
        Group Discussion
    </div>

    <div style="display: flex; justify-content: center; gap: 60px; margin: 40px 0;">
        {agent_html}
    </div>

    <div style="background: rgba(255,255,255,0.1); padding: 20px 50px; border-radius: 12px;
                margin-top: 30px; display: inline-block;">
        <div style="font-size: 28px; margin-bottom: 6px;">👤</div>
        <div style="font-weight: 600; font-size: 1.1rem;">You</div>
    </div>
</div>
    """, unsafe_allow_html=True)

    # Instructions
    st.markdown("### 📋 What to Expect")
    st.markdown("""
You'll join a team meeting to discuss a workplace challenge.
Your AI teammates have different perspectives — engage naturally,
share your opinions, and work together toward a solution.
    """)

    st.markdown("### 💡 Tips")
    st.markdown("""
- Be yourself — respond as you would in a real meeting
- Engage with your teammates' ideas
- It's okay to agree, disagree, or ask questions
    """)

    st.markdown("")

    # Start button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Enter Meeting Room", type="primary", use_container_width=True):
            st.session_state.group_ready_to_start = True
            st.rerun()


def show_group_discussion_page():
    """Display group discussion interface."""
    # Initialize session state
    if "group_session_id" not in st.session_state:
        st.session_state.group_session_id = None
    if "group_messages" not in st.session_state:
        st.session_state.group_messages = []
    if "group_start_time" not in st.session_state:
        st.session_state.group_start_time = None
    if "group_ended" not in st.session_state:
        st.session_state.group_ended = False
    if "group_ready_to_start" not in st.session_state:
        st.session_state.group_ready_to_start = False

    # Show instructions first if not ready to start
    if not st.session_state.group_ready_to_start and st.session_state.group_session_id is None:
        show_instruction_page()
        return

    # Start session if not started
    if st.session_state.group_session_id is None and not st.session_state.group_ended:
        start_group_session()
        return

    # Header with timer and agent status
    render_header()

    st.markdown("---")

    # Layout: Agent panel on left, chat in center
    agent_col, chat_col = st.columns([1, 3])

    with agent_col:
        render_agent_panel()

    with chat_col:
        render_chat_interface()


def render_header():
    """Render the header with timer and controls."""
    scenario = get_active_scenario()
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st.header("Group Discussion")
        st.caption(f"**Scenario:** {scenario['title']}")

    with col2:
        if st.session_state.group_start_time:
            elapsed = int(time.time() - st.session_state.group_start_time)
            remaining = max(0, DISCUSSION_DURATION - elapsed)
            mins, secs = divmod(remaining, 60)

            if remaining < 300:
                st.warning(f"Time: {mins}:{secs:02d}")
            else:
                st.info(f"Time: {mins}:{secs:02d}")

    with col3:
        if st.button("End Discussion", type="secondary"):
            end_group_session()
            return


def render_agent_panel():
    """Render the agent profile panel."""
    agents = get_active_agents()
    scenario = get_active_scenario()

    st.subheader("Team Members")

    # Show participant first
    st.markdown(f"""
    <div style="padding: 10px; background-color: #1E3A5F; border-radius: 8px; margin-bottom: 10px;">
        <strong style="color: white;">{st.session_state.participant_name}</strong><br>
        <span style="color: #94A3B8; font-size: 0.85em;">You</span>
    </div>
    """, unsafe_allow_html=True)

    # Show AI agents
    for agent_id, agent in agents.items():
        st.markdown(f"""
        <div style="padding: 10px; background-color: {agent['color']}22; border-left: 4px solid {agent['color']}; border-radius: 4px; margin-bottom: 8px;">
            <strong>{agent['name']}</strong><br>
            <span style="font-size: 0.85em; color: #666;">{agent['role']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Scenario brief
    st.subheader("Scenario")
    st.markdown(scenario["brief"])

    # Show focus skills if available
    if "focus_skills" in scenario:
        st.markdown("---")
        st.caption("**Skills Assessed:**")
        for skill in scenario["focus_skills"]:
            st.caption(f"• {skill}")


def render_chat_interface():
    """Render the main chat interface."""
    agents = get_active_agents()
    st.subheader("Discussion")

    # Chat container
    chat_container = st.container()

    with chat_container:
        for msg in st.session_state.group_messages:
            speaker = msg.get("speaker", "unknown").lower()

            if speaker == "candidate" or speaker == st.session_state.participant_name.lower():
                with st.chat_message("user", avatar=":material/person:"):
                    st.markdown(msg["content"])
            elif speaker in agents:
                agent = agents[speaker]
                with st.chat_message("assistant", avatar=agent["avatar"]):
                    st.markdown(f"**{agent['name']}:** {msg['content']}")
            else:
                # System or unknown
                with st.chat_message("assistant"):
                    st.markdown(msg["content"])

    # Input area
    if not st.session_state.group_ended:
        user_input = st.chat_input(
            "Share your thoughts with the team...",
            key="group_input"
        )

        if user_input:
            handle_user_message(user_input)


def start_group_session():
    """Initialize the group discussion session."""
    st.info("Starting group discussion session...")

    if st.session_state.get("demo_mode"):
        # Demo mode
        st.session_state.group_session_id = "demo_group_001"
        st.session_state.group_start_time = time.time()

        # Opening messages
        st.session_state.group_messages = [
            {"speaker": "jordan", "content": msg["content"]}
            for msg in DEMO_RESPONSES["opening"]
        ]
        st.rerun()
    else:
        # Call API
        try:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    f"{API_BASE}/session/create",
                    json={
                        "participant_id": st.session_state.participant_id,
                        "mode": "group",
                    }
                )
                response.raise_for_status()
                data = response.json()

                st.session_state.group_session_id = data["session_id"]
                st.session_state.group_start_time = time.time()

                # Convert opening messages
                st.session_state.group_messages = [
                    {"speaker": msg["speaker"].lower(), "content": msg["content"]}
                    for msg in data.get("opening_messages", [])
                ]
                st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to start session: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")


def handle_user_message(content: str):
    """Handle user message submission."""
    # Add user message
    st.session_state.group_messages.append({
        "speaker": "candidate",
        "content": content
    })

    if st.session_state.get("demo_mode"):
        # Demo mode: generate agent responses
        responses = generate_demo_agent_responses(content)
        for resp in responses:
            st.session_state.group_messages.append(resp)
        st.rerun()
    else:
        # Call API
        try:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    f"{API_BASE}/session/{st.session_state.group_session_id}/message",
                    json={"content": content}
                )
                response.raise_for_status()
                data = response.json()

                # Add AI responses
                for turn in data.get("ai_turns", []):
                    st.session_state.group_messages.append({
                        "speaker": turn["speaker"].lower(),
                        "content": turn["content"]
                    })

                # Check if session should end
                if data.get("session_state") == "ended":
                    st.session_state.group_ended = True

                st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Message failed: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")


def generate_demo_agent_responses(user_input: str) -> list[dict]:
    """Generate demo agent responses based on user input and conversation state."""
    import random

    responses = []
    turn_count = len([m for m in st.session_state.group_messages if m.get("speaker") == "candidate"])

    # Determine which agents respond
    if turn_count <= 2:
        # Early discussion: 2 agents respond
        responding_agents = random.sample(["alex", "jordan", "riley"], 2)
    elif turn_count <= 5:
        # Middle discussion: 1-2 agents
        responding_agents = random.sample(["alex", "jordan", "riley"], random.randint(1, 2))
    else:
        # Later discussion: 1 agent, occasionally 2
        responding_agents = random.sample(["alex", "jordan", "riley"], 1)

    for agent in responding_agents:
        response_pool = DEMO_RESPONSES.get(f"generic_{agent}", [])
        if response_pool:
            content = random.choice(response_pool)
            responses.append({
                "speaker": agent,
                "content": content
            })

    return responses


def end_group_session():
    """End the group discussion session and run evaluation."""
    st.session_state.group_ended = True

    if st.session_state.get("demo_mode"):
        # Demo mode: generate mock results
        st.session_state.group_assessment = {
            "openness": {"score": 0.72, "evidence": ["Engaged with creative AI assistant idea", "Asked probing questions about alternatives"]},
            "conscientiousness": {"score": 0.65, "evidence": ["Considered practical constraints", "Mentioned timeline concerns"]},
            "extraversion": {"score": 0.78, "evidence": ["Active participant in discussion", "Initiated several conversation threads"]},
            "agreeableness": {"score": 0.81, "evidence": ["Acknowledged others' viewpoints", "Sought to build consensus"]},
            "neuroticism": {"score": 0.25, "evidence": ["Remained calm when challenged by Alex", "Handled disagreement constructively"]},
            "strengths": ["Strong collaboration skills", "Balanced assertiveness with openness"],
            "development_areas": ["Could be more decisive when group stalls"],
        }
        st.session_state.group_completed = True

        # Determine next phase based on active modes
        st.session_state.current_phase = get_next_phase_after_group()

        st.rerun()
    else:
        # Call API
        try:
            with httpx.Client(timeout=120.0) as client:
                response = client.post(
                    f"{API_BASE}/session/{st.session_state.group_session_id}/end"
                )
                response.raise_for_status()
                data = response.json()

                st.session_state.group_assessment = data.get("summary", {})
                st.session_state.group_completed = True
                st.session_state.current_phase = get_next_phase_after_group()

                st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to end session: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
