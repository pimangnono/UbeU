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
    # 8 new features (Critiques 2 & 3)
    "structure_marker_count", "reference_back_count", "action_item_count",
    "hypothetical_count", "apology_count", "self_doubt_count",
    "reassurance_seeking_count", "negation_count",
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
            "intervention": data.get("intervention", "none"),
            "overall_confidence": data.get("overall_confidence", 0.0),
        }

        # Controller log (BCFC sessions only)
        ctrl_log = data.get("controller_log")
        if ctrl_log and isinstance(ctrl_log, dict):
            row["ctrl_nudge_rate"] = ctrl_log.get("nudge_rate", 0.0)
            row["ctrl_regen_rate"] = ctrl_log.get("regeneration_rate", 0.0)
            row["ctrl_total_nudges"] = ctrl_log.get("total_nudges", 0)
            row["ctrl_total_regens"] = ctrl_log.get("total_regenerations", 0)
            row["ctrl_total_turns"] = ctrl_log.get("total_candidate_turns", 0)
        else:
            row["ctrl_nudge_rate"] = None
            row["ctrl_regen_rate"] = None
            row["ctrl_total_nudges"] = None
            row["ctrl_total_regens"] = None
            row["ctrl_total_turns"] = None

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

        # Trajectory metrics
        traj = data.get("trajectory_scores") or {}
        row["traj_avg_appropriateness"] = traj.get("avg_appropriateness")
        row["traj_avg_coherence"] = traj.get("avg_coherence")

        # Pressure metrics
        pm = data.get("pressure_metrics") or {}
        perceived = pm.get("perceived_pressure") or {}
        row["pressure_perceived"] = perceived.get("perceived_pressure") if isinstance(perceived, dict) else pm.get("perceived_pressure")
        row["pressure_stress_index"] = pm.get("stress_index")

        # Usage / cost
        usage = data.get("usage") or {}
        row["candidate_gen_in_tokens"] = usage.get("candidate_generation_input_tokens")
        row["candidate_gen_out_tokens"] = usage.get("candidate_generation_output_tokens")
        row["judge_in_tokens"] = usage.get("judge_input_tokens")
        row["judge_out_tokens"] = usage.get("judge_output_tokens")
        row["escalation_extra_tokens"] = usage.get("escalation_extra_tokens")
        row["total_session_cost_usd"] = usage.get("total_session_cost_usd")
        row["wall_clock_seconds"] = usage.get("wall_clock_seconds")

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
# RQ3b: PHASE-CONTROLLED TEMPORAL ANALYSIS (V5.1)
# =============================================================================

def phase_normalized_rq3(window_results: list[dict]) -> dict:
    """
    Phase-controlled RQ3: regress abs_error on phase_pos_norm + C(phase_name).

    Uses mixed-effects model (random intercept by session_key) if statsmodels is
    available; falls back to OLS with clustered standard errors.

    Args:
        window_results: Temporal analysis output with "phases" list per session.

    Returns:
        Per-trait regression results: beta_time, p_time, model type.
    """
    if not window_results:
        return {"error": "no temporal data"}

    # Build phase-level DataFrame
    rows = []
    for session in window_results:
        av = session.get("assigned_vector") or {}
        session_key = session.get("session_key", "")
        phases = session.get("windows", {}).get("phases", [])

        for phase in phases:
            iv = phase.get("inferred_vector")
            if not iv:
                continue
            row = {
                "session_key": session_key,
                "phase_name": phase.get("phase_name", ""),
                "phase_pos_norm": phase.get("phase_pos_norm", 0.0),
            }
            for trait in TRAITS:
                if trait in av and trait in iv:
                    row[f"assigned_{trait}"] = av[trait]
                    row[f"inferred_{trait}"] = iv[trait]
            rows.append(row)

    if not rows:
        return {"error": "no phase-level data"}

    df_phase = pd.DataFrame(rows)
    results = {}

    for trait in TRAITS:
        a_col = f"assigned_{trait}"
        i_col = f"inferred_{trait}"
        d = df_phase.dropna(subset=[a_col, i_col]).copy()
        if len(d) < 5:
            results[trait] = {"error": "insufficient data"}
            continue

        d["abs_error"] = (d[a_col] - d[i_col]).abs()

        try:
            import statsmodels.formula.api as smf

            try:
                m = smf.mixedlm(
                    "abs_error ~ phase_pos_norm + C(phase_name)",
                    d, groups=d["session_key"],
                )
                fit = m.fit(reml=False, method="lbfgs", maxiter=200)
                beta = fit.params.get("phase_pos_norm", np.nan)
                pval = fit.pvalues.get("phase_pos_norm", np.nan)
                results[trait] = {
                    "beta_time": round(float(beta), 4),
                    "p_time": round(float(pval), 6),
                    "model": "mixedlm",
                    "n": len(d),
                }
            except Exception:
                # Fallback: OLS with clustered SE
                ols = smf.ols(
                    "abs_error ~ phase_pos_norm + C(phase_name)", d,
                ).fit(cov_type="cluster", cov_kwds={"groups": d["session_key"]})
                beta = ols.params.get("phase_pos_norm", np.nan)
                pval = ols.pvalues.get("phase_pos_norm", np.nan)
                results[trait] = {
                    "beta_time": round(float(beta), 4),
                    "p_time": round(float(pval), 6),
                    "model": "ols_cluster_fallback",
                    "n": len(d),
                }
        except ImportError:
            # No statsmodels — simple correlation as last resort
            r, p = scipy_stats.pearsonr(d["phase_pos_norm"], d["abs_error"])
            results[trait] = {
                "beta_time": round(float(r), 4),
                "p_time": round(float(p), 6),
                "model": "pearson_fallback",
                "n": len(d),
            }

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
    # 8 new feature expectations (Critiques 2 & 3)
    ("feat_structure_marker_count", "assigned_C", "positive", "Structure markers -> C"),
    ("feat_reference_back_count", "assigned_C", "positive", "Reference back -> C"),
    ("feat_action_item_count", "assigned_C", "positive", "Action items -> C"),
    ("feat_hypothetical_count", "assigned_O", "positive", "Hypotheticals -> O"),
    ("feat_apology_count", "assigned_N", "positive", "Apologies -> N"),
    ("feat_self_doubt_count", "assigned_N", "positive", "Self-doubt -> N"),
    ("feat_reassurance_seeking_count", "assigned_N", "positive", "Reassurance seeking -> N"),
    ("feat_negation_count", "assigned_A", "negative", "Negations -> -A"),
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
# POSITIVITY BIAS ANALYSIS (Critique 10)
# =============================================================================

