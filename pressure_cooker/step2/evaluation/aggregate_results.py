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
from io import StringIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


TRAITS = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]
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
    """Load all participant data (record + session_output + validation)."""
    participants = []
    for pid_dir in sorted(participants_dir.iterdir()):
        if not pid_dir.is_dir() or not pid_dir.name.startswith("P"):
            continue

        entry = {"pid": pid_dir.name, "has_record": False, "has_session": False, "has_validation": False}

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

        # Load logic validation
        validation_path = pid_dir / "logic_validation.json"
        if validation_path.exists():
            with open(validation_path) as f:
                entry["validation"] = json.load(f)
            entry["has_validation"] = True

        participants.append(entry)

    return participants


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


def generate_report(participants: list[dict], summary_rows: list[dict]) -> str:
    """Generate a comprehensive markdown report."""
    lines = []
    lines.append("# Step 2 Aggregate Analysis Report")
    lines.append("")

    total = len(participants)
    completed = [p for p in participants if p["has_session"]]
    with_survey = [p for p in participants if p.get("record", {}).get("survey")]
    with_validation = [p for p in participants if p["has_validation"]]

    lines.append("## 1. Overview")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total participants registered | {total} |")
    lines.append(f"| Completed sessions | {len(completed)} |")
    lines.append(f"| With post-session survey | {len(with_survey)} |")
    lines.append(f"| With logic validation | {len(with_validation)} |")
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

    # --- Per-Participant Summary Table ---
    lines.append("---")
    lines.append("## 8. Per-Participant Summary")
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
        "--output-dir",
        type=str,
        default="outputs/step2/analysis",
        help="Directory for output files",
    )
    parser.add_argument("--csv-only", action="store_true", help="Only export CSVs, skip report")
    args = parser.parse_args()

    participants_dir = Path(args.participants_dir)
    output_dir = Path(args.output_dir)

    if not participants_dir.is_absolute():
        participants_dir = Path(__file__).parent.parent.parent / participants_dir
    if not output_dir.is_absolute():
        output_dir = Path(__file__).parent.parent.parent / output_dir

    output_dir.mkdir(parents=True, exist_ok=True)

    # Load all data
    print("Loading participant data...")
    participants = load_all_participants(participants_dir)
    total = len(participants)
    completed = sum(1 for p in participants if p["has_session"])
    print(f"  Found {total} participants, {completed} with completed sessions")

    if not participants:
        print("No participants found.")
        return

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
        report = generate_report(participants, summary_rows)
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
        "participants": [
            {
                "pid": p["pid"],
                "has_session": p["has_session"],
                "has_validation": p["has_validation"],
                "record": p.get("record"),
                "assessment": p.get("session", {}).get("assessment_mapping"),
                "intent_statistics": p.get("session", {}).get("intent_statistics"),
                "validation_summary": {
                    "analytical_depth": p.get("validation", {}).get("analytical_depth"),
                    "recommendation_quality": p.get("validation", {}).get("recommendation_quality"),
                    "num_gaps": len(p.get("validation", {}).get("logical_gaps", [])),
                } if p["has_validation"] else None,
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
