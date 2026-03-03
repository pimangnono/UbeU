"""
Statistical Analysis Pipeline for the Behavioral Fidelity Experiment.

Implements analysis for all three research questions:
- RQ1: Personality fidelity (correlation, MAE, comparison to baselines)
- RQ2: Consistency (ICC, within-profile SD)
- RQ3: Temporal decay (window comparisons, decay classification)
- Rule-based validation (feature-trait correlations)

Dependencies: pandas, numpy, scipy, pingouin
"""

import json
import logging
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
from scipy import stats as scipy_stats

logger = logging.getLogger(__name__)

TRAITS = ["O", "C", "E", "A", "N"]
TRAIT_NAMES = {
    "O": "Openness",
    "C": "Conscientiousness",
    "E": "Extraversion",
    "A": "Agreeableness",
    "N": "Neuroticism",
}

FEATURE_NAMES = [
    "avg_words_per_turn", "max_words_in_turn", "min_words_in_turn",
    "word_count_variance", "question_ratio", "exclamation_ratio",
    "hedge_count", "certainty_count", "first_person_ratio",
    "inclusive_pronoun_ratio", "disagreement_count", "acknowledgment_count",
    "idea_count", "name_mention_count", "conditional_ratio",
    "planning_count", "emotional_word_count", "positive_emotion_count",
    "turn_initiation_ratio", "avg_response_latency_rank",
    "unique_word_ratio", "long_sentence_ratio",
]


# =============================================================================
# DATA LOADING
# =============================================================================

def load_results(results_dir: str) -> pd.DataFrame:
    """
    Load all session results from JSON files into a DataFrame.

    Returns DataFrame with columns:
    - session_key, condition, profile_id, scenario_id, rep
    - assigned_O, assigned_C, assigned_E, assigned_A, assigned_N
    - inferred_O, inferred_C, inferred_E, inferred_A, inferred_N
    - overall_confidence
    - Behavioral stats columns
    """
    results_path = Path(results_dir)
    rows = []

    for filepath in sorted(results_path.glob("session_*.json")):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        row = {
            "session_key": data.get("session_key"),
            "condition": data.get("condition"),
            "profile_id": data.get("profile_id"),
            "profile_name": data.get("profile_name"),
            "scenario_id": data.get("scenario_id"),
            "rep": data.get("rep"),
            "overall_confidence": data.get("overall_confidence", 0.0),
        }

        # Assigned vector
        av = data.get("assigned_vector") or {}
        for trait in TRAITS:
            row[f"assigned_{trait}"] = av.get(trait)

        # Inferred vector
        iv = data.get("inferred_vector") or {}
        for trait in TRAITS:
            row[f"inferred_{trait}"] = iv.get(trait)

        # Rule-based vector
        rv = data.get("rule_based_vector") or {}
        for trait in TRAITS:
            row[f"rule_based_{trait}"] = rv.get(trait)

        # Per-model scores
        pms = data.get("per_model_scores") or {}
        row["_per_model_scores"] = pms

        # Behavioral features (all 22)
        feat = data.get("features") or {}
        for feat_name in FEATURE_NAMES:
            row[f"feat_{feat_name}"] = feat.get(feat_name, 0.0)

        # Behavioral stats (legacy)
        st = data.get("stats") or {}
        row["candidate_turns"] = st.get("candidate_turns", 0)
        row["candidate_word_count"] = st.get("candidate_word_count", 0)
        row["candidate_avg_words"] = st.get("candidate_avg_words_per_turn", 0.0)
        row["name_mentions"] = st.get("times_addressed_others_by_name", 0)
        row["questions_asked"] = st.get("times_asked_questions", 0)
        row["disagreements"] = st.get("times_expressed_disagreement", 0)
        row["acknowledgments"] = st.get("times_acknowledged_others", 0)
        row["new_ideas"] = st.get("times_proposed_new_ideas", 0)

        rows.append(row)

    df = pd.DataFrame(rows)
    logger.info(f"Loaded {len(df)} sessions from {results_dir}")
    return df


# =============================================================================
# RQ1: PERSONALITY FIDELITY
# =============================================================================

