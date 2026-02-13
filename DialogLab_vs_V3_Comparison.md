# DialogLab 소스코드 vs V3 아키텍처 비교 분석

**분석 대상**: [DialogLab GitHub](https://github.com/ecruhue/DialogLab) 소스코드 전체 vs Uber_V3.md 아키텍처 설계  
**분석일**: 2026-02-12

---

## 1. 핵심 요약: 범용 도구 vs 도메인 특화 시스템

DialogLab은 **범용 multi-party conversation authoring tool**이다. 어떤 대화든 설계할 수 있지만, 특정 평가 목적에 최적화되어 있지 않다. V3는 DialogLab의 프레임워크 개념을 채택하되, **personality assessment와 logical assessment라는 구체적 도메인**에 특화된 시스템을 설계한다.

| 차원 | DialogLab (코드 기준) | V3 Architecture |
|------|----------------------|-----------------|
| **목적** | 범용 대화 저작 도구 | 면접 평가 플랫폼 (personality + logic) |
| **Agent 성격** | 텍스트 서술 (`"a friendly person"`) | BFI 벡터 (O=0.6, C=0.5, E=0.8, A=0.3, N=0.3) |
| **화자 선택** | Round-robin / Party queue | TraitElicitationSelector (trait gap 기반) |
| **대화 구조** | Snippet 노드 그래프 (자유 설계) | 고정 시나리오 + Phase 구조 (trait-targeted) |
| **평가 체계** | Coherence/Sentiment (generic) | 6차원 Logic Rubric + 28-facet BFI detection |
| **증거 기반** | 없음 (점수만 제공) | Citation-based (모든 점수에 transcript 인용) |
| **Validation** | 없음 | Convergent/Discriminant/Test-retest validity |
| **Tech Stack** | React + Express (Node.js) | Streamlit + FastAPI (Python) |

---

## 2. 아키텍처 구조 비교

### 2.1 DialogLab 실제 구조 (코드에서 확인)

```
DialogLab/
├── client/                          # React + Vite (port 5173)
│   └── src/components/
│       ├── inspector/               # 설정 패널
│       │   ├── SnippetInspector.tsx  # Snippet(phase) 설정 UI
│       │   ├── store.ts             # Zustand 상태 관리
│       │   ├── PartyInspector.jsx   # Party 그룹 설정
│       │   └── SceneSelector.tsx    # Scene 전환 관리
│       ├── nodeeditor/              # 노드 기반 대화 흐름 편집기
│       ├── verification/            # 분석 대시보드
│       │   └── ConversationMetricsDashboard.tsx
│       ├── experience/              # 완성된 대화 재생 뷰어
│       └── preview/                 # 실시간 미리보기
│
└── server/                          # Express (port 3010)
    ├── server.js          (1241줄)  # API 라우팅, 대화 시작/관리
    ├── chat.js            (3053줄)  # ConversationManager (핵심 엔진)
    ├── agent.js           (392줄)   # Agent 클래스
    ├── chatutils.js       (306줄)   # 화자 선택, 컨텍스트 생성
    ├── conversationmemory.js        # 대화 기억 및 요약
    ├── verificationAPI.js           # Coherence/Sentiment 분석
    ├── contentManager.js            # 콘텐츠 파일 관리
    └── providers/                   # LLM 연동 (OpenAI, Gemini)
```

### 2.2 V3 설계 구조

```
pressure_cooker/
├── step2/
│   ├── engines/
│   │   ├── base_engine.py           # 공통 엔진 인터페이스
│   │   ├── case_engine.py           # Mode 1 전용 (1:1)
│   │   └── group_engine.py          # Mode 2 전용 (1:N)
│   ├── agents/
│   │   ├── facilitator_agent.py     # Mode 1: Data clerk만 수행
│   │   ├── group_agents.py          # Mode 2: Alex/Jordan/Riley
│   │   └── trait_selector.py        # Mode 2: 전략적 화자 선택
│   ├── evaluation/
│   │   ├── logic_evaluator.py       # Mode 1: 6차원 3-pass 평가
│   │   ├── trait_evaluator.py       # Mode 2: 3-layer 성격 추론
│   │   ├── validation_mode1.py      # Inter-rater reliability
│   │   ├── validation_mode2.py      # Convergent validity
│   │   └── cross_mode_analysis.py   # 구성 개념 독립성 검증
│   └── ui/pages/
│       ├── case_interview_page.py   # Mode 1 UI
│       ├── group_discussion_page.py # Mode 2 UI
│       └── results_page.py          # HR 대시보드
└── pipeline/
    ├── facet_detector.py            # 28-facet BFI detection
    ├── ensemble_detector.py         # 3-judge ensemble
    └── evidence_extractor.py        # Citation 기반 증거 추출
```

**핵심 차이**: DialogLab은 하나의 `ConversationManager` (3053줄)가 모든 것을 처리. V3는 Mode별로 독립 엔진을 분리하여 각 construct에 최적화.

---

## 3. Agent 시스템 비교

### 3.1 DialogLab의 Agent (`agent.js`)

```javascript
// DialogLab Agent - 성격이 자유 텍스트
class Agent {
  constructor(name, personality, interactionPattern, isHumanProxy = false,
              customAttributes = {}, fillerWordsFrequency = "none") {
    this.name = name;
    this.personality = personality;  // 예: "a friendly, outgoing person"
    this.interactionPattern = interactionPattern; // "neutral", "agree", "disagree"
    this.isDerailer = false;
    this.derailMode = "drift";  // "drift", "extend", "question", "emotional"
  }

  async reply(message, context, nextSpeaker, interruptionInfo, options) {
    const prompt = `You are ${this.name}, a ${this.personality} person.
            ${this.roleDescription ? "Role: " + this.roleDescription : ""}
            ${derailerContext}
            ${context}
            Respond briefly (1-2 sentences), building on previous points.
            After you speak, ${nextSpeaker} will respond.`;
    // ...
  }
}
```

**특징**:
- 성격이 자유 텍스트 (`"a friendly person"`) — 정량적 제어 불가
- `interactionPattern`은 전역 설정 (neutral/agree/disagree) — agent별 행동 차별화 제한적
- Derailer 모드는 대화 흐름 방해 용도 — 평가 목적이 아님
- 프롬프트가 간결 (1-2 sentences 지시) — 복잡한 역할 수행 불가

### 3.2 V3의 Agent 설계

```python
# V3 Mode 2 Agent - BFI 벡터로 정량적 성격 제어
AGENT_PROFILES = {
    "Alex": {
        "bfi_vector": {"O": 0.6, "C": 0.5, "E": 0.8, "A": 0.3, "N": 0.3},
        "role": "Assertive Challenger",
        "purpose": "Elicit conflict handling (A), stress response (N), assertiveness (E)",
        "behavior_instructions": [
            "Push back on ideas you disagree with",
            "Speak confidently in 3-5 sentences",
            "Challenge weak reasoning directly",
            "Propose competing alternatives"
        ],
        "trait_elicitation_targets": ["Agreeableness", "Neuroticism"]
    },
    # Jordan, Riley similarly defined...
}
```

**핵심 차이점**:

| 측면 | DialogLab | V3 |
|------|-----------|-----|
| 성격 표현 | 자유 텍스트 | BFI 5차원 벡터 (0.0-1.0) |
| 행동 지시 | 1줄 (`"a friendly person"`) | 구체적 행동 리스트 (4-6개 지시) |
| 목적 | 자연스러운 대화 생성 | 특정 trait elicitation |
| 검증 | 없음 | Step 1에서 trait consistency 검증 완료 (r ≈ 0.77-0.78) |
| 고정성 | 설정 자유 변경 가능 | 연구 목적으로 고정 (통제 변수) |

---

## 4. 대화 흐름 관리 비교

### 4.1 DialogLab의 Snippet 시스템

DialogLab에서 "snippet"은 **클라이언트 측 노드 그래프의 노드**이다. 서버에서는 snippet이라는 개념이 직접 구현되어 있지 않고, 각 snippet이 하나의 대화 세션 설정으로 변환되어 서버에 전송된다.

```typescript
// store.ts - SnippetNode 인터페이스
interface SnippetNode extends Node {
  subTopic?: string;
  topic?: string;
  turns?: number;                    // phase당 턴 수
  interactionPattern?: string;       // "neutral", "positive", "negative"
  turnTakingMode?: string;           // "round-robin", "free-form", "directed"
  partyMode?: boolean;
  partyTurnMode?: 'free' | 'round-robin' | 'moderated';
  conversationPrompt?: string;       // 자유 텍스트 프롬프트
  derailerMode?: boolean;
  interruptionRules?: InterruptionRule[];
  backChannelRules?: BackChannelRule[];
}
```

**실제 동작**: 각 snippet은 독립적인 대화 세션으로 실행됨. Snippet 간 전환은 클라이언트의 노드 에디터가 관리. 서버의 `ConversationManager`는 하나의 snippet 내에서만 동작.

### 4.2 V3의 Phase 시스템

```python
# V3 Mode 2 - 시나리오별 고정 Phase 구조
SCENARIOS = {
    "resource_conflict": {
        "primary_traits": ["Agreeableness", "Conscientiousness"],
        "phases": [
            {
                "name": "INTRODUCTION",
                "style": "neutral",
                "turns": 3,
                "ai_behavior": "Present scenario context"
            },
            {
                "name": "EXPLORATION",
                "style": "neutral",
                "turns": 4,
                "ai_behavior": "Share perspectives"
            },
            {
                "name": "CONFLICT",
                "style": "disagreement",
                "turns": 5,
                "ai_behavior": "Alex disagrees strongly",
                "trigger": "Alex challenges candidate's proposal"
            },
            {
                "name": "RESOLUTION",
                "style": "consensus",
                "turns": 4,
                "ai_behavior": "Move toward agreement"
            },
            {
                "name": "CLOSING",
                "style": "neutral",
                "turns": 2,
                "ai_behavior": "Summarize outcomes"
            }
        ]
    }
}
```

**핵심 차이점**:

| 측면 | DialogLab Snippet | V3 Phase |
|------|-------------------|----------|
| 설계 방식 | GUI 노드 에디터로 자유 설계 | 연구 목적으로 사전 고정 |
| 목적 | 대화 흐름 시각적 저작 | 특정 trait elicitation 순서 |
| Phase간 관계 | 노드 연결로 순서 지정 | 시나리오 내 순차 진행 |
| interaction style | "neutral/positive/negative" (3종) | "neutral/agreement/disagreement/consensus" (4종) |
| 유연성 | 완전 자유 (연구 도구) | 통제된 설계 (실험 변수) |

---

## 5. 화자 선택 로직 비교 — 가장 큰 차이

### 5.1 DialogLab: Round-Robin + Party Queue

DialogLab의 화자 선택은 **기계적**이다:

```javascript
// chatutils.js - 단순 round-robin
function getNextRoundRobinSpeaker(participants, lastSpeaker, lastSpeakerIndex) {
  const lastIndex = participants.indexOf(lastSpeaker);
  let nextIndex = (lastIndex + 1) % participants.length;
  // Skip same speaker
  while (participants[nextIndex] === lastSpeaker) {
    nextIndex = (nextIndex + 1) % participants.length;
  }
  return { nextSpeaker: participants[nextIndex], updatedIndex: nextIndex };
}

// chat.js - Party mode에서의 선택
// Party queue에서 순차적으로 꺼냄
if (this.partySpeakerQueue && this.partySpeakerQueue.length > 0) {
  currentSpeaker = this.partySpeakerQueue.shift();
}
```

**한계**: 누가 말하든 상관없이 순서대로 돌아감. "지금 Agreeableness를 더 관찰해야 하니까 Alex가 도전적 발언을 해야 한다" 같은 전략적 판단이 없음.

### 5.2 V3: TraitElicitationSelector (전략적 선택)

```python
# V3 Mode 2 - trait coverage gap 기반 전략적 화자 선택
class TraitElicitationSelector:
    def __init__(self):
        self.trait_coverage = {
            "Openness": 0.0, "Conscientiousness": 0.0,
            "Extraversion": 0.0, "Agreeableness": 0.0,
            "Neuroticism": 0.0
        }
        self.agent_trait_mapping = {
            "Alex":   ["Agreeableness", "Neuroticism"],    # 도전 → A, N 관찰
            "Jordan": ["Openness", "Conscientiousness"],    # 지지 → O, C 관찰
            "Riley":  ["Extraversion"]                      # 침묵 → E 관찰
        }

    def select_next_speaker(self, last_speaker, phase):
        # 가장 관찰 부족한 trait 파악
        least_covered = min(self.trait_coverage, key=self.trait_coverage.get)

        # 해당 trait을 elicit할 수 있는 agent 선택
        for agent, traits in self.agent_trait_mapping.items():
            if least_covered in traits and agent != last_speaker:
                return agent

        # Fallback: round-robin
        return self._round_robin(last_speaker)
```

**이것이 V3의 가장 핵심적인 학술적 기여**다. DialogLab은 "누가 다음에 말할까?"를 기계적으로 결정하지만, V3는 "어떤 trait을 더 관찰해야 하는가?"를 기준으로 전략적으로 결정한다.

---

## 6. 평가/분석 시스템 비교

### 6.1 DialogLab의 Verification

DialogLab의 분석은 **generic conversation analytics**에 그친다:

```javascript
// verificationAPI.js - LLM에 전체 대화를 던져서 점수를 받음
const prompt = `Analyze the following conversation and provide:
  1. A coherence score between 0 and 1
  2. An overall sentiment score between -1 and 1
  3. Individual sentiment scores for each participant
  Conversation: ${conversationText}`;

// ConversationMetricsDashboard.tsx - 시각화
// - PieChart: Speaking time distribution
// - BarChart: Engagement level
// - LineChart: Speaking time over time
// - RadarChart: Coherence, Turn-taking, Participation, Sentiment
```

**제공하는 지표**:
- Coherence score (0-1)
- Overall sentiment (-1 to 1)
- Per-participant sentiment
- Participation time
- Turn-taking frequency
- Speaking balance

**제공하지 않는 것**:
- ❌ 성격 추론
- ❌ 역량 평가
- ❌ 증거 기반 인용 (어떤 발언이 어떤 점수를 뒷받침하는지)
- ❌ Rubric 기반 평가
- ❌ Validation framework

### 6.2 V3의 Evidence-Based Evaluation

**Mode 1 (3-Pass Citation-Based Logic Evaluation)**:

```python
# 각 pass가 독립적으로 6차원을 평가하며, 반드시 transcript 인용 포함
LOGIC_EVAL_PROMPT = """
For each dimension, provide:
- Score (1-5) based on rubric anchors
- 2-4 direct quotes (verbatim, max 2 sentences each, with turn number)
- What each quote demonstrates
- Absent behaviors (expected but not observed)
- Rubric justification mapping score to specific anchor level

Example output:
{
  "problem_structuring": {
    "score": 4,
    "evidence": [
      {
        "quote": "Let me break this down into three areas: revenue, costs, and market share",
        "turn": 3,
        "demonstrates": "Clear framework application with 3 distinct dimensions"
      }
    ],
    "absent_behaviors": ["Did not revisit or update framework as new data emerged"],
    "rubric_justification": "Score 4: 'Strong structure, clear framework systematically applied'"
  }
}
"""
```

**Mode 2 (3-Layer Personality Inference)**:

```
Layer 1 (Real-time, rule-based):
  - word_count per turn → Extraversion signal
  - hedging language → Agreeableness signal
  - proposed_new_idea → Openness signal

Layer 2 (Post-session, LLM):
  - 28-facet BFI detection (기존 Step 1 인프라 재사용)

Layer 3 (Post-session, ensemble):
  - DeepSeek + Claude + Gemini → median aggregation
  - Inter-judge agreement 측정
```

**비교 요약**:

| 측면 | DialogLab | V3 Mode 1 | V3 Mode 2 |
|------|-----------|-----------|-----------|
| 평가 대상 | Coherence, Sentiment | 논리적 사고력 (6차원) | Big Five 성격 (5차원, 28 facet) |
| 평가 방법 | LLM 1회 호출 | 3-pass 독립 평가 → median | 3-layer (rule + LLM + ensemble) |
| 증거 체계 | 없음 | 직접 인용 + turn number | 직접 인용 + signal direction |
| Rubric | 없음 | 5-level anchored rubric | BFI-44 ground truth 대비 |
| 신뢰도 측정 | 없음 | Inter-rater reliability (3-pass agreement) | Inter-judge agreement (3-model) |

---

## 7. Conversation Mode 비교

### 7.1 DialogLab의 3가지 모드 (코드에서 확인)

```javascript
// server.js - 대화 모드 설정
switch (config.conversationMode) {
  case 'human-control':
    // 사용자가 AI 발언을 승인/거부 가능
    conversationManager.requireImpromptuApproval = true;
    conversationManager.autoApproveImpromptu = false;
    break;
  case 'autonomous':
    // AI가 자동으로 대화 진행
    conversationManager.autoApproveImpromptu = true;
    break;
  case 'reactive':
    // AI가 직접 언급될 때만 반응
    conversationManager.derailingEnabled = false;
    break;
}
```

DialogLab 논문의 실험 결과: **Human Control이 Engagement, Effectiveness, Realism에서 가장 높은 평가**.

### 7.2 V3의 하이브리드 모드

V3는 DialogLab의 실험 결과를 근거로 하이브리드 접근:

- **Candidate 측**: 자유 입력 (Human Control 요소 — 언제든 원하는 말 가능)
- **AI 측**: TraitElicitationSelector가 전략적으로 응답 에이전트 선택 (Autonomous 요소)
- **결과**: Candidate는 자연스럽게 느끼면서도, 시스템은 평가에 필요한 행동을 체계적으로 elicit

이 하이브리드 설계가 DialogLab 논문을 근거로 학술적 정당화가 되는 부분.

---

## 8. Party Mode vs Personality Tension Triangle

### 8.1 DialogLab의 Party 시스템

DialogLab은 agent들을 "Party"로 그룹화하는 범용 시스템을 제공:

```javascript
// chat.js - Party 생성
createParty(partyName, members, config = {}) {
  this.parties.set(partyName, [...members]);
  members.forEach(member => {
    this.partyMembership.set(member, partyName);
  });
  // speakingMode: "all", "representative", "subset", "sequential"
}

// Party 턴 모드: "free", "round-robin", "moderated"
enablePartyMode(turnMode = "free", moderatorParty = null)
```

**용도**: 토론 팀 구성, 대표 발언자 지정, 사회자 제어 등 범용적 그룹 관리.

### 8.2 V3의 Personality Tension Triangle

V3는 Party 개념 대신 **고정된 성격 관계 구조**를 설계:

```
Alex (Assertive) ←──갈등──→ Candidate
     ↓                          ↑
     ↕ 의견 충돌                 ↕ 리더십/협업
     ↑                          ↓
Jordan (Supportive) ───지지──→ Candidate
                                ↑
Riley (Silent) ────────침묵────→ (engage하는가?)
```

**각 관계가 특정 trait을 elicit**:
- Alex vs Candidate → **Agreeableness** (수용 vs 반박), **Neuroticism** (침착 vs 스트레스)
- Jordan + Candidate → **Openness** (아이디어 탐색), **Extraversion** (주도 vs 따라감)
- Riley의 침묵 → **Extraversion** (먼저 말 거는가), **Agreeableness** (포용 vs 무시)
- Alex vs Jordan 의견 충돌 → Candidate의 중재 행동 관찰

이건 DialogLab이 전혀 제공하지 않는, **평가 목적에 특화된 사회적 구조 설계**.

---

## 9. V3가 DialogLab에서 가져가야 할 것 vs 새로 만들어야 할 것

### ✅ 가져갈 수 있는 개념 (논문 citation 근거)

| DialogLab 개념 | V3에서의 활용 | 코드 참고 가능? |
|----------------|--------------|----------------|
| Group Dynamics ↔ Flow 분리 | Agent persona를 Phase 관리에서 독립 | ✅ 개념적으로 참고 |
| Snippet = Phase | 시나리오별 phase 구조 정당화 | ✅ SnippetNode 인터페이스 참고 |
| Human Control 우월성 | 하이브리드 모드 정당화 (p < .05) | ✅ 실험 결과 citation |
| Verification dashboard | HR 대시보드 정당화 | ⚠️ 매우 basic, 대부분 새로 설계 필요 |
| InteractionPattern | Phase별 interaction style | ✅ neutral/agree/disagree 매핑 |
| BackchannelRules | Non-verbal 반응 (끄덕임 등) | ⚠️ 컨셉은 좋으나 personality assessment에선 불필요할 수 있음 |

### 🔨 새로 만들어야 할 것 (DialogLab에 없음)

| 기능 | 왜 DialogLab에 없는가 | V3에서 필요한 이유 |
|------|----------------------|-------------------|
| **TraitElicitationSelector** | 범용 도구라 평가 목적 없음 | Personality assessment의 핵심 |
| **BFI 벡터 기반 Agent** | 성격이 자유 텍스트 | 정량적 성격 제어 + Step 1 검증 연결 |
| **Citation-based evaluation** | 분석이 전체 점수만 제공 | Evidence-based assessment의 핵심 |
| **Logic Rubric (6차원)** | Case study 평가 기능 없음 | Mode 1의 핵심 평가 체계 |
| **3-layer personality inference** | 성격 추론 기능 없음 | Mode 2의 핵심 평가 체계 |
| **Convergent validity** | Validation 개념 자체 없음 | 학술 논문의 핵심 증거 |
| **Construct independence test** | 단일 모드만 존재 | 두 모드가 다른 것을 측정하는지 증명 |
| **Behavioral scenario design** | 시나리오가 자유 설정 | Trait-targeted 상황 설계 |

---

## 10. 코드 수준에서의 구체적 차이점

### 10.1 DialogLab `ConversationManager.continueConversation()` (핵심 루프)

```javascript
// chat.js:661 - 3053줄짜리 클래스의 핵심 메서드
async continueConversation(participants, lastSpeaker, lastRecipient) {
  // 1. Derailer 체크 (대화 탈선 시도)
  if (!this.impromptuPhaseActive && this.derailingEnabled) {
    const derailResponse = await this.checkForDerailInterventions(/*...*/);
    // 승인 모드면 pause, 자동이면 즉시 실행
  }

  // 2. 턴 루프
  while (this.currentTurn < this.maxTurns) {
    // Party mode 처리...
    // 화자 선택 (round-robin 또는 party queue)
    let currentSpeaker = this.partySpeakerQueue.shift()
                      || this.getNextSpeakerExcluding(participants, lastSpeaker);

    // 3. Agent reply 생성
    const reply = await this.generateReplyMessage(currentAgent, lastMessage, nextRecipient);

    // 4. 대화 업데이트
    this.updateConversation(message);
    this.currentTurn++;
  }
}
```

**특징**: 범용적이고 유연하지만, 평가 로직 없음. 대화 생성에만 집중.

### 10.2 V3 `GroupEngine` (설계)

```python
# V3 Mode 2 - 평가 중심 대화 루프 (설계)
class GroupEngine:
    async def run_discussion(self, scenario, candidate_id):
        for phase in scenario.phases:
            self.current_phase = phase
            turns_in_phase = 0

            while turns_in_phase < phase.max_turns:
                # 1. Candidate 입력 대기
                candidate_msg = await self.wait_for_candidate_input()

                # 2. Real-time behavioral signal 추출 (Layer 1)
                signals = self.extract_behavioral_signals(candidate_msg)
                self.trait_coverage.update(signals)

                # 3. 전략적 AI 화자 선택 (trait gap 기반)
                next_speaker = self.trait_selector.select_next_speaker(
                    last_speaker=candidate_msg.speaker,
                    phase=phase,
                    trait_coverage=self.trait_coverage
                )

                # 4. 선택된 Agent의 응답 생성
                ai_response = await self.generate_agent_response(
                    agent=next_speaker,
                    phase=phase,
                    context=self.conversation_history
                )

                # 5. Phase 전환 체크
                if self.should_transition_phase(turns_in_phase, phase):
                    break

        # Post-session: Layer 2 + Layer 3 평가
        facet_scores = await self.facet_detector.detect(self.transcript)
        ensemble_scores = await self.ensemble_detector.evaluate(self.transcript)
        evidence = await self.evidence_extractor.extract(self.transcript, ensemble_scores)
```

---

## 11. 학술적 positioning 전략

DialogLab 코드를 분석한 결과, 논문에서 다음과 같이 positioning 가능:

### Citation 전략

> "DialogLab (Hu et al., UIST 2025) demonstrates that multi-party human-AI conversations can be effectively orchestrated through a separation of group dynamics from conversation flow, with snippet-based phase management. Their evaluation showed Human Control mode achieved significantly higher engagement (p < .05). We adopt this framework for a specific applied domain — personality assessment — extending it with three key innovations:
>
> 1. **Trait-calibrated agents** with quantified BFI personality vectors (replacing DialogLab's free-text personality descriptions) whose behavioral consistency is empirically validated (Pearson r ≥ 0.77);
> 2. **Strategic speaker selection** driven by trait coverage gaps (replacing DialogLab's round-robin selection) to systematically elicit observable personality signals; and
> 3. **Citation-based evidence evaluation** linking every assessment score to specific transcript quotes (extending DialogLab's generic coherence/sentiment analytics into domain-specific competency assessment)."

### 학술적 기여 차별화

| DialogLab의 기여 (UIST 2025) | V3의 기여 (너의 논문) |
|------------------------------|---------------------|
| 범용 multi-party 대화 저작 프레임워크 | 도메인 특화 (personality assessment) 적용 |
| 3가지 conversation mode 비교 | Hybrid mode의 심리측정학적 정당화 |
| Coherence/Sentiment 분석 | Evidence-based 역량/성격 평가 |
| Node-based snippet 편집기 | Trait-targeted phase 설계 |
| LLM-powered 3D avatar 대화 | LLM-powered 심리측정 도구 |

---

## 12. 실행 시사점

### DialogLab 코드에서 직접 가져올 수 있는 것
1. **InteractionPattern 개념**: `"neutral" | "positive" | "negative" | "questioning"` → Phase별 style로 활용
2. **Backchannel 개념**: Non-verbal 반응 생성 → Group discussion의 자연스러움 향상에 선택적 활용
3. **ConversationMemory의 covered points tracking**: 중복 발언 방지 로직 → 시나리오 내 반복 방지에 참고
4. **LLM Provider abstraction**: Multi-provider 지원 패턴 → OpenRouter 사용 시 참고

### DialogLab 코드에서 가져오면 안 되는 것
1. **3053줄 단일 ConversationManager**: 모든 로직이 한 파일 — Mode 분리 불가
2. **Round-robin speaker selection**: 평가 목적에 부적합
3. **자유 텍스트 성격 설정**: 정량적 제어 불가
4. **Derailer 시스템**: 대화 방해 용도 — 평가 시스템에서는 불필요
5. **Client-side snippet management**: React + node editor — Streamlit 기반인 V3와 호환 불가

---

## 13. 결론

DialogLab은 **훌륭한 연구 도구이자 학술적 프레임워크**지만, 실제 코드는 범용 대화 저작에 초점이 맞춰져 있어 personality assessment에 직접 활용하기 어렵다. V3 아키텍처는 DialogLab의 **개념적 프레임워크** (Group Dynamics ↔ Flow 분리, Snippet/Phase, Human Control 우월성)를 학술적 근거로 citation하되, **핵심 엔진은 완전히 새로 설계**해야 한다.

가장 중요한 차별화 포인트:
1. **화자 선택이 평가 목적을 반영** (TraitElicitationSelector)
2. **모든 점수에 transcript 인용이 동반** (Citation-based evidence)
3. **두 모드가 서로 다른 construct를 측정함을 검증** (Construct independence)

이 세 가지가 DialogLab을 넘어서는 V3만의 학술적 기여다.
