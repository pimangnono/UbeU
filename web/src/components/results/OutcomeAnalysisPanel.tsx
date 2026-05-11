import { CheckCircle2, Compass, Target, TriangleAlert, XCircle } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import { RelationshipNetworkCompare } from './RelationshipNetworkCompare';
import { OutcomeDriverTimeline } from './OutcomeDriverTimeline';
import type {
  ActorEvidenceItem,
  FinalRelationshipSummary,
  InitialRelationshipSummary,
  OutcomeAnalysis,
  RelationshipAnalysisItem,
  StakeholderActor,
} from '../../types/simulation';

interface OutcomeAnalysisPanelProps {
  mode: 'guided' | 'exploratory';
  outcomeAnalysis: OutcomeAnalysis | null;
  actors: StakeholderActor[];
  beforeRelationships: InitialRelationshipSummary[];
  afterRelationships: FinalRelationshipSummary[];
  selectedPair: RelationshipAnalysisItem | null;
  selectedPhase: string | null;
  selectedActorId: string | null;
  selectedRelationshipId: string | null;
  outcomeEvidence: ActorEvidenceItem[];
  actorNames: Record<string, string>;
  selectedTurn: number | null;
  onSelectActor: (actorId: string) => void;
  onSelectRelationship: (relationshipId: string, sourceActorId: string, targetActorId: string) => void;
  onSelectTurn: (turnIndex: number) => void;
}

const STATUS_STYLE = {
  hit: { icon: CheckCircle2, label: 'Hit', tone: 'text-accent-green', bg: 'bg-emerald-500/10 border-emerald-500/20' },
  partial: { icon: TriangleAlert, label: 'Partial', tone: 'text-accent-amber', bg: 'bg-amber-500/10 border-amber-500/20' },
  miss: { icon: XCircle, label: 'Miss', tone: 'text-accent-red', bg: 'bg-red-500/10 border-red-500/20' },
  emergent: { icon: Compass, label: 'Emergent', tone: 'text-accent-blue', bg: 'bg-blue-500/10 border-blue-500/20' },
} as const;

function formatTarget(targetOutcome: Record<string, unknown> | null | undefined) {
  if (!targetOutcome || Object.keys(targetOutcome).length === 0) return 'No explicit target outcome was recorded.';
  return Object.entries(targetOutcome)
    .map(([key, value]) => `${key.replace(/_/g, ' ')}: ${String(value)}`)
    .join(' | ');
}

