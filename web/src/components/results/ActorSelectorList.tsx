import { ChevronDown, ChevronUp } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import type { ActorAnalysisItem } from '../../types/simulation';

interface ActorSelectorListProps {
  actors: ActorAnalysisItem[];
  selectedActorId: string | null;
  onSelectActor: (actorId: string) => void;
  renderExpanded?: (actor: ActorAnalysisItem) => React.ReactNode;
}

export function ActorSelectorList({
  actors,
  selectedActorId,
  onSelectActor,
  renderExpanded,
}: ActorSelectorListProps) {
  return (
    <GlassCard className="p-4">
      <div className="text-sm font-semibold text-text-primary mb-3">Actors</div>
      <div className="space-y-3">
        {actors.map((actor) => {
          const selected = actor.actor_id === selectedActorId;
          return (
            <div
              key={actor.actor_id}
              className={`rounded-2xl border transition-colors ${
                selected
                  ? 'border-accent-blue/40 bg-blue-50/50'
                  : 'border-border-subtle bg-bg-elevated/60 hover:border-accent-blue/20 hover:bg-blue-50/20'
              }`}
            >
              <button
                onClick={() => onSelectActor(actor.actor_id)}
                className="w-full text-left px-4 py-4"
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="min-w-0 flex-1">
                    <div className="text-sm font-semibold text-text-primary">{actor.before_summary.role}</div>
                    <div className="text-sm text-text-muted mt-2 leading-relaxed break-words">
                      {actor.before_summary.stance}
                    </div>
                    <div className="text-sm text-text-secondary mt-2 leading-relaxed break-words">
                      {actor.after_summary.end_state}
                    </div>
                  </div>
                  <div className="shrink-0 flex items-start gap-4">
                    <div className="text-right">
                      <div className="text-[11px] uppercase tracking-wider text-text-muted">Drift</div>
                      <div className="text-sm font-mono text-text-primary mt-1">{actor.final_drift_score.toFixed(2)}</div>
                    </div>
                    <div className="text-text-muted mt-0.5">
                      {selected ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
                    </div>
                  </div>
                </div>
              </button>

              {selected && renderExpanded && (
                <div className="px-4 pb-4 pt-1 border-t border-accent-blue/10">
                  {renderExpanded(actor)}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </GlassCard>
  );
}
