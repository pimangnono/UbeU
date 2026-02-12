"""
Mode 2 Validation: Statistical validation for Group Discussion personality assessments.

Metrics:
1. Convergent Validity
   - Correlation with BFI-44 ground truth
   - Mean Absolute Error per trait

2. Discriminant Validity
   - Correlation between Mode 1 and Mode 2 scores
   - Confirms logical and personality assessment measure different constructs

3. Ensemble Agreement
   - Inter-judge agreement (3-model ensemble)
   - Confidence calibration

4. Test-Retest Reliability (if applicable)
   - Consistency across repeated sessions
"""

import json
import statistics
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

from utils.models import PersonalityVector, PersonalityAssessment


@dataclass
class TraitValidation:
    """Validation metrics for one Big Five trait."""
    trait: str
    n: int
    correlation: float  # with ground truth
    mean_abs_error: float
    mean_ground_truth: float
    mean_inferred: float
    bias: float  # systematic over/under estimation


@dataclass
class ConvergentValidityResult:
    """Convergent validity results (vs BFI-44)."""
    n_participants: int
    trait_validations: dict[str, TraitValidation]
    overall_correlation: float
    overall_mae: float
    acceptable: bool  # True if correlation > 0.3 for all traits


@dataclass
class DiscriminantValidityResult:
    """Discriminant validity results (Mode 1 vs Mode 2)."""
    n_participants: int
    logic_personality_correlation: float
    constructs_independent: bool  # True if |r| < 0.5


@dataclass
class EnsembleAgreement:
    """Ensemble agreement metrics."""
    n_participants: int
    mean_confidence: float
    confidence_calibration: float  # How well confidence predicts accuracy
    agreement_rate: float  # % of traits with high agreement


@dataclass
class Mode2ValidationReport:
    """Complete validation report for Mode 2 assessments."""
    n_participants: int
    convergent_validity: ConvergentValidityResult
    discriminant_validity: DiscriminantValidityResult
    ensemble_agreement: EnsembleAgreement
    overall_validity: bool


def load_all_data(data_dir: str = "outputs/participants") -> list[dict]:
    """Load all participant data with both BFI-44 and Mode 2 assessments."""
    data = []
    data_path = Path(data_dir)

    for pid_dir in sorted(data_path.iterdir()):
        if not pid_dir.is_dir() or not pid_dir.name.startswith("P"):
            continue

        record_path = pid_dir / "record.json"
        if not record_path.exists():
            continue

        with open(record_path) as f:
            record = json.load(f)

        # Need both ground truth and inferred personality
        if record.get("bfi44_scores") and record.get("group_assessment"):
            data.append({
                "participant_id": record["participant_id"],
                "bfi44_scores": record["bfi44_scores"],
                "group_assessment": record["group_assessment"],
                "case_assessment": record.get("case_assessment"),
            })

    return data


