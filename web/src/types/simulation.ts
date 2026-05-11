/* ── Core simulation types ───────────────────────────────────── */

export interface StakeholderActor {
  actor_id: string;
  display_name: string;
  role: string;
  identity_core: Record<string, string>;
  personality_prior: OceanTraits;
  personality_envelope: Record<string, [number, number]>;
  incentives: string[];
  concerns: string[];
  communication_style: Record<string, string>;
  experience_summary: string;
  strategic_disposition: Disposition;
  disposition_strength: number;
}

export interface OceanTraits {
  [key: string]: number;
  O: number;
  C: number;
  E: number;
  A: number;
  N: number;
}

export type Disposition = 'cooperative' | 'neutral' | 'competitive' | 'adversarial';

export interface SimulationPhase {
  name: string;
  goal: string;
  style: string;
  max_turns: number;
  cues: string[];
}

export interface SimulationScript {
  simulation_id: string;
  title: string;
  objective: string;
  brief: string;
  stakeholders: StakeholderActor[];
  phases: SimulationPhase[];
  scenario_family: string;
  simulation_mode: 'guided' | 'exploratory';
  world_state_schema: string[];
  initial_world_state: Record<string, number>;
  outcome_spec?: Record<string, unknown>;
  allowed_action_types: string[];
  world_events: WorldEvent[];
  metadata: Record<string, unknown>;
}

export interface WorldEvent {
  event_id: string;
  title: string;
  description: string;
  trigger_phase: string;
}

export interface ActorRelationship {
  id: string;
  source: string;   // actor_id
  target: string;   // actor_id
  label: string;    // e.g., "competing for budget", "policy allies"
}

/* ── WebSocket Events ────────────────────────────────────────── */

export interface ActorMeta {
  actor_id: string;
  display_name: string;
  role: string;
  disposition: Disposition;
}

export type SimEvent =
  | { type: 'turn'; data: TurnEvent }
  | { type: 'action'; data: ActionEvent }
  | { type: 'relationship'; data: RelationshipEvent }
  | { type: 'phase_change'; data: PhaseChangeEvent }
  | { type: 'metric_update'; data: MetricUpdate }
  | { type: 'actors_init'; data: { actors: ActorMeta[] } }
  | { type: 'complete'; data: { simulation_id: string } }
  | { type: 'status'; data: { status: string; simulation_id: string } }
  | { type: 'error'; data: { message: string } }
  | { type: 'ping'; data: Record<string, never> };

export interface TurnEvent {
  actor_id: string;
  display_name: string;
  content: string;
  phase: string;
  turn_index: number;
}

export interface ActionEvent {
  actor_id: string;
  action_type: string;
  target_key: string;
  deltas: Record<string, number>;
  phase: string;
}

export interface RelationshipEvent {
  source: string;
  target: string;
  sentiment: 'positive' | 'negative' | 'challenging' | 'neutral';
  trust_delta: number;
  tension_delta: number;
  evidence: string;
  turn_index: number;
}

export interface PhaseChangeEvent {
  from: string;
  to: string;
}

export interface MetricUpdate {
  persona_drift_mae: number;
  commitment_contradiction_rate: number;
  relationship_inconsistency: number;
  envelope_violations: number;
}

/* ── Conclusion ──────────────────────────────────────────────── */

export interface ActorArc {
  actor_id: string;
  role: string;
  arc: string;
}

export interface SimulationConclusion {
  mode: 'guided' | 'exploratory';
  outcome_achieved?: 'achieved' | 'partial' | 'not_achieved';
  outcome_summary: string;
  contributing_factors?: string[];
  key_discoveries?: string[];
  actor_arcs: ActorArc[];
  unresolved_tensions: string[];
  emergent_patterns?: string[];
}

/* ── Results ─────────────────────────────────────────────────── */

export interface KeyMoment {
  turn_index: number;
  phase_name: string;
  event_type: 'relationship_shift' | 'action' | 'drift_spike' | 'phase_change' | 'commitment';
  title: string;
  description: string;
  evidence: string;
  impact: Record<string, unknown>;
  actors_involved: string[];
  score: number;
}

export interface SimulationResults {
  simulation_id: string;
  runtime_summary: RuntimeSummary;
  metrics: SimulationMetrics;
  key_moments: KeyMoment[];
  conclusion?: SimulationConclusion;
  script: SimulationScript;
  initial_relationships?: InitialRelationshipSummary[];
  final_relationships?: FinalRelationshipSummary[];
  actor_final_state_summary?: ActorFinalStateSummary[];
  change_events?: ChangeEventSummary[];
  change_attribution?: Record<string, ChangeTrigger[]>;
  phase_summaries?: PhaseSummary[];
  insight_cards?: InsightCard[];
  relationship_analysis?: RelationshipAnalysis;
  actor_analysis?: ActorAnalysis;
  outcome_analysis?: OutcomeAnalysis;
  phase_filtered_attribution?: Record<string, PhaseFilteredAttribution>;
}

