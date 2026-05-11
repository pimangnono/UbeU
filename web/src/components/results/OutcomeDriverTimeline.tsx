import { ArrowRight, MessageCircle, Sparkles, Zap } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import type { ActorEvidenceItem, OutcomeDriverSummary } from '../../types/simulation';

interface OutcomeDriverTimelineProps {
  drivers: OutcomeDriverSummary[];
  evidenceItems: ActorEvidenceItem[];
  actorNames: Record<string, string>;
  selectedTurn: number | null;
  onSelectTurn: (turnIndex: number) => void;
}

const KIND_ICON = {
  relationship: <MessageCircle size={14} className="text-accent-blue" />,
  actor_drift: <Sparkles size={14} className="text-accent-amber" />,
  action: <Zap size={14} className="text-accent-green" />,
} as const;

function evidenceMeta(item: ActorEvidenceItem) {
  return [
    item.intention ? ['Intention', item.intention] : null,
    item.incentive ? ['Incentive', item.incentive] : null,
    item.penalty ? ['Penalty', item.penalty] : null,
    item.action ? ['Action', item.action] : null,
  ].filter(Boolean) as Array<[string, string]>;
}

export function OutcomeDriverTimeline({
  drivers,
  evidenceItems,
  actorNames,
  selectedTurn,
  onSelectTurn,
}: OutcomeDriverTimelineProps) {
  return (
    <GlassCard className="p-5">
      <div className="mb-4">
        <h3 className="text-sm font-semibold text-text-primary">Outcome Driver Timeline</h3>
        <p className="text-xs text-text-muted mt-1">
          Which actor, situation, and dialogue pushed the result toward its final outcome.
        </p>
      </div>

      <div className="space-y-4">
        {drivers.map((driver) => {
          const relatedEvidence = evidenceItems.filter((item) => driver.evidence_ids.includes(item.evidence_id));
          return (
            <div key={driver.driver_id} className="rounded-2xl border border-border-subtle bg-bg-elevated/60 p-4">
              <div className="text-xs uppercase tracking-wider text-text-muted">Outcome driver</div>
              <div className="text-sm font-semibold text-text-primary mt-1">{driver.title}</div>
              <div className="text-sm text-text-secondary mt-2">{driver.summary}</div>
              <div className="rounded-xl bg-blue-50/60 border border-blue-100 px-3 py-2 text-sm text-text-secondary mt-3">
                {driver.why_it_matters}
              </div>
              <div className="space-y-3 mt-4">
                {relatedEvidence.length > 0 ? relatedEvidence.map((evidence) => {
                  const highlighted = selectedTurn === evidence.turn_index;
                  return (
                    <div key={evidence.evidence_id} className={`pl-4 border-l-2 ${highlighted ? 'border-accent-blue' : 'border-border-subtle'}`}>
                      <div className="flex items-start gap-2">
                        <div className="mt-0.5">{KIND_ICON[evidence.type]}</div>
                        <div className="min-w-0 flex-1">
                          <div className="flex items-center gap-2 text-xs text-text-muted flex-wrap">
                            <span className="font-mono">Turn {evidence.turn_index || '—'}</span>
                            {evidence.phase_name && <span>{evidence.phase_name}</span>}
                            <span>{actorNames[evidence.actor_id] || evidence.actor_id}</span>
                            {evidence.other_actor_id && <span>with {actorNames[evidence.other_actor_id] || evidence.other_actor_id}</span>}
                          </div>
                          <div className="text-sm text-text-primary mt-1">{evidence.summary}</div>
                          <div className="text-xs text-text-secondary mt-1">{evidence.why_it_matters}</div>
                          {evidenceMeta(evidence).length > 0 && (
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-2 mt-2">
                              {evidenceMeta(evidence).map(([label, value]) => (
                                <div key={`${evidence.evidence_id}-${label}`} className="rounded-lg border border-border-subtle bg-bg-primary/70 px-3 py-2">
                                  <div className="text-[11px] uppercase tracking-wider text-text-muted">{label}</div>
                                  <div className="text-xs text-text-secondary mt-1">{value}</div>
                                </div>
                              ))}
                            </div>
                          )}
                          {evidence.quote && (
                            <div className="text-xs text-text-secondary italic mt-1 line-clamp-3">"{evidence.quote}"</div>
                          )}
                          {evidence.turn_index > 0 && (
                            <button
                              onClick={() => onSelectTurn(evidence.turn_index)}
                              className="text-xs text-accent-blue hover:text-blue-600 mt-2 inline-flex items-center gap-1"
                            >
                              Jump to transcript <ArrowRight size={11} />
                            </button>
                          )}
                        </div>
                      </div>
                    </div>
                  );
                }) : (
                  <div className="text-sm text-text-muted">No linked evidence was generated for this outcome driver.</div>
                )}
              </div>
            </div>
          );
        })}

        {drivers.length === 0 && (
          <div className="text-sm text-text-muted">No explicit outcome drivers were generated for this run.</div>
        )}
      </div>
    </GlassCard>
  );
}