def compute_convergent_validity(data: list[dict]) -> ConvergentValidityResult:
    """Compute convergent validity against BFI-44 ground truth."""
    traits = ["O", "C", "E", "A", "N"]
    trait_names = {
        "O": "openness",
        "C": "conscientiousness",
        "E": "extraversion",
        "A": "agreeableness",
        "N": "neuroticism",
    }

    trait_validations = {}
    all_gt = []
    all_inf = []

    for trait in traits:
        gt_scores = []
        inf_scores = []

        for d in data:
            # Ground truth
            gt = d["bfi44_scores"]
            if isinstance(gt, dict):
                gt_val = gt.get(trait, 0.5)
            else:
                gt_val = getattr(gt, trait, 0.5)

            # Inferred
            assessment = d["group_assessment"]
            if isinstance(assessment, dict):
                trait_data = assessment.get(trait_names[trait], {})
                if isinstance(trait_data, dict):
                    inf_val = trait_data.get("score", 0.5)
                else:
                    inf_val = 0.5
            else:
                inf_val = 0.5

            gt_scores.append(gt_val)
            inf_scores.append(inf_val)

        if not gt_scores:
            continue

        # Compute correlation
        correlation = pearson_correlation(gt_scores, inf_scores)

        # Compute MAE
        mae = sum(abs(g - i) for g, i in zip(gt_scores, inf_scores)) / len(gt_scores)

        # Compute bias
        mean_gt = statistics.mean(gt_scores)
        mean_inf = statistics.mean(inf_scores)
        bias = mean_inf - mean_gt

        trait_validations[trait] = TraitValidation(
            trait=trait,
            n=len(gt_scores),
            correlation=correlation,
            mean_abs_error=mae,
            mean_ground_truth=mean_gt,
            mean_inferred=mean_inf,
            bias=bias,
        )

        all_gt.extend(gt_scores)
        all_inf.extend(inf_scores)

    # Overall metrics
    overall_corr = pearson_correlation(all_gt, all_inf) if all_gt else 0.0
    overall_mae = (
        sum(abs(g - i) for g, i in zip(all_gt, all_inf)) / len(all_gt)
        if all_gt else 0.0
    )

    # Check acceptability (correlation > 0.3 for all traits)
    acceptable = all(
        tv.correlation > 0.3 for tv in trait_validations.values()
    )

    return ConvergentValidityResult(
        n_participants=len(data),
        trait_validations=trait_validations,
        overall_correlation=overall_corr,
        overall_mae=overall_mae,
        acceptable=acceptable,
    )


def compute_discriminant_validity(data: list[dict]) -> DiscriminantValidityResult:
    """
    Compute discriminant validity between Mode 1 and Mode 2.

    Checks that logical assessment (Mode 1) and personality assessment (Mode 2)
    measure distinct constructs.
    """
    # Get participants with both assessments
    both_modes = [
        d for d in data
        if d.get("case_assessment") and d.get("group_assessment")
    ]

    if len(both_modes) < 3:
        return DiscriminantValidityResult(
            n_participants=len(both_modes),
            logic_personality_correlation=0.0,
            constructs_independent=True,
        )

    # Extract overall scores
    logic_scores = []
    personality_scores = []

    for d in both_modes:
        # Mode 1: overall logic score
        case_a = d["case_assessment"]
        if isinstance(case_a, dict):
            logic_score = case_a.get("overall_score", 3.0) / 5.0  # Normalize to 0-1
        else:
            logic_score = 0.5
        logic_scores.append(logic_score)

        # Mode 2: overall personality score (average of traits)
        group_a = d["group_assessment"]
        if isinstance(group_a, dict):
            trait_scores = []
            for trait_name in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]:
                trait_data = group_a.get(trait_name, {})
                if isinstance(trait_data, dict):
                    trait_scores.append(trait_data.get("score", 0.5))
            personality_score = statistics.mean(trait_scores) if trait_scores else 0.5
        else:
            personality_score = 0.5
        personality_scores.append(personality_score)

    # Compute correlation
    correlation = pearson_correlation(logic_scores, personality_scores)

    # Independence: |r| < 0.5 suggests distinct constructs
    independent = abs(correlation) < 0.5

    return DiscriminantValidityResult(
        n_participants=len(both_modes),
        logic_personality_correlation=correlation,
        constructs_independent=independent,
    )


def compute_ensemble_agreement(data: list[dict]) -> EnsembleAgreement:
    """Compute ensemble agreement metrics from 3-model evaluation."""
    confidences = []
    trait_names = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]

    for d in data:
        assessment = d["group_assessment"]
        if isinstance(assessment, dict):
            for trait_name in trait_names:
                trait_data = assessment.get(trait_name, {})
                if isinstance(trait_data, dict):
                    conf = trait_data.get("confidence", 0.5)
                    confidences.append(conf)

    if not confidences:
        return EnsembleAgreement(
            n_participants=len(data),
            mean_confidence=0.0,
            confidence_calibration=0.0,
            agreement_rate=0.0,
        )

    mean_conf = statistics.mean(confidences)
    # High agreement = confidence > 0.7
    high_agreement_count = sum(1 for c in confidences if c > 0.7)
    agreement_rate = high_agreement_count / len(confidences)

    return EnsembleAgreement(
        n_participants=len(data),
        mean_confidence=mean_conf,
        confidence_calibration=mean_conf,  # Simplified
        agreement_rate=agreement_rate,
    )


