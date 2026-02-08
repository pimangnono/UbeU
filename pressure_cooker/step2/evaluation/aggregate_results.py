#!/usr/bin/env python3
"""
Aggregate Results: Cross-participant analysis for Step 2 Live Interviews.

Loads all participant folders and produces:
  1. Summary CSV (one row per participant — BFI-44, session stats, assessment, survey)
  2. Conversation export CSV (all turns from all sessions for qualitative review)
  3. Markdown report with descriptive statistics, distributions, and insights
  4. Optional JSON dump of all aggregated data

Usage:
    python step2/evaluation/aggregate_results.py
    python step2/evaluation/aggregate_results.py --output-dir outputs/step2/analysis
    python step2/evaluation/aggregate_results.py --csv-only
"""

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


TRAITS = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
FACET_IDS = [
    # Openness
    "O_ideas", "O_fantasy", "O_aesthetics", "O_conventionality", "O_practicality", "O_narrow_focus",
    # Conscientiousness
    "C_order", "C_dutifulness", "C_achievement", "C_flexibility", "C_casualness", "C_disorganization",
    # Extraversion
    "E_assertiveness", "E_gregariousness", "E_positive_emotions", "E_reserve", "E_independence", "E_brevity",
    # Agreeableness
    "A_trust", "A_altruism", "A_compliance", "A_skepticism", "A_competitiveness",
    # Neuroticism
    "N_anxiety", "N_anger", "N_self_consciousness", "N_calm", "N_resilience",
]
ASSESSMENT_KEYS = [
    "collaboration_score", "leadership_score", "stress_management_score",
    "communication_score", "problem_solving_score",
]
SURVEY_ITEMS = ["naturalness", "authenticity", "realism", "engagement", "recommendation"]
INTENT_TYPES = [
    "assertive", "cooperative", "avoidant", "aggressive", "anxious",
    "analytical", "creative", "empathetic", "defensive", "neutral",
]


def load_all_participants(participants_dir: Path) -> list[dict]:
    """Load all participant data (record + session_output + validation + facet_assessment)."""
    participants = []
    for pid_dir in sorted(participants_dir.iterdir()):
        if not pid_dir.is_dir() or not pid_dir.name.startswith("P"):
            continue

        entry = {
            "pid": pid_dir.name,
            "has_record": False,
            "has_session": False,
            "has_validation": False,
            "has_facet_assessment": False,
        }

        # Load record
        record_path = pid_dir / "record.json"
        if record_path.exists():
            with open(record_path) as f:
                entry["record"] = json.load(f)
            entry["has_record"] = True

        # Load session output
        session_path = pid_dir / "session_output.json"
        if session_path.exists():
            with open(session_path) as f:
                entry["session"] = json.load(f)
            entry["has_session"] = True
            # Check for embedded facet_assessment
            if entry["session"].get("facet_assessment"):
                entry["facet_assessment"] = entry["session"]["facet_assessment"]
                entry["has_facet_assessment"] = True

        # Load logic validation
        validation_path = pid_dir / "logic_validation.json"
        if validation_path.exists():
            with open(validation_path) as f:
                entry["validation"] = json.load(f)
            entry["has_validation"] = True

        # Load standalone facet assessment if not embedded
        facet_path = pid_dir / "facet_assessment.json"
        if facet_path.exists() and not entry["has_facet_assessment"]:
            with open(facet_path) as f:
                entry["facet_assessment"] = json.load(f)
            entry["has_facet_assessment"] = True

        participants.append(entry)

    return participants


def load_ensemble_results(evaluation_dir: Path) -> dict:
    """Load ensemble aggregation results if available."""
    ensemble_data = {}

    for method in ["median", "mean", "weighted"]:
        ensemble_path = evaluation_dir / f"ensemble_{method}_results.json"
        if ensemble_path.exists():
            with open(ensemble_path) as f:
                ensemble_data[method] = json.load(f)

    return ensemble_data


