"""
Aggregate Human Anchor Ratings.

Reads CSV of human ratings, computes inter-rater reliability (ICC),
and correlates with LLM and rule-based evaluations.

Expected CSV format:
session_key,O,C,E,A,N,rater_id,notes
"""

import csv
import json
import logging
from pathlib import Path
from typing import Optional

import numpy as np
from scipy import stats as scipy_stats

logger = logging.getLogger(__name__)

TRAITS = ["O", "C", "E", "A", "N"]


def load_human_ratings(csv_path: str) -> list[dict]:
    """Load human ratings from CSV file."""
    ratings = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            entry = {
                "session_key": row["session_key"],
                "rater_id": row.get("rater_id", "unknown"),
            }
            for trait in TRAITS:
                try:
                    entry[trait] = float(row[trait])
                except (ValueError, KeyError):
                    entry[trait] = None
            ratings.append(entry)
    return ratings


def compute_icc(ratings: list[dict]) -> dict:
    """
    Compute ICC(2,k) per trait across raters.

    Requires at least 2 raters per session.
    """
    results = {}

    for trait in TRAITS:
        # Group by session
        session_scores = {}
        for r in ratings:
            if r[trait] is not None:
                session_scores.setdefault(r["session_key"], []).append(r[trait])

        # Filter sessions with 2+ ratings
        multi_rated = {k: v for k, v in session_scores.items() if len(v) >= 2}

        if len(multi_rated) < 3:
            results[trait] = {"error": "insufficient multi-rater data"}
            continue

        try:
            import pingouin as pg
            import pandas as pd

            rows = []
            for session_key, scores in multi_rated.items():
                for i, score in enumerate(scores):
                    rows.append({
                        "targets": session_key,
                        "raters": f"rater_{i}",
                        "ratings": score,
                    })

            icc_df = pd.DataFrame(rows)
            icc_result = pg.intraclass_corr(
                data=icc_df,
                targets="targets",
                raters="raters",
                ratings="ratings",
            )
            icc2k = icc_result[icc_result["Type"] == "ICC2k"]
            if not icc2k.empty:
                results[trait] = {
                    "icc2k": round(float(icc2k["ICC"].values[0]), 4),
                    "ci95_low": round(float(icc2k["CI95%"].values[0][0]), 4),
                    "ci95_high": round(float(icc2k["CI95%"].values[0][1]), 4),
                    "n_sessions": len(multi_rated),
                }
            else:
                results[trait] = {"error": "ICC2k not computed"}
        except ImportError:
            results[trait] = {"error": "pingouin not installed"}
        except Exception as e:
            results[trait] = {"error": str(e)}

    return results


def triangulate(
    ratings: list[dict],
    results_dir: str,
) -> dict:
    """
    Correlate human mean ratings vs LLM inferred and rule-based scores.

    Returns per-trait Pearson r for:
    - human vs LLM
    - human vs rule-based
    """
    # Compute human mean per session
    session_means = {}
    for r in ratings:
        key = r["session_key"]
        for trait in TRAITS:
            if r[trait] is not None:
                session_means.setdefault(key, {}).setdefault(trait, []).append(r[trait])

    human_scores = {}
    for key, traits in session_means.items():
        human_scores[key] = {t: np.mean(scores) for t, scores in traits.items()}

    # Load LLM and rule-based scores
    results_path = Path(results_dir)
    llm_scores = {}
    rb_scores = {}

    for filepath in sorted(results_path.glob("session_*.json")):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue
        key = data.get("session_key")
        if key in human_scores:
            iv = data.get("inferred_vector") or {}
            rv = data.get("rule_based_vector") or {}
            llm_scores[key] = iv
            rb_scores[key] = rv

    results = {}
    for trait in TRAITS:
        human_vals = []
        llm_vals = []
        rb_vals = []

        for key in human_scores:
            h = human_scores[key].get(trait)
            l = llm_scores.get(key, {}).get(trait)
            r = rb_scores.get(key, {}).get(trait)
            if h is not None and l is not None:
                human_vals.append(h)
                llm_vals.append(l)
                if r is not None:
                    rb_vals.append(r)

        trait_result = {}

        if len(human_vals) >= 5:
            r_llm, p_llm = scipy_stats.pearsonr(human_vals, llm_vals)
            trait_result["human_vs_llm_r"] = round(r_llm, 4)
            trait_result["human_vs_llm_p"] = round(p_llm, 6)

        if len(rb_vals) >= 5:
            r_rb, p_rb = scipy_stats.pearsonr(human_vals[:len(rb_vals)], rb_vals)
            trait_result["human_vs_rb_r"] = round(r_rb, 4)
            trait_result["human_vs_rb_p"] = round(p_rb, 6)

        trait_result["n"] = len(human_vals)
        results[trait] = trait_result

    return results


def run_human_anchor_analysis(
    csv_path: str,
    results_dir: str,
    output_path: Optional[str] = None,
) -> dict:
    """
    Full human-anchor analysis pipeline.

    Args:
        csv_path: Path to human ratings CSV.
        results_dir: Directory with session JSONs.
        output_path: Optional path to save results JSON.

    Returns:
        Dict with ICC and triangulation results.
    """
    ratings = load_human_ratings(csv_path)
    print(f"Loaded {len(ratings)} human ratings")

    icc = compute_icc(ratings)
    print("ICC per trait:")
    for trait, data in icc.items():
        if "error" in data:
            print(f"  {trait}: {data['error']}")
        else:
            print(f"  {trait}: ICC(2,k) = {data['icc2k']} [{data['ci95_low']}, {data['ci95_high']}]")

    tri = triangulate(ratings, results_dir)
    print("\nTriangulation:")
    for trait, data in tri.items():
        r_llm = data.get("human_vs_llm_r", "N/A")
        r_rb = data.get("human_vs_rb_r", "N/A")
        print(f"  {trait}: Human vs LLM r={r_llm}, Human vs RB r={r_rb}, n={data.get('n', 0)}")

    result = {"icc": icc, "triangulation": tri}

    if output_path:
        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to {output_path}")

    return result
