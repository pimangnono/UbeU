# 2026-03-08 Action Layer v0.5 Plan

## Why v0.5

`v0.4`까지의 결과는 명확했다.

- `structured_action_validity`, `owner_resolution`, `state_transition_coherence`는 이미 높다.
- 그런데 `engine_action_v0`는 `engine_dialogue_only`보다 평균 drift에서 계속 밀렸다.
- 특히 `new_product_launch`에서 action layer가 여전히 role flattening을 만들었다.

즉 남은 병목은 `more valid action`이 아니라 `too much action pressure`다.

`v0.5`의 목표는:

- 모든 actor를 매 phase에 action-bearing으로 밀지 않고
- phase별 action budget과 family cap을 두고
- actor-local state와 role priority가 충분히 강할 때만 action을 활성화하는 것이다.

## Core Hypothesis

현재 action layer는 `planner-first + action-aware scoring`으로 인해

- action coverage는 높아지지만
- hard phase에서 모든 actor가 비슷한 action family를 택하고
- 그 결과 persona drift가 커진다.

따라서 다음 조정은 `better parser`가 아니라:

1. `sparse activation gate`
2. `phase-level max action budget`
3. `family cap`
4. `controller-side sparsity penalty`

이다.

## Implementation

### 1. Script metadata

`SimulationScript.phase_action_policy()`에 다음 필드를 추가한다.

- `allow_no_action`
- `family_cap`
- `max_actions_per_phase`
- `sparsity_threshold`

그리고 `new_product_launch`, `post_merger_integration`는
`NEGOTIATION`과 `TENSION`에서 더 보수적인 cap/budget을 사용한다.

### 2. Action activation score

새 점수는 다음을 결합한다.

- `role_fit`
- `state_priority_fit`
- `state_need_fit`
- `family duplication`
- `phase action budget saturation`

이 점수가 threshold 아래면, planner action이 있어도 proposal을 `sparse_action_gate`로 reject한다.

### 3. Controller-side sparsity

후보 점수화 시에도 같은 gate를 soft penalty로 반영한다.

- threshold 이하 action은 `action_sparsity_penalty`
- sparsity penalty가 걸리면 action-aware scoring weight도 줄인다

즉 action layer는 유지하되, 무조건 action-bearing 후보가 이기지 못하게 한다.

## KPI

Headline:

- `persona_drift_mae`
- `envelope_violations`
- `action_family_convergence_rate`
- `role_action_diversity_score`
- `negotiation_uniqueness_rate`

Guardrail:

- `structured_action_validity_rate >= 0.90`
- `state_transition_coherence >= 0.90`
- `executed_action_contradiction_rate <= 0.05`

Pass criteria for smoke:

- `engine_action_v0`가 `new_product_launch`에서 `engine_dialogue_only`보다 drift 개선
- `commuting_support_policy`에서 existing win을 크게 망치지 않음
- `action_family_convergence_rate` 하락
- `negotiation_uniqueness_rate` 상승 또는 유지

## What changes operationally

`v0.5`는 더 많은 모델이나 graph backend를 추가하지 않는다.

- no Graphiti / Neo4j
- no runtime LLM judge
- no new scenario family builder

지금 단계의 변화는 전부 `script metadata + controller + compile gate` 안에서 해결한다.
