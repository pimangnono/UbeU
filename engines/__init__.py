"""
V3 Engines Module: Dual-Mode Interview Platform

Mode 1: CaseEngine - 1-on-1 case study interview for logical assessment
Mode 2: GroupEngine - 1-to-many group discussion for personality assessment
"""

from engines.base_engine import BaseEngine
from engines.case_engine import CaseEngine
from engines.group_engine import GroupEngine

__all__ = ["BaseEngine", "CaseEngine", "GroupEngine"]
