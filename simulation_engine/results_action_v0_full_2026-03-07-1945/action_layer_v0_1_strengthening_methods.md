# Action Layer v0.1 강화 리서치 & 설계 제안 (5 Methods + 실험 순서)

작성일: 2026-03-07  
목표: **현재 `engine_dialogue_only` 수준의 persona stability를 유지하면서**, `dialogue -> typed action -> world-state transition` 품질을 끌어올려 **Action Layer가 “붙어도 품질이 안 떨어지는”** 상태를 만들기.

---

## 0) 현재 v0의 상태 (문제 정의)

현재 3-arm 벤치마크 요약:

- `naive_action_baseline`  
  - persona drift MAE `0.1793`  
  - structured action validity `0.4957`  
  - action feedback utilization `0.1000`

- `engine_dialogue_only`  
  - persona drift MAE `0.1692`  
  - structured action validity `0.5894`  
  - executed action contradiction `0.0000`  
  - state trajectory variance `0.0008`

- `engine_action_v0`  
  - persona drift MAE `0.1676` (미세 개선)  
  - structured action validity `0.5282` (**dialogue-only보다 악화**)  
  - executed action contradiction `0.0667` (**새로 발생**)  
  - relationship inconsistency `0.0961` (**새로 발생**)  
  - state trajectory variance `0.0014` (**dialogue-only보다 큼**)  

즉, **baseline 대비 pass / dialogue-only 대비 partial fail**이라는 해석이 가장 정확합니다.  
Action Layer는 “행동-상태 전이” 루프를 만들었지만, **행동 파싱/정합성/갈등해결이 아직 product-grade가 아닙니다.**

---

## 1) 강화 전략의 핵심 원칙 (CTO 관점)

1. **ActionProposal은 “추출(extraction)” 대상이 아니라 “컴파일(compile)” 대상**  
   - 자연어 발화에서 행동을 뽑는 방식은 구조적 오류(미싱 필드/허용되지 않은 타입/타겟키 오류)를 피하기 어렵습니다.
   - 따라서 “자연어 → action”은 v0에서는 가능했지만, v0.1부터는 **plan/action을 first-class artifact로 생성**해야 validity ceiling이 올라갑니다.

2. **품질 보증은 generation이 아니라 “검증/수리/감사(audit)”로 가져가야 함**  
   - agentic 시스템은 작은 오류가 누적되어 시스템 행동으로 번집니다(특히 stateful + multi-turn). 따라서 “왜 invalid가 났는지”를 남기는 audit 체계가 먼저입니다.

3. **Graph DB(Neo4j/Graphiti)는 지금 문제의 bottleneck이 아님**  
   - 지금의 KPI 실패는 memory query power 부족이 아니라 **action proposal 품질, arbitration 품질, feedback 설계** 문제입니다.
   - v0.1~v0.2는 JSON ledger 기반으로 충분히 해결 가능하고, Graph backend는 “스케일 조건 충족” 후에 붙이는 게 안전합니다.

---

## 2) Method 1 — Schema-Constrained Action Generation (정형 출력 강제)

### 아이디어
`ActionProposal` 생성 자체를 **JSON Schema/Grammar 제약** 하에 수행해서 *구문적 validity*를 먼저 0.85+로 끌어올립니다.

### 근거 (연구)
- Constrained decoding을 사용하면 모델 출력이 사전 정의된 문법/형식 제약을 만족하도록 강제할 수 있습니다. (Grammar-Aligned Decoding)  
- Constrained decoding 방식들은 안정성/정확도 tradeoff가 존재하므로, 벤치마크 기반으로 어떤 제약 방식이 유리한지 측정해야 합니다. (JSONSchemaBench 등)  
- function calling/structured output은 “행동을 API call처럼 취급”하는 실용적 패러다임으로 자리잡고 있고, 이를 평가하는 벤치마크들도 존재합니다. (BFCL)

### 구현 (production-grade)
**A. ActionCompiler를 3-tier로 분리**
1) `schema_first`: (가능하면) 모델의 native structured output / function calling 사용  
2) `json_only`: JSON-only prompt + strict parser  
3) `repair`: JSON repair (Method 3과 결합)

**B. 제약 방식**
- OpenRouter에서 모델별 structured output 지원이 불균일할 가능성이 큽니다.  
  그래서 v0.1은 “가능하면 schema-first, 아니면 json-only”로 fallback.

