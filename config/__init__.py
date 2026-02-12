"""
V3 Config Module: Configuration files for dual-mode interview platform.

- logic_rubric: 6-dimension rubric for Mode 1 case study evaluation
- group_scenarios: 4 behavioral scenarios for Mode 2 group discussions
- group_agent_profiles: Agent personality configurations
"""

from config.logic_rubric import LOGIC_RUBRIC, LogicDimension
from config.group_scenarios import GROUP_SCENARIOS, create_scenario
from config.case_studies import CASE_STUDIES, create_case_study

__all__ = [
    "LOGIC_RUBRIC",
    "LogicDimension",
    "GROUP_SCENARIOS",
    "create_scenario",
    "CASE_STUDIES",
    "create_case_study",
]