def positivity_bias_analysis(df: pd.DataFrame) -> dict:
    """
    Quantify systematic evaluator bias per trait (Critique 10).

    Computes signed error (inferred - assigned) for both LLM ensemble and
    rule-based evaluator. Positive bias = trait overestimated, negative = under.
    Tests whether the signed error is significantly different from 0.

    Returns per-trait bias with statistical tests and LLM-specific bias
    (LLM bias minus rule-based bias).
    """
    main = df[df["condition"] == "main"].copy()

    if len(main) < 5:
        return {"error": "insufficient data"}

    results = {"per_trait": {}, "summary": ""}

    for trait in TRAITS:
        assigned_col = f"assigned_{trait}"
        inferred_col = f"inferred_{trait}"
        rb_col = f"rule_based_{trait}"

        valid = main.dropna(subset=[assigned_col, inferred_col])
        if len(valid) < 5:
            results["per_trait"][trait] = {"error": "insufficient data"}
            continue

        assigned = valid[assigned_col].values
        inferred = valid[inferred_col].values

        # LLM signed error
        llm_errors = inferred - assigned
        llm_mean_bias = float(np.mean(llm_errors))

        # One-sample t-test: is mean signed error != 0?
        t_stat, t_p = scipy_stats.ttest_1samp(llm_errors, 0.0)

        trait_result = {
            "llm_mean_bias": round(llm_mean_bias, 4),
            "llm_t_stat": round(t_stat, 4),
            "llm_t_p_value": round(t_p, 6),
            "llm_significant": bool(t_p < 0.05),
            "n": len(valid),
        }

        # Rule-based signed error
        rb_valid = valid.dropna(subset=[rb_col])
        if len(rb_valid) >= 5:
            rb_inferred = rb_valid[rb_col].values
            rb_assigned = rb_valid[assigned_col].values
            rb_errors = rb_inferred - rb_assigned
            rb_mean_bias = float(np.mean(rb_errors))

            rb_t, rb_p = scipy_stats.ttest_1samp(rb_errors, 0.0)

            trait_result["rb_mean_bias"] = round(rb_mean_bias, 4)
            trait_result["rb_t_stat"] = round(rb_t, 4)
            trait_result["rb_t_p_value"] = round(rb_p, 6)
            trait_result["rb_significant"] = bool(rb_p < 0.05)

            # LLM-specific bias = LLM bias - rule-based bias
            llm_specific = llm_mean_bias - rb_mean_bias
            trait_result["llm_specific_bias"] = round(llm_specific, 4)
        else:
            trait_result["rb_mean_bias"] = None
            trait_result["llm_specific_bias"] = None

        results["per_trait"][trait] = trait_result

    # Summary: identify most biased traits
    biased_traits = [
        (t, d["llm_mean_bias"])
        for t, d in results["per_trait"].items()
        if isinstance(d, dict) and "error" not in d and d.get("llm_significant")
    ]
    biased_traits.sort(key=lambda x: abs(x[1]), reverse=True)

    if biased_traits:
        labels = [f"{TRAIT_NAMES[t]} ({b:+.3f})" for t, b in biased_traits]
        results["summary"] = f"Significantly biased traits: {', '.join(labels)}"
    else:
        results["summary"] = "No statistically significant per-trait bias detected."

    return results


# =============================================================================
# FDR CORRECTION + BOOTSTRAP CIs (V5.1 Phase 6)
# =============================================================================

def apply_fdr_correction(results_dict: dict, alpha: float = 0.05) -> dict:
    """
    Apply FDR-BH correction to p-values across trait-family tests.

    Args:
        results_dict: Dict with per-trait sub-dicts containing "p_value" keys.
        alpha: Significance level.

    Returns:
        Updated dict with "q_value" and "fdr_significant" added per trait.
    """
    per_trait = results_dict.get("per_trait", {})
    pvals = []
    trait_order = []

    for trait in TRAITS:
        data = per_trait.get(trait, {})
        p = data.get("p_value") or data.get("t_p_value") or data.get("p_time")
        if isinstance(p, (int, float)) and not np.isnan(p):
            pvals.append(p)
            trait_order.append(trait)

    if not pvals:
        return results_dict

    try:
        from statsmodels.stats.multitest import multipletests
        rej, qvals, _, _ = multipletests(pvals, alpha=alpha, method="fdr_bh")
        for i, trait in enumerate(trait_order):
            per_trait[trait]["q_value"] = round(float(qvals[i]), 6)
            per_trait[trait]["fdr_significant"] = bool(rej[i])
    except ImportError:
        logger.warning("statsmodels not installed, skipping FDR correction")
        # Manual BH procedure as fallback
        n = len(pvals)
        sorted_indices = np.argsort(pvals)
        for rank, idx in enumerate(sorted_indices, 1):
            threshold = alpha * rank / n
            per_trait[trait_order[idx]]["q_value"] = round(pvals[idx] * n / rank, 6)
            per_trait[trait_order[idx]]["fdr_significant"] = bool(pvals[idx] <= threshold)

    return results_dict


def bootstrap_ci(
    values: np.ndarray,
    statistic=np.mean,
    n_resamples: int = 2000,
    ci: float = 0.95,
    seed: int = 42,
) -> tuple[float, float, float]:
    """
    Compute bootstrap confidence interval for a statistic.

    Args:
        values: Array of observed values.
        statistic: Function to compute (default: mean).
        n_resamples: Number of bootstrap resamples.
        ci: Confidence level (default: 0.95).
        seed: Random seed for reproducibility.

    Returns:
        (point_estimate, ci_lower, ci_upper)
    """
    rng = np.random.RandomState(seed)
    point = float(statistic(values))
    boot_stats = []
    for _ in range(n_resamples):
        sample = rng.choice(values, size=len(values), replace=True)
        boot_stats.append(float(statistic(sample)))

    alpha = 1 - ci
    lower = float(np.percentile(boot_stats, 100 * alpha / 2))
    upper = float(np.percentile(boot_stats, 100 * (1 - alpha / 2)))
    return point, lower, upper


def trait_confidence_matrix(
    rq1: dict,
    rq2: dict,
    rq3_pc: dict,
    judge_bias: dict,
    bias_analysis: dict,
) -> dict:
    """
    Build a trait confidence matrix summarizing evidence quality per trait.

    Dimensions:
    - detectability: RQ1 pearson_r significance
    - consistency: RQ2 ICC value
    - judge_robustness: judge order-bias uncertain rate
    - phase_stability: RQ3 phase-controlled beta significance
    - evaluator_bias: positivity bias significance

    Returns dict per trait with quality ratings.
    """
    matrix = {}

    for trait in TRAITS:
        row = {}

        # Detectability (RQ1)
        rq1_data = rq1.get("per_trait", {}).get(trait, {})
        r = rq1_data.get("pearson_r")
        p = rq1_data.get("p_value")
        if isinstance(r, float) and isinstance(p, float):
            if p < 0.05 and abs(r) > 0.5:
                row["detectability"] = "strong"
            elif p < 0.05:
                row["detectability"] = "moderate"
            else:
                row["detectability"] = "weak"
        else:
            row["detectability"] = "no_data"

        # Consistency (RQ2)
        rq2_data = rq2.get("per_trait", {}).get(trait, {})
        icc = rq2_data.get("icc3k")
        if isinstance(icc, float):
            if icc >= 0.75:
                row["consistency"] = "excellent"
            elif icc >= 0.5:
                row["consistency"] = "moderate"
            else:
                row["consistency"] = "poor"
        else:
            row["consistency"] = "no_data"

        # Judge robustness
        jb_data = (judge_bias or {}).get("per_trait", {}).get(trait, {})
        uc_rate = jb_data.get("uncertain_rate")
        if isinstance(uc_rate, float):
            if uc_rate < 0.10:
                row["judge_robustness"] = "robust"
            elif uc_rate < 0.20:
                row["judge_robustness"] = "moderate"
            else:
                row["judge_robustness"] = "fragile"
        else:
            row["judge_robustness"] = "no_data"

        # Phase stability (RQ3 phase-controlled)
        rq3_data = (rq3_pc or {}).get(trait, {})
        p_time = rq3_data.get("p_time")
        if isinstance(p_time, float):
            if p_time >= 0.05:
                row["phase_stability"] = "stable"
            else:
                row["phase_stability"] = "decaying"
        else:
            row["phase_stability"] = "no_data"

        # Evaluator bias
        bias_data = (bias_analysis or {}).get("per_trait", {}).get(trait, {})
        if bias_data.get("llm_significant"):
            row["evaluator_bias"] = f"biased ({bias_data.get('llm_mean_bias', 0):+.3f})"
        elif isinstance(bias_data.get("llm_mean_bias"), float):
            row["evaluator_bias"] = "unbiased"
        else:
            row["evaluator_bias"] = "no_data"

        matrix[trait] = row

    return matrix


