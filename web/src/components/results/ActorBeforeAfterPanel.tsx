import { GlassCard } from '../ui/GlassCard';
import type { ActorAnalysisItem } from '../../types/simulation';

interface ActorBeforeAfterPanelProps {
  actor: ActorAnalysisItem;
}

export function ActorBeforeAfterPanel({ actor }: ActorBeforeAfterPanelProps) {
  const relationshipChange = actor.after_summary.strongest_relationship_change;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      <GlassCard className="p-5">
        <div className="text-xs uppercase tracking-wider text-text-muted mb-1">Before</div>
        <h3 className="text-base font-semibold text-text-primary">{actor.before_summary.role}</h3>
        <div className="text-sm text-text-secondary mt-3">{actor.before_summary.stance}</div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-4 text-sm">
          <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-3">
            <div className="text-xs uppercase tracking-wider text-text-muted">Disposition</div>
            <div className="text-text-primary mt-1 capitalize">{actor.before_summary.disposition}</div>
          </div>
          <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-3">
            <div className="text-xs uppercase tracking-wider text-text-muted">Primary Incentive</div>
            <div className="text-text-primary mt-1">{actor.before_summary.incentives[0] || 'Not specified'}</div>
          </div>
          <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-3 md:col-span-2">
            <div className="text-xs uppercase tracking-wider text-text-muted">Primary Concern</div>
            <div className="text-text-primary mt-1">{actor.before_summary.concerns[0] || 'Not specified'}</div>
          </div>
        </div>
      </GlassCard>

      <GlassCard className="p-5">
        <div className="text-xs uppercase tracking-wider text-text-muted mb-1">After</div>
        <h3 className="text-base font-semibold text-text-primary">{actor.display_name}</h3>
        <div className="text-sm text-text-secondary mt-3">{actor.after_summary.comparison_text}</div>
        <div className="grid grid-cols-1 gap-3 mt-4 text-sm">
          <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-3">
            <div className="text-xs uppercase tracking-wider text-text-muted">End State</div>
            <div className="text-text-primary mt-1">{actor.after_summary.end_state}</div>
          </div>
          <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-3">
            <div className="text-xs uppercase tracking-wider text-text-muted">Strongest Relationship Change</div>
            <div className="text-text-primary mt-1">
              {relationshipChange
                ? `${relationshipChange.counterpart_label}: trust ${relationshipChange.trust_delta >= 0 ? '+' : ''}${relationshipChange.trust_delta.toFixed(2)}, tension ${relationshipChange.tension_delta >= 0 ? '+' : ''}${relationshipChange.tension_delta.toFixed(2)}.`
                : 'No meaningful relationship change was recorded.'}
            </div>
          </div>
          <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-3">
            <div className="text-xs uppercase tracking-wider text-text-muted">Final Drift Interpretation</div>
            <div className="text-text-primary mt-1">{actor.after_summary.drift_interpretation}</div>
          </div>
        </div>
      </GlassCard>
    </div>
  );
}
