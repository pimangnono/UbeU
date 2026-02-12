"""
Case Interview Page: Mode 1 - One-on-one case study interview with AI facilitator.
"""

import streamlit as st
import httpx
import time
from typing import Optional


API_BASE = "http://localhost:8000"

# Interview duration in seconds (15 minutes)
INTERVIEW_DURATION = 15 * 60

# Demo case for testing
DEMO_CASE = {
    "company_name": "TechFlow Solutions",
    "problem_statement": """TechFlow Solutions is an enterprise SaaS company that has seen its profit margins
decline by 15% over the past two years, despite revenue growth of 25%. The CEO has hired your
consulting team to understand why profitability is declining and to recommend actions to
improve the situation.""",
    "data_gates": {
        "revenue_breakdown": {
            "title": "Revenue Breakdown",
            "content": """
**Revenue by Segment (FY23):**
- Enterprise (500+ employees): $45M (45%) - Growth: +30%
- Mid-Market (50-500 employees): $35M (35%) - Growth: +25%
- SMB (<50 employees): $20M (20%) - Growth: +15%

**Revenue by Product:**
- Core Platform: $70M (70%) - Margin: 75%
- Add-on Modules: $20M (20%) - Margin: 85%
- Professional Services: $10M (10%) - Margin: 35%
"""
        },
        "cost_structure": {
            "title": "Cost Structure",
            "content": """
**Operating Expenses (FY23):**
- Cloud Infrastructure: $25M (25% of revenue) - Up from 18% two years ago
- Sales & Marketing: $30M (30% of revenue) - Up from 25%
- R&D: $20M (20% of revenue) - Stable
- G&A: $10M (10% of revenue) - Stable
- Customer Success: $8M (8% of revenue) - Up from 5%

**Key Drivers:**
- Cloud costs driven by 3x data usage per customer
- Sales costs driven by enterprise segment expansion
- Customer success expanded to reduce churn
"""
        },
        "customer_metrics": {
            "title": "Customer Metrics",
            "content": """
**Customer Acquisition & Retention:**
- Total Customers: 2,500 (up from 2,000)
- Enterprise: 150 customers, CAC: $50K, LTV: $400K
- Mid-Market: 500 customers, CAC: $15K, LTV: $90K
- SMB: 1,850 customers, CAC: $2K, LTV: $12K

**Churn Rates:**
- Enterprise: 5% annually (improved from 8%)
- Mid-Market: 12% annually (stable)
- SMB: 25% annually (worsened from 20%)
"""
        },
        "market_context": {
            "title": "Market Context",
            "content": """
**Competitive Landscape:**
- 3 major competitors, TechFlow is #2 by market share
- Enterprise segment highly competitive, heavy discounting
- Price pressure from new entrants in SMB segment

**Industry Trends:**
- Shift to usage-based pricing
- Increasing data security requirements
- AI feature expectations from customers
"""
        },
    }
}


def show_case_interview_page():
    """Display case study interview interface."""
    # Initialize session state
    if "case_session_id" not in st.session_state:
        st.session_state.case_session_id = None
    if "case_messages" not in st.session_state:
        st.session_state.case_messages = []
    if "case_start_time" not in st.session_state:
        st.session_state.case_start_time = None
    if "revealed_data" not in st.session_state:
        st.session_state.revealed_data = set()
    if "case_ended" not in st.session_state:
        st.session_state.case_ended = False

    # Start session if not started
    if st.session_state.case_session_id is None and not st.session_state.case_ended:
        start_case_session()
        return

    # Header with timer
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.header("Case Study Interview")
    with col2:
        if st.session_state.case_start_time:
            elapsed = int(time.time() - st.session_state.case_start_time)
            remaining = max(0, INTERVIEW_DURATION - elapsed)
            mins, secs = divmod(remaining, 60)

            if remaining < 300:  # Less than 5 minutes
                st.warning(f"Time: {mins}:{secs:02d}")
            else:
                st.info(f"Time: {mins}:{secs:02d}")
    with col3:
        if st.button("End Interview", type="secondary"):
            end_case_session()
            return

    st.markdown("---")

    # Layout: Chat on left, Data panel on right
    chat_col, data_col = st.columns([3, 2])

    with data_col:
        render_data_panel()

    with chat_col:
        render_chat_interface()


