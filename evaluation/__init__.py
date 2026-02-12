"""
V3 Evaluation Module: Post-session assessment for both interview modes.

- LogicEvaluator: 3-pass citation-based evaluation for Mode 1
- TraitEvaluator: Evidence-based personality inference for Mode 2
"""

from evaluation.logic_evaluator import LogicEvaluator
from evaluation.trait_evaluator import TraitEvaluator

__all__ = ["LogicEvaluator", "TraitEvaluator"]
