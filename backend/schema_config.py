# schema_config.py
"""
Strict ontology for interview skill and personality trait extraction.
Defines CCS (Critical Core Skills) hierarchy and OCEAN traits.
"""

import json

# 1. Critical Core Skills (CCS) Hierarchy
# Based on SkillsFuture Singapore framework
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

# 2. OCEAN Personality Traits (Big Five)
OCEAN_TRAITS = [
    "Openness",
    "Conscientiousness", 
    "Extraversion",
    "Agreeableness",
    "Neuroticism"
]

# 3. Flatten skills for validation
ALL_SKILLS = []
for domain, skills in CCS_HIERARCHY.items():
    ALL_SKILLS.extend(skills)

# 4. Graphiti Prompt Configuration
GRAPH_INSTRUCTIONS = f"""
You are an expert Interview Assessor. Your goal is to extract structured data from the candidate's responses.

RULES:
1. Identify if the candidate demonstrates any of the following SKILLS: {json.dumps(CCS_HIERARCHY, indent=2)}
2. Identify if the candidate exhibits any of the following PERSONALITY TRAITS: {OCEAN_TRAITS}
3. **CRITICAL:** You must create an 'Evidence' node containing the exact quote from the candidate.
4. Do NOT create new Skill names. Map strictly to the provided lists.
5. Rate trait intensity as: Low, Moderate, or High based on the strength of evidence.
6. If unclear, do not force a classification. Skip ambiguous content.

OUTPUT FORMAT:
For each observation, return a JSON object with:
- skill: The skill name (from CCS_HIERARCHY) or null
- skill_domain: The parent domain of the skill or null  
- trait: The OCEAN trait or null
- trait_intensity: Low/Moderate/High or null
- evidence: The exact quote supporting this classification
"""

def get_skill_domain(skill_name: str) -> str | None:
    """Get the parent domain for a given skill."""
    for domain, skills in CCS_HIERARCHY.items():
        if skill_name in skills:
            return domain
    return None

def is_valid_skill(skill_name: str) -> bool:
    """Check if a skill name is in our ontology."""
    return skill_name in ALL_SKILLS

def is_valid_trait(trait_name: str) -> bool:
    """Check if a trait name is valid."""
    return trait_name in OCEAN_TRAITS