**C. Validator**
- Pydantic/JSON schema로 다음을 *반드시* 검증:
  - `action_type ∈ allowed_action_types`
  - `target_key ∈ allowed_target_keys`
  - `phase_name` 유효성
  - optional fields type check
- 실패 시 `rejected(reason="schema_validation_failed")` 형태로 **정상 기록** (silent drop 금지)

### 기대 효과
- `structured_action_validity_rate`가 가장 직접적으로 개선됩니다.
- invalid 비율이 줄면 downstream arbitration/transition도 안정화됩니다(garbage-in 감소).

### 리스크/부작용
- **제약을 강하게 걸수록 표현 다양성이 줄어** “모든 행동이 비슷한 JSON”이 될 수 있음.
- 일부 모델은 constrained decoding에서 품질이 떨어질 수 있음(bench로 확인 필요).

### 증명해야 하는 것 (v0.1 Gate)
- `engine_action_v0.1`에서  
  - structured action validity `>= 0.75` (smoke) → `>= 0.85` (5-script pilot)  
  - persona drift MAE는 `engine_dialogue_only +0.01` 이상 악화 금지

**References**
- Park et al., 2024, *Grammar-Aligned Decoding* (arXiv:2405.21047)  
- Geng et al., 2025, *Evaluating Constrained Decoding Methods for LLMs via JSONSchemaBench* (OpenReview)  
- Patil et al., 2024/2025, *Berkeley Function Calling Leaderboard (BFCL)* (PMLR)

---

## 3) Method 2 — Action-First Generation (ReAct-style: Decide→Say, not Say→Extract)

### 아이디어
지금은 `selected turn text -> compile_action_proposal` 흐름이라 “대화가 행동을 암시하면” extractor가 행동을 추론해야 합니다.  
이를 뒤집어:

1) **action plan(JSON)** 을 먼저 만든다 (policy planner 단계)  
2) 그 action을 **발화 생성 prompt에 주입**해서 말로 “설명/설득”만 하게 한다  
3) phase-end에는 planner JSON을 authoritative action proposal로 쓴다 (추출 최소화)

이러면 **action validity ceiling이 크게 올라가고**, “발화는 자연어, 행동은 typed artifact”로 contract가 분리됩니다.

### 근거 (연구)
- ReAct는 reasoning/acting을 분리하지 않고 interleave하는 것이 도구 사용과 multi-step task 성능을 높일 수 있음을 보여줍니다.  
- Function calling 계열 연구/벤치마크는 “행동을 호출 단위로 다루는 것”이 practical agent design에 중요하다는 것을 뒷받침합니다.

### 구현 (production-grade)
**A. Planner JSON을 authoritative로 승격**
- `policy_planner` 출력에 아래 필드를 **필수**로:
  - `action_type`
  - `target_key`
  - `owner_actor_id` (가능하면)
  - `deadline_phase` (가능하면)
  - `confidence`
  - `evidence_text` (짧게)

**B. Utterance Generator는 “행동 일관성”을 보장**
- 발화 생성 prompt에 planner JSON을 넣고:
  - “너의 발화는 이 action을 지지/설명해야 한다”
  - “planner JSON과 모순되는 내용 금지”
- Controller scoring에 `action_plan_alignment` 항목 추가:
  - utterance가 planner action을 *명시적으로 반영*했는지(= feedback utilization 향상에도 도움)

**C. Extraction은 fallback**
- planner JSON이 schema fail이면 Method 1/3로 fallback해서 action compiler가 생성.

### 기대 효과
- `structured_action_validity_rate` 상향
- `action_feedback_utilization` 상승 (행동이 발화와 결합되므로 다음 phase에서도 언급될 확률↑)
- “발화가 좋아서 행동이 엉터리” / “행동은 맞는데 발화는 딴소리” 분리가 가능

### 리스크/부작용
- planner가 행동을 과도하게 넣으면 **대화가 도구적/기계적으로 변할** 수 있음.
- planner 품질이 낮으면 (특히 target_key 선택이 엉망이면) 문제가 더 빨리 전파됨 → Method 3/4 필요.

### 증명해야 하는 것 (v0.1 Gate)
- `planner_schema_validity >= 0.90`
- `action_plan_alignment >= 0.70`
- `engine_action_v0.1`에서 structured validity `>= engine_dialogue_only + 0.10` (pilot)

