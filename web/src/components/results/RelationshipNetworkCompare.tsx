import { GlassCard } from '../ui/GlassCard';
import { BeforeAfterNetworkPanel } from './BeforeAfterNetworkPanel';
import type {
  ActorEvidenceItem,
  FinalRelationshipSummary,
  InitialRelationshipSummary,
  RelationshipAnalysisItem,
  StakeholderActor,
} from '../../types/simulation';

interface RelationshipNetworkCompareProps {
  actors: StakeholderActor[];
  beforeRelationships: InitialRelationshipSummary[];
  afterRelationships: FinalRelationshipSummary[];
  selectedPair: RelationshipAnalysisItem | null;
  selectedPhase: string | null;
  selectedActorId: string | null;
  selectedRelationshipId: string | null;
  onSelectActor: (actorId: string) => void;
  onSelectRelationship: (relationshipId: string, sourceActorId: string, targetActorId: string) => void;
}

function changeSummary(pair: RelationshipAnalysisItem | null) {
  if (!pair) return 'No relationship shift is selected.';
  const trust = pair.delta.trust;
  const tension = pair.delta.tension;
  return `Trust moved ${trust >= 0 ? '+' : ''}${trust.toFixed(2)} and tension moved ${tension >= 0 ? '+' : ''}${tension.toFixed(2)}.`;
}

export function RelationshipNetworkCompare({
  actors,
  beforeRelationships,
  afterRelationships,
  selectedPair,
  selectedPhase,
  selectedActorId,
  selectedRelationshipId,
  onSelectActor,
  onSelectRelationship,
}: RelationshipNetworkCompareProps) {
  const topEvidence = selectedPair?.top_trigger_summaries?.[0] as ActorEvidenceItem | undefined;
  const highlightedActorIds = selectedActorId
    ? [selectedActorId]
    : selectedPair
      ? [selectedPair.source_actor_id, selectedPair.target_actor_id]
      : [];

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-1 2xl:grid-cols-2 gap-4">
        <BeforeAfterNetworkPanel
          title="Before"
          actors={actors}
          relationships={beforeRelationships}
          highlightedActorIds={highlightedActorIds}
          highlightedRelationshipId={selectedRelationshipId}
          phaseLabel={selectedPhase ? `Reference state before ${selectedPhase}` : 'Reference state at simulation start'}
          onSelectActor={onSelectActor}
          onSelectRelationship={onSelectRelationship}
        />
        <BeforeAfterNetworkPanel
          title="After"
          actors={actors}
          relationships={afterRelationships}
          highlightedActorIds={highlightedActorIds}
          highlightedRelationshipId={selectedRelationshipId}
          phaseLabel={selectedPhase ? `Cumulative state through ${selectedPhase}` : 'Cumulative state at simulation end'}
          onSelectActor={onSelectActor}
          onSelectRelationship={onSelectRelationship}
        />
      </div>

      <GlassCard className="p-5">
        <div className="grid grid-cols-1 xl:grid-cols-[1.1fr_0.9fr] gap-4">
          <div>
            <div className="text-xs uppercase tracking-wider text-text-muted mb-1">What changed in the network</div>
            <h3 className="text-base font-semibold text-text-primary">
              {selectedPair?.display_label || 'Relationship network remained mostly stable'}
            </h3>
            <p className="text-sm text-text-secondary mt-2">{changeSummary(selectedPair)}</p>
            {selectedPair && (
              <div className="rounded-xl bg-blue-50/60 border border-blue-100 px-4 py-3 text-sm text-text-secondary mt-4">
                {selectedPair.event_count > 0
                  ? `This tie changed through ${selectedPair.event_count} recorded relationship event${selectedPair.event_count > 1 ? 's' : ''}.`
                  : 'No direct relationship event was recorded for this tie in the selected phase window.'}
              </div>
            )}
          </div>
          <div className="space-y-3">
            <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 px-4 py-3">
              <div className="text-xs uppercase tracking-wider text-text-muted">Who caused it</div>
              <div className="text-sm text-text-primary mt-1">
                {topEvidence ? topEvidence.summary : 'No strong trigger was identified for the selected relationship.'}
              </div>
            </div>
            <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 px-4 py-3">
              <div className="text-xs uppercase tracking-wider text-text-muted">In which phase</div>
              <div className="text-sm text-text-primary mt-1">
                {selectedPhase || topEvidence?.phase_name || 'Across the full run'}
              </div>
            </div>
            <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 px-4 py-3">
              <div className="text-xs uppercase tracking-wider text-text-muted">Triggering dialogue</div>
              <div className="text-sm text-text-secondary mt-1">
                {topEvidence?.quote ? `"${topEvidence.quote}"` : 'No direct quote was stored for this change.'}
              </div>
            </div>
          </div>
        </div>
      </GlassCard>
    </div>
  );
}