def rq1_analysis(df: pd.DataFrame) -> dict:
    """
    RQ1: Does the system produce behaviors matching assigned personality profiles?

    Metrics:
    - Pearson r per trait (assigned vs inferred)
    - MAE per trait
    - t-test vs Baseline A (Cohen's d, Levene's)
    - Fisher z-test vs Baseline B
    """
    main = df[df["condition"] == "main"].copy()
    baseline_a = df[df["condition"] == "baseline_a"].copy()
    baseline_b = df[df["condition"] == "baseline_b"].copy()

    results = {"per_trait": {}, "overall": {}}

    all_r = []
    all_mae = []

    for trait in TRAITS:
        assigned_col = f"assigned_{trait}"
        inferred_col = f"inferred_{trait}"

        # Filter valid rows
        valid = main.dropna(subset=[assigned_col, inferred_col])
        if len(valid) < 3:
            results["per_trait"][trait] = {"error": "insufficient data"}
            continue

        assigned = valid[assigned_col].values
        inferred = valid[inferred_col].values

        # Pearson correlation
        r, p_val = scipy_stats.pearsonr(assigned, inferred)
        all_r.append(r)

        # MAE
        mae = np.mean(np.abs(assigned - inferred))
        all_mae.append(mae)

        trait_result = {
            "pearson_r": round(r, 4),
            "p_value": round(p_val, 6),
            "mae": round(mae, 4),
            "n": len(valid),
        }

        # T-test vs Baseline A (do inferred scores differ from no-personality baseline?)
        if len(baseline_a) > 0:
            ba_inferred = baseline_a[inferred_col].dropna().values
            if len(ba_inferred) >= 2:
                # Compare MAE distributions
                main_errors = np.abs(assigned - inferred)
                # For baseline A, compute error vs the main profile's assigned values
                # This tests whether main condition produces closer matches
                t_stat, t_p = scipy_stats.ttest_ind(main_errors, ba_inferred, equal_var=False)

                # Cohen's d
                pooled_std = np.sqrt(
                    (np.var(main_errors) + np.var(ba_inferred)) / 2
                )
                cohens_d = (np.mean(main_errors) - np.mean(ba_inferred)) / pooled_std if pooled_std > 0 else 0

                # Levene's test for variance equality
                levene_stat, levene_p = scipy_stats.levene(main_errors, ba_inferred)

                trait_result["vs_baseline_a"] = {
                    "t_stat": round(t_stat, 4),
                    "t_p_value": round(t_p, 6),
                    "cohens_d": round(cohens_d, 4),
                    "levene_stat": round(levene_stat, 4),
                    "levene_p": round(levene_p, 6),
                }

        # Fisher z-test vs Baseline B
        if len(baseline_b) > 0:
            bb_valid = baseline_b.dropna(subset=[assigned_col, inferred_col])
            if len(bb_valid) >= 3:
                bb_assigned = bb_valid[assigned_col].values
                bb_inferred = bb_valid[inferred_col].values
                r_bb, _ = scipy_stats.pearsonr(bb_assigned, bb_inferred)

                # Fisher z-transform
                z_main = np.arctanh(np.clip(r, -0.999, 0.999))
                z_bb = np.arctanh(np.clip(r_bb, -0.999, 0.999))
                se = np.sqrt(1 / (len(valid) - 3) + 1 / (len(bb_valid) - 3))
                z_diff = (z_main - z_bb) / se if se > 0 else 0
                fisher_p = 2 * (1 - scipy_stats.norm.cdf(abs(z_diff)))

                trait_result["vs_baseline_b"] = {
                    "r_baseline_b": round(r_bb, 4),
                    "fisher_z": round(z_diff, 4),
                    "fisher_p": round(fisher_p, 6),
                }

        results["per_trait"][trait] = trait_result

    # Overall metrics
    results["overall"] = {
        "mean_r": round(np.mean(all_r), 4) if all_r else None,
        "mean_mae": round(np.mean(all_mae), 4) if all_mae else None,
        "n_main": len(main),
        "n_baseline_a": len(baseline_a),
        "n_baseline_b": len(baseline_b),
    }

    return results


# =============================================================================
# RQ2: CONSISTENCY (ICC)
# =============================================================================