# =============================================================================
# BCFC PAIRED ANALYSIS (RQ1-RQ4)
# =============================================================================

def bcfc_paired_analysis(df: pd.DataFrame) -> dict:
    """
    BCFC paired comparison: baseline vs BCFC for matched profile-scenario pairs.

    RQ1: Overall fidelity improvement (paired t-test on MAE)
    RQ2: Per-trait improvement (especially C, O)
    RQ3: Drift reduction (if temporal data exists)
    RQ4: Variance reduction (within-profile SD)
    """
    baseline = df[df["intervention"] == "none"].copy()
    # Include both bcfc and bcfc_v3 as BCFC conditions (use best available)
    bcfc = df[df["intervention"].isin(["bcfc", "bcfc_v3"])].copy()
    # If both bcfc and bcfc_v3 exist for same pair, prefer bcfc_v3
    if (df["intervention"] == "bcfc_v3").any():
        bcfc_v3 = df[df["intervention"] == "bcfc_v3"].copy()
        bcfc_v2_only = df[(df["intervention"] == "bcfc") &
                          ~(df["profile_id"] + "_" + df["scenario_id"]).isin(
                              bcfc_v3["profile_id"] + "_" + bcfc_v3["scenario_id"])].copy()
        bcfc = pd.concat([bcfc_v3, bcfc_v2_only], ignore_index=True)

    if len(baseline) < 3 or len(bcfc) < 3:
        return {"error": "insufficient BCFC data", "n_baseline": len(baseline), "n_bcfc": len(bcfc)}

    # Match pairs by profile_id + scenario_id
    baseline["pair_key"] = baseline["profile_id"] + "_" + baseline["scenario_id"]
    bcfc["pair_key"] = bcfc["profile_id"] + "_" + bcfc["scenario_id"]

    common_keys = set(baseline["pair_key"]) & set(bcfc["pair_key"])
    if len(common_keys) < 3:
        return {"error": f"only {len(common_keys)} matched pairs"}

    results = {
        "n_pairs": len(common_keys),
        "n_baseline": len(baseline),
        "n_bcfc": len(bcfc),
        "rq1_overall": {},
        "rq2_per_trait": {},
        "rq4_variance": {},
    }

    # RQ1: Overall MAE comparison
    baseline_maes = []
    bcfc_maes = []

    for key in sorted(common_keys):
        bl_row = baseline[baseline["pair_key"] == key].iloc[0]
        bc_row = bcfc[bcfc["pair_key"] == key].iloc[0]

        bl_errors = []
        bc_errors = []
        for trait in TRAITS:
            a = bl_row.get(f"assigned_{trait}")
            bl_i = bl_row.get(f"inferred_{trait}")
            bc_i = bc_row.get(f"inferred_{trait}")
            if a is not None and bl_i is not None and bc_i is not None:
                bl_errors.append(abs(a - bl_i))
                bc_errors.append(abs(a - bc_i))

        if bl_errors and bc_errors:
            baseline_maes.append(np.mean(bl_errors))
            bcfc_maes.append(np.mean(bc_errors))

    if len(baseline_maes) >= 3:
        bl_arr = np.array(baseline_maes)
        bc_arr = np.array(bcfc_maes)
        t_stat, t_p = scipy_stats.ttest_rel(bl_arr, bc_arr)
        diff = bl_arr - bc_arr
        cohens_d = np.mean(diff) / np.std(diff, ddof=1) if np.std(diff, ddof=1) > 0 else 0

        results["rq1_overall"] = {
            "baseline_mean_mae": round(float(np.mean(bl_arr)), 4),
            "bcfc_mean_mae": round(float(np.mean(bc_arr)), 4),
            "mae_reduction": round(float(np.mean(bl_arr) - np.mean(bc_arr)), 4),
            "paired_t_stat": round(float(t_stat), 4),
            "paired_t_p": round(float(t_p), 6),
            "cohens_d": round(float(cohens_d), 4),
            "n_pairs": len(baseline_maes),
            "significant": bool(t_p < 0.05),
        }

    # RQ2: Per-trait comparison
    for trait in TRAITS:
        bl_vals = []
        bc_vals = []
        assigned_vals = []

        for key in sorted(common_keys):
            bl_row = baseline[baseline["pair_key"] == key].iloc[0]
            bc_row = bcfc[bcfc["pair_key"] == key].iloc[0]

            a = bl_row.get(f"assigned_{trait}")
            bl_i = bl_row.get(f"inferred_{trait}")
            bc_i = bc_row.get(f"inferred_{trait}")

            if a is not None and bl_i is not None and bc_i is not None:
                assigned_vals.append(a)
                bl_vals.append(bl_i)
                bc_vals.append(bc_i)

        if len(assigned_vals) < 3:
            results["rq2_per_trait"][trait] = {"error": "insufficient data"}
            continue

        assigned_arr = np.array(assigned_vals)
        bl_arr = np.array(bl_vals)
        bc_arr = np.array(bc_vals)

        # Correlations
        r_bl, p_bl = scipy_stats.pearsonr(assigned_arr, bl_arr)
        r_bc, p_bc = scipy_stats.pearsonr(assigned_arr, bc_arr)

        # MAE
        mae_bl = float(np.mean(np.abs(assigned_arr - bl_arr)))
        mae_bc = float(np.mean(np.abs(assigned_arr - bc_arr)))

        # Paired t-test on per-pair absolute errors
        bl_errors = np.abs(assigned_arr - bl_arr)
        bc_errors = np.abs(assigned_arr - bc_arr)
        t_stat, t_p = scipy_stats.ttest_rel(bl_errors, bc_errors)

        results["rq2_per_trait"][trait] = {
            "baseline_r": round(float(r_bl), 4),
            "bcfc_r": round(float(r_bc), 4),
            "r_improvement": round(float(r_bc - r_bl), 4),
            "baseline_mae": round(mae_bl, 4),
            "bcfc_mae": round(mae_bc, 4),
            "mae_reduction": round(mae_bl - mae_bc, 4),
            "paired_t_stat": round(float(t_stat), 4),
            "paired_t_p": round(float(t_p), 6),
            "n": len(assigned_vals),
            "significant": bool(t_p < 0.05),
        }

    # RQ4: Variance comparison (within-profile SD)
    for trait in TRAITS:
        inferred_col = f"inferred_{trait}"

        # Filter to main condition profiles only
        bl_main = baseline[baseline["condition"] == "main"]
        bc_main = bcfc[bcfc["condition"] == "main"]

        bl_sds = bl_main.groupby("profile_id")[inferred_col].std().dropna()
        bc_sds = bc_main.groupby("profile_id")[inferred_col].std().dropna()

        common_profiles = sorted(set(bl_sds.index) & set(bc_sds.index))

        if len(common_profiles) >= 3:
            bl_sd_vals = bl_sds.loc[common_profiles].values
            bc_sd_vals = bc_sds.loc[common_profiles].values

            results["rq4_variance"][trait] = {
                "baseline_mean_sd": round(float(np.mean(bl_sd_vals)), 4),
                "bcfc_mean_sd": round(float(np.mean(bc_sd_vals)), 4),
                "sd_reduction": round(float(np.mean(bl_sd_vals) - np.mean(bc_sd_vals)), 4),
                "n_profiles": len(common_profiles),
            }
        else:
            results["rq4_variance"][trait] = {"error": "insufficient profile data"}

    return results


