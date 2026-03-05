# V5.1 Hardening Plan: Research-Gap-Driven Upgrades With Code-Level Spec

## Summary
Your current codebase already includes major upgrades (13 profiles, 30 features, positivity-bias analysis).  
This plan targets the **remaining high-impact gaps** from external research: judge-order bias, strict leakage auditing, phase-controlled temporal analysis, uncertainty escalation, and human-anchor triangulation.

This is a full replacement plan with exact file-level changes, snippets, formulas, thresholds, and acceptance gates.

## Current-State Snapshot (Already Done)
1. `experiment/profiles.py`: 13 profiles and interaction notes are present.
2. `experiment/behavioral_features.py`: 30-feature extraction exists.
3. `evaluation/rule_based_evaluator.py`: C/O/N/A formulas updated for new features.
4. `experiment/analysis.py`: positivity bias + RQ3 caveat already implemented.
5. Remaining gaps are now mostly **robustness + inference validity**, not base pipeline completeness.

## Important Public Interface / Schema Changes

### Session result JSON (`experiment/results/session_*.json`)
Add these top-level keys:
```json
{
  "schema_version": 3,
  "quality_audit": {
    "hard_overlap_count": 0,
    "soft_overlap_count": 2,
    "hard_overlaps": [],
    "soft_overlaps": ["plan", "anxious"],
    "pass": true
  },
  "per_model_order_scores": {
    "openai/gpt-4o-mini": {
      "O": {"A": 0.62, "B": 0.58},
      "C": {"A": 0.71, "B": 0.69}
    }
  },
  "judge_diagnostics": {
    "per_trait": {
      "O": {"order_effect": 0.03, "model_range": 0.18, "parse_errors": 0, "uncertain": false}
    },
    "uncertain_traits": ["A"],
    "uncertain_reasons": {"A": ["model_range>0.30"]}
  }
}
```

### `PersonalityAssessment` (`utils/models.py`)
Add optional fields:
```python
per_model_order_scores: dict[str, dict[str, dict[str, float]]] = field(default_factory=dict)
judge_diagnostics: dict = field(default_factory=dict)
```

## Implementation Plan (Decision Complete)

## Phase 1: Leakage Audit Hardening (Critical)

### Files
1. `experiment/validation/overlap_audit.py` (new)
2. `experiment/run_experiment.py` (new `--audit-overlap` flag)
3. `experiment/batch_runner.py` (embed audit output into session JSON)

### Justification (with citations)
This phase is an internal-validity safeguard against instruction-to-measurement contamination and method bias. If lexical cues are shared between instruction and detector/evaluator channels, fidelity can be overstated due to circular signal pickup rather than genuine behavior.  
**Citations:** [R1], [R2], [R13]

### Logic
Use phrase-level overlap checks with **hard vs soft** categories:
1. Hard overlap: phrase length >= 2 words and exact occurrence in instructions.
2. Soft overlap: single-word overlaps that are semantically broad (e.g., `plan`, `anxious`) and do not fail run by default.

### Snippet
```python
# experiment/validation/overlap_audit.py
MIN_HARD_NGRAM = 2
SOFT_WORD_ALLOWLIST = {"plan", "anxious", "nervous", "stress", "risk"}

def audit_overlap(instructions_text: str, phrase_lists: dict[str, list[str]]) -> dict:
    hard, soft = [], []
    text = instructions_text.lower()
    for src, phrases in phrase_lists.items():
        for p in phrases:
            p = p.strip().lower()
            if not p:
                continue
            hit = p in text
            if not hit:
                continue
            token_count = len(p.split())
            if token_count >= MIN_HARD_NGRAM:
                hard.append((src, p))
            elif p not in SOFT_WORD_ALLOWLIST:
                hard.append((src, p))
            else:
                soft.append((src, p))
    return {
        "hard_overlap_count": len(hard),
        "soft_overlap_count": len(soft),
        "hard_overlaps": [f"{s}:{p}" for s, p in hard],
        "soft_overlaps": [f"{s}:{p}" for s, p in soft],
        "pass": len(hard) == 0,
    }
```

### Gate
1. Hard overlap must be 0 before pilot/full runs.
2. Soft overlaps are logged only.

---

## Phase 2: Judge Order-Bias Control (LLM-as-a-Judge Robustness)

