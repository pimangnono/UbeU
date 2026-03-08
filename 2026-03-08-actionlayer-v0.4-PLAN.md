# Action Layer v0.4 Plan

## Goal

`v0.4`의 목표는 `Action Layer v0`의 남은 병목인 `same-phase action family convergence`를 줄이는 것이다.  
현재 `v0.3`까지로:

- `structured_action_validity`
- `owner_resolution`
- `state_transition_coherence`
- `planned_action_coverage`
- `action_plan_alignment`

은 충분히 높다. 남은 문제는 특히 `NEGOTIATION` phase에서 여러 actor가 같은 action family로 몰리면서 persona drift가 다시 커지는 점이다.

## Design Direction

### 1. Script-driven metadata

`SimulationScript.metadata`에 아래를 명시적으로 넣는다.

- `phase_action_policies`
  - `diversity_required`
  - `duplicate_penalty`
  - `uniqueness_bonus`
  - `convergence_backoff_threshold`
- `actor_action_preferences`
  - actor별 `primary_families`
  - `secondary_families`
  - `avoid_families`
  - `state_priority_keys`

이 metadata는 현재 수동 script에 hand-authored로 넣고, future dynamic builder가 같은 shape를 생성하게 한다.

### 2. Controller diversity scoring

기존 action-aware scoring 위에 아래 항목을 추가한다.

- `phase_action_duplication_penalty`
- `role_action_uniqueness_score`
- `actor_local_state_fit`
- `convergence_backoff`

핵심 원칙:

- duplicate는 hard ban이 아니라 soft penalty
- `NEGOTIATION`에서는 unique family spread를 더 강하게 요구
- alignment가 이미 높은데 duplicate family면 alignment weight를 사실상 backoff

### 3. Observability

Selection/compile audit에 아래를 추가한다.

- `phase_action_family_counts_before_compile`
- `planned_action_family`
- `selected_action_family`
- `compiled_action_family`
- selection row별
  - `role_action_uniqueness`
  - `phase_action_duplication_penalty`

### 4. KPI update

새 headline KPI:

- `action_family_convergence_rate`
- `role_action_diversity_score`
- `negotiation_uniqueness_rate`

기존 guardrail 유지:

- `structured_action_validity_rate`
- `executed_action_contradiction_rate`
- `state_transition_coherence`
- `action_plan_alignment_mean`

## Experiment Plan

### Smoke

- scripts
  - `commuting_support_policy`
  - `new_product_launch`
- conditions
  - `naive_action_baseline`
  - `engine_dialogue_only`
  - `engine_action_v0`
- repetitions
  - `1`

Pass target:

- `new_product_launch`에서 `engine_action_v0` drift가 `engine_dialogue_only`보다 `>= 0.01` 개선
- `commuting_support_policy`에서 drift가 `> 0.01` 악화되지 않음
- `action_family_convergence_rate` 감소
- `negotiation_uniqueness_rate` 증가

### Full

Smoke pass 시:

- 5 scripts
- 3 conditions
- 3 repetitions

## Why this is the right next step

이 단계에서 필요한 것은 더 강한 schema나 더 많은 LLM이 아니다.  
이미 syntax와 alignment는 해결됐고, 현재 병목은 `phase-local convergence`다. 따라서 다음 수정은 parser가 아니라 `controller objective`와 `script metadata`를 바꾸는 것이 맞다.
