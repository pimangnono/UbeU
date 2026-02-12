"""
Logic Rubric: 6-Dimension × 5-Level Evaluation Framework for Mode 1.

Each dimension has explicit behavioral anchors at each level, enabling
consistent scoring across multiple evaluation passes.

Dimensions:
1. Problem Structuring - Decomposing ambiguous problems
2. Hypothesis-Driven Thinking - Forming and testing hypotheses
3. Quantitative Reasoning - Calculations and numerical interpretation
4. Data Synthesis - Connecting findings across categories
5. Recommendation Quality - Actionable, evidence-backed conclusions
6. Communication Clarity - Clear, structured expression

Based on management consulting case interview methodology (McKinsey, BCG, Bain).
"""

from dataclasses import dataclass
from enum import Enum


class LogicDimension(Enum):
    """The six dimensions of logical assessment."""
    PROBLEM_STRUCTURING = "problem_structuring"
    HYPOTHESIS_THINKING = "hypothesis_thinking"
    QUANTITATIVE_REASONING = "quantitative_reasoning"
    DATA_SYNTHESIS = "data_synthesis"
    RECOMMENDATION_QUALITY = "recommendation_quality"
    COMMUNICATION_CLARITY = "communication_clarity"


@dataclass
class RubricLevel:
    """A single level (1-5) in the rubric."""
    score: int
    name: str
    description: str
    evidence_signals: list[str]


@dataclass
class DimensionRubric:
    """Complete rubric for one dimension."""
    dimension: LogicDimension
    definition: str
    observable_behaviors: list[str]
    levels: dict[int, RubricLevel]


# =============================================================================
# PROBLEM STRUCTURING RUBRIC
# =============================================================================

PROBLEM_STRUCTURING = DimensionRubric(
    dimension=LogicDimension.PROBLEM_STRUCTURING,
    definition="Ability to decompose an ambiguous business problem into analyzable components",
    observable_behaviors=[
        "Uses frameworks (profitability tree, 4Ps, etc.)",
        "Identifies key dimensions",
        "Articulates hypotheses",
        "Maps the problem space before diving into data",
    ],
    levels={
        1: RubricLevel(
            score=1,
            name="No Structure",
            description="Dove into data requests or recommendations without any attempt to organize the problem. No framework or decomposition visible. Responses are reactive and scattered.",
            evidence_signals=[
                "Random data requests with no stated logic",
                "No 'let me break this down' type statements",
                "No hypothesis before requesting data",
                "Jumps between topics without connection",
            ],
        ),
        2: RubricLevel(
            score=2,
            name="Minimal Structure",
            description="Mentioned 1-2 dimensions but did not systematically decompose the problem. Partial awareness of structure without follow-through.",
            evidence_signals=[
                "Mentions one angle (e.g., 'let's look at costs') but doesn't map full space",
                "Some awareness of categories but incomplete coverage",
                "Structure mentioned but not followed",
            ],
        ),
        3: RubricLevel(
            score=3,
            name="Adequate Structure",
            description="Identified key dimensions of the problem and organized analysis around them, though with some gaps or inconsistency in execution.",
            evidence_signals=[
                "Names 2-3 key areas",
                "Requests data for most dimensions",
                "May skip some areas or lose track mid-session",
                "Framework present but not consistently applied",
            ],
        ),
        4: RubricLevel(
            score=4,
            name="Strong Structure",
            description="Used a clear, appropriate framework to decompose the problem. Systematically worked through each dimension and connected findings.",
            evidence_signals=[
                "Explicit framework statement early on",
                "Systematic data requests following the framework",
                "References back to framework during synthesis",
                "Covers all major dimensions",
            ],
        ),
        5: RubricLevel(
            score=5,
            name="Exceptional Structure",
            description="Demonstrated sophisticated problem decomposition using a well-chosen framework with customized dimensions. Adapted structure as new data revealed nuances.",
            evidence_signals=[
                "Custom framework beyond generic templates",
                "Dynamic restructuring based on data",
                "Clear prioritization of which dimensions matter most",
                "Explains why this structure fits this problem",
            ],
        ),
    },
)


# =============================================================================
# HYPOTHESIS-DRIVEN THINKING RUBRIC
# =============================================================================