def rq2_analysis(df: pd.DataFrame) -> dict:
    """
    RQ2: Are personality assessments consistent across repeated sessions?

    Metrics:
    - ICC(3,k) per trait via pingouin
    - Within-profile SD per trait
    """
    main = df[df["condition"] == "main"].copy()
    results = {"per_trait": {}, "per_profile": {}}

    for trait in TRAITS:
        inferred_col = f"inferred_{trait}"
        valid = main.dropna(subset=[inferred_col])

        if len(valid) < 4:
            results["per_trait"][trait] = {"error": "insufficient data"}
            continue

        # ICC via pingouin
        try:
            import pingouin as pg

            icc_df = valid[["profile_id", "rep", inferred_col]].copy()
            icc_df.columns = ["targets", "raters", "ratings"]

            # Need at least 2 raters (reps) per target
            rep_counts = icc_df.groupby("targets")["raters"].nunique()
            multi_rep = rep_counts[rep_counts >= 2].index
            icc_df = icc_df[icc_df["targets"].isin(multi_rep)]

            if len(icc_df) >= 4:
                icc_result = pg.intraclass_corr(
                    data=icc_df,
                    targets="targets",
                    raters="raters",
                    ratings="ratings",
                )
                # ICC3k (two-way mixed, consistency, average measures)
                icc3k_row = icc_result[icc_result["Type"] == "ICC3k"]
                if not icc3k_row.empty:
                    icc_val = icc3k_row["ICC"].values[0]
                    ci_low = icc3k_row["CI95%"].values[0][0]
                    ci_high = icc3k_row["CI95%"].values[0][1]
                    results["per_trait"][trait] = {
                        "icc3k": round(icc_val, 4),
                        "ci95_low": round(ci_low, 4),
                        "ci95_high": round(ci_high, 4),
                    }
                else:
                    results["per_trait"][trait] = {"error": "ICC3k not computed"}
            else:
                results["per_trait"][trait] = {"error": "insufficient multi-rep data"}
        except ImportError:
            logger.warning("pingouin not installed, skipping ICC calculation")
            results["per_trait"][trait] = {"error": "pingouin not installed"}
        except Exception as e:
            results["per_trait"][trait] = {"error": str(e)}

        # Within-profile SD
        profile_sds = valid.groupby("profile_id")[inferred_col].std()
        if trait not in results["per_trait"] or "error" in results["per_trait"][trait]:
            results["per_trait"].setdefault(trait, {})
        results["per_trait"][trait]["mean_within_profile_sd"] = round(profile_sds.mean(), 4) if not profile_sds.empty else None

    # Per-profile consistency
    for profile_id in main["profile_id"].unique():
        profile_data = main[main["profile_id"] == profile_id]
        profile_result = {}
        for trait in TRAITS:
            col = f"inferred_{trait}"
            vals = profile_data[col].dropna()
            if len(vals) >= 2:
                profile_result[trait] = {
                    "mean": round(vals.mean(), 4),
                    "sd": round(vals.std(), 4),
                    "n": len(vals),
                }
        results["per_profile"][profile_id] = profile_result

    return results


# =============================================================================
# RQ3: TEMPORAL DECAY
# =============================================================================

def rq3_analysis(window_results: list[dict]) -> dict:
    """
    RQ3: Do personality signals decay across the session?

    Metrics:
    - Paired t-test W1 vs W3 per trait
    - Cohen's d
    - Delta-r (correlation change)
    - Decay classification per profile
    """
    if not window_results:
        return {"error": "no temporal data"}

    results = {"per_trait": {}, "decay_classification": []}

    # Build arrays per trait
    for trait in TRAITS:
        early_scores = []
        late_scores = []
        assigned_vals = []

        for session in window_results:
            av = session.get("assigned_vector") or {}
            assigned = av.get(trait)
            if assigned is None:
                continue

            windows = session.get("windows", {})
            early = windows.get("early", {})
            late = windows.get("late", {})

            early_vec = early.get("inferred_vector")
            late_vec = late.get("inferred_vector")

            if early_vec and late_vec:
                early_scores.append(early_vec.get(trait, 0.5))
                late_scores.append(late_vec.get(trait, 0.5))
                assigned_vals.append(assigned)

        if len(early_scores) < 3:
            results["per_trait"][trait] = {"error": "insufficient data"}
            continue

        early_arr = np.array(early_scores)
        late_arr = np.array(late_scores)
        assigned_arr = np.array(assigned_vals)

        # Paired t-test (early vs late absolute errors)
        early_errors = np.abs(assigned_arr - early_arr)
        late_errors = np.abs(assigned_arr - late_arr)
        t_stat, t_p = scipy_stats.ttest_rel(early_errors, late_errors)

        # Cohen's d for paired samples
        diff = early_errors - late_errors
        cohens_d = np.mean(diff) / np.std(diff, ddof=1) if np.std(diff, ddof=1) > 0 else 0

        # Delta-r (correlation with assigned: early vs late)
        r_early, _ = scipy_stats.pearsonr(assigned_arr, early_arr) if len(assigned_arr) >= 3 else (0, 1)
        r_late, _ = scipy_stats.pearsonr(assigned_arr, late_arr) if len(assigned_arr) >= 3 else (0, 1)
        delta_r = r_early - r_late

        results["per_trait"][trait] = {
            "t_stat": round(t_stat, 4),
            "t_p_value": round(t_p, 6),
            "cohens_d": round(cohens_d, 4),
            "r_early": round(r_early, 4),
            "r_late": round(r_late, 4),
            "delta_r": round(delta_r, 4),
            "mean_early_mae": round(np.mean(early_errors), 4),
            "mean_late_mae": round(np.mean(late_errors), 4),
            "n": len(early_scores),
        }

    # Decay classification per profile
    profile_decay = {}
    for session in window_results:
        pid = session.get("profile_id")
        if pid not in profile_decay:
            profile_decay[pid] = {"early_errors": [], "late_errors": []}

        av = session.get("assigned_vector") or {}
        windows = session.get("windows", {})
        early_vec = (windows.get("early") or {}).get("inferred_vector")
        late_vec = (windows.get("late") or {}).get("inferred_vector")

        if early_vec and late_vec:
            for trait in TRAITS:
                assigned = av.get(trait)
                if assigned is not None:
                    profile_decay[pid]["early_errors"].append(abs(assigned - early_vec.get(trait, 0.5)))
                    profile_decay[pid]["late_errors"].append(abs(assigned - late_vec.get(trait, 0.5)))

    for pid, errors in profile_decay.items():
        if errors["early_errors"] and errors["late_errors"]:
            mean_early = np.mean(errors["early_errors"])
            mean_late = np.mean(errors["late_errors"])
            if mean_late > mean_early * 1.2:
                classification = "significant_decay"
            elif mean_late > mean_early:
                classification = "mild_decay"
            elif mean_late < mean_early * 0.8:
                classification = "improvement"
            else:
                classification = "stable"

            results["decay_classification"].append({
                "profile_id": pid,
                "mean_early_mae": round(mean_early, 4),
                "mean_late_mae": round(mean_late, 4),
                "classification": classification,
            })

    return results


