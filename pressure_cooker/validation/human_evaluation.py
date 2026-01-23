"""
Human Evaluation Interface for Pressure Cooker Framework.
Provides CLI and data structures for human raters to evaluate
generated conversations.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from utils.models import (
    PersonalityVector,
    SessionOutput,
    ValidationResult,
    Turn,
    SpeakerRole,
)


class HumanEvaluation:
    """
    Data structure for human evaluation of a session.
    """

    def __init__(
        self,
        session_id: str,
        evaluator_id: str,
        ground_truth: PersonalityVector,
    ):
        self.session_id = session_id
        self.evaluator_id = evaluator_id
        self.ground_truth = ground_truth
        self.timestamp = datetime.now()

        # Ratings (to be filled by evaluator)
        self.inferred_openness: Optional[float] = None
        self.inferred_conscientiousness: Optional[float] = None
        self.inferred_extraversion: Optional[float] = None
        self.inferred_agreeableness: Optional[float] = None
        self.inferred_neuroticism: Optional[float] = None

        # Qualitative ratings
        self.naturalness_rating: Optional[int] = None  # 1-5
        self.consistency_rating: Optional[int] = None  # 1-5
        self.believability_rating: Optional[int] = None  # 1-5

        self.notes: str = ""

    def get_inferred_vector(self) -> Optional[PersonalityVector]:
        """Get inferred personality as vector, if all traits rated."""
        if all([
            self.inferred_openness is not None,
            self.inferred_conscientiousness is not None,
            self.inferred_extraversion is not None,
            self.inferred_agreeableness is not None,
            self.inferred_neuroticism is not None,
        ]):
            return PersonalityVector(
                openness=self.inferred_openness,
                conscientiousness=self.inferred_conscientiousness,
                extraversion=self.inferred_extraversion,
                agreeableness=self.inferred_agreeableness,
                neuroticism=self.inferred_neuroticism,
            )
        return None

    def to_validation_result(self) -> Optional[ValidationResult]:
        """Convert to ValidationResult if complete."""
        inferred = self.get_inferred_vector()
        if inferred is None:
            return None

        # Calculate accuracy
        traits = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
        accuracy_scores = {}

        for trait in traits:
            inferred_val = getattr(inferred, trait)
            truth_val = getattr(self.ground_truth, trait)
            accuracy_scores[trait] = round(1.0 - abs(inferred_val - truth_val), 3)

        accuracy_scores["overall"] = round(
            sum(accuracy_scores.values()) / len(traits), 3
        )

        return ValidationResult(
            session_id=self.session_id,
            validation_type="human_evaluation",
            inferred_profile=inferred,
            ground_truth_profile=self.ground_truth,
            accuracy_scores=accuracy_scores,
            overall_accuracy=accuracy_scores["overall"],
            notes=f"Evaluator: {self.evaluator_id}. {self.notes}",
        )

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            "session_id": self.session_id,
            "evaluator_id": self.evaluator_id,
            "timestamp": self.timestamp.isoformat(),
            "inferred_traits": {
                "openness": self.inferred_openness,
                "conscientiousness": self.inferred_conscientiousness,
                "extraversion": self.inferred_extraversion,
                "agreeableness": self.inferred_agreeableness,
                "neuroticism": self.inferred_neuroticism,
            },
            "qualitative_ratings": {
                "naturalness": self.naturalness_rating,
                "consistency": self.consistency_rating,
                "believability": self.believability_rating,
            },
            "notes": self.notes,
        }


def format_session_for_display(session: SessionOutput) -> str:
    """
    Format session for human reading.

    Args:
        session: Session to format.

    Returns:
        Formatted string for display.
    """
    lines = [
        "=" * 70,
        f"Session ID: {session.metadata.session_id}",
        f"Scenario: {session.scenario.name}",
        "=" * 70,
        "",
        "CONTEXT:",
        session.scenario.context,
        "",
        "-" * 70,
        "CONVERSATION:",
        "-" * 70,
        "",
    ]

    for turn in session.conversation:
        role_tag = ""
        if turn.speaker == SpeakerRole.CANDIDATE:
            role_tag = " [CANDIDATE - evaluate this person]"
        elif turn.speaker == SpeakerRole.PROVOKER:
            role_tag = " [challenges]"
        elif turn.speaker == SpeakerRole.MEDIATOR:
            role_tag = " [mediates]"
        elif turn.speaker == SpeakerRole.SYSTEM:
            role_tag = " [facilitator]"

        lines.append(f"{turn.speaker_name}{role_tag}:")
        lines.append(f"  {turn.content}")
        lines.append("")

    lines.extend([
        "-" * 70,
        "END OF CONVERSATION",
        "-" * 70,
    ])

    return "\n".join(lines)


def run_cli_evaluation(session: SessionOutput, evaluator_id: str) -> HumanEvaluation:
    """
    Run interactive CLI evaluation.

    Args:
        session: Session to evaluate.
        evaluator_id: Identifier for the human evaluator.

    Returns:
        Completed HumanEvaluation.
    """
    evaluation = HumanEvaluation(
        session_id=session.metadata.session_id,
        evaluator_id=evaluator_id,
        ground_truth=session.profile.vector,
    )

    # Display conversation
    print(format_session_for_display(session))

    print("\n" + "=" * 70)
    print("EVALUATION")
    print("=" * 70)
    print("\nBased on the CANDIDATE's responses, rate their personality traits.")
    print("Use a scale from 0.0 (very low) to 1.0 (very high).\n")

    # Get trait ratings
    traits = [
        ("openness", "Openness (curiosity, creativity, openness to new ideas)"),
        ("conscientiousness", "Conscientiousness (organization, dependability, discipline)"),
        ("extraversion", "Extraversion (sociability, assertiveness, energy)"),
        ("agreeableness", "Agreeableness (cooperation, trust, empathy)"),
        ("neuroticism", "Neuroticism (anxiety, emotional reactivity, moodiness)"),
    ]

    for trait_key, trait_desc in traits:
        while True:
            try:
                rating = float(input(f"{trait_desc}: "))
                if 0.0 <= rating <= 1.0:
                    setattr(evaluation, f"inferred_{trait_key}", rating)
                    break
                else:
                    print("Please enter a value between 0.0 and 1.0")
            except ValueError:
                print("Please enter a valid number")

    # Get qualitative ratings
    print("\nNow rate the quality of the conversation (1-5 scale):\n")

    qualitative = [
        ("naturalness_rating", "Naturalness (how natural did the candidate's responses feel?)"),
        ("consistency_rating", "Consistency (how consistent was the personality throughout?)"),
        ("believability_rating", "Believability (how believable was this as a real conversation?)"),
    ]

    for attr, desc in qualitative:
        while True:
            try:
                rating = int(input(f"{desc} [1-5]: "))
                if 1 <= rating <= 5:
                    setattr(evaluation, attr, rating)
                    break
                else:
                    print("Please enter a value between 1 and 5")
            except ValueError:
                print("Please enter a valid integer")

    # Get notes
    evaluation.notes = input("\nAny additional notes (optional): ").strip()

    return evaluation


def save_evaluation(evaluation: HumanEvaluation, output_dir: str = "outputs/validation") -> str:
    """
    Save evaluation to file.

    Args:
        evaluation: Evaluation to save.
        output_dir: Directory to save to.

    Returns:
        Path to saved file.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    filename = f"human_eval_{evaluation.session_id}_{evaluation.evaluator_id}.json"
    filepath = output_path / filename

    with open(filepath, "w") as f:
        json.dump(evaluation.to_dict(), f, indent=2)

    return str(filepath)


def load_evaluation(filepath: str) -> HumanEvaluation:
    """
    Load evaluation from file.

    Args:
        filepath: Path to evaluation file.

    Returns:
        HumanEvaluation object.
    """
    with open(filepath) as f:
        data = json.load(f)

    evaluation = HumanEvaluation(
        session_id=data["session_id"],
        evaluator_id=data["evaluator_id"],
        ground_truth=PersonalityVector(
            openness=0.5, conscientiousness=0.5, extraversion=0.5,
            agreeableness=0.5, neuroticism=0.5,
        ),  # Will need to be set from session
    )

    traits = data.get("inferred_traits", {})
    evaluation.inferred_openness = traits.get("openness")
    evaluation.inferred_conscientiousness = traits.get("conscientiousness")
    evaluation.inferred_extraversion = traits.get("extraversion")
    evaluation.inferred_agreeableness = traits.get("agreeableness")
    evaluation.inferred_neuroticism = traits.get("neuroticism")

    qualitative = data.get("qualitative_ratings", {})
    evaluation.naturalness_rating = qualitative.get("naturalness")
    evaluation.consistency_rating = qualitative.get("consistency")
    evaluation.believability_rating = qualitative.get("believability")

    evaluation.notes = data.get("notes", "")

    return evaluation