HYPOTHESIS_THINKING = DimensionRubric(
    dimension=LogicDimension.HYPOTHESIS_THINKING,
    definition="Forms and tests hypotheses using data rather than exploring randomly",
    observable_behaviors=[
        "States explicit hypotheses before requesting data",
        "Updates beliefs based on evidence",
        "Tests hypotheses systematically",
        "Distinguishes confirmation from refutation",
    ],
    levels={
        1: RubricLevel(
            score=1,
            name="No Hypothesis",
            description="Pure data gathering with no stated hypotheses. Asked for information without explaining what it would prove or disprove.",
            evidence_signals=[
                "No 'I think...' or 'My hypothesis is...' statements",
                "Data requests without explanation of purpose",
                "No updating of beliefs when data arrives",
            ],
        ),
        2: RubricLevel(
            score=2,
            name="Implicit Hypothesis",
            description="Some implied direction but no explicit hypothesis formation. May have had a theory but never articulated it.",
            evidence_signals=[
                "Hints at an idea without stating it clearly",
                "Some focused data gathering suggesting hidden hypothesis",
                "Never explicitly states what they're testing",
            ],
        ),
        3: RubricLevel(
            score=3,
            name="Some Hypothesis",
            description="Stated at least one hypothesis and requested relevant data, but didn't consistently follow hypothesis-driven approach throughout.",
            evidence_signals=[
                "One or two explicit hypotheses stated",
                "Some data requests tied to hypotheses",
                "Inconsistent - sometimes hypothesis-driven, sometimes exploratory",
            ],
        ),
        4: RubricLevel(
            score=4,
            name="Strong Hypothesis-Driven",
            description="Consistently formed hypotheses and tested them with data. Updated beliefs when evidence contradicted initial thinking.",
            evidence_signals=[
                "Multiple hypotheses stated throughout",
                "Clear 'this data supports/contradicts my hypothesis' statements",
                "Willing to abandon hypotheses when disproven",
                "New hypotheses formed based on findings",
            ],
        ),
        5: RubricLevel(
            score=5,
            name="Exceptional Hypothesis",
            description="Sophisticated hypothesis testing with prioritization. Identified which hypotheses were most important to test first. Showed Bayesian updating.",
            evidence_signals=[
                "Prioritized hypotheses by importance/testability",
                "Explained expected outcomes before seeing data",
                "Quantified confidence levels",
                "Efficiently narrowed down possibilities",
            ],
        ),
    },
)


# =============================================================================
# QUANTITATIVE REASONING RUBRIC
# =============================================================================

QUANTITATIVE_REASONING = DimensionRubric(
    dimension=LogicDimension.QUANTITATIVE_REASONING,
    definition="Performs calculations, interprets numbers, draws quantitative conclusions",
    observable_behaviors=[
        "Mental math and estimation",
        "Back-of-envelope calculations",
        "Ratio and percentage interpretation",
        "Sanity checking numbers",
    ],
    levels={
        1: RubricLevel(
            score=1,
            name="Avoids Numbers",
            description="Made no attempt to engage with quantitative data. Ignored numbers or treated them superficially.",
            evidence_signals=[
                "No calculations attempted",
                "Numbers mentioned but not analyzed",
                "Qualitative interpretation only",
                "Obvious numerical insights missed",
            ],
        ),
        2: RubricLevel(
            score=2,
            name="Basic Numbers",
            description="Acknowledged numbers but made only simple observations. No calculations or deeper analysis.",
            evidence_signals=[
                "Noted 'this is high' or 'this is low' without context",
                "No comparisons or ratios computed",
                "Numbers restated without interpretation",
            ],
        ),
        3: RubricLevel(
            score=3,
            name="Some Calculation",
            description="Performed some basic calculations or comparisons. Showed ability to work with numbers but with some errors or missed opportunities.",
            evidence_signals=[
                "At least one calculation performed",
                "Basic ratios or percentages computed",
                "Some numerical comparisons made",
                "May have calculation errors",
            ],
        ),
        4: RubricLevel(
            score=4,
            name="Strong Quantitative",
            description="Performed accurate calculations and drew meaningful conclusions. Used numbers to support arguments effectively.",
            evidence_signals=[
                "Multiple accurate calculations",
                "Appropriate use of percentages, growth rates, margins",
                "Numbers connected to business implications",
                "Sanity-checked results",
            ],
        ),
        5: RubricLevel(
            score=5,
            name="Exceptional Quantitative",
            description="Sophisticated numerical analysis including estimation, sensitivity, and scenario building. Numbers drove the analysis.",
            evidence_signals=[
                "Back-of-envelope estimation when exact data unavailable",
                "Sensitivity analysis ('if X changes by Y%...')",
                "Scenario comparison with numbers",
                "Identified key numerical drivers",
            ],
        ),
    },
)


