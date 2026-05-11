import { ArrowRight, MessageCircle, RefreshCw, Zap } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import type { ChangeEventSummary, ChangeTrigger } from '../../types/simulation';

interface TriggerTracePanelProps {
  change: ChangeEventSummary | null;
  triggers: ChangeTrigger[];
  actorNames: Record<string, string>;
  selectedTurn: number | null;
  onSelectTurn: (turnIndex: number) => void;
}

const KIND_ICONS = {
  relationship: <MessageCircle size={14} className="text-accent-blue" />,
  action: <Zap size={14} className="text-accent-amber" />,
  turn: <ArrowRight size={14} className="text-accent-green" />,
  phase: <RefreshCw size={14} className="text-accent-red" />,
} as const;

function renderValue(value: unknown): string {
  if (typeof value === 'number') return value.toFixed(2);
  if (value && typeof value === 'object') {
    return Object.entries(value as Record<string, unknown>)
      .map(([key, item]) => `${key}: ${typeof item === 'number' ? item.toFixed(2) : String(item)}`)
      .join(' | ');
  }
  if (value === null || value === undefined) return '—';
  return String(value);
}

export function TriggerTracePanel({
  change,
  triggers,
  actorNames,
  selectedTurn,
  onSelectTurn,
}: TriggerTracePanelProps) {
  return (
    <GlassCard className="p-5 h-full">
      <div className="flex items-center justify-between gap-3 mb-4">
        <div>
          <h3 className="text-sm font-semibold text-text-primary">Trigger Trace</h3>
          <p className="text-xs text-text-muted mt-1">
            Why this change happened, in chronological evidence.
          </p>
        </div>
      </div>

      {!change ? (
        <div className="text-sm text-text-muted">Select a change to inspect its trigger trail.</div>
      ) : (
        <div className="space-y-4">
          <div className="rounded-xl bg-bg-elevated/70 border border-border-subtle p-3">
            <div className="text-xs uppercase tracking-wider text-text-muted mb-1">Selected change</div>
            <div className="text-sm font-semibold text-text-primary">{change.label}</div>
            <div className="text-xs text-text-secondary mt-1">{change.summary}</div>
            <div className="grid grid-cols-1 gap-2 mt-3 text-xs">
              <div className="rounded-lg bg-bg-primary/70 border border-border-subtle px-3 py-2">
                <span className="uppercase tracking-wider text-text-muted">What changed</span>
                <div className="text-text-secondary mt-1">
                  {renderValue(change.initial_value)} → {renderValue(change.final_value)}
                </div>
              </div>
              {change.meaning && (
                <div className="rounded-lg bg-blue-50/60 border border-blue-100 px-3 py-2 text-text-secondary">
                  <span className="uppercase tracking-wider text-text-muted">How to read this</span>
                  <div className="mt-1">{change.meaning}</div>
                </div>
              )}
            </div>
          </div>

          <div className="space-y-3">
            {triggers.map((trigger) => {
              const highlighted = selectedTurn === trigger.turn_index;
              return (
                <div
                  key={trigger.trigger_id}
                  className={`pl-4 border-l-2 transition-colors ${highlighted ? 'border-accent-blue' : 'border-border-subtle'}`}
                >
                  <div className="flex items-start gap-2">
                    <div className="mt-0.5 shrink-0">
                      {KIND_ICONS[trigger.kind] || <ArrowRight size={14} className="text-text-muted" />}
                    </div>
                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-2 text-xs text-text-muted flex-wrap">
                        <span className="font-mono">Turn {trigger.turn_index || '—'}</span>
                        {trigger.phase_name && <span>{trigger.phase_name}</span>}
                        {trigger.actor_id && <span>{actorNames[trigger.actor_id] || trigger.actor_id}</span>}
                        <span className="ml-auto font-mono text-text-secondary">weight {trigger.weight.toFixed(2)}</span>
                      </div>
                      <div className="text-sm text-text-primary mt-1">{trigger.summary}</div>
                      {trigger.evidence && (
                        <div className="text-xs text-text-secondary italic mt-1 line-clamp-3">
                          "{trigger.evidence}"
                        </div>
                      )}
                      {trigger.turn_index > 0 && (
                        <button
                          onClick={() => onSelectTurn(trigger.turn_index)}
                          className="text-xs text-accent-blue hover:text-blue-600 mt-2 inline-flex items-center gap-1"
                        >
                          Jump to transcript <ArrowRight size={11} />
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
            {triggers.length === 0 && (
              <div className="text-sm text-text-muted">No strong trigger attribution was generated for this change.</div>
            )}
          </div>
        </div>
      )}
    </GlassCard>
  );
}
