import { ArrowRight } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import type { ActorEvidenceItem } from '../../types/simulation';

interface ActorEvidenceListProps {
  evidenceItems: ActorEvidenceItem[];
  actorNames: Record<string, string>;
  selectedTurn: number | null;
  onSelectTurn: (turnIndex: number) => void;
}

export function ActorEvidenceList({
  evidenceItems,
  actorNames,
  selectedTurn,
  onSelectTurn,
}: ActorEvidenceListProps) {
  const metaEntries = (item: ActorEvidenceItem) => ([
    item.situation ? ['Situation', item.situation] : null,
    item.intention ? ['Intention', item.intention] : null,
    item.incentive ? ['Incentive', item.incentive] : null,
    item.penalty ? ['Penalty', item.penalty] : null,
    item.action ? ['Action', item.action] : null,
    item.decision_shift ? ['Decision Shift', item.decision_shift] : null,
  ].filter(Boolean) as Array<[string, string]>);

  return (
    <GlassCard className="p-5">
      <div className="text-sm font-semibold text-text-primary mb-3">Filtered Change Evidence</div>
      <div className="space-y-3">
        {evidenceItems.length > 0 ? evidenceItems.map((item) => {
          const highlighted = selectedTurn === item.turn_index;
          return (
            <div
              key={item.evidence_id}
              className={`rounded-2xl border p-4 ${highlighted ? 'border-accent-blue/40 bg-blue-50/40' : 'border-border-subtle bg-bg-elevated/60'}`}
            >
              <div className="flex items-center gap-2 text-xs text-text-muted flex-wrap">
                <span className="font-mono">Turn {item.turn_index || '—'}</span>
                {item.phase_name && <span>{item.phase_name}</span>}
                <span>{actorNames[item.actor_id] || item.actor_id}</span>
                {item.other_actor_id && <span>with {actorNames[item.other_actor_id] || item.other_actor_id}</span>}
              </div>
              <div className="text-sm font-semibold text-text-primary mt-2">{item.summary}</div>
              <div className="text-sm text-text-secondary mt-2">{item.why_it_matters}</div>
              {metaEntries(item).length > 0 && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-2 mt-3">
                  {metaEntries(item).map(([label, value]) => (
                    <div key={`${item.evidence_id}-${label}`} className="rounded-xl border border-border-subtle bg-bg-primary/70 px-3 py-2">
                      <div className="text-[11px] uppercase tracking-wider text-text-muted">{label}</div>
                      <div className="text-xs text-text-secondary mt-1">{value}</div>
                    </div>
                  ))}
                </div>
              )}
              {item.quote && (
                <div className="rounded-xl bg-bg-primary/70 border border-border-subtle px-3 py-2 text-sm text-text-secondary italic mt-3">
                  "{item.quote}"
                </div>
              )}
              {item.turn_index > 0 && (
                <button
                  onClick={() => onSelectTurn(item.turn_index)}
                  className="text-xs text-accent-blue hover:text-blue-600 mt-3 inline-flex items-center gap-1"
                >
                  Jump to transcript <ArrowRight size={11} />
                </button>
              )}
            </div>
          );
        }) : (
          <div className="text-sm text-text-muted">
            No evidence of this type was recorded for the selected actor in the current phase filter.
          </div>
        )}
      </div>
    </GlassCard>
  );
}