def start_case_session():
    """Initialize the case study session."""
    st.info("Starting case study session...")

    if st.session_state.get("demo_mode"):
        # Demo mode
        st.session_state.case_session_id = "demo_case_001"
        st.session_state.case_start_time = time.time()
        st.session_state.case_company = DEMO_CASE["company_name"]
        st.session_state.case_problem = DEMO_CASE["problem_statement"]
        st.session_state.case_data_gates = DEMO_CASE["data_gates"]

        # Opening message from facilitator
        st.session_state.case_messages = [{
            "role": "facilitator",
            "content": f"""Welcome to your case interview. Today we'll be analyzing {DEMO_CASE['company_name']}.

{DEMO_CASE['problem_statement']}

I have data available on revenue breakdown, cost structure, customer metrics, and market context.
What information would you like to start with, or would you prefer to share your initial thoughts on how to approach this problem?"""
        }]
        st.rerun()
    else:
        # Call API
        try:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    f"{API_BASE}/session/create",
                    json={
                        "participant_id": st.session_state.participant_id,
                        "mode": "case_study",
                    }
                )
                response.raise_for_status()
                data = response.json()

                st.session_state.case_session_id = data["session_id"]
                st.session_state.case_start_time = time.time()
                st.session_state.case_company = data.get("company_name", "Company")
                st.session_state.case_problem = data.get("problem_statement", "")

                # Convert opening messages
                st.session_state.case_messages = [
                    {"role": "facilitator", "content": msg["content"]}
                    for msg in data.get("opening_messages", [])
                ]
                st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to start session: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")


def render_chat_interface():
    """Render the main chat interface."""
    st.subheader("Conversation")

    # Chat container with scrolling
    chat_container = st.container()

    with chat_container:
        for msg in st.session_state.case_messages:
            if msg["role"] == "facilitator":
                with st.chat_message("assistant", avatar=":material/description:"):
                    st.markdown(msg["content"])
            else:
                with st.chat_message("user", avatar=":material/person:"):
                    st.markdown(msg["content"])

    # Input area
    if not st.session_state.case_ended:
        user_input = st.chat_input(
            "Type your response...",
            key="case_input"
        )

        if user_input:
            handle_user_message(user_input)


def handle_user_message(content: str):
    """Handle user message submission."""
    # Add user message
    st.session_state.case_messages.append({
        "role": "candidate",
        "content": content
    })

    if st.session_state.get("demo_mode"):
        # Demo mode: generate simple response
        response = generate_demo_facilitator_response(content)
        st.session_state.case_messages.append({
            "role": "facilitator",
            "content": response
        })
        st.rerun()
    else:
        # Call API
        try:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    f"{API_BASE}/session/{st.session_state.case_session_id}/message",
                    json={"content": content}
                )
                response.raise_for_status()
                data = response.json()

                # Add AI responses
                for turn in data.get("ai_turns", []):
                    st.session_state.case_messages.append({
                        "role": "facilitator",
                        "content": turn["content"]
                    })

                # Check if session should end
                if data.get("session_state") == "ended":
                    st.session_state.case_ended = True

                st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Message failed: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")


