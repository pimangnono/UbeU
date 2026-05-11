import { useMemo, useState, type ReactNode } from 'react';
import { ArrowRight, BarChart3, MessageCircle, SlidersHorizontal, Zap } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import { Button } from '../ui/Button';
import type { ChangeCategory, ChangeEventSummary } from '../../types/simulation';

interface ChangeCardRailProps {
  changeEvents: ChangeEventSummary[];
  actorNames: Record<string, string>;
  selectedChangeId: string | null;
  selectedActorId?: string | null;
  selectedPhase?: string | null;
  onSelectChange: (changeId: string) => void;
}

const CATEGORY_LABELS: Record<ChangeCategory, string> = {
  relationship: 'Relationship',
  world_state: 'World State',
  actor_drift: 'Actor Drift',
  action: 'Action',
};

const CATEGORY_ICONS: Record<ChangeCategory, ReactNode> = {
  relationship: <MessageCircle size={14} className="text-accent-blue" />,
  world_state: <SlidersHorizontal size={14} className="text-accent-green" />,
  actor_drift: <BarChart3 size={14} className="text-accent-amber" />,
  action: <Zap size={14} className="text-accent-red" />,
};

export function ChangeCardRail({
  changeEvents,
  actorNames,
  selectedChangeId,
  selectedActorId,
  selectedPhase,
  onSelectChange,
}: ChangeCardRailProps) {
  const [categoryFilter, setCategoryFilter] = useState<'all' | ChangeCategory>('all');

  const filteredChanges = useMemo(() => {
    return changeEvents.filter((change) => {
      if (categoryFilter !== 'all' && change.category !== categoryFilter) return false;
      if (selectedActorId && !change.affected_actor_ids.includes(selectedActorId)) return false;
      if (selectedPhase && change.phase_name && change.phase_name !== selectedPhase) return false;
      return true;
    });
  }, [changeEvents, categoryFilter, selectedActorId, selectedPhase]);

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between gap-3 flex-wrap">
        <div>
          <div className="text-sm font-semibold text-text-primary">Change Explorer</div>
          <div className="text-xs text-text-muted">Ranked by magnitude. Click a change to synchronize the rest of the page.</div>
        </div>
        <div className="flex items-center gap-2 flex-wrap">
          <Button size="sm" variant={categoryFilter === 'all' ? 'primary' : 'secondary'} onClick={() => setCategoryFilter('all')}>
            All
          </Button>
          {(['relationship', 'world_state', 'actor_drift', 'action'] as ChangeCategory[]).map((category) => (
            <Button
              key={category}
              size="sm"
              variant={categoryFilter === category ? 'primary' : 'secondary'}
              onClick={() => setCategoryFilter(category)}
            >
              {CATEGORY_LABELS[category]}
            </Button>
          ))}
        </div>
      </div>

      <div className="space-y-2 max-h-[34rem] overflow-y-auto pr-1">
        {filteredChanges.map((change, index) => {
          const selected = change.change_id === selectedChangeId;
          return (
            <GlassCard
              key={change.change_id}
              hover
              className={`p-4 cursor-pointer ${selected ? 'ring-2 ring-accent-blue/40 bg-blue-50/50' : ''}`}
              onClick={() => onSelectChange(change.change_id)}
            >
              <div className="flex items-start justify-between gap-3">
                <div className="min-w-0 flex-1">
                  <div className="flex items-center gap-2 text-xs text-text-muted mb-2">
                    <span className="font-mono">#{index + 1}</span>
                    {CATEGORY_ICONS[change.category]}
                    <span>{CATEGORY_LABELS[change.category]}</span>
                    {change.phase_name && (
                      <span className="px-1.5 py-0.5 rounded-full bg-bg-elevated text-text-muted">
                        {change.phase_name}
                      </span>
                    )}
                  </div>
                  <div className="text-sm font-semibold text-text-primary">{change.label}</div>
                  <div className="text-xs text-text-secondary mt-1">{change.summary}</div>
                  <div className="text-xs text-text-muted mt-2">
                    Actors: {change.affected_actor_ids.map((actorId) => actorNames[actorId] || actorId).join(', ') || 'system'}
                  </div>
                  <div className="text-xs text-accent-blue mt-1 inline-flex items-center gap-1">
                    {change.trigger_summary}
                    <ArrowRight size={11} />
                  </div>
                </div>
                <div className="text-right shrink-0">
                  <div className="text-[11px] uppercase tracking-wider text-text-muted">Magnitude</div>
                  <div className="text-lg font-bold text-text-primary">{change.magnitude.toFixed(2)}</div>
                </div>
              </div>
            </GlassCard>
          );
        })}

        {filteredChanges.length === 0 && (
          <GlassCard className="p-4">
            <div className="text-sm text-text-muted">No changes match the current actor or phase filter.</div>
          </GlassCard>
        )}
      </div>
    </div>
  );
}