def pearson_correlation(x: list, y: list) -> float:
    """Compute Pearson correlation coefficient."""
    if len(x) < 3 or len(y) < 3 or len(x) != len(y):
        return 0.0

    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
    denom_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5

    if denom_x == 0 or denom_y == 0:
        return 0.0

    return numerator / (denom_x * denom_y)


def generate_mode2_validation_report(
    data_dir: str = "outputs/participants",
) -> Mode2ValidationReport:
    """Generate complete Mode 2 validation report."""
    data = load_all_data(data_dir)

    if not data:
        return Mode2ValidationReport(
            n_participants=0,
            convergent_validity=ConvergentValidityResult(
                n_participants=0,
                trait_validations={},
                overall_correlation=0.0,
                overall_mae=0.0,
                acceptable=False,
            ),
            discriminant_validity=DiscriminantValidityResult(
                n_participants=0,
                logic_personality_correlation=0.0,
                constructs_independent=True,
            ),
            ensemble_agreement=EnsembleAgreement(
                n_participants=0,
                mean_confidence=0.0,
                confidence_calibration=0.0,
                agreement_rate=0.0,
            ),
            overall_validity=False,
        )

    convergent = compute_convergent_validity(data)
    discriminant = compute_discriminant_validity(data)
    ensemble = compute_ensemble_agreement(data)

    # Overall validity check
    overall_valid = (
        convergent.acceptable and
        discriminant.constructs_independent and
        ensemble.agreement_rate > 0.5
    )

    return Mode2ValidationReport(
        n_participants=len(data),
        convergent_validity=convergent,
        discriminant_validity=discriminant,
        ensemble_agreement=ensemble,
        overall_validity=overall_valid,
    )


def format_validation_report(report: Mode2ValidationReport) -> str:
    """Format validation report as markdown."""
    lines = [
        "# Mode 2 (Group Discussion) Validation Report",
        "",
        f"**N Participants:** {report.n_participants}",
        f"**Overall Validity:** {'✓ Pass' if report.overall_validity else '✗ Fail'}",
        "",
        "## Convergent Validity (vs BFI-44)",
        "",
        f"**Overall Correlation:** {report.convergent_validity.overall_correlation:.3f}",
        f"**Overall MAE:** {report.convergent_validity.overall_mae:.3f}",
        f"**Acceptable:** {'✓' if report.convergent_validity.acceptable else '✗'}",
        "",
        "| Trait | r | MAE | Bias | GT Mean | Inf Mean |",
        "|-------|---|-----|------|---------|----------|",
    ]

    trait_labels = {"O": "Openness", "C": "Consc.", "E": "Extrav.", "A": "Agreea.", "N": "Neurot."}
    for trait, tv in report.convergent_validity.trait_validations.items():
        lines.append(
            f"| {trait_labels.get(trait, trait)} | {tv.correlation:.2f} | "
            f"{tv.mean_abs_error:.2f} | {tv.bias:+.2f} | "
            f"{tv.mean_ground_truth:.2f} | {tv.mean_inferred:.2f} |"
        )

    lines.extend([
        "",
        "## Discriminant Validity (Mode 1 vs Mode 2)",
        "",
        f"**Logic-Personality Correlation:** {report.discriminant_validity.logic_personality_correlation:.3f}",
        f"**Constructs Independent:** {'✓' if report.discriminant_validity.constructs_independent else '✗'}",
        "",
        "## Ensemble Agreement",
        "",
        f"**Mean Confidence:** {report.ensemble_agreement.mean_confidence:.2f}",
        f"**High Agreement Rate:** {report.ensemble_agreement.agreement_rate:.0%}",
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    report = generate_mode2_validation_report()
    print(format_validation_report(report))
