"""
AI Candidate Test Runner for Interview Platform.
Runs automated interview sessions using AI test candidates.
"""

import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.test_candidate_agent import AITestCandidate
from clients.llm_client import LLMClient
from config.test_personas import get_test_persona, get_all_test_persona_ids
from step2.consulting_scenarios import get_consulting_scenario, get_all_consulting_scenario_ids
from step2.live_engine import LiveEngine, SmartLiveEngine
from step2.validator_agent import validate_session
from config.scenarios import SCENARIOS

DEFAULT_MAX_TURNS = 30


class AIInterviewTester:
    def __init__(self, output_dir: Path = Path("outputs/step2/ai_tests"), max_turns: int = DEFAULT_MAX_TURNS, use_smart_engine: bool = False):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.max_turns = max_turns
        self.use_smart_engine = use_smart_engine

    def _create_client(self) -> LLMClient:
        return LLMClient()

    def _create_validator_client(self) -> LLMClient:
        return LLMClient(pro_model="anthropic/claude-haiku-4.5")

    async def run_single_test(self, persona_id: str, scenario_id: str, test_number: int = 0, total_tests: int = 1) -> dict:
        client = self._create_client()
        validator_client = self._create_validator_client()
        persona = get_test_persona(persona_id)
        case_study = get_consulting_scenario(scenario_id)
        test_id = f"{persona_id}_{scenario_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        engine_type = "SmartLiveEngine" if self.use_smart_engine else "LiveEngine"
        print(f"\n[{test_number}/{total_tests}] Starting: {persona.name} on {case_study.company_name} ({engine_type})")

        scenario_config = list(SCENARIOS.values())[0]

        if self.use_smart_engine:
            engine = SmartLiveEngine(
                client=client,
                scenario=scenario_config,
                participant_name=persona.display_name,
                case_study=case_study,
                use_smart_agents=True,
            )
        else:
            engine = LiveEngine(client=client, scenario=scenario_config, participant_name=persona.display_name, case_study=case_study)

        ai_candidate = AITestCandidate(client=client, scenario=scenario_config, persona=persona, case_study=case_study)

        opening_turns = await engine.generate_opening()
        for turn in opening_turns:
            print(f"  [{turn.speaker_name}]: {turn.content[:80]}...")

        turn_count = 0
        while engine.state.value not in ("ended",) and turn_count < self.max_turns:
            turn_count += 1
            ai_candidate.update_revealed_categories(engine.revealed_categories)
            context = f"{engine.turns[-1].speaker_name}: {engine.turns[-1].content}" if engine.turns else ""
            candidate_response = await ai_candidate.generate_response(context)
            print(f"  [{persona.display_name}]: {candidate_response[:80]}...")
            engine.submit_human_turn(candidate_response)
            ai_turns = await engine.generate_ai_turns_until_human()
            for turn in ai_turns:
                print(f"  [{turn.speaker_name}]: {turn.content[:80]}...")

            # Show smart engine status
            if self.use_smart_engine:
                phase = engine.get_discussion_phase()
                coverage = engine.get_competency_coverage()
                tested = sum(c["tested"] for c in coverage.values())
                total = sum(c["total"] for c in coverage.values())
                targeting = engine.get_targeting_info()
                target_str = f"{targeting.get('target_competency', 'none')}" if targeting else "none"
                print(f"    [Phase: {phase} | Coverage: {tested}/{total} | Target: {target_str}]")

            if engine.state.value == "ended":
                break

        if engine.state.value != "ended":
            await engine.end_session()

        print(f"  Session complete: {len(engine.turns)} turns")
        session_output = await engine.finalize_session_output(f"ai_test_{persona_id}", persona.personality)

        print(f"  Running logical validation...")
        validation_result = await validate_session(engine.turns, case_study, validator_client, num_passes=3)
        print(f"  Validation: depth={validation_result.get('analytical_depth')}, rec={validation_result.get('recommendation_quality')}")

        result = {
            "test_id": test_id,
            "timestamp": datetime.now().isoformat(),
            "engine_type": "SmartLiveEngine" if self.use_smart_engine else "LiveEngine",
            "persona": {"id": persona.id, "name": persona.name, "display_name": persona.display_name},
            "scenario": {"id": scenario_id, "company": case_study.company_name},
            "session_stats": {
                "total_turns": len(engine.turns),
                "revealed_categories": list(engine.revealed_categories),
            },
            "personality_analysis": {
                "intent_statistics": session_output.intent_statistics.model_dump() if session_output.intent_statistics else None,
                "assessment_mapping": session_output.assessment_mapping.model_dump() if session_output.assessment_mapping else None,
            },
            "logical_assessment": validation_result,
            "conversation": [{"turn": t.turn_number, "speaker": t.speaker_name, "content": t.content} for t in engine.turns],
        }

        # Add smart engine data if applicable
        if self.use_smart_engine:
            result["smart_engine_data"] = {
                "final_phase": engine.get_discussion_phase(),
                "competency_coverage": engine.get_competency_coverage(),
            }
            # Add evidence assessment if available
            evidence = engine.get_evidence_assessment()
            if evidence:
                result["evidence_assessment"] = {
                    "turns_analyzed": evidence.total_turns_analyzed,
                    "competency_scores": {
                        score.dimension.value: {"score": score.score, "evidence_count": len(score.evidence)}
                        for score in evidence.competency_scores
                    } if evidence.competency_scores else {},
                }
            print(f"  Final phase: {engine.get_discussion_phase()}")
            coverage = engine.get_competency_coverage()
            for name, data in coverage.items():
                status = "✓" if data["coverage"] >= 0.5 else "○"
                print(f"    {status} {name}: {data['tested']}/{data['total']} ({data['coverage']*100:.0f}%)")

        output_file = self.output_dir / f"{test_id}.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2, default=str)
        print(f"  Saved: {output_file.name}")
        return result

    async def run_all_tests(self, persona_ids=None, scenario_ids=None):
        if persona_ids is None:
            persona_ids = get_all_test_persona_ids()
        if scenario_ids is None:
            scenario_ids = get_all_consulting_scenario_ids()

        test_configs = [(p, s) for p in persona_ids for s in scenario_ids]
        total = len(test_configs)
        print(f"\nRunning {total} tests...\n")

        results = []
        for i, (persona_id, scenario_id) in enumerate(test_configs):
            try:
                result = await self.run_single_test(persona_id, scenario_id, i + 1, total)
                results.append(result)
            except Exception as e:
                print(f"FAILED: {persona_id} x {scenario_id}: {e}")

        # Save summary
        summary_file = self.output_dir / f"test_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        summary = {"total": len(results), "results": [{"persona": r["persona"]["name"], "scenario": r["scenario"]["company"],
                   "depth": r["logical_assessment"].get("analytical_depth", 0),
                   "rec": r["logical_assessment"].get("recommendation_quality", 0)} for r in results]}
        with open(summary_file, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"\nSummary saved: {summary_file}")
        return results


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--persona", choices=get_all_test_persona_ids())
    parser.add_argument("--scenario", choices=get_all_consulting_scenario_ids())
    parser.add_argument("--max-turns", type=int, default=DEFAULT_MAX_TURNS)
    parser.add_argument("--smart", action="store_true", help="Use SmartLiveEngine with competency targeting")
    args = parser.parse_args()

    tester = AIInterviewTester(max_turns=args.max_turns, use_smart_engine=args.smart)
    persona_ids = [args.persona] if args.persona else None
    scenario_ids = [args.scenario] if args.scenario else None
    await tester.run_all_tests(persona_ids, scenario_ids)


if __name__ == "__main__":
    asyncio.run(main())
