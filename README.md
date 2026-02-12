# UbeU V3: Dual-Mode AI Interview Platform

A research platform for AI-simulated interviews, supporting two distinct assessment modes:

## Overview

**Mode 1: Case Study Interview**
- 1-on-1 with AI Facilitator (data clerk only)
- Assesses logical/analytical thinking
- Evidence-based scoring on 6 dimensions

**Mode 2: Group Discussion**
- 1-to-many with 3 AI agents (Alex, Jordan, Riley)
- Assesses Big Five personality traits
- Behavioral signal extraction with facet-level inference

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENROUTER_API_KEY=your_key_here

# Run the application
streamlit run ui/app.py
```

## Project Structure

```
UbeU_V2/
├── agents/           # AI agent implementations
│   ├── facilitator_agent.py    # Mode 1: Data clerk
│   ├── group_agents.py         # Mode 2: Alex, Jordan, Riley
│   └── trait_selector.py       # Speaker selection strategy
├── engines/          # Interview session engines
│   ├── case_engine.py          # Mode 1 engine
│   └── group_engine.py         # Mode 2 engine
├── evaluation/       # Post-session assessment
│   ├── logic_evaluator.py      # 6-dimension rubric scoring
│   └── trait_evaluator.py      # OCEAN trait inference
├── config/           # Configuration files
│   ├── logic_rubric.py         # Scoring rubrics
│   ├── case_studies.py         # Business cases
│   └── group_scenarios.py      # Discussion scenarios
├── clients/          # LLM API clients
├── ui/               # Streamlit interface
├── utils/            # Shared utilities and models
└── pipeline/         # Data flow management
```

## Modes

### Mode 1: Case Study (Logical Assessment)

Dimensions assessed:
1. Problem Structuring
2. Hypothesis-Driven Thinking
3. Quantitative Reasoning
4. Data Synthesis
5. Recommendation Quality
6. Communication Clarity

Each score (1-5) backed by direct transcript quotes.

### Mode 2: Group Discussion (Personality Assessment)

Traits assessed (Big Five / OCEAN):
- Openness
- Conscientiousness
- Extraversion
- Agreeableness
- Neuroticism

Agent roles:
- **Alex**: Assertive Challenger (tests conflict handling)
- **Jordan**: Supportive Collaborator (tests idea engagement)
- **Riley**: Quiet Skeptic (tests engagement with quiet members)

## Academic Context

This platform is part of an NUS Final Year Thesis in Computer Science.

Research Questions:
1. Can AI-facilitated case interviews produce reliable logical assessments?
2. Can multi-party group discussions with AI agents produce valid personality estimates?
3. Do the two modes measure distinct constructs?

## References

- DialogLab (Hu et al., UIST 2025) - Multi-party conversation design
- Assessment Center methodology (Arthur et al., 2003)
- BFI-44 personality framework (John & Srivastava, 1999)
