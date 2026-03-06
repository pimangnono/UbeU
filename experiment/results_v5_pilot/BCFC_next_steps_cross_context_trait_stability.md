# BCFC Next Steps — Cross‑Context Trait Stability (O/C Focus)

> Goal reminder (your paper’s success criterion):  
> **Assigned OCEAN stays stable under high‑pressure multi‑agent interaction** so you can run social observation simulations (marketing/negotiation/policy) without “persona drift”.

This memo answers: **“Do we ‘improve O/C’ by changing scenarios or by strengthening the system?”** and gives a **production‑implementable** upgrade path (API‑only, no fine‑tuning).

---

## 0) The key clarification: Scenario ≠ Solution

### What scenario changes are for (research)
Scenarios are a **test suite**: they decide *what evidence exists* to *measure* a trait. If a scenario never creates a moment where “creative exploration” is relevant, you can’t reliably *observe* Openness—even if the agent is truly high‑O.

### What your product needs (system)
Your product needs **cross‑context stability**:
1) **Latent trait state doesn’t drift** even when the environment is adversarial/high‑pressure.  
2) **Trait-consistent policy** appears *whenever the situation allows it*, without forcing unnatural behavior.

So:  
- **Do not “solve O” by making O‑friendly scenarios.**  
- **Do use scenarios to detect which contexts suppress expression** and to build robust controllers that work across contexts.

---

## 1) Why “O/C look weak” can be *real* even if the system is fine

In interactionist personality theory, **traits are expressed in response to trait‑relevant cues**, and **strong situations** constrain everyone into similar behavior. This means:
- In *strong* situations (tight deadlines, strict constraints), **variance shrinks** and trait signal can compress.
- In *weak/ambiguous* situations, traits differentiate behavior more.

**Implication for BCFC:**  
If your controller tries to enforce high‑O behaviors equally in every turn, you risk **unrealistic behavior** and **trajectory damage**. Instead, you need **situation‑aware activation**.

---

## 2) Production‑level upgrades (API‑only) to make traits stable across “any situation”

Below are 5 concrete system upgrades. They are designed to improve **general robustness**, not scenario‑specific performance.

### Upgrade 1 — Situation‑Aware Contract Scheduling (Activation‑Gated Control)

**Problem it solves:**  
Contract distance can collapse into “always minimize O/C counts”, which breaks realism in strong situations.

**Solution:**  
Add a *Situation Interpreter* that outputs an **activation mask** `a_t(trait) ∈ [0,1]` each turn (or phase window):
- `a_t(O)` high when: ambiguity, reframing opportunity, options requested, “why/what-if”, strategy discussions  
- `a_t(C)` high when: owner/deadline/dependency, execution planning, handoffs, accountability

Then scale contract penalties:
- `effective_contract_distance = Σ_i (w_i * a_t(trait_of_i) * distance_i)`
- Hard constraints apply only when `a_t(trait)` ≥ `hard_activation_threshold`

**Implementation notes**
- Make interpreter **rule-based first** (dialogue act + phase + keyword cues).
- Store `activation_mask` in logs for audit.

**Benefit**
- More realistic: prevents forcing O into “triage now” moments.
- More robust: stabilizes traits by focusing control where traits can be expressed.

**Risk**
- If activation mask is too strict, you “hide” failures by not applying pressure.
- Mitigation: report *both* raw and activation‑weighted drift; keep a small baseline penalty even when activation is low.

---

### Upgrade 2 — Lexicographic / Two‑Stage BoN (Fix “contract_only collapse”)

**Problem it solves:**  
Your ablation shows **full_score ≈ contract_only**. That’s a sign the reranker is effectively ignoring adequacy/relevance.

**Solution:**  
Use a **two‑stage selection** instead of a single linear weighted sum.

**Stage A: Adequacy gate (persona‑neutral)**
Reject or heavily penalize candidates that fail:
- direct question not answered
- contradiction with last 1–2 selected turns
- refusal/empty/too short
- violates conversation role constraints

**Stage B: Contract optimization among adequate candidates**
Pick the candidate with minimum activation‑weighted contract distance.

**Stage C: Tie‑breakers**
Use relevance and redundancy only as tie‑breakers inside a small epsilon band:
- if |d1 − d2| < δ, choose higher relevance / lower redundancy.

**Pseudocode**
```python
adequate = [c for c in pool if adequacy(c) >= tau]
if not adequate:
    adequate = pool  # fail-open

best = argmin(adequate, key=contract_distance)
near = [c for c in adequate if abs(contract_distance(c)-contract_distance(best)) < delta]
best = argmax(near, key=relevance_minus_redundancy)
return best
```

**Benefit**
- Prevents scoring collapse.
- Keeps trajectory stable (adequacy-first).

**Risk**
- If adequacy gate is too strict, you reduce diversity and overfit to “safe” responses.
- Mitigation: `fail-open` + log gate rejections + tune τ on pilot only.

---

### Upgrade 3 — Facet‑Level Policy Library (Behavior ≠ Surface Counts)

**Problem it solves:**  
O/C are not just “idea_count” or “planning_count”. Surface features can be brittle across contexts.

**Solution:**  
Move from “count-based” features to **facet‑level behavioral policies** and treat them as *actions*.

Example policies (simplified):
- **Openness facets → behaviors**
  - Ideas/curiosity → ask 1 clarifying “why/what-if” per phase if not disruptive
  - Reframing → propose 1 alternative framing when disagreement detected
  - Tradeoff exploration → articulate a 2‑option tradeoff before decision

- **Conscientiousness facets → behaviors**
  - Order → summarize decisions and next steps
  - Dutifulness → assign owner / confirm responsibility
  - Deliberation → request missing info before committing