### Files
1. `evaluation/trait_evaluator.py`
2. `utils/models.py`
3. `experiment/batch_runner.py`
4. `experiment/analysis.py` (new `judge_bias_analysis`)

### Justification (with citations)
Order sensitivity and evaluator inconsistency are known failure modes in LLM-as-a-judge pipelines. Two-order evaluation and robust aggregation reduce position effects and improve reliability.  
**Citations:** [R1], [R2], [R3], [R4], [R5]

### Exact logic
For each trait:
1. Build two prompts:
   - Order A: transcript -> features.
   - Order B: features -> transcript.
2. Call `client.generate_ensemble()` for both orders.
3. Per model + trait:
   - Parse score_A and score_B.
   - model_score = median(score_A, score_B).
4. Final trait score = median(model_score across models).
5. Diagnostics:
   - `order_effect = median(|score_A-score_B| across models)`
   - `model_range = max(model_score)-min(model_score)`
   - `uncertain=True` if `order_effect>0.12` or `model_range>0.30` or `parse_errors>=2`.

### Snippet
```python
# inside _evaluate_trait_ensemble(...)
prompt_a = build_prompt(order="A", **kwargs)
prompt_b = build_prompt(order="B", **kwargs)

resp_a, resp_b = await asyncio.gather(
    self.client.generate_ensemble(prompt=prompt_a, system_instruction=system_instruction, temperature=0.3, max_tokens=3000),
    self.client.generate_ensemble(prompt=prompt_b, system_instruction=system_instruction, temperature=0.3, max_tokens=3000),
)

# align by model name
scores_by_model = {}
for model, raw in resp_a:
    scores_by_model.setdefault(model, {})["A"] = self._parse_trait_response(raw, trait).score
for model, raw in resp_b:
    scores_by_model.setdefault(model, {})["B"] = self._parse_trait_response(raw, trait).score

model_scores = []
order_deltas = []
for model, d in scores_by_model.items():
    if "A" in d and "B" in d:
        s = statistics.median([d["A"], d["B"]])
        model_scores.append(s)
        order_deltas.append(abs(d["A"] - d["B"]))

trait_score = statistics.median(model_scores)
order_effect = statistics.median(order_deltas) if order_deltas else 0.0
model_range = (max(model_scores)-min(model_scores)) if model_scores else 1.0
uncertain = order_effect > 0.12 or model_range > 0.30
```

### Gate
1. Pilot median order effect per trait < 0.08.
2. Uncertain trait rate < 15% of trait evaluations.

---

## Phase 3: Phase-Controlled RQ3 (Fix temporal confound analytically)

### Files
1. `experiment/temporal_analysis.py` (add phase-level output)
2. `experiment/analysis.py` (add `phase_normalized_rq3`)
3. `requirements.txt` (add `statsmodels>=0.14.0`)

### Justification (with citations)
Sequential behavior studies show degradation over interaction length, but time-based claims are confounded when conversational phase content changes. A phase-controlled model is necessary to separate temporal drift from phase-appropriate behavior shifts.  
**Citations:** [R8], [R11]

### Data change
In temporal output, include per-phase vectors:
```json
"phases": [
  {"phase_name":"INTRODUCTION","phase_index":1,"phase_pos_norm":0.2,"inferred_vector":{"O":0.52,...}},
  {"phase_name":"CONFLICT","phase_index":3,"phase_pos_norm":0.6,"inferred_vector":{"O":0.47,...}}
]
```

### Model
For each trait, fit:
`abs_error ~ phase_pos_norm + C(phase_name)`  
with random intercept by `session_key` (fallback OLS cluster by session on convergence failure).

### Snippet
```python
# experiment/analysis.py
import statsmodels.formula.api as smf

def phase_normalized_rq3(df_phase):
    out = {}
    for trait in ["O","C","E","A","N"]:
        d = df_phase.dropna(subset=[f"assigned_{trait}", f"inferred_{trait}"]).copy()
        d["abs_error"] = (d[f"assigned_{trait}"] - d[f"inferred_{trait}"]).abs()
        try:
            m = smf.mixedlm("abs_error ~ phase_pos_norm + C(phase_name)", d, groups=d["session_key"])
            fit = m.fit(reml=False, method="lbfgs", maxiter=200)
            beta = fit.params.get("phase_pos_norm", np.nan)
            pval = fit.pvalues.get("phase_pos_norm", np.nan)
            out[trait] = {"beta_time": float(beta), "p_time": float(pval), "model": "mixedlm"}
        except Exception:
            ols = smf.ols("abs_error ~ phase_pos_norm + C(phase_name)", d).fit(cov_type="cluster", cov_kwds={"groups": d["session_key"]})
            out[trait] = {"beta_time": float(ols.params.get("phase_pos_norm", np.nan)), "p_time": float(ols.pvalues.get("phase_pos_norm", np.nan)), "model": "ols_cluster_fallback"}
    return out
```

