# Data Scarcity 대응 + (선택) ML/DL 적용 가능성 + 상업적 시간 예산(N) 제안 (BCFC/Simulation Engine)

> 질문 요지:  
> (1) 데이터가 부족할 때 “스스로 보완”하거나 **확률적으로 가장 가능성 높은 범위**를 제시할 수 있는가?  
> (2) ML/DL 없이도 비슷한 방식으로 적용할 수 있는가? 데이터는 어떻게 얻고 가공해야 하는가?  
> (3) ML/DL을 적용한다면 어떤 방식이 가능하고, 더 나은 결과를 낼 수 있는가? 단, **시뮬레이션 결과는 상업적으로 N시간 내**에 나와야 한다.  
> (4) N이 몇 시간 정도가 타당한가?  
> (5) ML/DL 없이 rule-based로 가야 한다면, 그 이유를 자세히 justify 해달라.

---

## 0. 전제: 당신의 “성공 기준”을 다시 고정
- 목표는 **어떤 상황(시나리오/토픽/상호작용 압력)에서도** assigned OCEAN이 *multi-turn* 동안 **안정적으로 유지**되는가이다.
- 즉 “trait을 잘 드러내는 상황을 만들어서 점수를 올리는 것”이 아니라, **상황 변화/압력/대화 영향 하에서도 stable한 persona dynamics**를 보장하는 “런타임 제어 시스템”이 핵심이다.

(이 관점이 맞기 때문에, 데이터 전략도 **scenario-specific overfit**을 피하도록 설계해야 한다.)

---

## 1) 데이터가 부족할 때 “스스로 보완” / “가능성 높은 범위”를 제시하는 5가지 방법 (ML/DL 없이도 가능)

### 방법 A — Sequential sampling + 조기종료(Anytime)로 “신뢰구간이 닫힐 때까지” 반복 실행
**아이디어:**  
각 시뮬레이션 run은 “샘플”이다. N시간 예산 안에서 **rep을 늘리다가**, 핵심 KPI(예: persona_drift_mae)의 신뢰구간(bootstrap CI 또는 Bayesian credible interval)이 충분히 좁아지면 stop한다.

- 장점: 데이터가 적어도 “지금 결론이 얼마나 불확실한지”를 제품이 정직하게 말할 수 있음.
- 위험: 비용/시간이 늘어날 수 있음 → “최대 N시간” budget 기반 early stop 필요.
- 구현: 실험 harness에 `stop_when(ci_width < τ OR time_budget_exceeded)` 추가.

> 결과 리포트도 “단일 숫자”가 아니라 `mean ± CI`로 출력하면, 상업용 의사결정에서 훨씬 설득력이 커진다.

---

### 방법 B — Hierarchical Bayes(계층 베이지안)로 “roles/traits/scenarios” 간 정보 공유(shrinkage)
**아이디어:**  
예를 들어 `Small property owner` 같은 hardest role에서 데이터가 부족하면,  
- role-level 효과, scenario-level 효과, trait-level 효과를 계층 구조로 두고  
- 적은 데이터는 전체 평균 쪽으로 shrink한다.  
→ “가능성 높은 범위”를 더 안정적으로 내고, 과대해석을 줄인다.

- 장점: 작은 N에서도 안정적 추정, outlier run의 영향 감소
- 위험: 모델링 가정이 들어가므로 가정이 잘못되면 bias 발생
- 구현: offline 분석(파이썬)에서 가능. 런타임에는 굳이 필요 없음(리포팅에 사용).

---

### 방법 C — Counterfactual evaluation(오프라인 재선택)으로 “데이터 증폭”
**아이디어:**  
당신은 이미 candidate_pool을 로깅하는 구조를 갖고 있다.  
그러면 같은 N-pool에서 `first/random/contract-only/full-score` 등 다양한 정책을 **추가 LLM 호출 없이** 오프라인에서 재계산할 수 있다.  
이건 “데이터가 부족해도” 정책 비교에 필요한 샘플을 **실질적으로 증폭**한다.

- 장점: 비용 0에 가까운 ablation, overfit 탐지(정책이 특정 scenario에서만 이득인지)
- 위험: candidate_pool이 비어 있으면 불가능 → 로그 품질이 제품 품질이 됨(감사/audit 필수)

---