# =============================================================================
# RULE-BASED VALIDATION
# =============================================================================

def rule_based_validation(df: pd.DataFrame) -> dict:
    """
    Validate inferred traits against behavioral features.

    Expected correlations:
    - candidate_avg_words -> E (positive)
    - disagreements -> -A (negative)
    - acknowledgments -> A (positive)
    - new_ideas -> O (positive)
    - questions_asked -> E (positive)
    """
    main = df[df["condition"] == "main"].copy()

    if len(main) < 5:
        return {"error": "insufficient data"}

    validations = {}

    feature_trait_pairs = [
        ("candidate_avg_words", "inferred_E", "positive", "Words per turn -> Extraversion"),
        ("disagreements", "inferred_A", "negative", "Disagreements -> -Agreeableness"),
        ("acknowledgments", "inferred_A", "positive", "Acknowledgments -> Agreeableness"),
        ("new_ideas", "inferred_O", "positive", "New ideas -> Openness"),
        ("questions_asked", "inferred_E", "positive", "Questions asked -> Extraversion"),
        ("name_mentions", "inferred_E", "positive", "Name mentions -> Extraversion"),
    ]

    for feature, trait_col, expected_dir, description in feature_trait_pairs:
        if feature not in main.columns or trait_col not in main.columns:
            continue

        valid = main.dropna(subset=[feature, trait_col])
        if len(valid) < 5:
            validations[description] = {"error": "insufficient data"}
            continue

        r, p = scipy_stats.pearsonr(valid[feature], valid[trait_col])
        correct_direction = (expected_dir == "positive" and r > 0) or (expected_dir == "negative" and r < 0)

        validations[description] = {
            "pearson_r": round(r, 4),
            "p_value": round(p, 6),
            "expected_direction": expected_dir,
            "correct_direction": correct_direction,
            "n": len(valid),
        }

    return validations


# =============================================================================
# DUAL EVALUATION (LLM vs Rule-Based)
# =============================================================================