export interface RuntimeSummary {
  simulation_id: string;
  title: string;
  objective: string;
  turns: TurnRecord[];
  relationship_events: RelationshipRecord[];
  actor_state_events: ActorStateRecord[];
  executed_actions: ExecutedActionRecord[];
  action_proposals: ActionProposalRecord[];
  world_state_history: WorldStateSnapshot[];
  phase_order: string[];
  actor_personality_priors: Record<string, OceanTraits>;
  actor_personality_envelopes: Record<string, Record<string, [number, number]>>;
  actor_display_names: Record<string, string>;
  actor_labels: Record<string, string>;
  turn_count: number;
}

export interface TurnRecord {
  turn_index: number;
  actor_id: string;
  display_name: string;
  content: string;
  phase_name: string;
  metadata: Record<string, unknown>;
}

export interface RelationshipRecord {
  source_actor_id: string;
  target_actor_id: string;
  trust_delta: number;
  tension_delta: number;
  evidence: string;
  turn_index: number;
  phase_name: string;
  source?: string;
  target?: string;
}

export interface ActorStateRecord {
  actor_id: string;
  turn_index: number;
  phase_name: string;
  cause_type?: string;
  drift_score?: number;
  rolling_trait_estimate?: OceanTraits;
  prior_state?: Record<string, unknown>;
  new_state?: {
    drift_score?: number;
    rolling_trait_estimate?: OceanTraits;
    stress?: number;
    trust_map?: Record<string, number>;
    stance_map?: Record<string, number>;
    [key: string]: unknown;
  };
}

export interface ExecutedActionRecord {
  proposal_id: string;
  action_type: string;
  phase_name: string;
  owner_actor_id: string;
  target_key: string;
  applied_delta: Record<string, number>;
}

export interface ActionProposalRecord {
  proposal_id: string;
  actor_id: string;
  phase_name: string;
  turn_index: number;
  action_type: string;
  status: string;
}

export interface WorldStateSnapshot {
  phase_name: string;
  turn_index: number;
  global_state: Record<string, number>;
}

export interface SimulationMetrics {
  persona_drift_mae: number;
  relationship_inconsistency: number;
  commitment_contradiction_rate: number;
  envelope_violations: number;
  actor_trait_estimates: Record<string, OceanTraits>;
  actor_trait_errors: Record<string, OceanTraits>;
  actor_display_names: Record<string, string>;
  [key: string]: unknown;
}

export interface InitialRelationshipSummary {
  relationship_id: string;
  source_actor_id: string;
  target_actor_id: string;
  label: string;
  trust: number;
  tension: number;
  display_label: string;
}

export interface FinalRelationshipSummary {
  relationship_id: string;
  source_actor_id: string;
  target_actor_id: string;
  display_label: string;
  initial_trust: number;
  initial_tension: number;
  total_trust_delta: number;
  total_tension_delta: number;
  final_trust: number;
  final_tension: number;
  event_count: number;
  last_turn_index: number;
  last_evidence: string;
  sentiment: string;
  label: string;
}

export interface ActorFinalStateSummary {
  actor_id: string;
  display_name: string;
  final_trait_estimate: OceanTraits;
  final_drift_score: number;
  stress: number;
  initial_stance_summary?: string;
  strongest_trait_shift?: {
    trait: string;
    initial: number;
    final: number;
    delta: number;
  } | null;
  top_relationship_shift?: {
    target_actor_id: string;
    target_label: string;
    trust_delta: number;
    tension_delta: number;
  } | null;
  end_state_summary: string;
  after_summary?: string;
}

export interface ActorEvidenceItem {
  evidence_id: string;
  type: 'relationship' | 'actor_drift' | 'action';
  actor_id: string;
  other_actor_id?: string | null;
  phase_name: string;
  turn_index: number;
  summary: string;
  why_it_matters: string;
  quote: string;
  related_relationship_id?: string | null;
  related_action_id?: string | null;
  situation?: string;
  intention?: string;
  incentive?: string;
  penalty?: string;
  action?: string;
  decision_shift?: string;
}

export interface RelationshipPhaseDelta {
  phase_name: string;
  trust_delta: number;
  tension_delta: number;
  event_count: number;
}

export interface RelationshipAnalysisItem {
  relationship_id: string;
  source_actor_id: string;
  target_actor_id: string;
  display_label: string;
  label: string;
  initial: {
    trust: number;
    tension: number;
  };
  final: {
    trust: number;
    tension: number;
  };
  delta: {
    trust: number;
    tension: number;
  };
  event_count: number;
  phase_deltas: RelationshipPhaseDelta[];
  top_trigger_summaries: ActorEvidenceItem[];
}