### Gate
1. Report must include naive RQ3 and phase-controlled RQ3 side-by-side.
2. Final interpretation uses phase-controlled result as primary; naive as supplementary.

---

## Phase 4: Uncertainty Escalation Queue (Trust-or-Escalate pattern)

### Files
1. `experiment/batch_runner.py`
2. `experiment/analysis.py`
3. `experiment/results/uncertain_queue.csv` (generated artifact)

### Justification (with citations)
Not all model judgments should be treated equally trustworthy. Escalation pathways for uncertain cases follow recent work on selective trust, model-jury disagreement handling, and evaluator reliability controls.  
**Citations:** [R2], [R4], [R5]

### Logic
If trait uncertain (from Phase 2), write queue row:
`session_key, trait, reason, score, assigned, scenario_id, profile_id`.

### Snippet
```python
if diag["uncertain"]:
    uncertain_rows.append({
        "session_key": spec.session_key,
        "trait": trait_abbrev,
        "reason": ",".join(reasons),
        "assigned": assigned_vector.get(trait_abbrev) if assigned_vector else None,
        "inferred": inferred_vector.get(trait_abbrev),
        "scenario_id": spec.scenario_id,
        "profile_id": spec.profile_id,
    })
```

### Gate
1. Queue generated automatically after analysis.
2. Queue drives human-anchor sampling (Phase 5).

---

## Phase 5: Human-Anchor Triangulation (Small but decisive external validity)

### Files
1. `experiment/human_anchor/sample_sessions.py` (new)
2. `experiment/human_anchor/rubric.md` (new)
3. `experiment/human_anchor/aggregate_ratings.py` (new)
4. `experiment/analysis.py` (ingest merged human ratings CSV)

### Justification (with citations)
A compact human-annotation anchor improves interpretability and construct validation by triangulating automated judgments with independent raters, consistent with multitrait-multimethod logic and recent personality-inference evaluations.  
**Citations:** [R13], [R15], [R16]

### Sampling protocol
Select exactly 32 sessions:
1. 16 from `uncertain_queue.csv` (highest uncertainty first).
2. 16 stratified random from confident sessions.
3. Balance by scenario and trait extremes.

### Rater output schema
`session_key,O,C,E,A,N,rater_id,notes`

### Agreement + triangulation
1. Inter-rater reliability: ICC(2,k) per trait.
2. Correlate human mean vs LLM inferred and vs rule-based.

### Gate
1. Human ICC >= 0.60 for at least 3 traits.
2. Include triangulation table in final report even if low agreement.

---

## Phase 6: Multiplicity and Uncertainty-Aware Reporting

### Files
1. `experiment/analysis.py`
2. `experiment/analysis_report.md` output format update

### Justification (with citations)
Multiple trait-level tests increase false-positive risk; FDR control and bootstrap intervals are standard safeguards for more defensible effect claims and uncertainty reporting.  
**Citations:** [R17], [R18], [R2]

### Logic
1. Apply FDR-BH correction to trait-family p-values (RQ1/RQ3/bias analyses).
2. Add bootstrap CI (2000 resamples, fixed seed 42) for key effects.
3. Add a trait confidence matrix:
   - detectability,
   - consistency,
   - judge robustness,
   - phase-controlled stability,
   - human-anchor agreement.

### Snippet
```python
from statsmodels.stats.multitest import multipletests

pvals = [results[t]["p_value"] for t in TRAITS if "p_value" in results[t]]
rej, qvals, _, _ = multipletests(pvals, alpha=0.05, method="fdr_bh")
```

### Gate
1. No claim labeled “strong evidence” unless both raw p<0.05 and q<0.05.
2. Confidence matrix appears in report.

---

## CLI / Workflow Updates