def dual_evaluation_comparison(df: pd.DataFrame) -> dict:
    """
    Compare LLM ensemble scores vs rule-based scores per trait.

    Computes Pearson r between the two evaluation methods. High agreement
    suggests validity; divergence identifies LLM-biased traits.
    """
    main = df[df["condition"] == "main"].copy()

    if len(main) < 5:
        return {"error": "insufficient data"}

    results = {}
    for trait in TRAITS:
        llm_col = f"inferred_{trait}"
        rb_col = f"rule_based_{trait}"

        valid = main.dropna(subset=[llm_col, rb_col])
        if len(valid) < 5:
            results[trait] = {"error": "insufficient data"}
            continue

        r, p = scipy_stats.pearsonr(valid[llm_col], valid[rb_col])

        # Also compare both against assigned
        assigned_col = f"assigned_{trait}"
        assigned_valid = valid.dropna(subset=[assigned_col])
        llm_vs_assigned = None
        rb_vs_assigned = None
        if len(assigned_valid) >= 5:
            r_llm, _ = scipy_stats.pearsonr(assigned_valid[assigned_col], assigned_valid[llm_col])
            r_rb, _ = scipy_stats.pearsonr(assigned_valid[assigned_col], assigned_valid[rb_col])
            llm_vs_assigned = round(r_llm, 4)
            rb_vs_assigned = round(r_rb, 4)

        results[trait] = {
            "llm_vs_rule_based_r": round(r, 4),
            "llm_vs_rule_based_p": round(p, 6),
            "llm_vs_assigned_r": llm_vs_assigned,
            "rule_based_vs_assigned_r": rb_vs_assigned,
            "n": len(valid),
        }

    return results


# =============================================================================
# EXPANDED FEATURE-TRAIT VALIDATION (22 features x 5 traits)
# =============================================================================

# Expected direction of each feature-trait correlation
FEATURE_TRAIT_EXPECTATIONS = {
    # (feature_col, trait_col, expected_direction, description)
    ("feat_avg_words_per_turn", "assigned_E", "positive", "Avg words -> E"),
    ("feat_max_words_in_turn", "assigned_E", "positive", "Max words -> E"),
    ("feat_word_count_variance", "assigned_O", "positive", "Word variance -> O"),
    ("feat_question_ratio", "assigned_E", "positive", "Question ratio -> E"),
    ("feat_exclamation_ratio", "assigned_E", "positive", "Exclamation ratio -> E"),
    ("feat_hedge_count", "assigned_N", "positive", "Hedges -> N"),
    ("feat_certainty_count", "assigned_E", "positive", "Certainty -> E"),
    ("feat_first_person_ratio", "assigned_N", "positive", "First-person -> N"),
    ("feat_inclusive_pronoun_ratio", "assigned_A", "positive", "Inclusive pronouns -> A"),
    ("feat_disagreement_count", "assigned_A", "negative", "Disagreements -> -A"),
    ("feat_acknowledgment_count", "assigned_A", "positive", "Acknowledgments -> A"),
    ("feat_idea_count", "assigned_O", "positive", "Ideas -> O"),
    ("feat_name_mention_count", "assigned_E", "positive", "Name mentions -> E"),
    ("feat_conditional_ratio", "assigned_C", "positive", "Conditionals -> C"),
    ("feat_planning_count", "assigned_C", "positive", "Planning -> C"),
    ("feat_emotional_word_count", "assigned_N", "positive", "Emotional words -> N"),
    ("feat_positive_emotion_count", "assigned_A", "positive", "Positive emotion -> A"),
    ("feat_turn_initiation_ratio", "assigned_E", "positive", "Turn initiation -> E"),
    ("feat_unique_word_ratio", "assigned_O", "positive", "Unique words -> O"),
    ("feat_long_sentence_ratio", "assigned_C", "positive", "Long sentences -> C"),
}


def expanded_feature_trait_validation(df: pd.DataFrame) -> dict:
    """
    Correlate all 22 features against assigned OCEAN values.

    Returns a dict of feature-trait pairs with correlation stats.
    """
    main = df[df["condition"] == "main"].copy()

    if len(main) < 5:
        return {"error": "insufficient data"}

    results = {}

    for feature_col, trait_col, expected_dir, description in FEATURE_TRAIT_EXPECTATIONS:
        if feature_col not in main.columns or trait_col not in main.columns:
            continue

        valid = main.dropna(subset=[feature_col, trait_col])
        if len(valid) < 5:
            results[description] = {"error": "insufficient data"}
            continue

        r, p = scipy_stats.pearsonr(valid[feature_col], valid[trait_col])
        correct = (expected_dir == "positive" and r > 0) or (expected_dir == "negative" and r < 0)

        results[description] = {
            "pearson_r": round(r, 4),
            "p_value": round(p, 6),
            "expected_direction": expected_dir,
            "correct_direction": correct,
            "n": len(valid),
        }

    # Also compute the full 22x5 correlation matrix
    feature_cols = [f"feat_{f}" for f in FEATURE_NAMES]
    trait_cols = [f"assigned_{t}" for t in TRAITS]

    existing_feat = [c for c in feature_cols if c in main.columns]
    existing_trait = [c for c in trait_cols if c in main.columns]

    if existing_feat and existing_trait:
        valid = main[existing_feat + existing_trait].dropna()
        if len(valid) >= 5:
            matrix = {}
            for fc in existing_feat:
                fname = fc.replace("feat_", "")
                matrix[fname] = {}
                for tc in existing_trait:
                    tname = tc.replace("assigned_", "")
                    r, p = scipy_stats.pearsonr(valid[fc], valid[tc])
                    matrix[fname][tname] = {"r": round(r, 4), "p": round(p, 6)}
            results["_correlation_matrix"] = matrix

    return results