export interface RelationshipAnalysis {
  pairs: RelationshipAnalysisItem[];
}

export interface ActorRelationshipChange {
  relationship_id: string;
  counterpart_actor_id: string;
  counterpart_label: string;
  direction: 'outgoing' | 'incoming';
  trust_delta: number;
  tension_delta: number;
}

export interface ActorBeforeSummary {
  role: string;
  disposition: string;
  incentives: string[];
  concerns: string[];
  stance: string;
}

export interface ActorAfterSummary {
  end_state: string;
  comparison_text: string;
  drift_interpretation: string;
  strongest_relationship_change?: ActorRelationshipChange | null;
}

export interface ActorAnalysisItem {
  actor_id: string;
  display_name: string;
  before_summary: ActorBeforeSummary;
  after_summary: ActorAfterSummary;
  initial_traits: OceanTraits;
  final_traits: OceanTraits;
  largest_trait_shift?: {
    trait: string;
    initial: number;
    final: number;
    delta: number;
  } | null;
  final_drift_score: number;
  relationship_changes: ActorRelationshipChange[];
  evidence_by_type: Record<'relationship' | 'actor_drift' | 'action', ActorEvidenceItem[]>;
  change_narrative: string;
}

export interface ActorAnalysis {
  actors: ActorAnalysisItem[];
}

export interface OutcomeDriverSummary {
  driver_id: string;
  change_id: string;
  title: string;
  summary: string;
  why_it_matters: string;
  phase_name: string;
  actor_ids: string[];
  evidence_ids: string[];
}

export interface OutcomeAnalysis {
  mode: 'guided' | 'exploratory';
  target_outcome?: Record<string, unknown> | null;
  actual_outcome: string;
  outcome_status: 'hit' | 'partial' | 'miss' | 'emergent';
  difference_summary: string;
  derivation_summary: string;
  driver_change_ids: string[];
  driver_summaries: OutcomeDriverSummary[];
  stage_summaries?: Array<{
    stage_id: string;
    label: string;
    conclusion: string;
    phase_names: string[];
    trigger_evidence_ids: string[];
  }>;
}

export interface PhaseFilteredAttribution {
  relationship: ActorEvidenceItem[];
  actor_drift: ActorEvidenceItem[];
  action: ActorEvidenceItem[];
  all: ActorEvidenceItem[];
}

export type ChangeCategory = 'relationship' | 'world_state' | 'actor_drift' | 'action';

export interface ChangeEventSummary {
  change_id: string;
  category: ChangeCategory;
  label: string;
  summary: string;
  magnitude: number;
  phase_name: string;
  affected_actor_ids: string[];
  affected_keys: string[];
  trigger_summary: string;
  meaning?: string;
  initial_value: unknown;
  final_value: unknown;
  delta: unknown;
}

export interface ChangeTrigger {
  trigger_id: string;
  kind: 'turn' | 'action' | 'relationship' | 'phase';
  turn_index: number;
  phase_name: string;
  actor_id: string;
  weight: number;
  summary: string;
  evidence: string;
  related_ids: string[];
}

export interface PhaseSummary {
  phase_name: string;
  top_change_ids: string[];
  world_state_deltas: Record<string, number>;
}

export interface InsightCard {
  insight_id: string;
  title: string;
  summary: string;
  meaning: string;
  related_change_ids: string[];
}

export interface ScenarioCard {
  id: string;
  title: string;
  brief: string;
  actor_count: number;
  tags: string[];
  category: string;          // e.g. "guided-policy", "exploratory-business"
  simulation_mode: string;   // "guided" or "exploratory"
}

/* ── Actor Colors ────────────────────────────────────────────── */

export const ACTOR_COLORS = [
  '#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6',
  '#06b6d4', '#ec4899', '#84cc16', '#f97316', '#14b8a6',
] as const;

export const DISPOSITION_CONFIG: Record<Disposition, { color: string; bg: string; lucide: string }> = {
  cooperative: { color: 'text-green-400', bg: 'bg-green-500/20', lucide: 'heart-handshake' },
  neutral:     { color: 'text-zinc-400', bg: 'bg-zinc-500/20',  lucide: 'scale' },
  competitive: { color: 'text-amber-400', bg: 'bg-amber-500/20', lucide: 'swords' },
  adversarial: { color: 'text-red-400',   bg: 'bg-red-500/20',   lucide: 'shield-alert' },
};

export const TRAIT_LABELS: Record<string, string> = {
  O: 'Openness',
  C: 'Conscientiousness',
  E: 'Extraversion',
  A: 'Agreeableness',
  N: 'Neuroticism',
};