def generate_demo_facilitator_response(user_input: str) -> str:
    """Generate a demo facilitator response based on user input."""
    user_lower = user_input.lower()

    # Check for data requests
    if any(word in user_lower for word in ["revenue", "sales", "segment"]):
        if "revenue_breakdown" not in st.session_state.revealed_data:
            st.session_state.revealed_data.add("revenue_breakdown")
            return """I've provided the revenue breakdown data in the Data Panel on the right.

Looking at this information, you can see revenue by segment and by product line.
What observations do you make from this data? What additional information would help your analysis?"""

    if any(word in user_lower for word in ["cost", "expense", "spending", "margin"]):
        if "cost_structure" not in st.session_state.revealed_data:
            st.session_state.revealed_data.add("cost_structure")
            return """I've provided the cost structure data in the Data Panel.

You can see the breakdown of operating expenses and how they've changed over time.
How do these cost trends relate to what you've observed in the revenue data?"""

    if any(word in user_lower for word in ["customer", "churn", "retention", "cac", "ltv"]):
        if "customer_metrics" not in st.session_state.revealed_data:
            st.session_state.revealed_data.add("customer_metrics")
            return """I've provided customer metrics including acquisition costs, lifetime value, and churn rates.

These metrics vary significantly by segment. What patterns do you notice?
How might this inform your recommendations?"""

    if any(word in user_lower for word in ["market", "compet", "industry", "trend"]):
        if "market_context" not in st.session_state.revealed_data:
            st.session_state.revealed_data.add("market_context")
            return """I've added the market context information to the Data Panel.

Given this competitive landscape and these industry trends, how does this context
influence your thinking about TechFlow's strategic options?"""

    # Default response based on conversation stage
    if len(st.session_state.case_messages) < 6:
        return """I understand your point. What data would help you develop this thinking further?

Remember, I have information on:
- Revenue breakdown by segment and product
- Cost structure and trends
- Customer metrics (CAC, LTV, churn)
- Market and competitive context"""

    elif len(st.session_state.case_messages) < 12:
        return """That's helpful context. Given what you've analyzed so far, what hypotheses
are you forming about the root causes of the margin decline?

What would you need to validate or refute these hypotheses?"""

    else:
        return """We're approaching the end of our time. Based on your analysis, what are your
top 2-3 recommendations for TechFlow? Please be specific about expected impact and
implementation considerations."""


def render_data_panel():
    """Render the data panel showing revealed information."""
    st.subheader("Data Panel")

    if not st.session_state.revealed_data:
        st.info("""
        **No data revealed yet.**

        Ask the facilitator for specific data to analyze:
        - Revenue breakdown
        - Cost structure
        - Customer metrics
        - Market context
        """)
        return

    data_gates = st.session_state.get("case_data_gates", DEMO_CASE["data_gates"])

    for data_key in st.session_state.revealed_data:
        if data_key in data_gates:
            data = data_gates[data_key]
            with st.expander(f"**{data['title']}**", expanded=True):
                st.markdown(data["content"])


def end_case_session():
    """End the case study session and run evaluation."""
    st.session_state.case_ended = True

    if st.session_state.get("demo_mode"):
        # Demo mode: generate mock results
        st.session_state.case_assessment = {
            "overall_score": 3.8,
            "problem_structuring": {"score": 4, "evidence": ["Candidate explicitly structured the problem by revenue and cost drivers"]},
            "hypothesis_thinking": {"score": 4, "evidence": ["Formed clear hypotheses about cloud cost growth"]},
            "quantitative_reasoning": {"score": 3, "evidence": ["Basic calculations performed correctly"]},
            "data_synthesis": {"score": 4, "evidence": ["Connected customer metrics to cost trends"]},
            "recommendation_quality": {"score": 4, "evidence": ["Specific, actionable recommendations provided"]},
            "communication_clarity": {"score": 4, "evidence": ["Clear, well-organized responses throughout"]},
            "strengths": ["Strong problem structuring", "Good data synthesis"],
            "development_areas": ["Could go deeper on quantitative analysis"],
        }
        st.session_state.case_completed = True

        # Determine next phase
        if st.session_state.get("first_mode") == "case":
            st.session_state.current_phase = "group"
        else:
            st.session_state.current_phase = "results"

        st.rerun()
    else:
        # Call API
        try:
            with httpx.Client(timeout=120.0) as client:
                response = client.post(
                    f"{API_BASE}/session/{st.session_state.case_session_id}/end"
                )
                response.raise_for_status()
                data = response.json()

                st.session_state.case_assessment = data.get("summary", {})
                st.session_state.case_completed = True
                st.session_state.current_phase = data.get("next_phase", "results")

                st.rerun()

        except httpx.HTTPError as e:
            st.error(f"Failed to end session: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
