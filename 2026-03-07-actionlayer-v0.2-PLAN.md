# Action Layer v0.2 Plan

## Goal

`v0.2` focuses on two upgrades only:

1. `Phase 0 observability`
2. `Method 2: action-first planning`

The current bottleneck is no longer syntactic action validity. `v0.1` already pushed `structured_action_validity_rate` to the ceiling in smoke, but semantic quality and persona fit got worse. That means the engine needs:

- an authoritative planned action artifact before utterance extraction
- a full audit chain from plan -> hint -> compiled proposal -> arbitration -> execution

## Why this change

`v0.1` proved that stronger schema validation alone is not enough. The failure mode is:

- actions become easy to validate
- but the selected action is not always well aligned with the actor, phase, and planner intent

So `v0.2` changes the control structure from:

- `say -> extract -> execute`

to:

- `decide -> say -> compile -> execute`

## Scope

### In
- authoritative `planned_action_artifact`
- `action_plan_alignment` scoring
- full per-turn action audit chain
- benchmark/report visibility for alignment and coverage

### Out
- more constrained decoding / structured output escalation
- graph DB / Graphiti / Neo4j
- institution-level optimization layer

## Design

### 1. Planned action artifact

Each `policy_plan` now carries a normalized nested `action_plan` object:

- `action_type`
- `target_key`
- `target_actor_id`
- `owner_actor_id`
- `deadline_phase`
- `strength`
- `expected_state_effect`
- `confidence`
- `rationale`
- `source`

This artifact becomes the primary source for `compile_action_proposal`.

### 2. Compile priority

The compile path becomes:

1. `planned_action_artifact`
2. `selected_action_hint`
3. `heuristic_action_proposal`
4. `llm extraction`

This deliberately removes `utterance-only extraction` as the primary path.

### 3. Controller alignment

For action-aware conditions, candidate scoring now includes:

- `action_executability`
- `state_consistency`
- `action_plan_alignment`

`action_plan_alignment` checks whether the candidate-level action hint matches the authoritative planned action on:

- action type
- target key
- owner
- deadline

### 4. Audit chain

Each action-bearing turn now records an audit row containing:

- `planned_action_artifact`
- `selected_action_hint`
- `compiled_proposal`
- `compiler_source`
- `compile_status`
- `compile_rejection_reason`
- `validation_trace`
- `action_plan_alignment`
- `arbitration_status`
- `arbitration_reason`
- `execution_status`
- `execution_rejection_reason`
- `executed_action`
- `pre_state`
- `post_state`

This is stored in runtime summary output so later benchmark analysis can inspect semantic failures directly.

## New metrics

- `action_plan_alignment_mean`
- `planned_action_coverage_rate`

These are not headline KPIs yet, but they are necessary diagnostics for `v0.2` and `v0.3`.

## Acceptance criteria

`v0.2` should improve relative to `v0.1` on at least the following in smoke:

- `engine_action_v0` no longer degrades badly versus `engine_dialogue_only`
- `action_plan_alignment_mean` is materially above baseline
- action audit rows clearly expose where proposals diverge or get over-accepted

## Immediate experiment order

1. smoke
   - `commuting_support_policy`
   - `new_product_launch`
2. inspect audit chain
3. only if smoke improves, rerun pilot/full
