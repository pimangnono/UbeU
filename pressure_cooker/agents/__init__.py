"""Agent module for Pressure Cooker framework."""

from agents.base_agent import BaseAgent
from agents.candidate_agent import CandidateAgent
from agents.colleague_agents import ProvokerAgent, MediatorAgent
from agents.system_manager import SystemManagerAgent

__all__ = [
    "BaseAgent",
    "CandidateAgent",
    "ProvokerAgent",
    "MediatorAgent",
    "SystemManagerAgent",
]