# =============================================================================
# INTER-MODEL AGREEMENT
# =============================================================================

def inter_model_agreement(df: pd.DataFrame) -> dict:
    """
    Analyze agreement across the 3 ensemble models per trait.

    Computes per-trait variance across models. High variance = low agreement.
    Sessions with high inter-model variance are flagged as uncertain.
    """
    main = df[df["condition"] == "main"].copy()

    if len(main) < 3:
        return {"error": "insufficient data"}

    # Collect per-model scores from the stored dict
    trait_variances = {t: [] for t in TRAITS}
    uncertain_sessions = []

    for _, row in main.iterrows():
        pms = row.get("_per_model_scores")
        if not pms or not isinstance(pms, dict):
            continue

        # pms is {model_name: {trait: score}}
        session_variances = {}
        for trait in TRAITS:
            scores = []
            for model_name, model_scores in pms.items():
                if isinstance(model_scores, dict) and trait in model_scores:
                    scores.append(model_scores[trait])

            if len(scores) >= 2:
                var = np.var(scores)
                trait_variances[trait].append(var)
                session_variances[trait] = var

        # Flag sessions where any trait has high variance
        if session_variances:
            max_var = max(session_variances.values())
            if max_var > 0.04:  # threshold: stdev > 0.2
                uncertain_sessions.append({
                    "session_key": row.get("session_key"),
                    "max_variance": round(max_var, 4),
                    "trait_variances": {t: round(v, 4) for t, v in session_variances.items()},
                })

    results = {"per_trait": {}, "uncertain_sessions": uncertain_sessions[:20]}

    for trait in TRAITS:
        variances = trait_variances[trait]
        if variances:
            results["per_trait"][trait] = {
                "mean_variance": round(np.mean(variances), 4),
                "mean_stdev": round(np.sqrt(np.mean(variances)), 4),
                "max_variance": round(np.max(variances), 4),
                "n": len(variances),
            }
        else:
            results["per_trait"][trait] = {"error": "no per-model data"}

    return results


# =============================================================================
# REPORT GENERATION
# =============================================================================