export function OutcomeAnalysisPanel({
  mode,
  outcomeAnalysis,
  actors,
  beforeRelationships,
  afterRelationships,
  selectedPair,
  selectedPhase,
  selectedActorId,
  selectedRelationshipId,
  outcomeEvidence,
  actorNames,
  selectedTurn,
  onSelectActor,
  onSelectRelationship,
  onSelectTurn,
}: OutcomeAnalysisPanelProps) {
  const statusKey = outcomeAnalysis?.outcome_status || (mode === 'guided' ? 'partial' : 'emergent');
  const status = STATUS_STYLE[statusKey];
  const StatusIcon = status.icon;
  const evidenceMap = new Map((outcomeEvidence || []).map((item) => [item.evidence_id, item]));

  return (
    <div className="space-y-4">
      <GlassCard className="p-5">
        <div className="grid grid-cols-1 xl:grid-cols-[1.15fr_0.85fr] gap-4">
          <div>
            <div className="flex items-center gap-3">
              <div className={`rounded-xl border px-3 py-2 ${status.bg}`}>
                <StatusIcon size={18} className={status.tone} />
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-text-muted">
                  {mode === 'guided' ? 'Outcome Analysis' : 'Emergent Outcome'}
                </div>
                <div className="text-lg font-semibold text-text-primary">
                  {mode === 'guided' ? `Guided result: ${status.label}` : 'Exploratory result'}
                </div>
              </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-4">
              {mode === 'guided' && (
                <div className="rounded-2xl border border-border-subtle bg-bg-elevated/60 p-4">
                  <div className="text-xs uppercase tracking-wider text-text-muted flex items-center gap-1">
                    <Target size={12} />
                    Target Outcome
                  </div>
                  <div className="text-sm text-text-primary mt-2">{formatTarget(outcomeAnalysis?.target_outcome)}</div>
                </div>
              )}
              <div className="rounded-2xl border border-border-subtle bg-bg-elevated/60 p-4">
                <div className="text-xs uppercase tracking-wider text-text-muted">
                  {mode === 'guided' ? 'Actual Outcome' : 'What Emerged'}
                </div>
                <div className="text-sm text-text-primary mt-2">{outcomeAnalysis?.actual_outcome || 'No outcome summary available.'}</div>
              </div>
            </div>
          </div>

          <div className="space-y-3">
            <div className="rounded-2xl border border-border-subtle bg-bg-elevated/60 p-4">
              <div className="text-xs uppercase tracking-wider text-text-muted">
                {mode === 'guided' ? 'Difference From Target' : 'Why It Emerged'}
              </div>
              <div className="text-sm text-text-secondary mt-2">
                {outcomeAnalysis?.difference_summary || 'No comparison summary available.'}
              </div>
            </div>
            <div className="rounded-2xl border border-border-subtle bg-bg-elevated/60 p-4">
              <div className="text-xs uppercase tracking-wider text-text-muted">How The Result Was Derived</div>
              <div className="text-sm text-text-secondary mt-2">
                {outcomeAnalysis?.derivation_summary || 'No derivation summary available.'}
              </div>
            </div>
          </div>
        </div>
      </GlassCard>

      {outcomeAnalysis?.stage_summaries && outcomeAnalysis.stage_summaries.length > 0 && (
        <GlassCard className="p-5">
          <div className="mb-4">
            <h3 className="text-sm font-semibold text-text-primary">Early / Middle / Late Trace</h3>
            <p className="text-xs text-text-muted mt-1">
              How the run moved from opening positions to final outcome, and what intentions, incentives, and penalties triggered each shift.
            </p>
          </div>
          <div className="grid grid-cols-1 xl:grid-cols-3 gap-4">
            {outcomeAnalysis.stage_summaries.map((stage) => {
              const stageEvidence = stage.trigger_evidence_ids
                .map((id) => evidenceMap.get(id))
                .filter(Boolean) as ActorEvidenceItem[];
              return (
                <div key={stage.stage_id} className="rounded-2xl border border-border-subtle bg-bg-elevated/60 p-4">
                  <div className="text-xs uppercase tracking-wider text-text-muted">{stage.label}</div>
                  <div className="text-sm font-semibold text-text-primary mt-1">{stage.phase_names.join(' / ')}</div>
                  <div className="text-sm text-text-secondary mt-3">{stage.conclusion}</div>
                  <div className="space-y-2 mt-4">
                    {stageEvidence.map((item) => (
                      <div key={item.evidence_id} className="rounded-xl border border-border-subtle bg-bg-primary/70 px-3 py-3">
                        <div className="text-xs text-text-muted">
                          Turn {item.turn_index}{item.phase_name ? ` · ${item.phase_name}` : ''}
                        </div>
                        <div className="text-sm text-text-primary mt-1">{item.summary}</div>
                        {item.intention && <div className="text-xs text-text-secondary mt-2"><span className="font-medium text-text-primary">Intention:</span> {item.intention}</div>}
                        {item.incentive && <div className="text-xs text-text-secondary mt-1"><span className="font-medium text-text-primary">Incentive:</span> {item.incentive}</div>}
                        {item.penalty && <div className="text-xs text-text-secondary mt-1"><span className="font-medium text-text-primary">Penalty:</span> {item.penalty}</div>}
                      </div>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        </GlassCard>
      )}

      <RelationshipNetworkCompare
        actors={actors}
        beforeRelationships={beforeRelationships}
        afterRelationships={afterRelationships}
        selectedPair={selectedPair}
        selectedPhase={selectedPhase}
        selectedActorId={selectedActorId}
        selectedRelationshipId={selectedRelationshipId}
        onSelectActor={onSelectActor}
        onSelectRelationship={onSelectRelationship}
      />

      <OutcomeDriverTimeline
        drivers={outcomeAnalysis?.driver_summaries || []}
        evidenceItems={outcomeEvidence}
        actorNames={actorNames}
        selectedTurn={selectedTurn}
        onSelectTurn={onSelectTurn}
      />
    </div>
  );
}
