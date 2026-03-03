"""
V4 Agents Module: AI agents for group discussion platform.

GroupAgents - Alex, Jordan, Riley for group discussions
"""

from agents.base_agent import BaseAgent
from agents.group_agents import AlexAgent, JordanAgent, RileyAgent
from agents.trait_selector import TraitElicitationSelector

__all__ = [
    "BaseAgent",
    "AlexAgent",
    "JordanAgent",
    "RileyAgent",
    "TraitElicitationSelector",
]