def generate_report(
    rq1: dict,
    rq2: dict,
    rq3: dict,
    rule_based: dict,
    dual_eval: Optional[dict] = None,
    feature_validation: Optional[dict] = None,
    model_agreement: Optional[dict] = None,
) -> str:
    """Generate a Markdown summary report."""
    lines = [
        "# Behavioral Fidelity Experiment Report",
        "",
        f"Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## RQ1: Personality Fidelity",
        "",
        "Do assigned personality profiles produce matching behavioral signals?",
        "",
        "| Trait | Pearson r | p-value | MAE | N |",
        "|-------|----------|---------|-----|---|",
    ]

    for trait in TRAITS:
        data = rq1.get("per_trait", {}).get(trait, {})
        if "error" in data:
            lines.append(f"| {TRAIT_NAMES[trait]} | - | - | - | {data['error']} |")
        else:
            r = data.get("pearson_r", "-")
            p = data.get("p_value", "-")
            mae = data.get("mae", "-")
            n = data.get("n", "-")
            sig = "*" if isinstance(p, float) and p < 0.05 else ""
            lines.append(f"| {TRAIT_NAMES[trait]} | {r}{sig} | {p} | {mae} | {n} |")

    overall = rq1.get("overall", {})
    lines.extend([
        "",
        f"**Overall mean r:** {overall.get('mean_r', 'N/A')}",
        f"**Overall mean MAE:** {overall.get('mean_mae', 'N/A')}",
        "",
        "---",
        "",
        "## RQ2: Assessment Consistency",
        "",
        "Are personality assessments consistent across repeated sessions?",
        "",
        "| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |",
        "|-------|---------|--------|------------------------|",
    ])

    for trait in TRAITS:
        data = rq2.get("per_trait", {}).get(trait, {})
        if "error" in data:
            sd = data.get("mean_within_profile_sd", "-")
            lines.append(f"| {TRAIT_NAMES[trait]} | {data['error']} | - | {sd} |")
        else:
            icc = data.get("icc3k", "-")
            ci_low = data.get("ci95_low", "-")
            ci_high = data.get("ci95_high", "-")
            sd = data.get("mean_within_profile_sd", "-")
            lines.append(f"| {TRAIT_NAMES[trait]} | {icc} | [{ci_low}, {ci_high}] | {sd} |")

    lines.extend([
        "",
        "---",
        "",
        "## RQ3: Temporal Decay",
        "",
        "Do personality signals weaken over the course of a session?",
        "",
        "| Trait | t-stat | p-value | Cohen's d | r(early) | r(late) | Delta-r |",
        "|-------|--------|---------|----------|----------|---------|---------|",
    ])

    for trait in TRAITS:
        data = rq3.get("per_trait", {}).get(trait, {})
        if "error" in data:
            lines.append(f"| {TRAIT_NAMES[trait]} | - | - | - | - | - | {data['error']} |")
        else:
            lines.append(
                f"| {TRAIT_NAMES[trait]} | {data.get('t_stat', '-')} | {data.get('t_p_value', '-')} | "
                f"{data.get('cohens_d', '-')} | {data.get('r_early', '-')} | "
                f"{data.get('r_late', '-')} | {data.get('delta_r', '-')} |"
            )

    # Decay classification
    decay_items = rq3.get("decay_classification", [])
    if decay_items:
        lines.extend([
            "",
            "### Decay Classification by Profile",
            "",
            "| Profile | Early MAE | Late MAE | Classification |",
            "|---------|-----------|----------|----------------|",
        ])
        for item in decay_items:
            lines.append(
                f"| {item['profile_id']} | {item['mean_early_mae']} | "
                f"{item['mean_late_mae']} | {item['classification']} |"
            )

    lines.extend([
        "",
        "---",
        "",
        "## Rule-Based Validation",
        "",
        "Feature-trait correlation checks:",
        "",
        "| Check | Pearson r | p-value | Expected | Correct? |",
        "|-------|----------|---------|----------|----------|",
    ])

    for desc, data in rule_based.items():
        if "error" in data:
            lines.append(f"| {desc} | - | - | - | {data['error']} |")
        else:
            check = "Yes" if data.get("correct_direction") else "No"
            lines.append(
                f"| {desc} | {data.get('pearson_r', '-')} | {data.get('p_value', '-')} | "
                f"{data.get('expected_direction', '-')} | {check} |"
            )

    # Dual Evaluation section
    if dual_eval and "error" not in dual_eval:
        lines.extend([
            "",
            "---",
            "",
            "## Dual Evaluation: LLM vs Rule-Based",
            "",
            "Convergent validity between LLM ensemble and deterministic rule-based evaluator.",
            "",
            "| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |",
            "|-------|--------------|---------|---------------------|-------------------|---|",
        ])
        for trait in TRAITS:
            data = dual_eval.get(trait, {})
            if "error" in data:
                lines.append(f"| {TRAIT_NAMES[trait]} | - | - | - | - | {data['error']} |")
            else:
                lines.append(
                    f"| {TRAIT_NAMES[trait]} | {data.get('llm_vs_rule_based_r', '-')} | "
                    f"{data.get('llm_vs_rule_based_p', '-')} | "
                    f"{data.get('llm_vs_assigned_r', '-')} | "
                    f"{data.get('rule_based_vs_assigned_r', '-')} | "
                    f"{data.get('n', '-')} |"
                )

        # Convergent validity statement
        rs = [dual_eval[t].get("llm_vs_rule_based_r", 0) for t in TRAITS
              if isinstance(dual_eval.get(t), dict) and "error" not in dual_eval[t]]
        if rs:
            mean_r = np.mean(rs)
            if mean_r > 0.6:
                lines.append(f"\n**Convergent validity: STRONG** (mean r = {mean_r:.3f})")
            elif mean_r > 0.3:
                lines.append(f"\n**Convergent validity: MODERATE** (mean r = {mean_r:.3f})")
            else:
                lines.append(f"\n**Convergent validity: WEAK** (mean r = {mean_r:.3f})")

    # Expanded Feature-Trait Validation section
    if feature_validation and "error" not in feature_validation:
        lines.extend([
            "",
            "---",
            "",
            "## Expanded Feature-Trait Validation (22 Features)",
            "",
            "Top significant feature-trait correlations:",
            "",
            "| Feature -> Trait | Pearson r | p-value | Expected | Correct? |",
            "|-----------------|----------|---------|----------|----------|",
        ])

        # Sort by absolute r value, show top 10 significant
        sorted_items = []
        for desc, data in feature_validation.items():
            if desc.startswith("_") or not isinstance(data, dict) or "error" in data:
                continue
            sorted_items.append((desc, data))
        sorted_items.sort(key=lambda x: abs(x[1].get("pearson_r", 0)), reverse=True)

        for desc, data in sorted_items[:15]:
            check = "Yes" if data.get("correct_direction") else "No"
            sig = "*" if isinstance(data.get("p_value"), float) and data["p_value"] < 0.05 else ""
            lines.append(
                f"| {desc} | {data.get('pearson_r', '-')}{sig} | {data.get('p_value', '-')} | "
                f"{data.get('expected_direction', '-')} | {check} |"
            )

    # Inter-Model Agreement section
    if model_agreement and "error" not in model_agreement:
        lines.extend([
            "",
            "---",
            "",
            "## Inter-Model Agreement",
            "",
            "Per-trait variance across ensemble models (lower = more agreement).",
            "",
            "| Trait | Mean Stdev | Mean Variance | Max Variance | N |",
            "|-------|-----------|--------------|-------------|---|",
        ])
        for trait in TRAITS:
            data = model_agreement.get("per_trait", {}).get(trait, {})
            if "error" in data:
                lines.append(f"| {TRAIT_NAMES[trait]} | - | - | - | {data['error']} |")
            else:
                lines.append(
                    f"| {TRAIT_NAMES[trait]} | {data.get('mean_stdev', '-')} | "
                    f"{data.get('mean_variance', '-')} | "
                    f"{data.get('max_variance', '-')} | {data.get('n', '-')} |"
                )

        uncertain = model_agreement.get("uncertain_sessions", [])
        if uncertain:
            lines.extend([
                "",
                f"**Uncertain sessions (high inter-model variance):** {len(uncertain)}",
            ])

    lines.append("")
    return "\n".join(lines)