# =============================================================================
# DATA SYNTHESIS RUBRIC
# =============================================================================

DATA_SYNTHESIS = DimensionRubric(
    dimension=LogicDimension.DATA_SYNTHESIS,
    definition="Connects findings across multiple data categories into coherent insights",
    observable_behaviors=[
        "Cross-references data points",
        "Identifies patterns",
        "Explains causal relationships",
        "Builds a coherent narrative from disparate facts",
    ],
    levels={
        1: RubricLevel(
            score=1,
            name="No Synthesis",
            description="Treated each data category in isolation. Never connected findings or built a coherent picture.",
            evidence_signals=[
                "Each data point discussed separately",
                "No 'this connects to...' statements",
                "Conclusion doesn't integrate multiple sources",
            ],
        ),
        2: RubricLevel(
            score=2,
            name="Minimal Synthesis",
            description="Made one or two connections between data points but missed obvious relationships.",
            evidence_signals=[
                "One connection made explicitly",
                "Most data discussed in isolation",
                "Obvious patterns not identified",
            ],
        ),
        3: RubricLevel(
            score=3,
            name="Some Synthesis",
            description="Connected multiple data points and identified some patterns, but synthesis was incomplete or surface-level.",
            evidence_signals=[
                "Multiple connections made",
                "Some pattern identification",
                "Synthesis present but could go deeper",
                "Some insights left on the table",
            ],
        ),
        4: RubricLevel(
            score=4,
            name="Strong Synthesis",
            description="Effectively connected findings across categories. Built a coherent narrative explaining the situation.",
            evidence_signals=[
                "Clear connections between cost, revenue, market data",
                "Causal explanations ('because X, therefore Y')",
                "Coherent story emerges from data",
                "Most important insights captured",
            ],
        ),
        5: RubricLevel(
            score=5,
            name="Exceptional Synthesis",
            description="Sophisticated integration revealing insights not obvious from any single data source. Identified second-order effects.",
            evidence_signals=[
                "Novel insights from data combination",
                "Second-order effects identified",
                "Contradictions in data noted and resolved",
                "Synthesis drives to the 'so what'",
            ],
        ),
    },
)


# =============================================================================
# RECOMMENDATION QUALITY RUBRIC
# =============================================================================

RECOMMENDATION_QUALITY = DimensionRubric(
    dimension=LogicDimension.RECOMMENDATION_QUALITY,
    definition="Arrives at actionable, evidence-backed recommendations with risk awareness",
    observable_behaviors=[
        "Specific action items proposed",
        "Supporting data cited",
        "Risks and trade-offs acknowledged",
        "Implementation considerations mentioned",
    ],
    levels={
        1: RubricLevel(
            score=1,
            name="No Recommendation",
            description="Failed to provide a clear recommendation or provided one completely disconnected from the analysis.",
            evidence_signals=[
                "No clear 'I recommend...' statement",
                "Recommendation contradicts own analysis",
                "Generic advice without specificity",
            ],
        ),
        2: RubricLevel(
            score=2,
            name="Weak Recommendation",
            description="Provided a recommendation but it was vague, unsupported, or missed key considerations.",
            evidence_signals=[
                "Recommendation stated but not specific",
                "Little connection to data analyzed",
                "No risks or trade-offs mentioned",
            ],
        ),
        3: RubricLevel(
            score=3,
            name="Adequate Recommendation",
            description="Clear recommendation with some supporting evidence. Some awareness of risks but not comprehensive.",
            evidence_signals=[
                "Clear recommendation with reasoning",
                "Some data cited in support",
                "At least one risk or trade-off mentioned",
                "Could be more specific on implementation",
            ],
        ),
        4: RubricLevel(
            score=4,
            name="Strong Recommendation",
            description="Well-supported recommendation with clear evidence trail. Acknowledges major risks and considers implementation.",
            evidence_signals=[
                "Specific, actionable recommendation",
                "Clear 'because the data shows...' support",
                "Multiple risks acknowledged",
                "Some implementation guidance",
            ],
        ),
        5: RubricLevel(
            score=5,
            name="Exceptional Recommendation",
            description="Sophisticated recommendation with prioritized actions, contingencies, and implementation roadmap. Demonstrates business judgment.",
            evidence_signals=[
                "Prioritized recommendations (do this first, then...)",
                "Contingency plans ('if X happens, then...')",
                "Clear success metrics suggested",
                "Next steps and timeline outlined",
            ],
        ),
    },
)