def bcfc_ablation_analysis(results_dir: str) -> dict:
    """
    Analyze BCFC controller intervention logs for ablation.

    From controller_log in each BCFC session:
    - Which traits needed most correction?
    - How often did regeneration trigger?
    - Did nudges correlate with improved post-nudge behavior?
    """
    results_path = Path(results_dir)
    trait_nudge_counts = {t: 0 for t in TRAITS}
    trait_violation_counts = {t: 0 for t in TRAITS}
    violation_types: dict[str, int] = {}
    total_sessions = 0
    total_nudges = 0
    total_regenerations = 0
    total_candidate_turns = 0
    nudge_rates = []
    regen_rates = []

    for filepath in sorted(results_path.glob("session_*.json")):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        if data.get("intervention") != "bcfc":
            continue

        ctrl = data.get("controller_log")
        if not ctrl:
            continue

        total_sessions += 1
        total_nudges += ctrl.get("total_nudges", 0)
        total_regenerations += ctrl.get("total_regenerations", 0)
        total_candidate_turns += ctrl.get("total_candidate_turns", 0)
        nudge_rates.append(ctrl.get("nudge_rate", 0))
        regen_rates.append(ctrl.get("regeneration_rate", 0))

        # Analyze deviation reports (nudges)
        for report in ctrl.get("deviation_reports", []):
            for dev in report.get("deviations", []):
                trait = dev.get("trait")
                if trait in trait_nudge_counts:
                    trait_nudge_counts[trait] += 1

        # Analyze constraint violations (regenerations)
        for violation in ctrl.get("constraint_violations", []):
            vtype = violation.get("violation_type", "unknown")
            violation_types[vtype] = violation_types.get(vtype, 0) + 1

            # Map violation types to traits
            vtype_trait_map = {
                "agreed_without_concern": "A",
                "criticized_without_acknowledgment": "A",
                "no_organizational_element": "C",
                "imposed_unsolicited_structure": "C",
                "accepted_without_alternative": "O",
                "expressed_self_doubt": "N",
                "no_hedge_under_pressure": "N",
                "response_too_long": "E",
                "no_name_mention": "E",
            }
            mapped_trait = vtype_trait_map.get(vtype)
            if mapped_trait and mapped_trait in trait_violation_counts:
                trait_violation_counts[mapped_trait] += 1

    if total_sessions == 0:
        return {"error": "no BCFC sessions with controller logs"}

    return {
        "total_sessions": total_sessions,
        "total_nudges": total_nudges,
        "total_regenerations": total_regenerations,
        "total_candidate_turns": total_candidate_turns,
        "mean_nudge_rate": round(float(np.mean(nudge_rates)), 3) if nudge_rates else 0,
        "mean_regen_rate": round(float(np.mean(regen_rates)), 3) if regen_rates else 0,
        "trait_nudge_counts": trait_nudge_counts,
        "trait_violation_counts": trait_violation_counts,
        "violation_type_counts": dict(sorted(violation_types.items(), key=lambda x: -x[1])),
        "most_corrected_traits": sorted(
            trait_nudge_counts.items(), key=lambda x: -x[1]
        )[:3],
    }


def bcfc_cost_analysis(df: pd.DataFrame) -> dict:
    """
    RQ5: BCFC cost overhead analysis.

    Compares controller overhead metrics between baseline and BCFC sessions.
    """
    bcfc = df[df["intervention"].isin(["bcfc", "bcfc_v3"])].copy()

    if len(bcfc) < 1:
        return {"error": "no BCFC sessions"}

    nudge_rates = bcfc["ctrl_nudge_rate"].dropna()
    regen_rates = bcfc["ctrl_regen_rate"].dropna()

    result = {
        "n_bcfc_sessions": len(bcfc),
        "nudge_rate": {
            "mean": round(float(nudge_rates.mean()), 3) if len(nudge_rates) > 0 else None,
            "median": round(float(nudge_rates.median()), 3) if len(nudge_rates) > 0 else None,
            "max": round(float(nudge_rates.max()), 3) if len(nudge_rates) > 0 else None,
        },
        "regeneration_rate": {
            "mean": round(float(regen_rates.mean()), 3) if len(regen_rates) > 0 else None,
            "median": round(float(regen_rates.median()), 3) if len(regen_rates) > 0 else None,
            "max": round(float(regen_rates.max()), 3) if len(regen_rates) > 0 else None,
        },
    }

    # Session cost (if available)
    if "total_session_cost_usd" in bcfc.columns:
        costs = bcfc["total_session_cost_usd"].dropna()
        if len(costs) > 0:
            result["mean_session_cost_usd"] = round(float(costs.mean()), 4)
            result["median_session_cost_usd"] = round(float(costs.median()), 4)

    # Estimate cost overhead: regenerations add ~1 extra API call each
    total_regens = bcfc["ctrl_total_regens"].dropna().sum()
    total_turns = bcfc["ctrl_total_turns"].dropna().sum()
    if total_turns > 0:
        overhead_pct = (total_regens / total_turns) * 100
        result["estimated_cost_overhead_pct"] = round(float(overhead_pct), 1)
        result["within_budget"] = overhead_pct < 50  # <1.5x baseline = <50% overhead

    return result


# =============================================================================
# BoN Pool Ablation (Compute-Effect Separation)
# =============================================================================

