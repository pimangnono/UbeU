"""
Group Discussion Page: Mode 2 - Group discussion with three AI agents.

Agents:
- Alex: Assertive Challenger (high E, low A)
- Jordan: Supportive Collaborator (high A, high E)
- Riley: Quiet Skeptic (low E, moderate A)
"""

import streamlit as st
import httpx
import time
from typing import Optional


API_BASE = "http://localhost:8000"

# Discussion duration in seconds (15 minutes)
DISCUSSION_DURATION = 15 * 60

# Agent profiles
AGENTS = {
    "alex": {
        "name": "Alex",
        "role": "Assertive Challenger",
        "avatar": ":material/fitness_center:",
        "color": "#EF4444",  # Red
        "description": "Direct communicator, challenges ideas constructively",
    },
    "jordan": {
        "name": "Jordan",
        "role": "Supportive Collaborator",
        "avatar": ":material/handshake:",
        "color": "#22C55E",  # Green
        "description": "Builds on others' ideas, seeks common ground",
    },
    "riley": {
        "name": "Riley",
        "role": "Quiet Skeptic",
        "avatar": ":material/psychology:",
        "color": "#3B82F6",  # Blue
        "description": "Thoughtful observer, raises important questions",
    },
}

# Demo scenario
DEMO_SCENARIO = {
    "title": "Resource Allocation Conflict",
    "brief": """Your team has been given 3 weeks to deliver a product update. However, you can only
realistically complete 2 out of 4 proposed features. The features are:

1. **Performance Optimization** - 30% speed improvement for existing users
2. **Mobile App** - New mobile version requested by enterprise clients
3. **AI Assistant** - Trendy feature that could attract new users
4. **Security Upgrade** - Address known vulnerabilities

As a team, you need to reach consensus on which 2 features to prioritize.""",
}

# Demo agent responses for different scenarios
DEMO_RESPONSES = {
    "opening": [
        {
            "speaker": "jordan",
            "content": "Thanks for joining everyone! So we've got a tough decision - we can only build 2 of these 4 features. I think we should start by understanding what each of us thinks is most important. What are your initial thoughts?",
        },
    ],
    "generic_alex": [
        "I don't think that's quite right. We need to think about what actually moves the needle here. Performance optimization affects every single user we have - that's a guaranteed impact.",
        "Let's be realistic about this. The AI assistant sounds exciting, but do we even have the expertise to build it well in 3 weeks? I'm skeptical.",
        "I hear what you're saying, but I think you're underweighting the risk of NOT doing the security upgrade. One breach and our reputation is gone.",
    ],
    "generic_jordan": [
        "That's a great point! I can see how that would benefit our users. How do you think we could build on that idea?",
        "I like where this is going. What if we combined elements of both approaches? Maybe we could do a scaled-down version of the mobile app alongside the security upgrade?",
        "You both make valid points. It seems like we all agree that user trust is important - whether through security or performance. Can we find common ground there?",
    ],
    "generic_riley": [
        "...I've been thinking about this. Has anyone considered what happens if we choose wrong? What's our fallback?",
        "I'm not sure I agree with the assumptions here. The enterprise clients want mobile, but have we actually validated that it would affect renewals?",
        "Something doesn't add up. If security is that critical, why wasn't it already prioritized?",
    ],
}


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
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st.header("Group Discussion")
        st.caption(f"**Scenario:** {DEMO_SCENARIO['title']}")

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
    st.subheader("Team Members")

    # Show participant first
    st.markdown(f"""
    <div style="padding: 10px; background-color: #1E3A5F; border-radius: 8px; margin-bottom: 10px;">
        <strong style="color: white;">{st.session_state.participant_name}</strong><br>
        <span style="color: #94A3B8; font-size: 0.85em;">You</span>
    </div>
    """, unsafe_allow_html=True)

    # Show AI agents
    for agent_id, agent in AGENTS.items():
        st.markdown(f"""
        <div style="padding: 10px; background-color: {agent['color']}22; border-left: 4px solid {agent['color']}; border-radius: 4px; margin-bottom: 8px;">
            <strong>{agent['name']}</strong><br>
            <span style="font-size: 0.85em; color: #666;">{agent['role']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Scenario brief
    st.subheader("Scenario")
    st.markdown(DEMO_SCENARIO["brief"])


def render_chat_interface():
    """Render the main chat interface."""
    st.subheader("Discussion")

    # Chat container
    chat_container = st.container()

    with chat_container:
        for msg in st.session_state.group_messages:
            speaker = msg.get("speaker", "unknown").lower()

            if speaker == "candidate" or speaker == st.session_state.participant_name.lower():
                with st.chat_message("user", avatar=":material/person:"):
                    st.markdown(msg["content"])
            elif speaker in AGENTS:
                agent = AGENTS[speaker]
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
                        "mode": "group_discussion",
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

        # Determine next phase
        if st.session_state.get("first_mode") == "group":
            st.session_state.current_phase = "case"
        else:
            st.session_state.current_phase = "results"

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
                st.session_state.current_phase = data.get("next_phase", "results")

                st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to end session: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