# =============================================================================
# COMMUNICATION CLARITY RUBRIC
# =============================================================================

COMMUNICATION_CLARITY = DimensionRubric(
    dimension=LogicDimension.COMMUNICATION_CLARITY,
    definition="Expresses reasoning clearly and structured",
    observable_behaviors=[
        "Logical flow between points",
        "Signposting ('First...', 'Second...')",
        "Concise explanations",
        "Appropriate level of detail",
    ],
    levels={
        1: RubricLevel(
            score=1,
            name="Unclear",
            description="Difficult to follow reasoning. Responses were disorganized, verbose, or confusing.",
            evidence_signals=[
                "Jumbled sentence structure",
                "Unclear what point is being made",
                "Excessive tangents",
                "Contradictory statements",
            ],
        ),
        2: RubricLevel(
            score=2,
            name="Somewhat Unclear",
            description="Some clarity but frequent confusion. Had to re-read or ask for clarification to understand.",
            evidence_signals=[
                "Occasional clear points",
                "Often loses the thread",
                "Some organization but inconsistent",
            ],
        ),
        3: RubricLevel(
            score=3,
            name="Adequate Clarity",
            description="Generally clear communication with occasional lack of structure or conciseness.",
            evidence_signals=[
                "Points generally understandable",
                "Some signposting used",
                "Occasional verbose or unclear passages",
            ],
        ),
        4: RubricLevel(
            score=4,
            name="Clear",
            description="Well-organized communication with logical flow. Easy to follow the reasoning.",
            evidence_signals=[
                "Clear signposting throughout",
                "Logical progression of ideas",
                "Appropriate conciseness",
                "Easy to follow and summarize",
            ],
        ),
        5: RubricLevel(
            score=5,
            name="Exceptionally Clear",
            description="Polished, executive-level communication. Could present this analysis directly to a client.",
            evidence_signals=[
                "Perfect logical flow",
                "Right level of detail throughout",
                "Compelling narrative structure",
                "Would need no editing for presentation",
            ],
        ),
    },
)


# =============================================================================
# COMPLETE RUBRIC
# =============================================================================

LOGIC_RUBRIC = {
    LogicDimension.PROBLEM_STRUCTURING: PROBLEM_STRUCTURING,
    LogicDimension.HYPOTHESIS_THINKING: HYPOTHESIS_THINKING,
    LogicDimension.QUANTITATIVE_REASONING: QUANTITATIVE_REASONING,
    LogicDimension.DATA_SYNTHESIS: DATA_SYNTHESIS,
    LogicDimension.RECOMMENDATION_QUALITY: RECOMMENDATION_QUALITY,
    LogicDimension.COMMUNICATION_CLARITY: COMMUNICATION_CLARITY,
}


def get_rubric_for_dimension(dimension: LogicDimension) -> DimensionRubric:
    """Get the rubric for a specific dimension."""
    return LOGIC_RUBRIC[dimension]


def get_level_description(dimension: LogicDimension, score: int) -> str:
    """Get the description for a specific score level."""
    rubric = LOGIC_RUBRIC[dimension]
    level = rubric.levels.get(score)
    return level.description if level else ""


def get_evidence_signals(dimension: LogicDimension, score: int) -> list[str]:
    """Get the evidence signals for a specific score level."""
    rubric = LOGIC_RUBRIC[dimension]
    level = rubric.levels.get(score)
    return level.evidence_signals if level else []