def bon_pool_ablation(results_dir: str) -> dict:
    """
    Offline ablation using stored candidate pools.
    Compares selection policies on the same candidate pool.
    """
    results_path = Path(results_dir)
    contract_vals = {
        "full_score": [],
        "first": [],
        "random_expected": [],
        "contract_only": [],
        "relevance_only": [],
    }

    adequacy_vals = {k: [] for k in contract_vals.keys()}
    n_pools = 0

    for filepath in sorted(results_path.glob("session_*.json")):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        pools = data.get("candidate_pool") or []
        for pool in pools:
            candidates = pool.get("candidates") or []
            if not candidates or not isinstance(candidates, list):
                continue
            # Only use pools with scoring info
            if not all(isinstance(c, dict) and "score" in c for c in candidates):
                continue

            n_pools += 1

            # Full score selection
            full_idx = max(range(len(candidates)), key=lambda i: candidates[i].get("score", 0))
            first_idx = 0

            # Contract-only
            contract_idx = max(range(len(candidates)), key=lambda i: 1.0 - candidates[i].get("contract_distance", 1.0))

            # Relevance-only
            relevance_idx = max(range(len(candidates)), key=lambda i: 1.0 - candidates[i].get("relevance_penalty", 1.0))

            # Random expected
            avg_contract = float(np.mean([c.get("contract_distance", 1.0) for c in candidates]))
            avg_adequacy = float(np.mean([c.get("adequacy_penalty", 1.0) for c in candidates]))

            def _push(label: str, idx: int):
                contract_vals[label].append(candidates[idx].get("contract_distance", 1.0))
                adequacy_vals[label].append(candidates[idx].get("adequacy_penalty", 1.0))

            _push("full_score", full_idx)
            _push("first", first_idx)
            _push("contract_only", contract_idx)
            _push("relevance_only", relevance_idx)
            contract_vals["random_expected"].append(avg_contract)
            adequacy_vals["random_expected"].append(avg_adequacy)

    if n_pools == 0:
        return {"error": "no candidate pools found"}

    result = {"n_pools": n_pools, "contract_distance": {}, "adequacy_penalty": {}}
    for k, v in contract_vals.items():
        result["contract_distance"][k] = round(float(np.mean(v)), 4) if v else None
    for k, v in adequacy_vals.items():
        result["adequacy_penalty"][k] = round(float(np.mean(v)), 4) if v else None
    return result


def bon_random_analysis(df: pd.DataFrame, scenario_id: Optional[str] = None) -> dict:
    """Compare BoN-random subset to baseline and BCFC on the same scenario."""
    bon = df[(df["intervention"] == "bon_random") & (df["condition"] == "main")]
    if scenario_id:
        bon = bon[bon["scenario_id"] == scenario_id]

    if len(bon) < 1:
        return {"error": "no bon_random sessions"}

    def _mean_mae(sub):
        errs = []
        for t in TRAITS:
            a = sub[f"assigned_{t}"].values
            i = sub[f"inferred_{t}"].values
            valid = ~np.isnan(a) & ~np.isnan(i)
            if valid.any():
                errs.append(np.mean(np.abs(a[valid] - i[valid])))
        return float(np.mean(errs)) if errs else None

    baseline = df[(df["intervention"] == "none") & (df["condition"] == "main")]
    bcfc = df[df["intervention"].isin(["bcfc", "bcfc_v3"]) & (df["condition"] == "main")]
    if scenario_id:
        baseline = baseline[baseline["scenario_id"] == scenario_id]
        bcfc = bcfc[bcfc["scenario_id"] == scenario_id]

    return {
        "n_bon_random": len(bon),
        "n_baseline": len(baseline),
        "n_bcfc": len(bcfc),
        "bon_random_mean_mae": round(_mean_mae(bon), 4),
        "baseline_mean_mae": round(_mean_mae(baseline), 4) if len(baseline) > 0 else None,
        "bcfc_mean_mae": round(_mean_mae(bcfc), 4) if len(bcfc) > 0 else None,
    }


def trajectory_analysis(df: pd.DataFrame) -> dict:
    """Compare trajectory coherence/appropriateness between baseline and BCFC."""
    baseline = df[(df["intervention"] == "none") & (df["condition"] == "main")]
    bcfc = df[df["intervention"].isin(["bcfc", "bcfc_v3"]) & (df["condition"] == "main")]
    if len(baseline) < 2 or len(bcfc) < 2:
        return {"error": "insufficient data"}

    def _mean(col, sub):
        return float(np.nanmean(sub[col].values)) if col in sub else None

    return {
        "baseline_avg_appropriateness": round(_mean("traj_avg_appropriateness", baseline), 4),
        "bcfc_avg_appropriateness": round(_mean("traj_avg_appropriateness", bcfc), 4),
        "baseline_avg_coherence": round(_mean("traj_avg_coherence", baseline), 4),
        "bcfc_avg_coherence": round(_mean("traj_avg_coherence", bcfc), 4),
    }


def pressure_manipulation_check(df: pd.DataFrame) -> dict:
    """Low-pressure vs high-pressure manipulation check (crisis only)."""
    high = df[df["scenario_id"] == "crisis_management"]
    low = df[df["scenario_id"] == "crisis_management_low"]
    if len(high) < 2 or len(low) < 2:
        return {"error": "insufficient pressure data"}

    return {
        "high_perceived": round(float(np.nanmean(high["pressure_perceived"])), 4),
        "low_perceived": round(float(np.nanmean(low["pressure_perceived"])), 4),
        "high_stress_index": round(float(np.nanmean(high["pressure_stress_index"])), 4),
        "low_stress_index": round(float(np.nanmean(low["pressure_stress_index"])), 4),
        "n_high": len(high),
        "n_low": len(low),
    }


def candidate_diversity_analysis(results_dir: str) -> dict:
    """Compute average candidate diversity (1 - Jaccard overlap) within pools."""
    results_path = Path(results_dir)
    overlaps: list[float] = []
    pools = 0

    def _tokens(text: str) -> set[str]:
        return {t.lower().strip(".,!?;:()[]") for t in text.split() if t}

    for filepath in sorted(results_path.glob("session_*.json")):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue
        pool_logs = data.get("candidate_pool") or []
        for pool in pool_logs:
            candidates = pool.get("candidates") or []
            texts = []
            for c in candidates:
                if isinstance(c, dict):
                    t = c.get("text")
                else:
                    t = c
                if t:
                    texts.append(t)
            if len(texts) < 2:
                continue
            pools += 1
            # pairwise Jaccard overlap
            pair_overlaps = []
            for i in range(len(texts)):
                for j in range(i + 1, len(texts)):
                    a = _tokens(texts[i])
                    b = _tokens(texts[j])
                    if not a and not b:
                        continue
                    inter = len(a & b)
                    union = len(a | b) or 1
                    pair_overlaps.append(inter / union)
            if pair_overlaps:
                overlaps.append(float(np.mean(pair_overlaps)))

    if pools == 0:
        return {"error": "no candidate pools found"}

    avg_overlap = float(np.mean(overlaps)) if overlaps else None
    return {
        "pools": pools,
        "avg_jaccard_overlap": round(avg_overlap, 4) if avg_overlap is not None else None,
        "avg_diversity": round(1 - avg_overlap, 4) if avg_overlap is not None else None,
    }


# =============================================================================
# JUDGE ORDER-BIAS AGGREGATION (V5.1)
# =============================================================================

