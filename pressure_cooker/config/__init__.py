"""Configuration module for Pressure Cooker framework."""

from config.personality_profiles import (
    PERSONALITY_PROFILES,
    get_profile,
    get_all_profile_ids,
)
from config.scenarios import (
    SCENARIOS,
    get_scenario,
    get_all_scenario_ids,
)
from config.bfi_mappings import (
    get_behaviors_for_trait,
    get_relevant_behaviors,
    generate_behavioral_prompt_injection,
)

__all__ = [
    "PERSONALITY_PROFILES",
    "get_profile",
    "get_all_profile_ids",
    "SCENARIOS",
    "get_scenario",
    "get_all_scenario_ids",
    "get_behaviors_for_trait",
    "get_relevant_behaviors",
    "generate_behavioral_prompt_injection",
]