# =============================================================================
# CONVENIENCE FUNCTION
# =============================================================================

def run_full_analysis(
    results_dir: str,
    temporal_path: Optional[str] = None,
):
    """
    One-shot convenience function to run all analyses and generate report.

    Args:
        results_dir: Directory containing session JSON files.
        temporal_path: Path to temporal analysis JSON (if already computed).
    """
    print("Loading results...")
    df = load_results(results_dir)
    print(f"Loaded {len(df)} sessions")

    print("\nRQ1: Personality Fidelity...")
    rq1 = rq1_analysis(df)

    print("RQ2: Assessment Consistency...")
    rq2 = rq2_analysis(df)

    # RQ3: Temporal decay (requires temporal analysis data)
    rq3 = {}
    if temporal_path is None:
        temporal_path = str(Path(results_dir) / "temporal_analysis.json")
    if Path(temporal_path).exists():
        print("RQ3: Temporal Decay...")
        with open(temporal_path) as f:
            window_results = json.load(f)
        rq3 = rq3_analysis(window_results)
    else:
        print("RQ3: Skipped (no temporal analysis data found)")
        rq3 = {"error": "temporal analysis not run yet"}

    print("Rule-based validation (legacy 6-pair)...")
    rb = rule_based_validation(df)

    print("Dual evaluation comparison (LLM vs Rule-Based)...")
    dual_eval = dual_evaluation_comparison(df)

    print("Expanded feature-trait validation (22 features)...")
    feat_val = expanded_feature_trait_validation(df)

    print("Inter-model agreement analysis...")
    model_agree = inter_model_agreement(df)

    # Generate report
    report = generate_report(rq1, rq2, rq3, rb, dual_eval, feat_val, model_agree)

    # Save all outputs
    output_dir = Path(results_dir)

    report_path = output_dir / "analysis_report.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"\nReport saved to {report_path}")

    # Save raw results
    raw_path = output_dir / "analysis_raw.json"
    raw_results = {
        "rq1": rq1,
        "rq2": rq2,
        "rq3": rq3,
        "rule_based": rb,
        "dual_evaluation": dual_eval,
        "feature_trait_validation": feat_val,
        "inter_model_agreement": model_agree,
    }
    with open(raw_path, "w") as f:
        json.dump(raw_results, f, indent=2, default=str)
    print(f"Raw results saved to {raw_path}")

    # Print summary
    print(f"\n{'='*60}")
    print(report)
    print(f"{'='*60}")
