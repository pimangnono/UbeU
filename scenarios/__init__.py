"""
V3 Scenarios Module: Case studies and group scenarios.

Case Studies: Business cases with gated data for Mode 1
Group Scenarios: Behavioral situations for Mode 2
"""

from config.case_studies import CASE_STUDIES, create_case_study
from config.group_scenarios import GROUP_SCENARIOS, create_scenario

__all__ = [
    "CASE_STUDIES",
    "create_case_study",
    "GROUP_SCENARIOS",
    "create_scenario",
]