def _aggregate_judge_bias(results_dir: str) -> dict:
    """
    Aggregate judge diagnostics across all sessions for the report.

    Reads judge_diagnostics from session JSONs and computes median order_effect,
    model_range, and uncertain rate per trait.
    """
    results_path = Path(results_dir)
    trait_order_effects = {t: [] for t in TRAITS}
    trait_model_ranges = {t: [] for t in TRAITS}
    trait_parse_errors = {t: [] for t in TRAITS}
    trait_uncertain_count = {t: 0 for t in TRAITS}
    total_sessions = 0

    for filepath in sorted(results_path.glob("session_*.json")):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        diag = data.get("judge_diagnostics")
        if not diag or not isinstance(diag, dict):
            continue

        total_sessions += 1
        per_trait = diag.get("per_trait", {})
        for trait in TRAITS:
            td = per_trait.get(trait, {})
            if "order_effect" in td:
                trait_order_effects[trait].append(td["order_effect"])
            if "model_range" in td:
                trait_model_ranges[trait].append(td["model_range"])
            if "parse_errors" in td:
                trait_parse_errors[trait].append(td["parse_errors"])
            if td.get("uncertain"):
                trait_uncertain_count[trait] += 1

    if total_sessions == 0:
        return {"error": "no sessions with judge_diagnostics"}

    per_trait = {}
    uncertain_traits = []
    for trait in TRAITS:
        oe = trait_order_effects[trait]
        mr = trait_model_ranges[trait]
        pe = trait_parse_errors[trait]
        uc = trait_uncertain_count[trait]
        n = len(oe)
        uncertain_rate = uc / total_sessions if total_sessions > 0 else 0

        per_trait[trait] = {
            "median_order_effect": round(float(np.median(oe)), 4) if oe else None,
            "median_model_range": round(float(np.median(mr)), 4) if mr else None,
            "total_parse_errors": int(sum(pe)) if pe else 0,
            "uncertain_count": uc,
            "uncertain_rate": round(uncertain_rate, 4),
            "n": n,
        }

        if uncertain_rate > 0.15:
            uncertain_traits.append(trait)

    return {
        "per_trait": per_trait,
        "total_sessions": total_sessions,
        "uncertain_traits": uncertain_traits,
    }


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
    bias_analysis: Optional[dict] = None,
    rq3_phase_controlled: Optional[dict] = None,
    judge_bias: Optional[dict] = None,
    bcfc_paired: Optional[dict] = None,
    bcfc_ablation: Optional[dict] = None,
    bcfc_cost: Optional[dict] = None,
    bon_ablation: Optional[dict] = None,
    bon_random: Optional[dict] = None,
    trajectory: Optional[dict] = None,
    pressure: Optional[dict] = None,
    diversity: Optional[dict] = None,
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

    # Phase-content caveat (Critique 6)
    lines.extend([
        "",
        "**Caveat (Phase-Content Confound):** The Early/Peak/Late windows differ in both "
        "time AND conversational content (introduction vs. conflict vs. resolution). "
        "Changes in personality signals across windows may reflect phase-appropriate "
        "behavior shifts rather than pure temporal decay. These results should be "
        "interpreted as *phase-specific fidelity* rather than *temporal decay* in the "
        "strict sense. See Section 4.3 of the research design for full discussion.",
    ])

    # Phase-controlled RQ3 (V5.1)
    if rq3_phase_controlled and "error" not in rq3_phase_controlled:
        lines.extend([
            "",
            "### Phase-Controlled RQ3 (Primary)",
            "",
            "Regresses |error| on phase_pos_norm + C(phase_name), controlling for content confound.",
            "",
            "| Trait | Beta(time) | p-value | Model | N |",
            "|-------|-----------|---------|-------|---|",
        ])
        for trait in TRAITS:
            data = rq3_phase_controlled.get(trait, {})
            if "error" in data:
                lines.append(f"| {TRAIT_NAMES[trait]} | - | - | - | {data['error']} |")
            else:
                sig = "*" if isinstance(data.get("p_time"), float) and data["p_time"] < 0.05 else ""
                lines.append(
                    f"| {TRAIT_NAMES[trait]} | {data.get('beta_time', '-')}{sig} | "
                    f"{data.get('p_time', '-')} | {data.get('model', '-')} | {data.get('n', '-')} |"
                )

    # Judge Order-Bias Analysis (V5.1)
    if judge_bias and "error" not in judge_bias:
        lines.extend([
            "",
            "---",
            "",
            "## Judge Order-Bias Analysis",
            "",
            "Per-trait diagnostics from dual-order evaluation (Order A: transcript→features, B: features→transcript).",
            "",
            "| Trait | Order Effect | Model Range | Parse Errors | Uncertain? |",
            "|-------|-------------|-------------|-------------|-----------|",
        ])
        per_trait = judge_bias.get("per_trait", {})
        for trait in TRAITS:
            data = per_trait.get(trait, {})
            oe = data.get("median_order_effect")
            mr = data.get("median_model_range")
            pe = data.get("total_parse_errors", 0)
            uc_rate = data.get("uncertain_rate", 0)
            is_uncertain = uc_rate > 0.15
            lines.append(
                f"| {TRAIT_NAMES[trait]} | {oe if oe is not None else '-'} | "
                f"{mr if mr is not None else '-'} | {pe} | "
                f"{'Yes ({:.0%})'.format(uc_rate) if is_uncertain else 'No'} |"
            )

        uncertain = judge_bias.get("uncertain_traits", [])
        if uncertain:
            lines.append(f"\n**Uncertain traits (>15% sessions):** {', '.join(TRAIT_NAMES.get(t, t) for t in uncertain)}")
        lines.append(f"\n**Total sessions analyzed:** {judge_bias.get('total_sessions', '?')}")

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
        if not isinstance(data, dict):
            lines.append(f"| {desc} | - | - | - | {data} |")
        elif "error" in data:
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

    # Positivity Bias Analysis (Critique 10)
    if bias_analysis and "error" not in bias_analysis:
        lines.extend([
            "",
            "---",
            "",
            "## Evaluator Positivity Bias Analysis",
            "",
            "Systematic signed error (inferred - assigned) per trait. Positive = overestimated.",
            "",
            "| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |",
            "|-------|----------|------|-----------------|-------------------|",
        ])
        for trait in TRAITS:
            data = bias_analysis.get("per_trait", {}).get(trait, {})
            if "error" in data:
                lines.append(f"| {TRAIT_NAMES[trait]} | - | - | - | - |")
            else:
                llm_b = data.get("llm_mean_bias", "-")
                llm_sig = "*" if data.get("llm_significant") else ""
                rb_b = data.get("rb_mean_bias", "-")
                specific = data.get("llm_specific_bias", "-")
                if isinstance(llm_b, float):
                    llm_b = f"{llm_b:+.4f}"
                if isinstance(rb_b, float):
                    rb_b = f"{rb_b:+.4f}"
                if isinstance(specific, float):
                    specific = f"{specific:+.4f}"
                lines.append(
                    f"| {TRAIT_NAMES[trait]} | {llm_b}{llm_sig} | "
                    f"{'Yes' if data.get('llm_significant') else 'No'} | "
                    f"{rb_b} | {specific} |"
                )

        summary = bias_analysis.get("summary", "")
        if summary:
            lines.extend(["", f"**{summary}**"])

    # Trait Confidence Matrix (V5.1)
    if rq3_phase_controlled or judge_bias or bias_analysis:
        tcm = trait_confidence_matrix(
            rq1, rq2, rq3_phase_controlled or {}, judge_bias or {}, bias_analysis or {},
        )
        lines.extend([
            "",
            "---",
            "",
            "## Trait Confidence Matrix",
            "",
            "Overall evidence quality per trait across all analysis dimensions.",
            "",
            "| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |",
            "|-------|--------------|-------------|-----------------|-----------------|---------------|",
        ])
        for trait in TRAITS:
            row = tcm.get(trait, {})
            lines.append(
                f"| {TRAIT_NAMES[trait]} | {row.get('detectability', '-')} | "
                f"{row.get('consistency', '-')} | {row.get('judge_robustness', '-')} | "
                f"{row.get('phase_stability', '-')} | {row.get('evaluator_bias', '-')} |"
            )

    # =================================================================
    # BCFC ANALYSIS SECTIONS
    # =================================================================

    if bcfc_paired and "error" not in bcfc_paired:
        lines.extend([
            "",
            "---",
            "",
            "## BCFC Paired Analysis",
            "",
            f"Within-subject comparison: {bcfc_paired.get('n_pairs', '?')} matched profile-scenario pairs.",
            "",
        ])

        # RQ1: Overall fidelity
        rq1_bc = bcfc_paired.get("rq1_overall", {})
        if rq1_bc:
            sig = "*" if rq1_bc.get("significant") else ""
            lines.extend([
                "### RQ1: Overall Fidelity Improvement",
                "",
                "| Metric | Baseline | BCFC | Delta |",
                "|--------|----------|------|-------|",
                f"| Mean MAE | {rq1_bc.get('baseline_mean_mae', '-')} | "
                f"{rq1_bc.get('bcfc_mean_mae', '-')} | "
                f"{rq1_bc.get('mae_reduction', '-')} |",
                "",
                f"Paired t-test: t={rq1_bc.get('paired_t_stat', '-')}, "
                f"p={rq1_bc.get('paired_t_p', '-')}{sig}, "
                f"Cohen's d={rq1_bc.get('cohens_d', '-')}, "
                f"N={rq1_bc.get('n_pairs', '-')}",
                "",
            ])

        # RQ2: Per-trait
        rq2_bc = bcfc_paired.get("rq2_per_trait", {})
        if rq2_bc:
            lines.extend([
                "### RQ2: Per-Trait Improvement",
                "",
                "| Trait | Baseline r | BCFC r | Delta r | Baseline MAE | BCFC MAE | Delta MAE | p-value |",
                "|-------|-----------|--------|---------|-------------|---------|-----------|---------|",
            ])
            for trait in TRAITS:
                data = rq2_bc.get(trait, {})
                if "error" in data:
                    lines.append(f"| {TRAIT_NAMES[trait]} | - | - | - | - | - | - | {data['error']} |")
                else:
                    sig = "*" if data.get("significant") else ""
                    lines.append(
                        f"| {TRAIT_NAMES[trait]} | {data.get('baseline_r', '-')} | "
                        f"{data.get('bcfc_r', '-')} | {data.get('r_improvement', '-'):+.4f} | "
                        f"{data.get('baseline_mae', '-')} | {data.get('bcfc_mae', '-')} | "
                        f"{data.get('mae_reduction', '-'):+.4f} | "
                        f"{data.get('paired_t_p', '-')}{sig} |"
                    )
            lines.append("")

        # RQ4: Variance
        rq4_bc = bcfc_paired.get("rq4_variance", {})
        if rq4_bc:
            lines.extend([
                "### RQ4: Within-Profile Variance Reduction",
                "",
                "| Trait | Baseline SD | BCFC SD | Reduction |",
                "|-------|-----------|---------|-----------|",
            ])
            for trait in TRAITS:
                data = rq4_bc.get(trait, {})
                if "error" in data:
                    lines.append(f"| {TRAIT_NAMES[trait]} | - | - | {data['error']} |")
                else:
                    lines.append(
                        f"| {TRAIT_NAMES[trait]} | {data.get('baseline_mean_sd', '-')} | "
                        f"{data.get('bcfc_mean_sd', '-')} | {data.get('sd_reduction', '-')} |"
                    )
            lines.append("")

    # BCFC Ablation
    if bcfc_ablation and "error" not in bcfc_ablation:
        lines.extend([
            "---",
            "",
            "## BCFC Ablation Analysis",
            "",
            f"Controller interventions across {bcfc_ablation.get('total_sessions', '?')} BCFC sessions.",
            "",
            f"- Total nudges: {bcfc_ablation.get('total_nudges', 0)}",
            f"- Total regenerations: {bcfc_ablation.get('total_regenerations', 0)}",
            f"- Mean nudge rate: {bcfc_ablation.get('mean_nudge_rate', 0):.1%}",
            f"- Mean regeneration rate: {bcfc_ablation.get('mean_regen_rate', 0):.1%}",
            "",
            "### Corrections by Trait",
            "",
            "| Trait | Nudge Count | Violation Count |",
            "|-------|------------|-----------------|",
        ])
        nudge_counts = bcfc_ablation.get("trait_nudge_counts", {})
        viol_counts = bcfc_ablation.get("trait_violation_counts", {})
        for trait in TRAITS:
            lines.append(
                f"| {TRAIT_NAMES[trait]} | {nudge_counts.get(trait, 0)} | "
                f"{viol_counts.get(trait, 0)} |"
            )

        vtype_counts = bcfc_ablation.get("violation_type_counts", {})
        if vtype_counts:
            lines.extend([
                "",
                "### Violation Types",
                "",
                "| Type | Count |",
                "|------|-------|",
            ])
            for vtype, count in vtype_counts.items():
                lines.append(f"| {vtype} | {count} |")

        lines.append("")

    # BCFC Cost Analysis (RQ5)
    if bcfc_cost and "error" not in bcfc_cost:
        lines.extend([
            "---",
            "",
            "## RQ5: BCFC Cost Overhead",
            "",
            f"N sessions: {bcfc_cost.get('n_bcfc_sessions', '?')}",
            "",
        ])
        nr = bcfc_cost.get("nudge_rate", {})
        rr = bcfc_cost.get("regeneration_rate", {})
        overhead = bcfc_cost.get("estimated_cost_overhead_pct")
        within = bcfc_cost.get("within_budget")

        lines.extend([
            "| Metric | Mean | Median | Max |",
            "|--------|------|--------|-----|",
            f"| Nudge rate | {nr.get('mean', '-')} | {nr.get('median', '-')} | {nr.get('max', '-')} |",
            f"| Regen rate | {rr.get('mean', '-')} | {rr.get('median', '-')} | {rr.get('max', '-')} |",
            "",
        ])
        if overhead is not None:
            status = "PASS" if within else "FAIL"
            lines.append(
                f"**Estimated cost overhead: {overhead}%** ({status}: "
                f"{'<' if within else '>'} 50% threshold for <1.5x budget)"
            )
        if bcfc_cost.get("mean_session_cost_usd") is not None:
            lines.append(
                f"**Mean session cost (USD): {bcfc_cost.get('mean_session_cost_usd')}**"
            )
        lines.append("")

    # BoN pool ablation
    if bon_ablation and "error" not in bon_ablation:
        lines.extend([
            "---",
            "",
            "## BoN Pool Ablation (Offline)",
            "",
            f"Pools analyzed: {bon_ablation.get('n_pools', '?')}",
            "",
            "| Policy | Contract Distance (avg) | Adequacy Penalty (avg) |",
            "|--------|--------------------------|------------------------|",
        ])
        cd = bon_ablation.get("contract_distance", {})
        ap = bon_ablation.get("adequacy_penalty", {})
        for key in ["full_score", "contract_only", "relevance_only", "first", "random_expected"]:
            lines.append(
                f"| {key} | {cd.get(key, '-')} | {ap.get(key, '-')} |"
            )
        lines.append("")

    if bon_random and "error" not in bon_random:
        lines.extend([
            "---",
            "",
            "## BoN-Random Compute-Control Subset",
            "",
            f"N (BoN-random): {bon_random.get('n_bon_random', '?')} | "
            f"Baseline: {bon_random.get('n_baseline', '?')} | BCFC: {bon_random.get('n_bcfc', '?')}",
            "",
            "| Group | Mean MAE |",
            "|-------|----------|",
            f"| BoN-random | {bon_random.get('bon_random_mean_mae', '-')} |",
            f"| Baseline | {bon_random.get('baseline_mean_mae', '-')} |",
            f"| BCFC | {bon_random.get('bcfc_mean_mae', '-')} |",
            "",
        ])

    if trajectory and "error" not in trajectory:
        lines.extend([
            "---",
            "",
            "## Trajectory Continuity Metrics",
            "",
            "| Metric | Baseline | BCFC |",
            "|--------|----------|------|",
            f"| Avg Appropriateness | {trajectory.get('baseline_avg_appropriateness', '-')} | {trajectory.get('bcfc_avg_appropriateness', '-')} |",
            f"| Avg Coherence | {trajectory.get('baseline_avg_coherence', '-')} | {trajectory.get('bcfc_avg_coherence', '-')} |",
            "",
        ])

    if pressure and "error" not in pressure:
        lines.extend([
            "---",
            "",
            "## Pressure Manipulation Check (Crisis Only)",
            "",
            f"N High: {pressure.get('n_high', '?')} | N Low: {pressure.get('n_low', '?')}",
            "",
            "| Metric | High Pressure | Low Pressure |",
            "|--------|---------------|--------------|",
            f"| Perceived Pressure | {pressure.get('high_perceived', '-')} | {pressure.get('low_perceived', '-')} |",
            f"| Stress Index | {pressure.get('high_stress_index', '-')} | {pressure.get('low_stress_index', '-')} |",
            "",
        ])

    if diversity and "error" not in diversity:
        lines.extend([
            "---",
            "",
            "## Candidate Diversity",
            "",
            f"Pools analyzed: {diversity.get('pools', '-')}",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            f"| Avg Jaccard overlap | {diversity.get('avg_jaccard_overlap', '-')} |",
            f"| Avg diversity (1 - overlap) | {diversity.get('avg_diversity', '-')} |",
            "",
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

    # Remap non-standard conditions to "main" so all RQ analyses work
    if "condition" in df.columns:
        non_standard = ~df["condition"].isin(["main", "baseline_a", "baseline_b"])
        if non_standard.any():
            print(f"  Remapping {non_standard.sum()} sessions with condition='{df.loc[non_standard, 'condition'].iloc[0]}' -> 'main'")
            df.loc[non_standard, "condition"] = "main"

    print("\nRQ1: Personality Fidelity...")
    rq1 = rq1_analysis(df)
    rq1 = apply_fdr_correction(rq1)

    # Add bootstrap CIs for RQ1 correlations
    main = df[df["condition"] == "main"]
    for trait in TRAITS:
        a_col = f"assigned_{trait}"
        i_col = f"inferred_{trait}"
        valid = main.dropna(subset=[a_col, i_col])
        if len(valid) >= 10:
            errors = np.abs(valid[a_col].values - valid[i_col].values)
            mae_est, mae_lo, mae_hi = bootstrap_ci(errors)
            rq1["per_trait"].setdefault(trait, {})["mae_ci95"] = [round(mae_lo, 4), round(mae_hi, 4)]

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

    print("Expanded feature-trait validation (30 features)...")
    feat_val = expanded_feature_trait_validation(df)

    print("Inter-model agreement analysis...")
    model_agree = inter_model_agreement(df)

    print("Positivity bias analysis (Critique 10)...")
    bias = positivity_bias_analysis(df)

    # Phase-controlled RQ3 (V5.1)
    rq3_pc = {}
    if temporal_path and Path(temporal_path).exists():
        print("RQ3b: Phase-controlled temporal analysis (V5.1)...")
        with open(temporal_path) as f:
            window_results_pc = json.load(f)
        rq3_pc = phase_normalized_rq3(window_results_pc)
    else:
        print("RQ3b: Skipped (no temporal data)")

    # Judge order-bias aggregation (V5.1)
    judge_bias = _aggregate_judge_bias(results_dir)

    # BCFC analysis (if BCFC sessions exist)
    bcfc_paired_result = None
    bcfc_ablation_result = None
    bcfc_cost_result = None
    bon_ablation_result = None
    bon_random_result = None
    trajectory_result = None
    pressure_result = None

    has_bcfc = "intervention" in df.columns and df["intervention"].isin(["bcfc", "bcfc_v3"]).any()
    if has_bcfc:
        print("\nBCFC Paired Analysis (RQ1-RQ4)...")
        bcfc_paired_result = bcfc_paired_analysis(df)

        print("BCFC Ablation Analysis...")
        bcfc_ablation_result = bcfc_ablation_analysis(results_dir)

        print("BCFC Cost Analysis (RQ5)...")
        bcfc_cost_result = bcfc_cost_analysis(df)
    else:
        print("\nNo BCFC sessions detected — skipping BCFC analysis")

    # BoN pool ablation + compute-control subset
    print("BoN pool ablation analysis...")
    bon_ablation_result = bon_pool_ablation(results_dir)
    try:
        from experiment.bcfc_config import DEFAULT_CONFIG
        bon_random_result = bon_random_analysis(df, scenario_id=DEFAULT_CONFIG.bon_random_scenario)
    except Exception:
        bon_random_result = bon_random_analysis(df)

    # Trajectory and pressure analyses
    print("Trajectory analysis...")
    trajectory_result = trajectory_analysis(df)
    print("Pressure manipulation check...")
    pressure_result = pressure_manipulation_check(df)
    print("Candidate diversity analysis...")
    diversity_result = candidate_diversity_analysis(results_dir)

    # Generate report
    report = generate_report(
        rq1, rq2, rq3, rb, dual_eval, feat_val, model_agree, bias,
        rq3_phase_controlled=rq3_pc,
        judge_bias=judge_bias,
        bcfc_paired=bcfc_paired_result,
        bcfc_ablation=bcfc_ablation_result,
        bcfc_cost=bcfc_cost_result,
        bon_ablation=bon_ablation_result,
        bon_random=bon_random_result,
        trajectory=trajectory_result,
        pressure=pressure_result,
        diversity=diversity_result,
    )

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
        "rq3_phase_controlled": rq3_pc,
        "judge_bias": judge_bias,
        "rule_based": rb,
        "dual_evaluation": dual_eval,
        "feature_trait_validation": feat_val,
        "inter_model_agreement": model_agree,
        "positivity_bias": bias,
        "bcfc_paired": bcfc_paired_result,
        "bcfc_ablation": bcfc_ablation_result,
        "bcfc_cost": bcfc_cost_result,
        "bon_ablation": bon_ablation_result,
        "bon_random": bon_random_result,
        "trajectory": trajectory_result,
        "pressure": pressure_result,
        "diversity": diversity_result,
    }
    with open(raw_path, "w") as f:
        json.dump(raw_results, f, indent=2, default=str)
    print(f"Raw results saved to {raw_path}")

    # Print summary
    print(f"\n{'='*60}")
    print(report)
    print(f"{'='*60}")