### 방법 D — Theory-driven priors(심리학 이론 기반 priors)로 data-free 안정화
**아이디어:**  
Trait Activation Theory(TAT) 관점에서 “상황 단서(opportunity)”가 trait 표현을 촉발한다.  
즉 **상황의 cue 강도**와 **assigned trait 강도**를 결합한 prior를 두고, controller는 “cue가 강해도 low-trait는 band 내에서만 반응”하도록 만든다.

- 장점: 데이터가 적어도 설계가 원리적으로 말이 됨(논문 설득력↑)
- 위험: cue 설계가 부정확하면 잘못된 nudge/penalty를 줄 수 있음
- 구현: 현재 v5에서 문제였던 “모든 actor에게 동일한 O/C 실행 보상”을 방지하는 데 직접적으로 유효.

---

### 방법 E — Uncertainty-aware product output(“범위+근거” 보고서)
**아이디어:**  
사용자에게 “최종 결론”만 주지 말고  
- 핵심 outcome의 분포(예: policy impact score)  
- outcome을 만든 executed actions/commitments 근거  
- persona drift 위험 경고(uncertainty, judge variance)  
를 같이 준다.

- 장점: 상업적 신뢰(enterprise adoption)에 매우 중요
- 위험: 리포트가 길어질 수 있음 → 요약/상세 두 단계로 제공

---

## 2) 데이터는 어떻게 얻고, 어떻게 가공해야 하나? (production-grade 관점)

### 2.1 데이터 단위(권장 스키마)
**최소 단위는 “turn”이 아니라 “(actor, phase, turn)”이다.**  
각 샘플에 아래를 저장하면, ML 없이도 분석/검증이 급격히 쉬워진다.

- Context:
  - `script_id`, `phase_name`, `turn_index`, `actor_id`, `role`, `scenario_family`
  - `visible_state_summary`(actor가 본 world state)
- Persona prior:
  - `assigned_OCEAN`, `identity_core`, `stable_expression_prior`
- Generation:
  - `prompt_hash`(재현성), `model_id`, `seed`
  - `candidate_pool`: 각 후보의 text + style_slot + token_count + policy_plan
- Selection/Audit:
  - `selected_candidate_index`
  - controller score breakdown(각 penalty 항목)
  - near-tie 여부, tie-break 이유
- Action layer:
  - action_proposal(raw JSON), validation 결과, rejection reason
  - phase-end arbitration 결과(approved/rejected/executed)
- Outcomes:
  - persona drift metrics(rolling), envelope violations
  - relationship edges delta, commitments delta
  - world_state pre/post

이렇게 되면 “데이터 부족” 문제를 **가장 먼저 해결하는 건 로그 품질**이 된다.

---

### 2.2 데이터 확보 전략(가장 비용 효율적인 순서)
1) **자동 로그 + 오프라인 재계산**으로 “무료 샘플”부터 확보  
2) **소량 human calibration set(예: 50~200 turn)**  
   - 목적: judge bias / proxy validity 확인(라벨이 흔들리면 학습도 흔들림)  
3) **시나리오 분산(randomization)으로 coverage 확보**  
   - “policy 5개만” 같은 좁은 분포는 overfit을 부른다.  
   - 최소한: 같은 role을 다른 토픽/압력/상대 조합에 노출시키는 교차 설계 필요.
4) synthetic data는 마지막: “보정/증강” 용도로 제한

---

### 2.3 가공(Preprocessing) 체크리스트
- JSON schema validate(실패는 별도 테이블로)
- role/actor mapping을 “stable ID”로 표준화(지금처럼 Soojin → role)
- 텍스트에서 feature 추출 파이프라인 고정(버전 태깅)
- 평가/판정(LLM judges)도 prompt 버전과 모델 버전을 함께 저장

---

## 3) ML/DL을 적용한다면 “어떻게” + “더 나은 결과 가능성” (단, N시간 내 결과)

당신의 제약은 “대형 LLM fine-tuning 불가(노트북)”이고, “API-only”가 핵심이다.  
그래서 여기서 말하는 ML/DL은 **런타임 안정성은 rule-based로 유지하되**, 일부 서브모듈을 “작게” 학습해서 개선하는 방향이 가장 현실적이다.

### 옵션 1 — Lightweight reranker 학습(GBDT/LogReg)으로 score weight 자동화
- 무엇을 학습하나?
  - 입력: candidate feature vector(계약거리, adequacy flags, redundancy, action executability 등)
  - 출력: “이 후보가 선택되면 drift/contradiction/world-state coherence가 개선되는가”
