import { GlassCard } from '../ui/GlassCard';
import { ActorSelectorList } from './ActorSelectorList';
import { ActorBeforeAfterPanel } from './ActorBeforeAfterPanel';
import { ActorOceanRadar } from './ActorOceanRadar';
import { ActorEvidenceFilter } from './ActorEvidenceFilter';
import { ActorEvidenceList } from './ActorEvidenceList';
import type { ActorAnalysisItem } from '../../types/simulation';

interface ActorAnalysisPanelProps {
  actors: ActorAnalysisItem[];
  selectedActorId: string | null;
  selectedPhase: string | null;
  selectedEvidenceType: 'relationship' | 'actor_drift' | 'action';
  actorNames: Record<string, string>;
  selectedTurn: number | null;
  onSelectActor: (actorId: string) => void;
  onSelectEvidenceType: (type: 'relationship' | 'actor_drift' | 'action') => void;
  onSelectTurn: (turnIndex: number) => void;
}

export function ActorAnalysisPanel({
  actors,
  selectedActorId,
  selectedPhase,
  selectedEvidenceType,
  actorNames,
  selectedTurn,
  onSelectActor,
  onSelectEvidenceType,
  onSelectTurn,
}: ActorAnalysisPanelProps) {
  const selectedActor = actors.find((actor) => actor.actor_id === selectedActorId) || actors[0] || null;

  return (
    <div className="space-y-4">
      {selectedActor ? (
        <ActorSelectorList
          actors={actors}
          selectedActorId={selectedActor.actor_id}
          onSelectActor={onSelectActor}
          renderExpanded={(actor) => {
            const filteredEvidence = actor.evidence_by_type[selectedEvidenceType].filter(
              (item) => !selectedPhase || item.phase_name === selectedPhase,
            );

            return (
              <div className="space-y-4">
                <ActorBeforeAfterPanel actor={actor} />
                <ActorOceanRadar actor={actor} />
                <GlassCard className="p-5">
                  <div className="flex items-start justify-between gap-3 flex-wrap">
                    <div>
                      <h3 className="text-sm font-semibold text-text-primary">Filter Change Evidence</h3>
                      <p className="text-xs text-text-muted mt-1">
                        Relationship, persona drift, and action evidence for the selected actor.
                      </p>
                    </div>
                    <ActorEvidenceFilter selected={selectedEvidenceType} onSelect={onSelectEvidenceType} />
                  </div>
                </GlassCard>
                <ActorEvidenceList
                  evidenceItems={filteredEvidence}
                  actorNames={actorNames}
                  selectedTurn={selectedTurn}
                  onSelectTurn={onSelectTurn}
                />
                <GlassCard className="p-5">
                  <div className="text-sm font-semibold text-text-primary">Why This Actor Changed</div>
                  <div className="text-sm text-text-secondary mt-3">{actor.change_narrative}</div>
                </GlassCard>
              </div>
            );
          }}
        />
      ) : (
        <GlassCard className="p-5">
          <div className="text-sm text-text-muted">No actor analysis data is available for this run.</div>
        </GlassCard>
      )}
    </div>
  );
}
