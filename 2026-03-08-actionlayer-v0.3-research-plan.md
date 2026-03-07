# Action Layer v0.3 Research Plan

## Problem

`v0.2` fixed observability and action-plan alignment, but `engine_action_v0` still underperformed `engine_dialogue_only` on persona drift and envelope stability.

The evidence from smoke suggests:

- syntactic validity is solved
- action-plan alignment is solved
- the remaining failure is `role flattening`

In practice, multiple actors inside the same phase converge on the same action family, which improves action consistency but harms persona differentiation.

## Research-Guided Direction

### 1. Role ability limits should constrain action choice

Role-playing research consistently shows that role fidelity is not only about tone. It also depends on preserving the role's capability boundaries and decision style.

- [RoleMRC](https://aclanthology.org/2025.findings-acl.1064/) argues that role fidelity in instruction following depends on maintaining the role's `ability limits` and not just surface persona.
- [Can LLM Agents Maintain a Persona in Discourse?](https://aclanthology.org/2025.emnlp-main.1487/) shows that multi-turn discourse makes persona drift likely, especially when interaction pressure accumulates.

Implication for this engine:

- `Marketing lead` should not collapse into the same action pattern as `Operations lead`
- `Founders / owners / affected stakeholders` should preserve protective or autonomy-oriented behavior
- `Coordinators / administrators / strategy leads` can remain more ownership-oriented

### 2. Action pressure should be conditional, not global

The current `engine_action_v0` still rewards action-bearing dialogue too broadly. That creates over-structuring and E/C inflation.

- [ReAct](https://arxiv.org/abs/2210.03629) supports coupling reasoning and acting, but not every step needs explicit action pressure.
- [Generative Agents](https://arxiv.org/abs/2304.03442) supports explicit planning and memory artifacts, but behavior should remain context-sensitive rather than uniformly plan-expressive.

Implication:

- action-aware scoring should be strongest when a planner-produced action exists
- when there is no clear planner action, the engine should not force overt action-bearing turns

### 3. Dialogue-action coupling should preserve differentiated social roles

- [SPARK](https://aclanthology.org/2025.emnlp-main.1176/) emphasizes that distinct psychological traits and memory lead to differentiated discourse dynamics.

Implication:

- action plans should be role-conditioned, not just phase-conditioned
- the controller should reward `role-appropriate action choice`, not only `action executability`

## v0.3 Changes

1. Add `role-conditioned action priors`
   - infer preferred action families and target keys from:
     - role
     - incentives
     - concerns
     - phase
     - phase cues

2. Use those priors in both places
   - planner augmentation
   - controller action-aware scoring

3. Reduce action pressure when no planned action exists
   - if no planner-produced action artifact is available, action-aware terms get sharply reduced weight

4. Keep observability from v0.2
   - no rollback

## Expected Outcome

Compared with `v0.2`, the next smoke should show:

- lower persona drift for `engine_action_v0`
- lower envelope violations
- less over-structuring for:
  - `Product launch lead`
  - `Operations and reliability lead`
  - `Early-career commuter`

while preserving:

- high action validity
- low contradiction
- high action-plan alignment
