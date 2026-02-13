"""
CCS (Critical Core Skills) schema for group discussion customization.
Based on SkillsFuture Singapore framework.
"""

# Critical Core Skills Hierarchy
CCS_HIERARCHY = {
    "Thinking Critically": [
        "Creative Thinking",
        "Decision Making",
        "Problem Solving",
        "Sense Making",
        "Transdisciplinary Thinking"
    ],
    "Interacting with Others": [
        "Building Inclusivity",
        "Collaboration",
        "Communication",
        "Customer Orientation",
        "Developing People",
        "Influence"
    ],
    "Staying Relevant": [
        "Adaptability",
        "Digital Fluency",
        "Global Perspective",
        "Learning Agility",
        "Self Management"
    ]
}

# OCEAN Personality Traits (Big Five)
OCEAN_TRAITS = {
    "O": {"name": "Openness", "description": "Curiosity, creativity, preference for novelty"},
    "C": {"name": "Conscientiousness", "description": "Organization, dependability, self-discipline"},
    "E": {"name": "Extraversion", "description": "Sociability, assertiveness, positive emotions"},
    "A": {"name": "Agreeableness", "description": "Cooperation, trust, empathy"},
    "N": {"name": "Neuroticism", "description": "Emotional instability, anxiety, moodiness"}
}

# Flatten skills for validation
ALL_SKILLS = []
for domain, skills in CCS_HIERARCHY.items():
    ALL_SKILLS.extend(skills)


def get_skill_domain(skill_name: str) -> str | None:
    """Get the parent domain for a given skill."""
    for domain, skills in CCS_HIERARCHY.items():
        if skill_name in skills:
            return domain
    return None


# Default agent configurations with CCS skill focus
DEFAULT_AGENT_CONFIGS = {
    "alex": {
        "name": "Alex",
        "role": "Team Lead",
        "avatar": ":material/fitness_center:",
        "color": "#EF4444",
        "personality": {"E": "high", "A": "low"},
        "focus_skills": ["Decision Making", "Influence", "Problem Solving"],
        "description": "Direct communicator, challenges ideas constructively"
    },
    "jordan": {
        "name": "Jordan",
        "role": "Product Manager",
        "avatar": ":material/handshake:",
        "color": "#22C55E",
        "personality": {"A": "high", "E": "high"},
        "focus_skills": ["Collaboration", "Communication", "Building Inclusivity"],
        "description": "Builds on others' ideas, seeks common ground"
    },
    "riley": {
        "name": "Riley",
        "role": "Senior Engineer",
        "avatar": ":material/psychology:",
        "color": "#3B82F6",
        "personality": {"E": "low", "A": "moderate"},
        "focus_skills": ["Sense Making", "Transdisciplinary Thinking", "Adaptability"],
        "description": "Thoughtful observer, raises important questions"
    }
}

# Scenario templates for different job roles
SCENARIO_TEMPLATES = {
    "product_team": {
        "title": "Resource Allocation Conflict",
        "brief": """Your team has been given 3 weeks to deliver a product update. However, you can only
realistically complete 2 out of 4 proposed features. The features are:

1. **Performance Optimization** - 30% speed improvement for existing users
2. **Mobile App** - New mobile version requested by enterprise clients
3. **AI Assistant** - Trendy feature that could attract new users
4. **Security Upgrade** - Address known vulnerabilities

As a team, you need to reach consensus on which 2 features to prioritize.""",
        "focus_skills": ["Decision Making", "Collaboration", "Communication"]
    },
    "leadership": {
        "title": "Team Restructuring",
        "brief": """Your department needs to reorganize due to budget constraints. You must decide:

1. **Option A** - Merge two teams, resulting in 2 redundancies
2. **Option B** - Cut project scope by 40%, keeping all staff
3. **Option C** - Outsource one team's work to contractors
4. **Option D** - Request additional budget (50% chance of approval)

Discuss and reach a consensus on the best approach.""",
        "focus_skills": ["Influence", "Developing People", "Problem Solving"]
    },
    "innovation": {
        "title": "New Market Entry",
        "brief": """Your company is considering entering a new market segment. The options are:

1. **Southeast Asia** - Large market, high competition, requires localization
2. **Europe** - Premium pricing possible, strict regulations (GDPR)
3. **Latin America** - Growing market, currency volatility risk
4. **Partnership** - Partner with local player vs. go alone

Evaluate the options and recommend a market entry strategy.""",
        "focus_skills": ["Creative Thinking", "Global Perspective", "Sense Making"]
    }
}