- 데이터는 어떻게 얻나?
  - candidate_pool 로깅만 제대로 되면, 각 turn에서 N개 후보가 곧 학습 데이터가 됨.
  - 라벨은 (a) rule-based KPI, (b) LLM jury inference, (c) 소량 human label을 혼합 가능.
- 왜 좋은가?
  - 수동 weight 튜닝보다 scenario 일반화가 쉬움(특히 role-specific failure 줄이기)
- 위험:
  - 라벨(특히 LLM judge)이 편향되면 그 편향을 학습함 → bias audit 필수

**런타임 영향:**  
학습된 reranker는 CPU에서 ms~수십 ms 수준으로 가능하므로 N시간 예산에 거의 영향 없음.

---

### 옵션 2 — Action compiler 전용 “슬롯 추출 모델”(작은 seq2seq/encoder) 학습
- 목표: structured_action_validity_rate를 올리는 가장 직접적인 방법
- 접근:
  - utterance + phase + allowed_action_types + target_keys → action_type/slots 분류
  - distill을 쓸 수도 있고(LLM이 teacher), human이 일부만 라벨링해도 됨
- 기대 효과:
  - action JSON 파싱 실패 감소
  - rejection reason 감소
- 위험:
  - 새 도메인(policy 외)에 일반화 실패 가능
  - 라벨링 비용

**런타임 영향:**  
작은 모델이면 로컬에서도 빠름. LLM 호출을 줄여서 오히려 전체 시간/비용이 내려갈 수 있음.

---

### 옵션 3 — “Judge distillation”(평가 비용/시간 절감) + 불확실성 동반
- 문제: 5-model × dual-order jury는 비용이 크고 불확실성도 존재
- 해결:
  - jury를 teacher로 사용해, trait inference/appropriateness/coherence를 예측하는 student 모델을 학습
  - 단, student는 “최종 판정”이 아니라 **fast screen**으로만 사용
  - 불확실하면 jury로 escalate(= 당신이 이미 하고 있는 selective escalation 철학)
- 기대:
  - 상업용에서 N시간 예산 안에 더 많은 rep를 돌릴 수 있음
- 위험:
  - teacher(LLM judge)의 bias/불안정성이 그대로 증류됨 → calibration set로 감시 필요

---

### 옵션 4 — Offline RL / preference optimization(장기적 상한은 높지만, 지금은 비용/리스크 큼)
- 연구적으로는 multi-turn RL로 persona drift를 줄인 연구가 존재함(예: multi-turn RL로 일관성 개선)  
- 그러나:
  - 학습 비용이 크고
  - reward hacking/over-optimization 리스크가 높고
  - 평가 자체가 흔들리면 학습이 잘못된 방향으로 갈 수 있음  
따라서 현재는 “외부 GPU/클라우드가 있는 경우”에만 고려하는 게 현실적.

---

### 옵션 5 — Weak supervision(규칙 + 다수 judge + human 소량)로 라벨 생성 후 학습
- 핵심: 라벨을 “하나의 judge”로 만들지 말고,  
  - rule-based signals  
  - jury median  
  - human spot-check  
를 결합해서 라벨 품질을 끌어올린 뒤 학습한다.

이건 “데이터가 부족할 때” 가장 ROI가 좋은 ML 루트다.

---

## 4) N시간(상업적으로 쓸만한 최대 런타임)은 몇 시간인가?

단일 정답은 없지만, **제품 모드**를 나누면 정리된다.

### 권장 SLA(현실적이고 방어 가능한 제안)
- **Interactive preview 모드:** 5~10분 이내  
  - 사용자가 “이 설정이 의미 있나?” 빠르게 확인하는 모드
- **Full report 모드:** 60분 이내(= N=1h)  
  - 한 번의 업무 세션/회의 안에서 결과를 보고 의사결정에 쓰는 모드
- **Overnight batch(옵션):** 2~5시간(엔터프라이즈 배치)  
  - 더 많은 rep/더 큰 actor 수/더 긴 horizon

N=1h를 기본으로 잡는 이유(근거):
- 상용 BI/분석 시스템에서도 “리프레시/배치 작업”이 60분 단위로 운영되는 경우가 있고, 제한도 시간 단위로 존재한다(예: Power BI 문서에서 refresh/업데이트 관련 시간 제약이 명시됨).  
- 다만, 사용자가 기다리는 동안 “아무것도 안 보이면” UX가 급격히 나빠지므로, progressive/anytime 형태로 부분 결과를 계속 내주는 것이 좋다.