**How to enforce without fine‑tuning**
- Add a **Policy Controller** that tracks whether each phase satisfied minimal required policy acts.
- Use the BoN reranker to prefer candidates that satisfy missing policy acts *when activation is high*.

**Benefit**
- Stronger cross-context generalization.
- Matches how humans express traits: **different surface actions, consistent deeper policy**.

**Risk**
- Over-prescriptive policies can make agents feel scripted.
- Mitigation: treat policies as “minimum commitments” + randomize phrasing via style slots.

---

### Upgrade 4 — Memory for Stability: “Commitment & Belief Ledger” (Graphiti optional)

**Problem it solves:**  
Long multi‑turn interactions drift because the agent forgets what it committed to / what it believes.

**Minimum viable memory (recommended first)**
Maintain a compact structured block per agent:
```json
{
  "traits": {"O":0.7,"C":0.8,"E":0.3,"A":0.5,"N":0.2},
  "commitments":[{"task":"X","owner":"me","deadline":"...","status":"open"}],
  "positions":[{"topic":"Y","stance":"...","confidence":0.6}],
  "relationships":[{"agent":"Z","valence":"neutral","trust":0.4}]
}
```
Update it every 1–2 turns via a cheap deterministic parser + occasional LLM summarizer.

**Graphiti evaluation (when to use)**
Graphiti is an **open-source temporal knowledge-graph memory** designed for AI agents, built to incrementally update entities/relationships and query historical states.  
It is compelling if you want: multi-session continuity, relationship graphs, long-horizon simulations, and auditability.

**When Graphiti helps BCFC**
- C-heavy stability: commitments/dependencies become graph edges.
- Multi-agent simulation: relationships and shared facts become queryable state.

**Costs / risks**
- Requires running Neo4j (infra/ops).
- Retrieval bugs can inject wrong context; needs strong observability.
- Privacy/security and memory bloat need policies (TTL, redaction).

**Recommendation**
- For the paper + near-term product: ship **ledger memory first**.  
- Add Graphiti only if you need multi-episode simulations where relationship/history queries matter.

---

### Upgrade 5 — Evaluation that matches your real goal (State Stability + Conditional Expression)

**Problem it solves:**  
Raw “overall MAE/r” can mislead when situations suppress trait expression.

**Add two evaluation slices**
1) **State Stability under pressure**  
   - variance of inferred traits across turns (or phases) within a session
   - drift rate over time
2) **Opportunity‑conditional fidelity**  
   - compute fidelity only on turns with activation ≥ threshold
   - report coverage: what fraction of turns were “O-opportunity / C-opportunity”

**Why this is not cheating**
This matches interactionist theory: you’re measuring traits **when the situation allows them**, while separately ensuring the latent state doesn’t drift even when it can’t be expressed.

---

## 3) Recommended experiment order (minimal cost, maximum signal)

### Phase 0 — Measurement sanity + instrumentation (must-have)
**Implement**
- Candidate pool logging always-on
- Adequacy gate metrics (answer rate, contradiction rate)
- Activation mask logs (O/C opportunity)

**Success criteria**
- Logging complete (no empty pools)
- Judges stable enough to compare A/B (low parse errors, uncertainty tracked)

---

### Phase 1 — Reranker collapse fix (Two-stage BoN)
**Run**
- A/B mini: baseline vs bcfc_v5 on 3 profiles × 3 scenarios (with one strong + one weak situation)
- Use identical candidate pools where possible for offline counterfactual.

**Success criteria**
- full_score ≠ contract_only (ablation divergence)
- no trajectory tax (appropriateness/coherence not worse than baseline by >0.05)
- hard violations remain < 25%

---

### Phase 2 — Cross-context stress test (mid-check)
**Run**
- 20-session mid-check across mixed scenarios (not O/C-friendly only)
- include at least 1 “strong pressure” and 1 “weak/ambiguous” scenario

**Success criteria**
- **Primary:** activation-conditional MAE improves or stays equal while state stability improves
- **Secondary:** overall MAE improves by ≥ small effect size (define before running)
- cost overhead bounded

---

### Phase 3 — Full run (paper)
Proceed only after Phase 2 passes.

**Paper endpoint**
- Report both unconditional and conditional metrics
- Provide pressure manipulation checks + situation strength diagnostics

---

## 4) What you should NOT do next
- Don’t tune by rewriting scenarios to make O easy. Treat that as test-suite work only.
- Don’t add heavy memory graphs before the reranker collapse is fixed.
- Don’t freeze hyperparameters if your selection policy is effectively “contract-only”.

---

## 5) References (for your paper)
- Tett, R. P., Toich, M. J., & Ozkum, S. B. (2021). *Trait Activation Theory: A Review of the Literature and Applications to Five Lines of Personality Dynamics Research.* Annual Review of Organizational Psychology and Organizational Behavior, 8, 199–233. doi:10.1146/annurev-orgpsych-012420-062228
- García-Arroyo, J., et al. (2020). *Understanding the Relationship between Situational Strength and Burnout: A Multi-Sample Analysis.* (For strong situation hypothesis discussion).  
- Abdulhai, M., Cheng, R., Clay, D., Althoff, T., Levine, S., & Jaques, N. (2025). *Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning.* arXiv:2511.00222
- Rasmussen, P., Paliychuk, P., Beauvais, T., Ryan, J., & Chalef, D. (2025). *Zep: A Temporal Knowledge Graph Architecture for Agent Memory.* arXiv:2501.13956
- getzep/graphiti (2025). *Graphiti: Build Real-Time Knowledge Graphs for AI Agents.* GitHub repository.
- Chalef, D. (2025). *Graphiti: Knowledge Graph Memory for an Agentic World.* Neo4j developer blog.
- Jiang, D., Li, Y., Li, G., & Li, B. (2026). *MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents.* arXiv:2601.03236

---