### `experiment/run_experiment.py`
1. Add `--audit-overlap`.
2. Add `--pilot-v5` with fixed session matrix:
   - Profiles: `assertive_leader`, `passive_avoider`, `anxious_perfectionist`, `withdrawn_critic`
   - Scenarios: `resource_conflict`, `crisis_management`
   - Reps: 1
   - Total main pilot: 8 (+ optional 2 baseline_a + 2 baseline_b = 12)

### Commands
```bash
python -m experiment.run_experiment --audit-overlap
python -m experiment.run_experiment --pilot-v5 --output-dir experiment/results_v5_pilot
python -m experiment.run_experiment --temporal --output-dir experiment/results_v5_pilot
python -m experiment.run_experiment --analyze --output-dir experiment/results_v5_pilot
```

---

## Test Cases and Scenarios

### Unit tests (`experiment/tests/`)
1. `test_overlap_audit.py`: hard overlap detection, soft allowlist behavior, fail/pass logic.
2. `test_trait_ensemble_order_bias.py`: dual-order aggregation correctness, uncertainty flag thresholds.
3. `test_phase_normalized_rq3.py`: mixed model success + OLS fallback behavior.
4. `test_result_schema_v3.py`: ensure all new keys exist and types are correct.

### Integration tests
1. Smoke pilot run writes `schema_version=3`.
2. At least one session has populated `per_model_order_scores`.
3. Temporal output includes `phases` list with `phase_pos_norm`.
4. Analysis report includes:
   - RQ3 phase-controlled table,
   - judge bias table,
   - uncertainty queue summary,
   - FDR-adjusted significance marks.

### Acceptance thresholds
1. Hard overlap count = 0.
2. Median order effect < 0.08.
3. Uncertain trait rate < 15%.
4. RQ3 section includes both naive and phase-controlled estimates.
5. Human-anchor section present with ICC and correlation tables.

---

## Assumptions and Defaults
1. Keep DeepSeek V3 as generation model for this cycle.
2. Keep 5-model ensemble evaluators unchanged.
3. Median remains the primary aggregator (order then model).
4. Add `statsmodels` dependency for mixed-effects; fallback OLS ensures robustness.
5. If human annotation bandwidth is limited, minimum viable anchor set is 20 sessions (not below 20).

---

## References (Citation Keys)

- **[R1]** Wang, P. et al. (2023). *Large Language Models are not Fair Evaluators*. arXiv. https://arxiv.org/abs/2305.17926
- **[R2]** Stureborg, R., Alikaniotis, D., & Suhara, Y. (2024). *Large Language Models are Inconsistent and Biased Evaluators*. arXiv. https://arxiv.org/abs/2405.01724
- **[R3]** Shi, L. et al. (2025). *Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge*. arXiv. https://arxiv.org/abs/2406.07791
- **[R4]** Verga, P. et al. (2024). *Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models*. arXiv. https://arxiv.org/abs/2404.18796
- **[R5]** Jung, J., Brahman, F., & Choi, Y. (2024). *Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement*. arXiv. https://arxiv.org/abs/2407.18370
- **[R8]** Li, R. et al. (2025). *How Far are LLMs from Being Our Digital Twins? A Benchmark for Persona-Based Behavior Chain Simulation*. Findings of ACL 2025. https://aclanthology.org/2025.findings-acl.813/
- **[R11]** Abdulhai, M. et al. (2025). *Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning*. arXiv. https://arxiv.org/abs/2511.00222
- **[R13]** Campbell, D. T., & Fiske, D. W. (1959). *Convergent and discriminant validation by the multitrait-multimethod matrix*. Psychological Bulletin, 56(2), 81-105. https://pubmed.ncbi.nlm.nih.gov/13634291/
- **[R15]** Niculae, V. et al. (2025). *Can LLMs Infer Personality from Real World Conversations?* arXiv. https://arxiv.org/abs/2507.14355
- **[R16]** (2026). *Assessing personality using zero-shot generative AI scoring*. Nature Human Behaviour. https://www.nature.com/articles/s41562-025-02389-x
- **[R17]** Benjamini, Y., & Hochberg, Y. (1995). *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*. Journal of the Royal Statistical Society: Series B, 57(1), 289-300. https://www.jstor.org/stable/2346101
- **[R18]** Efron, B., & Tibshirani, R. J. (1994). *An Introduction to the Bootstrap*. CRC Press. https://www.routledge.com/9780412042317