**References**
- Yao et al., 2023, *ReAct: Synergizing Reasoning and Acting in Language Models* (arXiv:2210.03629)  
- Patil et al., *BFCL* (PMLR)

---

## 4) Method 3 — Generate→Verify→Repair Loop (Selective, Cheap, Auditable)

### 아이디어
“invalid JSON을 그냥 버린다/노 리젠”은 실험에서는 깔끔하지만, 제품에서는 **품질을 담보하지 못합니다.**  
대신, **대화 발화는 재생성하지 않더라도**, action proposal만큼은 다음의 *짧은* 루프를 허용하는 게 ROI가 큽니다.

- `proposal_raw` 생성
- deterministic validation
- 실패 시 `repair` 1회 (또는 top-2 생성 후 valid한 것 선택)
- (옵션) verifier model이 “semantic validity(허용 타입/타겟키/phase 목적)”까지 체크

### 근거 (연구)
- Self-Refine / Reflexion 계열은 “모델 스스로 비평/수정” 루프가 품질을 개선할 수 있음을 보여줍니다.  
- SEQCV는 LLM-driven workflow에서 subtask output을 검증/수정하는 절차(예: peer-review, sequential correction)가 효과적일 수 있음을 제안합니다.

### 구현 (production-grade)
**A. Repair를 ‘action-only’로 제한**
- repair prompt는 매우 짧게:
  - “다음 JSON이 schema를 만족하도록 최소 변경으로 수정하라”
  - “허용된 action_type과 target_key 목록은 이것뿐”
  - “추론 설명 금지, JSON만 출력”
- 수리 결과도 validator 통과 못 하면 `no_action`으로 기록 (하지만 raw+error는 남김)

**B. Verifier 선택**
- 비용 최소화: `gpt-4o-mini` 같은 저가 모델을 verifier로  
- 또는 같은 모델로 2-shot self-check (하지만 편향 가능)

**C. 로깅 (이게 핵심)**
- `proposal_raw_text`
- `parse_error`
- `repair_attempted: bool`
- `repair_success: bool`
- `final_status` + `rejection_reason`
- 이게 없으면 v0처럼 “왜 validity가 낮은지” 추적이 안 됩니다.

### 기대 효과
- structured validity 상승(특히 `new_product_launch`처럼 validity가 낮은 script에서)
- executed action contradiction 감소 (semantic verifier가 ‘충돌’ 사전 감지 가능)

### 리스크/부작용
- latency/token 상승 (하지만 action JSON은 짧아서 대화 regen보다 훨씬 싸다)
- repair가 과도하면 행동이 획일화될 수 있음 → “1회만” 원칙 권장

### 증명해야 하는 것 (v0.1 Gate)
- repair 사용 비율(`repair_rate`)이 0.3 이하인데도 structured validity가 0.85를 달성하는지  
- repair가 persona drift를 악화시키지 않는지 (drift MAE +0.01 이상 악화 금지)

**References**
- Madaan et al., 2023, *Self-Refine* (arXiv:2303.17651)  
- Shinn et al., 2023, *Reflexion* (arXiv:2303.11366)  
- NeurIPS 2025, *SEQCV: Sequential Cross-Verification for LLM Collaboration* (OpenReview)

---

## 5) Method 4 — Institution/Arbiter Upgrade (Conflict Resolution을 “기관”으로 분리)

### 아이디어
현재 phase-end arbitration은 규칙 기반 우선순위로 resolve하지만, v0에서 **executed action contradiction이 새로 발생**했습니다.  
이는 “행동이 늘어나면 갈등/충돌이 필연적으로 늘어나는데”, 지금은 그 갈등을 해결하는 **institutional layer가 약한 것**으로 해석할 수 있습니다.

따라서 `arbiter_phase_actions`를 단순 정렬/필터가 아니라, **명시적 제약 + 목적 함수**를 가진 기관으로 강화합니다.

### 근거 (연구)
- 사회 시뮬레이션에서 agent-agent 대화만으로는 한계가 있고, **explicit environment, exposure, scheduling mechanisms**가 필요하다는 문제제기가 있습니다.  
  이건 “action/state”를 넣는 방향 자체가 맞다는 근거이면서, 동시에 “기관/규칙이 없으면 이상해진다”는 경고입니다.
- agentic 시스템은 stateful + multi-turn에서 작은 오류가 누적되기 쉬우므로, observability/logging과 governance가 중요하다는 논의가 있습니다.

