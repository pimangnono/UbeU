# 2026-03-08 Action Layer v0.6 Plan

## Why v0.6

`v0.5`는 sparse gate를 넣었지만 실제 smoke에서

- `planned_action_coverage_rate = 1.0`
- `action_family_convergence_rate = 0.75`
- `engine_action_v0` drift가 `engine_dialogue_only`보다 여전히 높았다

즉 문제는 action validity가 아니라, action layer가 너무 이른 phase부터 대화를 action-bearing 방향으로 당긴다는 점이다.

## Hypothesis

`OPENING`과 `TENSION`은 아직 environment-changing action을 실행할 단계가 아닐 수 있다.

따라서:

- early phase는 `shadow planning`
- late phase(`NEGOTIATION`, `CLOSING`)만 `execute`

로 바꾸면 dialogue quality를 덜 해치면서도 action-conditioned simulation을 유지할 수 있다.

## Changes

### 1. Phase action mode

`phase_action_policy`에 `action_mode`를 추가한다.

- `OPENING`: `shadow`
- `TENSION`: `shadow`
- `NEGOTIATION`: `execute`
- `CLOSING`: `execute`

### 2. Action-aware scoring

`action_mode != execute`인 phase에서는:

- action compile/audit는 유지
- but controller의 `use_action_aware_scoring`은 끈다

즉 candidate selection은 dialogue-first로 간다.

### 3. Transition application

`action_mode == shadow`인 phase에서는:

- proposal은 audit용으로만 남긴다
- proposal ledger에는 넣지 않는다
- arbitration / world-state transition / phase feedback 실행 안 한다

## KPI

Smoke pass 기준:

- `engine_action_v0` drift가 `engine_dialogue_only`보다 낮아질 것
- `new_product_launch`에서 최소 `0.01` 이상 개선
- `commuting_support_policy`를 크게 망치지 않을 것
- `structured_action_validity_rate`, `state_transition_coherence` 유지

## Scope

이번 변경은 ontology를 다시 바꾸지 않는다.

- no new graph backend
- no new LLM judge
- no new actor builder

오직 `when action executes`를 바꾸는 phase-gating 실험이다.
