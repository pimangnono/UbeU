"""
V3 Agents Module: AI agents for dual-mode interview platform.

Mode 1: FacilitatorAgent - Data clerk for case study interviews
Mode 2: GroupAgents - Alex, Jordan, Riley for group discussions
"""

from agents.base_agent import BaseAgent
from agents.facilitator_agent import FacilitatorAgent
from agents.group_agents import AlexAgent, JordanAgent, RileyAgent
from agents.trait_selector import TraitElicitationSelector

__all__ = [
    "BaseAgent",
    "FacilitatorAgent",
    "AlexAgent",
    "JordanAgent",
    "RileyAgent",
    "TraitElicitationSelector",
]