### 구현 (production-grade)
**A. Conflict set을 명시적으로 정의**
- action family별로 “동시에 실행 불가능” 제약:
  - 예: `assign_owner(target_key=X)`는 phase에 1개만
  - 예: `defer_decision` vs `commit_resource`는 같은 target에서 동시 실행 불가
- 이를 `action_compatibility_matrix`로 코드화

**B. Arbiter의 목적 함수 (간단 버전)**
각 proposal에 점수:
- `confidence`
- `owner/deadline 완비`
- `phase_goal_alignment`
- `persona_consistency` (특정 role이 절대 하지 말아야 할 action이면 penalty)

그 다음:
- 제약 만족하는 action set 중 score 합 최대인 set 선택  
  (작은 ontology라면 greedy + backtracking으로 충분)

**C. 역할 기반 기관 규칙**
- 특정 action은 특정 role만 제안/승인 가능하게 (예: `publish_update`는 admin/coordinator만)
- 이게 “role drift”를 줄이는 핵심 장치가 됩니다.

### 기대 효과
- executed action contradiction 감소
- relationship inconsistency 감소 (기관이 행동 충돌을 줄이면 관계 업데이트가 덜 흔들림)
- state trajectory variance 감소 (충돌/우발적 행동이 줄어들기 때문)

### 리스크/부작용
- 너무 강한 기관 규칙은 시뮬레이션을 “각본”처럼 만들 수 있음.
- 목적 함수 설계가 편향을 만들 수 있음 → audit 로그로 감시

### 증명해야 하는 것 (v0.2 Gate)
- executed action contradiction `<= 0.05` (pilot) 그리고 dialogue-only 대비 열화 금지
- state trajectory variance가 dialogue-only 이하로 내려가는지(또는 최소 동급)

**References**
- Li & Tao, 2026, *Position: AI Agents Are Not (Yet) a Panacea for Social Simulation* (arXiv:2603.00113)  
- *Agents of Chaos* (2026 preprint) — stateful/multi-turn agentic 시스템에서 observability와 governance 중요성 논의

---

## 6) Method 5 — Feedback Retrieval + Anti-Sycophancy Guard (Action이 Persona를 망치지 않게)

### 아이디어
Action layer가 붙으면 state feedback이 늘고, 그게 모델의 상호작용 스타일을 바꾸면서 **E inflation / 과도한 구조화 / 관계 흔들림**이 생길 수 있습니다.  
즉 “행동-상태 전이”는 맞는데, **feedback을 어떻게 노출하느냐**가 persona 안정성과 직결됩니다.

### 근거 (연구)
- interaction context가 늘어나면 sycophancy가 증가할 수 있다는 결과가 보고됩니다.  
  (state feedback이 곧 interaction context 증가)
- multi-turn에서 모델이 “정확한 전략/추출” 단계에서 오류를 낼 수 있고, 일부 오류는 나중에 수정되지만 시스템 설계가 이를 고려해야 합니다. (multi-turn reliability 연구)

### 구현 (production-grade)
**A. Actor-specific “visibility budget”을 고정**
- 지금의 1줄 요약 + 2개 action 제한은 좋은 방향.  
  다만 “사용자에게 보여주기 위한 요약”이 아니라 “행동을 유도하는 최소 충분 통제 신호”가 되도록 구성:
  - `Δ`가 큰 state key만 노출 (변화량 기반)
  - actor incentive/concern과 연관된 key만 노출 (타깃 기반)
  - “내가 뭘 해야 하는지” 1줄로 강제 (next-action hint)

**B. Feedback utilization을 점수화해서 controller에 넣기**
- 다음 phase의 발화가 직전 executed action을 *언급*하고 *반영*하면 보상
- 단, persona에 반하는 “과도한 적극성”을 보상하면 안 됨 → persona band 내에서만

**C. Anti-sycophancy / anti-genericity penalty**
- action feedback이 들어오면 모델이 “무난한 동의/공손한 리포트”로 수렴할 수 있으니,
  - generic compliance 패널티
  - role-specific dissent 허용 규칙
  - E inflation 억제 패널티
  를 controller에 추가

### 기대 효과
- action feedback utilization 0.60+ 달성
- relationship inconsistency 감소
- persona drift MAE가 action 때문에 악화되지 않음

