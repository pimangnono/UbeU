"""
Behavioral Fidelity Experiment (V4).

Automated experiment pipeline for evaluating personality-based behavioral fidelity
in group discussion simulations. Runs 164 sessions across 12 profiles, 4 scenarios,
with temporal decay analysis and statistical validation.
"""

from experiment.profiles import (
    EXPERIMENT_PROFILES,
    ExperimentProfile,
    build_baseline_a_prompt,
    build_baseline_b_prompt,
)
