import { Zap, MessageCircle, BarChart3, RefreshCw, Handshake, Pin, ArrowRight } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import type { KeyMoment } from '../../types/simulation';
import { useSelectionStore } from '../../stores/selectionStore';

interface KeyMomentsPanelProps {
  moments: KeyMoment[];
  actorNames?: Record<string, string>;
}

const EVENT_ICONS: Record<string, React.ReactNode> = {
  relationship_shift: <MessageCircle size={14} />,
  action: <Zap size={14} />,
  drift_spike: <BarChart3 size={14} />,
  phase_change: <RefreshCw size={14} />,
  commitment: <Handshake size={14} />,
};

export function KeyMomentsPanel({ moments }: KeyMomentsPanelProps) {
  const setTurn = useSelectionStore((s) => s.setTurn);

  if (moments.length === 0) return null;

  return (
    <GlassCard className="p-5">
      <h3 className="text-sm font-semibold text-text-primary mb-4 flex items-center gap-2">
        <Zap size={16} className="text-accent-amber" />
        {moments.length} Key Moments That Shaped The Outcome
      </h3>
      <div className="space-y-3">
        {moments.map((moment, i) => (
          <div
            key={i}
            className="group pl-4 border-l-2 border-border-subtle hover:border-accent-blue transition-colors"
          >
            <div className="flex items-start gap-2">
              <span className="shrink-0 mt-0.5 text-text-muted">
                {EVENT_ICONS[moment.event_type] || <Pin size={14} />}
              </span>
              <div className="min-w-0 flex-1">
                <div className="flex items-baseline gap-2 flex-wrap">
                  <span className="text-xs font-mono text-text-muted">
                    Turn {moment.turn_index}
                  </span>
                  <span className="text-xs px-1.5 py-0.5 rounded bg-bg-elevated text-text-muted">
                    {moment.phase_name}
                  </span>
                </div>
                <div className="text-sm text-text-primary mt-1 font-medium">
                  {moment.title}
                </div>
                {moment.evidence && (
                  <div className="text-xs text-text-secondary mt-1 line-clamp-2 italic">
                    "{moment.evidence.slice(0, 150)}{moment.evidence.length > 150 ? '...' : ''}"
                  </div>
                )}
                <button
                  onClick={() => setTurn(moment.turn_index)}
                  className="text-xs text-accent-blue hover:text-blue-600 mt-1 cursor-pointer inline-flex items-center gap-1"
                >
                  Jump to transcript <ArrowRight size={12} />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </GlassCard>
  );
}