### 리스크/부작용
- feedback이 너무 적으면 utilization이 올라가지 않음(지금 0.5555 근소 미달)  
- feedback이 너무 많으면 persona drift/sycophancy 증가

### 증명해야 하는 것 (v0.2 Gate)
- action_feedback_utilization `>= 0.60` (pilot)  
- relationship inconsistency가 `engine_dialogue_only` 대비 악화되지 않을 것  
- E inflation(역할별 E error)이 감소하는지

**References**
- *Interaction Context Often Increases Sycophancy in LLMs* (2025)  
- *LLMs Get Lost in Multi-Turn Conversation* (2024 preprint)

---

## 7) 추천 구현/실험 순서 (Phase Plan)

### Phase 0 — Observability Patch (필수)
**구현**
- proposal/rejection audit 저장(원문 + parse error + rejection_reason + repair flags)
- script별 `allowed_action_types/target_keys` 분포 리포트 추가

**성공 기준**
- invalid proposal의 95% 이상이 “이유 라벨”을 갖고 있다(unknown/empty 금지)
- 실험 리포트에서 script별 invalid 원인 Top-5가 나온다

---

### Phase 1 — Validity Ceiling 올리기 (Method 1 + 2)
**구현**
- planner JSON을 authoritative로 승격(action-first)
- schema-first or json-only action generation 적용
- strict validator

**실험**
- smoke 2 scripts × 1 rep × 3 conditions
- 그 다음 5-script pilot × 3 reps

**성공 기준**
- structured action validity `>= 0.85`
- persona drift MAE `<= engine_dialogue_only + 0.01`

---

### Phase 2 — Contradiction/Variance 줄이기 (Method 4 + 일부 Method 3)
**구현**
- arbiter를 제약 + 목적함수 기반으로 강화
- (선택) verifier 1회로 semantic conflict 탐지

**성공 기준**
- executed action contradiction `<= 0.05`
- state trajectory variance `<= engine_dialogue_only`

---

### Phase 3 — Feedback Utilization & Relationship 안정화 (Method 5)
**구현**
- 변화량 기반/타깃 기반 feedback retrieval
- controller에 utilization 보상 + sycophancy/genericity 패널티

**성공 기준**
- action_feedback_utilization `>= 0.60`
- relationship inconsistency `<= engine_dialogue_only + 0.02`

---

### Phase 4 — Scale-up & Graph Backend Decision
**조건**
- actor ≥ 8, phases ≥ 6, multi-hop temporal query가 실제 제품 요구로 등장  
- JSON ledger 디버깅이 어려워지고 “관계/행동/상태” 쿼리가 병목이면 그때 Graphiti/Neo4j 검토

---

## 8) 마지막 코멘트 (지금 확장해도 되는가?)

결론적으로 **“Action 방향으로 확대는 지금 해도 됨”** 입니다.  
이미 v0가 baseline 대비 의미 있는 개선을 보여주고 있고(contradiction 대폭 감소, drift 개선), 제품 목표(환경에 영향)로 가려면 action layer는 필수입니다. 다만 **v0.1의 핵심 목표는 기능 추가가 아니라 ‘품질 보증’**입니다:

- action validity를 0.85 이상으로 올리고  
- arbitration으로 인한 contradiction/relationship 흔들림을 제거하고  
- dialogue-only 수준의 persona drift를 유지하는 것

이 3개가 “Action Layer가 붙어도 품질이 안 떨어진다”는 최소 claim입니다.

---

## Appendix: Reference List (ID only; no raw URLs)

- Park et al. (2024). Grammar-Aligned Decoding. arXiv:2405.21047  
- Geng et al. (2025). Evaluating Constrained Decoding Methods for LLMs via JSONSchemaBench. OpenReview  
- Patil et al. (2024/2025). Berkeley Function Calling Leaderboard (BFCL). PMLR  
- Yao et al. (2023). ReAct. arXiv:2210.03629  
- Madaan et al. (2023). Self-Refine. arXiv:2303.17651  
- Shinn et al. (2023). Reflexion. arXiv:2303.11366  
- SEQCV (2025). Sequential Cross-Verification for LLM Collaboration. OpenReview  
- Li & Tao (2026). Position: AI Agents Are Not (Yet) a Panacea for Social Simulation. arXiv:2603.00113  
- Interaction Context Often Increases Sycophancy in LLMs (2025).  
- LLMs Get Lost in Multi-Turn Conversation (2024 preprint).