def compute_stats(values: list[float]) -> dict:
    """Compute descriptive statistics for a list of numbers."""
    if not values:
        return {"n": 0, "mean": 0, "std": 0, "min": 0, "max": 0, "median": 0}
    values = sorted(values)
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n if n > 1 else 0
    std = variance ** 0.5
    median = values[n // 2] if n % 2 == 1 else (values[n // 2 - 1] + values[n // 2]) / 2
    return {
        "n": n,
        "mean": round(mean, 3),
        "std": round(std, 3),
        "min": round(min(values), 3),
        "max": round(max(values), 3),
        "median": round(median, 3),
    }


def build_summary_rows(participants: list[dict]) -> list[dict]:
    """Build one flat row per participant for CSV export."""
    rows = []
    for p in participants:
        row = {"participant_id": p["pid"]}

        rec = p.get("record", {})
        row["name"] = rec.get("name", "")
        row["consent"] = rec.get("consent_given", False)
        row["scenario"] = rec.get("assigned_scenario", "")
        row["created_at"] = rec.get("created_at", "")

        # BFI-44 scores
        bfi = rec.get("bfi44_scores") or {}
        for t in TRAITS:
            row[f"bfi_{t}"] = bfi.get(t, "")
        row["bfi_duration_sec"] = rec.get("bfi44_duration_seconds", "")

        # Session metadata
        sess = p.get("session", {})
        meta = sess.get("metadata", {})
        row["session_completed"] = p["has_session"]
        row["total_turns"] = meta.get("total_turns", "")
        row["duration_sec"] = meta.get("duration_seconds", "")
        row["model_used"] = meta.get("model_used", "")

        # Candidate turn count
        conv = sess.get("conversation", [])
        candidate_turns = [t for t in conv if t.get("speaker") == "candidate"]
        row["candidate_turns"] = len(candidate_turns)
        row["candidate_avg_words"] = ""
        if candidate_turns:
            word_counts = [len(t.get("content", "").split()) for t in candidate_turns]
            row["candidate_avg_words"] = round(sum(word_counts) / len(word_counts), 1)

        # Intent statistics
        intent_pct = sess.get("intent_statistics", {}).get("intent_percentages", {})
        row["dominant_intent"] = sess.get("intent_statistics", {}).get("dominant_intent", "")
        for intent in INTENT_TYPES:
            row[f"intent_{intent}_pct"] = round(intent_pct.get(intent, 0), 1)

        # Assessment scores
        assessment = sess.get("assessment_mapping", {})
        for key in ASSESSMENT_KEYS:
            row[key] = assessment.get(key, "")

        # Logic validation (supports multi-pass scoring)
        val = p.get("validation", {})
        row["analytical_depth"] = val.get("analytical_depth", "")
        row["recommendation_quality"] = val.get("recommendation_quality", "")
        row["num_logical_gaps"] = len(val.get("logical_gaps", []))
        row["num_assumptions"] = len(val.get("assumptions_made", []))
        scoring = val.get("scoring", {})
        row["validation_passes"] = scoring.get("num_passes", "")
        row["depth_scores"] = str(scoring.get("analytical_depth_scores", ""))
        row["rec_scores"] = str(scoring.get("recommendation_quality_scores", ""))
        row["depth_agreement"] = scoring.get("depth_agreement", "")
        row["rec_agreement"] = scoring.get("rec_agreement", "")

        # Facet assessment (28-facet BFI detection)
        facet = p.get("facet_assessment", {})
        row["has_facet_assessment"] = p.get("has_facet_assessment", False)
        facet_ocean = facet.get("ocean_scores", {})
        facet_conf = facet.get("ocean_confidence", {})
        for t in TRAITS:
            row[f"facet_{t}"] = facet_ocean.get(t, "")
            row[f"facet_{t}_conf"] = facet_conf.get(t, "")
        row["facet_evidence_count"] = facet.get("total_evidence_count", "")

        # Evidence-based personality inference (from turn analysis)
        evidence = sess.get("evidence_assessment", {})
        pi = evidence.get("personality_inference", {})
        pi_ocean = pi.get("ocean_scores", {}) if isinstance(pi, dict) else {}
        for t in TRAITS:
            row[f"evidence_{t}"] = pi_ocean.get(t, "")
        row["evidence_confidence"] = pi.get("confidence", "") if isinstance(pi, dict) else ""

        # Survey
        survey = rec.get("survey")
        if survey:
            for item in SURVEY_ITEMS:
                row[f"survey_{item}"] = survey.get(item, "")
            row["survey_mean"] = round(
                sum(survey.get(item, 0) for item in SURVEY_ITEMS) / len(SURVEY_ITEMS), 2
            )
            row["survey_feedback"] = survey.get("open_feedback", "")
        else:
            for item in SURVEY_ITEMS:
                row[f"survey_{item}"] = ""
            row["survey_mean"] = ""
            row["survey_feedback"] = ""

        rows.append(row)

    return rows


def build_conversation_rows(participants: list[dict]) -> list[dict]:
    """Build one row per conversation turn across all participants."""
    rows = []
    for p in participants:
        if not p["has_session"]:
            continue
        conv = p["session"].get("conversation", [])
        for turn in conv:
            rows.append({
                "participant_id": p["pid"],
                "turn_number": turn.get("turn_number", ""),
                "speaker": turn.get("speaker", ""),
                "speaker_name": turn.get("speaker_name", ""),
                "content": turn.get("content", ""),
                "intent": turn.get("intent", ""),
                "emotion": turn.get("emotion", ""),
                "tension_level": turn.get("tension_level", ""),
            })
    return rows


def generate_report(
    participants: list[dict],
    summary_rows: list[dict],
    ensemble_data: dict = None,
) -> str:
    """Generate a comprehensive markdown report."""
    lines = []
    lines.append("# Step 2 Aggregate Analysis Report")
    lines.append("")

    total = len(participants)
    completed = [p for p in participants if p["has_session"]]
    with_survey = [p for p in participants if p.get("record", {}).get("survey")]
    with_validation = [p for p in participants if p["has_validation"]]
    with_facet = [p for p in participants if p.get("has_facet_assessment")]

    lines.append("## 1. Overview")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total participants registered | {total} |")
    lines.append(f"| Completed sessions | {len(completed)} |")
    lines.append(f"| With post-session survey | {len(with_survey)} |")
    lines.append(f"| With logic validation | {len(with_validation)} |")
    lines.append(f"| With facet assessment | {len(with_facet)} |")
    if ensemble_data:
        lines.append(f"| With ensemble evaluation | {len(ensemble_data.get('median', {}))} |")
    lines.append("")

    # Scenario distribution
    scenarios = Counter(p.get("record", {}).get("assigned_scenario", "unknown") for p in participants)
    lines.append("**Scenario distribution:**")
    for scen, cnt in scenarios.most_common():
        lines.append(f"- {scen}: {cnt}")
    lines.append("")

    # Completion rate
    if total > 0:
        lines.append(f"**Completion rate**: {len(completed)}/{total} ({100*len(completed)/total:.0f}%)")
        lines.append("")

    # --- BFI-44 ---
    lines.append("---")
    lines.append("## 2. BFI-44 Ground Truth Distribution")
    lines.append("")

    bfi_data = {}
    for t in TRAITS:
        vals = []
        for p in participants:
            bfi = p.get("record", {}).get("bfi44_scores", {})
            if bfi and t in bfi:
                vals.append(bfi[t])
        bfi_data[t] = vals

    lines.append("| Trait | N | Mean | Std | Min | Max | Median |")
    lines.append("|-------|---|------|-----|-----|-----|--------|")
    for t in TRAITS:
        s = compute_stats(bfi_data[t])
        lines.append(f"| {t.capitalize()} | {s['n']} | {s['mean']:.3f} | {s['std']:.3f} | {s['min']:.3f} | {s['max']:.3f} | {s['median']:.3f} |")
    lines.append("")

    # --- Session Statistics ---
    lines.append("---")
    lines.append("## 3. Session Statistics (Completed Sessions Only)")
    lines.append("")

    durations = []
    turn_counts = []
    candidate_turn_counts = []
    candidate_word_counts = []

    for p in completed:
        meta = p["session"].get("metadata", {})
        if meta.get("duration_seconds"):
            durations.append(meta["duration_seconds"])
        if meta.get("total_turns"):
            turn_counts.append(meta["total_turns"])

        conv = p["session"].get("conversation", [])
        ct = [t for t in conv if t.get("speaker") == "candidate"]
        candidate_turn_counts.append(len(ct))
        for t in ct:
            candidate_word_counts.append(len(t.get("content", "").split()))

    stats_table = [
        ("Duration (seconds)", durations),
        ("Total turns", turn_counts),
        ("Candidate turns", candidate_turn_counts),
        ("Candidate words/turn", candidate_word_counts),
    ]

    lines.append("| Metric | N | Mean | Std | Min | Max | Median |")
    lines.append("|--------|---|------|-----|-----|-----|--------|")
    for label, vals in stats_table:
        s = compute_stats(vals)
        lines.append(f"| {label} | {s['n']} | {s['mean']:.1f} | {s['std']:.1f} | {s['min']:.1f} | {s['max']:.1f} | {s['median']:.1f} |")
    lines.append("")

    # --- Assessment Scores ---
    lines.append("---")
    lines.append("## 4. Assessment Scores")
    lines.append("")

    assessment_data = {k: [] for k in ASSESSMENT_KEYS}
    for p in completed:
        am = p["session"].get("assessment_mapping", {})
        for k in ASSESSMENT_KEYS:
            if k in am and am[k] is not None:
                assessment_data[k].append(am[k])

    lines.append("| Dimension | N | Mean | Std | Min | Max | Median |")
    lines.append("|-----------|---|------|-----|-----|-----|--------|")
    for k in ASSESSMENT_KEYS:
        label = k.replace("_score", "").replace("_", " ").title()
        s = compute_stats(assessment_data[k])
        lines.append(f"| {label} | {s['n']} | {s['mean']:.3f} | {s['std']:.3f} | {s['min']:.3f} | {s['max']:.3f} | {s['median']:.3f} |")
    lines.append("")

    # --- Intent Distribution ---
    lines.append("---")
    lines.append("## 5. Intent Distribution (Candidate Turns)")
    lines.append("")

    intent_totals = {intent: [] for intent in INTENT_TYPES}
    for p in completed:
        pcts = p["session"].get("intent_statistics", {}).get("intent_percentages", {})
        for intent in INTENT_TYPES:
            intent_totals[intent].append(pcts.get(intent, 0))

    lines.append("| Intent | Mean % | Std | Max % |")
    lines.append("|--------|--------|-----|-------|")
    for intent in sorted(INTENT_TYPES, key=lambda i: -(sum(intent_totals[i]) / max(len(intent_totals[i]), 1))):
        vals = intent_totals[intent]
        s = compute_stats(vals)
        lines.append(f"| {intent.capitalize()} | {s['mean']:.1f} | {s['std']:.1f} | {s['max']:.1f} |")
    lines.append("")

    # Dominant intent distribution
    dominant_intents = Counter()
    for p in completed:
        di = p["session"].get("intent_statistics", {}).get("dominant_intent", "")
        if di:
            dominant_intents[di] += 1

    if dominant_intents:
        lines.append("**Dominant intent distribution:**")
        for intent, cnt in dominant_intents.most_common():
            lines.append(f"- {intent}: {cnt} ({100*cnt/len(completed):.0f}%)")
        lines.append("")

    # --- Logic Validation ---
    lines.append("---")
    lines.append("## 6. Logic Validation (Senior Analyst — Multi-Pass)")
    lines.append("")

    if with_validation:
        depths = []
        rec_quals = []
        gap_counts = []
        assumption_counts = []
        depth_agreements = []
        rec_agreements = []
        pass_counts = []

        for p in with_validation:
            v = p["validation"]
            if "error" in v:
                continue
            if v.get("analytical_depth") is not None:
                depths.append(v["analytical_depth"])
            if v.get("recommendation_quality") is not None:
                rec_quals.append(v["recommendation_quality"])
            gap_counts.append(len(v.get("logical_gaps", [])))
            assumption_counts.append(len(v.get("assumptions_made", [])))

            scoring = v.get("scoring", {})
            if scoring.get("num_passes"):
                pass_counts.append(scoring["num_passes"])
            if scoring.get("depth_agreement") is not None:
                depth_agreements.append(scoring["depth_agreement"])
            if scoring.get("rec_agreement") is not None:
                rec_agreements.append(scoring["rec_agreement"])

        lines.append("### Aggregated Scores (median across passes)")
        lines.append("")
        lines.append("| Metric | N | Mean | Std | Min | Max | Median |")
        lines.append("|--------|---|------|-----|-----|-----|--------|")
        for label, vals in [
            ("Analytical Depth (1-5)", depths),
            ("Recommendation Quality (1-5)", rec_quals),
            ("Logical Gaps (count)", gap_counts),
            ("Assumptions Made (count)", assumption_counts),
        ]:
            s = compute_stats(vals)
            lines.append(f"| {label} | {s['n']} | {s['mean']:.1f} | {s['std']:.1f} | {s['min']:.1f} | {s['max']:.1f} | {s['median']:.1f} |")
        lines.append("")

        # Multi-pass agreement
        if depth_agreements:
            lines.append("### Scoring Consistency (inter-pass agreement)")
            lines.append("")
            avg_passes = sum(pass_counts) / len(pass_counts) if pass_counts else 0
            avg_depth_agr = sum(depth_agreements) / len(depth_agreements)
            avg_rec_agr = sum(rec_agreements) / len(rec_agreements) if rec_agreements else 0
            lines.append(f"- **Passes per participant**: {avg_passes:.0f}")
            lines.append(f"- **Depth score spread** (max-min across passes): mean={avg_depth_agr:.1f}")
            lines.append(f"- **Recommendation score spread** (max-min across passes): mean={avg_rec_agr:.1f}")
            lines.append(f"- Spread of 0 = perfect agreement, 1 = minor variance, 2+ = inconsistent")
            lines.append("")

            # Per-participant pass details
            lines.append("| PID | Depth Scores | Depth (median) | Rec Scores | Rec (median) |")
            lines.append("|-----|-------------|----------------|-----------|-------------|")
            for p in with_validation:
                v = p["validation"]
                if "error" in v:
                    continue
                sc = v.get("scoring", {})
                d_scores = sc.get("analytical_depth_scores", [v.get("analytical_depth", "?")])
                r_scores = sc.get("recommendation_quality_scores", [v.get("recommendation_quality", "?")])
                lines.append(
                    f"| {p['pid']} | {d_scores} | {v.get('analytical_depth', '-')} "
                    f"| {r_scores} | {v.get('recommendation_quality', '-')} |"
                )
            lines.append("")

        # Common logical gaps
        all_gaps = []
        for p in with_validation:
            v = p["validation"]
            if "error" not in v:
                all_gaps.extend(v.get("logical_gaps", []))
        if all_gaps:
            lines.append("### Sample Logical Gaps Identified")
            lines.append("")
            for gap in all_gaps[:5]:
                gap_text = gap[:150] + "..." if len(gap) > 150 else gap
                lines.append(f"- {gap_text}")
            if len(all_gaps) > 5:
                lines.append(f"- _...and {len(all_gaps) - 5} more_")
            lines.append("")
    else:
        lines.append("_No completed validations found._")
        lines.append("")

    # --- Survey Results ---
    lines.append("---")
    lines.append("## 7. Post-Session Survey")
    lines.append("")

    survey_data = {item: [] for item in SURVEY_ITEMS}
    feedbacks = []
    for p in participants:
        survey = p.get("record", {}).get("survey")
        if not survey:
            continue
        for item in SURVEY_ITEMS:
            val = survey.get(item)
            if val is not None:
                survey_data[item].append(val)
        fb = survey.get("open_feedback", "")
        if fb:
            feedbacks.append(f"**{p['pid']}**: {fb}")

    if any(survey_data[item] for item in SURVEY_ITEMS):
        lines.append("| Item | N | Mean | Std | Min | Max |")
        lines.append("|------|---|------|-----|-----|-----|")
        for item in SURVEY_ITEMS:
            s = compute_stats(survey_data[item])
            lines.append(f"| {item.capitalize()} | {s['n']} | {s['mean']:.2f} | {s['std']:.2f} | {s['min']:.0f} | {s['max']:.0f} |")
        lines.append("")

        # Overall mean
        all_means = []
        for p in participants:
            survey = p.get("record", {}).get("survey")
            if survey:
                m = sum(survey.get(item, 0) for item in SURVEY_ITEMS) / len(SURVEY_ITEMS)
                all_means.append(m)
        if all_means:
            s = compute_stats(all_means)
            lines.append(f"**Overall survey mean**: {s['mean']:.2f} (std={s['std']:.2f}, n={s['n']})")
            lines.append("")

        if feedbacks:
            lines.append("### Open Feedback")
            lines.append("")
            for fb in feedbacks:
                lines.append(f"- {fb}")
            lines.append("")
    else:
        lines.append("_No survey responses collected yet._")
        lines.append("")

    # --- Facet Assessment Summary ---
    lines.append("---")
    lines.append("## 8. Facet-Level Personality Assessment (28 BFI Facets)")
    lines.append("")

    with_facet = [p for p in participants if p.get("has_facet_assessment")]
    if with_facet:
        lines.append(f"**Participants with facet assessment**: {len(with_facet)}")
        lines.append("")

        # OCEAN scores from facets
        facet_ocean_data = {t: [] for t in TRAITS}
        facet_conf_data = {t: [] for t in TRAITS}
        evidence_counts = []

        for p in with_facet:
            fa = p.get("facet_assessment", {})
            ocean = fa.get("ocean_scores", {})
            conf = fa.get("ocean_confidence", {})
            for t in TRAITS:
                if t in ocean and ocean[t] is not None:
                    facet_ocean_data[t].append(ocean[t])
                if t in conf and conf[t] is not None:
                    facet_conf_data[t].append(conf[t])
            if fa.get("total_evidence_count"):
                evidence_counts.append(fa["total_evidence_count"])

        lines.append("### OCEAN Scores (Aggregated from 28 Facets)")
        lines.append("")
        lines.append("| Trait | N | Mean | Std | Min | Max | Avg Confidence |")
        lines.append("|-------|---|------|-----|-----|-----|----------------|")
        for t in TRAITS:
            s = compute_stats(facet_ocean_data[t])
            c = compute_stats(facet_conf_data[t])
            lines.append(f"| {t.capitalize()} | {s['n']} | {s['mean']:.3f} | {s['std']:.3f} | {s['min']:.3f} | {s['max']:.3f} | {c['mean']:.3f} |")
        lines.append("")

        # Evidence statistics
        if evidence_counts:
            ev_stats = compute_stats(evidence_counts)
            lines.append(f"**Evidence extraction**: mean={ev_stats['mean']:.1f} quotes/session (range: {ev_stats['min']:.0f}-{ev_stats['max']:.0f})")
            lines.append("")

        # Top detected facets across all participants
        facet_detections = Counter()
        for p in with_facet:
            fa = p.get("facet_assessment", {})
            for fid, fdata in fa.get("facet_scores", {}).items():
                if isinstance(fdata, dict) and fdata.get("score", 0) > 0:
                    facet_detections[fid] += 1

        if facet_detections:
            lines.append("### Most Frequently Detected Facets")
            lines.append("")
            lines.append("| Facet | Trait | Direction | Detected In |")
            lines.append("|-------|-------|-----------|-------------|")
            for fid, count in facet_detections.most_common(10):
                # Parse facet info from ID
                trait_prefix = fid.split("_")[0]
                trait_map = {"O": "Openness", "C": "Conscientiousness", "E": "Extraversion", "A": "Agreeableness", "N": "Neuroticism"}
                trait_name = trait_map.get(trait_prefix, trait_prefix)
                facet_name = fid.replace(trait_prefix + "_", "").replace("_", " ").title()
                # Determine direction based on facet
                low_facets = ["conventionality", "practicality", "narrow_focus", "flexibility", "casualness",
                             "disorganization", "reserve", "independence", "brevity", "skepticism",
                             "competitiveness", "calm", "resilience"]
                direction = "LOW" if any(lf in fid.lower() for lf in low_facets) else "HIGH"
                pct = 100 * count / len(with_facet)
                lines.append(f"| {facet_name} | {trait_name} | {direction} | {count}/{len(with_facet)} ({pct:.0f}%) |")
            lines.append("")
    else:
        lines.append("_No facet assessments found._")
        lines.append("")

    # --- Ensemble Evaluation Summary ---
    lines.append("---")
    lines.append("## 9. Multi-Judge Ensemble Evaluation")
    lines.append("")

    if ensemble_data and ensemble_data.get("median"):
        median_ensemble = ensemble_data["median"]
        lines.append(f"**Participants evaluated**: {len(median_ensemble)}")
        lines.append(f"**Aggregation methods available**: {', '.join(ensemble_data.keys())}")
        lines.append("")

        # Ensemble accuracy vs ground truth
        ensemble_accuracies = {t: [] for t in TRAITS}
        ensemble_accuracies["overall"] = []
        improvements = []
        confidences = []
        low_agreement_counts = Counter()

        for pid, result in median_ensemble.items():
            ea = result.get("ensemble_accuracy", {})
            for t in TRAITS:
                if t in ea:
                    ensemble_accuracies[t].append(ea[t])
            if "overall" in ea:
                ensemble_accuracies["overall"].append(ea["overall"])
            if result.get("improvement_over_best_judge") is not None:
                improvements.append(result["improvement_over_best_judge"])
            if result.get("overall_confidence") is not None:
                confidences.append(result["overall_confidence"])
            for trait in result.get("low_agreement_traits", []):
                low_agreement_counts[trait] += 1

        lines.append("### Ensemble Accuracy vs BFI-44 Ground Truth (Median Method)")
        lines.append("")
        lines.append("| Trait | N | Mean Accuracy | Std | Min | Max |")
        lines.append("|-------|---|---------------|-----|-----|-----|")
        for t in TRAITS + ["overall"]:
            s = compute_stats(ensemble_accuracies[t])
            label = t.capitalize() if t != "overall" else "**Overall**"
            lines.append(f"| {label} | {s['n']} | {s['mean']:.3f} | {s['std']:.3f} | {s['min']:.3f} | {s['max']:.3f} |")
        lines.append("")

        # Improvement and confidence
        if improvements:
            imp_stats = compute_stats(improvements)
            lines.append(f"**Improvement over best single judge**: mean={imp_stats['mean']:+.3f} (range: {imp_stats['min']:+.3f} to {imp_stats['max']:+.3f})")
        if confidences:
            conf_stats = compute_stats(confidences)
            lines.append(f"**Inter-judge agreement (confidence)**: mean={conf_stats['mean']:.3f} (range: {conf_stats['min']:.3f}-{conf_stats['max']:.3f})")
        lines.append("")

        # Low agreement traits
        if low_agreement_counts:
            lines.append("### Traits with Low Inter-Judge Agreement")
            lines.append("")
            lines.append("| Trait | Flagged In | % of Participants |")
            lines.append("|-------|------------|-------------------|")
            for trait, count in low_agreement_counts.most_common():
                pct = 100 * count / len(median_ensemble)
                lines.append(f"| {trait.capitalize()} | {count} | {pct:.0f}% |")
            lines.append("")
            lines.append("_Low agreement (std_dev > 0.15) indicates judges detected different signals for this trait._")
            lines.append("")
    else:
        lines.append("_No ensemble evaluation results found. Run `run_step2_evaluation.py` to generate._")
        lines.append("")

    # --- OCEAN Comparison Across Methods ---
    lines.append("---")
    lines.append("## 10. OCEAN Score Comparison Across Methods")
    lines.append("")

    # Build comparison data
    comparison_data = []
    for p in participants:
        if not p["has_session"]:
            continue

        pid = p["pid"]
        row = {"pid": pid}

        # BFI-44 ground truth
        bfi = p.get("record", {}).get("bfi44_scores", {})
        for t in TRAITS:
            row[f"bfi_{t}"] = bfi.get(t)

        # Evidence-based (turn analysis)
        evidence = p.get("session", {}).get("evidence_assessment", {})
        pi = evidence.get("personality_inference", {})
        pi_ocean = pi.get("ocean_scores", {}) if isinstance(pi, dict) else {}
        for t in TRAITS:
            row[f"evidence_{t}"] = pi_ocean.get(t)

        # Facet-based
        if p.get("has_facet_assessment"):
            facet_ocean = p.get("facet_assessment", {}).get("ocean_scores", {})
            for t in TRAITS:
                row[f"facet_{t}"] = facet_ocean.get(t)
        else:
            for t in TRAITS:
                row[f"facet_{t}"] = None

        # Ensemble (if available)
        if ensemble_data and ensemble_data.get("median"):
            ens_result = ensemble_data["median"].get(pid, {})
            ens_scores = ens_result.get("ensemble_scores", {})
            for t in TRAITS:
                row[f"ensemble_{t}"] = ens_scores.get(t)
        else:
            for t in TRAITS:
                row[f"ensemble_{t}"] = None

        comparison_data.append(row)

    if comparison_data:
        # Show method availability
        has_evidence = sum(1 for r in comparison_data if r.get("evidence_openness") is not None)
        has_facet = sum(1 for r in comparison_data if r.get("facet_openness") is not None)
        has_ensemble = sum(1 for r in comparison_data if r.get("ensemble_openness") is not None)

        lines.append(f"| Method | Participants with Data |")
        lines.append(f"|--------|------------------------|")
        lines.append(f"| BFI-44 Ground Truth | {sum(1 for r in comparison_data if r.get('bfi_openness') is not None)} |")
        lines.append(f"| Evidence-Based (Turn Analysis) | {has_evidence} |")
        lines.append(f"| Facet-Based (28 Facets) | {has_facet} |")
        lines.append(f"| Ensemble (3 Judges) | {has_ensemble} |")
        lines.append("")

        # Per-participant comparison table (first 10)
        lines.append("### Sample Comparison (First 10 Participants)")
        lines.append("")
        lines.append("| PID | Trait | BFI-44 | Evidence | Facet | Ensemble | Δ Facet | Δ Ensemble |")
        lines.append("|-----|-------|--------|----------|-------|----------|---------|------------|")

        for row in comparison_data[:10]:
            for t in TRAITS:
                bfi_val = row.get(f"bfi_{t}")
                ev_val = row.get(f"evidence_{t}")
                fa_val = row.get(f"facet_{t}")
                en_val = row.get(f"ensemble_{t}")

                bfi_str = f"{bfi_val:.2f}" if bfi_val is not None else "-"
                ev_str = f"{ev_val:.2f}" if ev_val is not None else "-"
                fa_str = f"{fa_val:.2f}" if fa_val is not None else "-"
                en_str = f"{en_val:.2f}" if en_val is not None else "-"

                # Calculate deltas vs ground truth
                delta_fa = f"{fa_val - bfi_val:+.2f}" if (fa_val is not None and bfi_val is not None) else "-"
                delta_en = f"{en_val - bfi_val:+.2f}" if (en_val is not None and bfi_val is not None) else "-"

                lines.append(f"| {row['pid']} | {t[:1].upper()} | {bfi_str} | {ev_str} | {fa_str} | {en_str} | {delta_fa} | {delta_en} |")
        lines.append("")

        # Method correlation summary
        lines.append("### Method Agreement Summary")
        lines.append("")
        lines.append("Mean absolute error vs BFI-44 ground truth:")
        lines.append("")

        for method, prefix in [("Evidence-Based", "evidence"), ("Facet-Based", "facet"), ("Ensemble", "ensemble")]:
            errors = {t: [] for t in TRAITS}
            for row in comparison_data:
                for t in TRAITS:
                    bfi_val = row.get(f"bfi_{t}")
                    method_val = row.get(f"{prefix}_{t}")
                    if bfi_val is not None and method_val is not None:
                        errors[t].append(abs(method_val - bfi_val))

            if any(errors[t] for t in TRAITS):
                all_errors = [e for t in TRAITS for e in errors[t]]
                overall_mae = sum(all_errors) / len(all_errors) if all_errors else 0
                overall_acc = 1 - overall_mae
                lines.append(f"- **{method}**: MAE={overall_mae:.3f}, Accuracy={overall_acc:.3f}")
        lines.append("")
    else:
        lines.append("_No data available for comparison._")
        lines.append("")

    # --- Per-Participant Summary Table ---
    lines.append("---")
    lines.append("## 11. Per-Participant Summary")
    lines.append("")
    lines.append("| PID | Name | Scenario | Completed | Turns | Duration | Depth | Rec. Quality | Survey Mean |")
    lines.append("|-----|------|----------|-----------|-------|----------|-------|-------------|-------------|")
    for p in participants:
        pid = p["pid"]
        rec = p.get("record", {})
        name = rec.get("name", "-")
        scenario = rec.get("assigned_scenario", "-")
        completed_str = "Yes" if p["has_session"] else "No"
        turns = "-"
        duration = "-"
        depth = "-"
        rec_q = "-"
        survey_mean = "-"

        if p["has_session"]:
            meta = p["session"].get("metadata", {})
            turns = str(meta.get("total_turns", "-"))
            dur = meta.get("duration_seconds")
            if dur:
                duration = f"{dur:.0f}s"

        if p["has_validation"]:
            v = p["validation"]
            if "error" not in v:
                depth = str(v.get("analytical_depth", "-"))
                rec_q = str(v.get("recommendation_quality", "-"))

        survey = rec.get("survey")
        if survey:
            m = sum(survey.get(item, 0) for item in SURVEY_ITEMS) / len(SURVEY_ITEMS)
            survey_mean = f"{m:.1f}"

        lines.append(f"| {pid} | {name} | {scenario} | {completed_str} | {turns} | {duration} | {depth} | {rec_q} | {survey_mean} |")
    lines.append("")

    return "\n".join(lines)


def write_csv(rows: list[dict], path: Path) -> None:
    """Write rows to CSV file."""
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate Step 2 results across all participants"
    )
    parser.add_argument(
        "--participants-dir",
        type=str,
        default="outputs/step2/participants",
        help="Participants data directory",
    )
    parser.add_argument(
        "--evaluation-dir",
        type=str,
        default="outputs/step2/evaluation",
        help="Evaluation results directory (for ensemble data)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs/step2/analysis",
        help="Directory for output files",
    )
    parser.add_argument("--csv-only", action="store_true", help="Only export CSVs, skip report")
    args = parser.parse_args()

    participants_dir = Path(args.participants_dir)
    evaluation_dir = Path(args.evaluation_dir)
    output_dir = Path(args.output_dir)

    if not participants_dir.is_absolute():
        participants_dir = Path(__file__).parent.parent.parent / participants_dir
    if not evaluation_dir.is_absolute():
        evaluation_dir = Path(__file__).parent.parent.parent / evaluation_dir
    if not output_dir.is_absolute():
        output_dir = Path(__file__).parent.parent.parent / output_dir

    output_dir.mkdir(parents=True, exist_ok=True)

    # Load all data
    print("Loading participant data...")
    participants = load_all_participants(participants_dir)
    total = len(participants)
    completed = sum(1 for p in participants if p["has_session"])
    with_facet = sum(1 for p in participants if p.get("has_facet_assessment"))
    print(f"  Found {total} participants, {completed} with completed sessions, {with_facet} with facet assessment")

    if not participants:
        print("No participants found.")
        return

    # Load ensemble results
    print("Loading ensemble evaluation results...")
    ensemble_data = load_ensemble_results(evaluation_dir)
    if ensemble_data:
        print(f"  Found ensemble results: {', '.join(ensemble_data.keys())}")
        for method, data in ensemble_data.items():
            print(f"    {method}: {len(data)} participants")
    else:
        print("  No ensemble results found (run run_step2_evaluation.py to generate)")

    # Build summary CSV
    print("Building summary CSV...")
    summary_rows = build_summary_rows(participants)
    summary_path = output_dir / "participant_summary.csv"
    write_csv(summary_rows, summary_path)
    print(f"  Written to: {summary_path}")

    # Build conversation CSV
    print("Building conversation CSV...")
    conv_rows = build_conversation_rows(participants)
    conv_path = output_dir / "all_conversations.csv"
    write_csv(conv_rows, conv_path)
    print(f"  Written to: {conv_path} ({len(conv_rows)} turns)")

    # Generate report
    if not args.csv_only:
        print("Generating report...")
        report = generate_report(participants, summary_rows, ensemble_data)
        report_path = output_dir / "aggregate_report.md"
        with open(report_path, "w") as f:
            f.write(report)
        print(f"  Written to: {report_path}")

    # JSON dump
    json_path = output_dir / "aggregate_data.json"
    print("Exporting JSON...")
    json_output = {
        "generated_at": str(__import__("datetime").datetime.now()),
        "total_participants": total,
        "completed_sessions": completed,
        "with_facet_assessment": with_facet,
        "with_ensemble_evaluation": len(ensemble_data.get("median", {})) if ensemble_data else 0,
        "participants": [
            {
                "pid": p["pid"],
                "has_session": p["has_session"],
                "has_validation": p["has_validation"],
                "has_facet_assessment": p.get("has_facet_assessment", False),
                "record": p.get("record"),
                "assessment": p.get("session", {}).get("assessment_mapping"),
                "intent_statistics": p.get("session", {}).get("intent_statistics"),
                "validation_summary": {
                    "analytical_depth": p.get("validation", {}).get("analytical_depth"),
                    "recommendation_quality": p.get("validation", {}).get("recommendation_quality"),
                    "num_gaps": len(p.get("validation", {}).get("logical_gaps", [])),
                } if p["has_validation"] else None,
                "facet_ocean_scores": p.get("facet_assessment", {}).get("ocean_scores") if p.get("has_facet_assessment") else None,
                "facet_confidence": p.get("facet_assessment", {}).get("ocean_confidence") if p.get("has_facet_assessment") else None,
                "ensemble_scores": ensemble_data.get("median", {}).get(p["pid"], {}).get("ensemble_scores") if ensemble_data else None,
                "ensemble_accuracy": ensemble_data.get("median", {}).get(p["pid"], {}).get("ensemble_accuracy") if ensemble_data else None,
            }
            for p in participants
        ],
    }
    with open(json_path, "w") as f:
        json.dump(json_output, f, indent=2, default=str)
    print(f"  Written to: {json_path}")

    print(f"\nDone. All outputs in: {output_dir}/")


if __name__ == "__main__":
    main()