> 결론:  
> **N=1시간**을 “상업적 기본 상한”으로 두고,  
> 그 안에서 **preview→full**을 계층화(Anytime)하는 게 가장 안전한 제품 전략이다.

---

## 5) ML/DL 없이 rule-based로 가야 한다면? (왜 그게 합리적인가)

### 5.1 당신의 문제는 “학습”보다 “제어(control) + 감사(audit)” 성격이 강함
- 목표가 “정답 예측”이 아니라  
  **multi-agent interaction 중 persona collapse 방지 + bounded influence 보장**이다.
- 이건 규칙/제약/상태 머신/점수 함수가 강점을 갖는 영역이다.

### 5.2 평가 라벨(LLM judges)이 편향/불안정할 수 있음 → 학습이 오히려 망가질 위험
LLM judge는 bias/inconsistency/position bias 문제가 계속 보고되고 있다.  
따라서 라벨 품질이 확보되기 전에는, 그 라벨로 학습하는 건 위험하다.

(이 리스크가 큰 이유: 학습이 되면 시스템이 더 “설득력 있게” 잘못된 방향으로 drift할 수 있음)

### 5.3 생산 환경에서의 장점(CTO 관점)
- **재현성/디버깅**: 규칙 기반은 실패 원인 추적이 가능
- **안정성**: 모델 업데이트(OpenRouter 모델 버전 변경)에도 영향이 상대적으로 제한
- **비용 예측 가능**: N시간/비용 예산을 계약하기 쉬움
- **규제/신뢰**: 정책/협상/마케팅 같은 도메인은 “왜 이런 결론이 나왔는지”가 중요

### 5.4 그래도 rule-based 안에서 “학습 같은 것”을 할 수 있다
- 오프라인에서 score weight를 베이지안 최적화/그리드로 튜닝
- candidate_pool counterfactual로 무료 ablation
- 불확실하면 rep를 추가(Sequential sampling)

즉, 모델 파라미터를 학습하지 않아도 “데이터 기반 개선”은 가능하다.

---

## 6) 추천 실행 순서(현실적인 로드맵)
1) **로그/감사 강화**  
   - action proposal 실패 이유, schema fail 이유, arbitration conflict 이유를 반드시 저장
2) **Anytime/CI 기반 반복 실행**  
   - “데이터 부족”을 제품 레벨에서 정면으로 다루기(범위 출력)
3) **Rule-based 강화(오버핏 방지)**  
   - scenario cue 기반 ‘절대 실행 보상’을 제거하고 band-matching 유지
4) (선택) **작은 ML 모듈 1개만**  
   - 가장 ROI 높은 건 보통 `action compiler` 또는 `reranker weight 학습`
5) (선택) judge distillation + selective escalation  
   - 상업 비용/시간 최적화 단계

---

## References (Bib-style)
- Jakob Nielsen. “Response Times: The 3 Important Limits.” 1993.
- Microsoft. “Data refresh in Power BI.” (문서; refresh 시간 제약/사례 포함)
- Zhicheng Liu et al. “The Effects of Interactive Latency on Exploratory Visual Analysis.” IEEE InfoVis, 2014.
- M. Angelini et al. “A Review and Characterization of Progressive Visual Analytics.” Big Data and Cognitive Computing, 2018.
- Pranav Bhandari et al. “Can LLM Agents Maintain a Persona in Discourse?” arXiv:2502.11843, 2025.
- Pat Verga et al. “Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models.” arXiv:2404.18796, 2024.
- Peiyi Wang et al. “Large Language Models are not Fair Evaluators.” arXiv:2305.17926, 2023.
- Rickard Stureborg et al. “Large Language Models are Inconsistent and Biased Evaluators.” arXiv:2405.01724, 2024.
- Jaehun Jung et al. “Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement.” arXiv:2407.18370, 2024.
- Joon Sung Park et al. “Generative Agents: Interactive Simulacra of Human Behavior.” arXiv:2304.03442, 2023.
- Shunyu Yao et al. “ReAct: Synergizing Reasoning and Acting in Language Models.” arXiv:2210.03629, 2022/2023.
- Marwa Abdulhai et al. “Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning.” arXiv:2511.00222, 2025.
