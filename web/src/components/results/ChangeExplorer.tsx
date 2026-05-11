import { useEffect, useMemo, useState } from 'react';
import { Activity, ArrowRightLeft, Sparkles } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import { Button } from '../ui/Button';
import { ChangeCardRail } from './ChangeCardRail';
import { TriggerTracePanel } from './TriggerTracePanel';
import { BeforeAfterNetworkPanel } from './BeforeAfterNetworkPanel';
import { PhaseScrubber } from './PhaseScrubber';
import { useSelectionStore } from '../../stores/selectionStore';
import type {
  ChangeEventSummary,
  ChangeTrigger,
  FinalRelationshipSummary,
  StakeholderActor,
} from '../../types/simulation';

interface ChangeExplorerProps {
  actors: StakeholderActor[];
  changeEvents: ChangeEventSummary[];
  changeAttribution: Record<string, ChangeTrigger[]>;
  finalRelationships: FinalRelationshipSummary[];
  actorNames: Record<string, string>;
  phases: string[];
}

export function ChangeExplorer({
  actors,
  changeEvents,
  changeAttribution,
  finalRelationships,
  actorNames,
  phases,
}: ChangeExplorerProps) {
  const {
    selectedActor,
    selectedChangeId,
    selectedPhase,
    selectedTurn,
    setActor,
    setChange,
    setPhase,
    setTurn,
  } = useSelectionStore();
  const [vizMode, setVizMode] = useState<'network' | 'state'>('network');

  useEffect(() => {
    if (!selectedChangeId && changeEvents.length > 0) {
      setChange(changeEvents[0].change_id);
    }
  }, [changeEvents, selectedChangeId, setChange]);

  const selectedChange = useMemo(
    () => changeEvents.find((change) => change.change_id === selectedChangeId) || changeEvents[0] || null,
    [changeEvents, selectedChangeId],
  );
  const selectedTriggers = selectedChange ? (changeAttribution[selectedChange.change_id] || []) : [];

  useEffect(() => {
    if (selectedChange && selectedTriggers.length > 0) {
      setTurn(selectedTriggers[0].turn_index || null);
    }
  }, [selectedChange?.change_id, selectedTriggers, setTurn]);

  const highlightedActorIds = selectedChange?.affected_actor_ids || [];
  const focusedRelationshipId = selectedChange?.category === 'relationship'
    ? `rel:${selectedChange.affected_actor_ids[0]}:${selectedChange.affected_actor_ids[1]}`
    : null;

  const stateRows = useMemo(() => {
    if (!selectedChange) return [];
    if (selectedChange.category === 'world_state' && typeof selectedChange.initial_value === 'number' && typeof selectedChange.final_value === 'number') {
      return [{
        key: selectedChange.affected_keys[0] || selectedChange.label,
        initial: selectedChange.initial_value,
        final: selectedChange.final_value,
      }];
    }
    if (selectedChange.category === 'actor_drift' && typeof selectedChange.final_value === 'number') {
      return [{
        key: 'drift_score',
        initial: typeof selectedChange.initial_value === 'number' ? selectedChange.initial_value : 0,
        final: selectedChange.final_value,
      }];
    }
    if (selectedChange.category === 'action' && selectedChange.final_value && typeof selectedChange.final_value === 'object') {
      return Object.entries(selectedChange.final_value as Record<string, number>).map(([key, value]) => ({
        key,
        initial: 0,
        final: value,
      }));
    }
    return [];
  }, [selectedChange]);

  return (
    <section id="change-explorer" className="space-y-4">
      <div className="sticky top-3 z-10">
        <GlassCard className="p-3 border border-border-subtle/80 backdrop-blur-sm bg-bg-primary/90">
          <div className="flex items-center justify-between gap-4 flex-wrap">
            <PhaseScrubber phases={phases} selectedPhase={selectedPhase} onSelectPhase={setPhase} />
            <div className="flex items-center gap-2">
              <Button size="sm" variant={vizMode === 'network' ? 'primary' : 'secondary'} onClick={() => setVizMode('network')}>
                <ArrowRightLeft size={14} className="inline mr-1" /> Network mode
              </Button>
              <Button size="sm" variant={vizMode === 'state' ? 'primary' : 'secondary'} onClick={() => setVizMode('state')}>
                <Activity size={14} className="inline mr-1" /> State mode
              </Button>
            </div>
          </div>
        </GlassCard>
      </div>

      <div className="grid grid-cols-1 xl:grid-cols-[1.05fr_1.1fr_0.95fr] gap-4 items-start">
        <ChangeCardRail
          changeEvents={changeEvents}
          actorNames={actorNames}
          selectedChangeId={selectedChange?.change_id || null}
          selectedActorId={selectedActor}
          selectedPhase={selectedPhase}
          onSelectChange={(changeId) => {
            setChange(changeId);
            const next = changeEvents.find((change) => change.change_id === changeId);
            if (next?.affected_actor_ids[0]) setActor(next.affected_actor_ids[0]);
          }}
        />

        <GlassCard className="p-5 h-full">
          <div className="flex items-center justify-between gap-3 mb-4">
            <div>
              <h3 className="text-sm font-semibold text-text-primary">
                {vizMode === 'network' ? 'Selected Change Visualisation' : 'Selected Change Values'}
              </h3>
              <p className="text-xs text-text-muted mt-1">
                {selectedChange?.trigger_summary || 'Select a change to inspect it.'}
              </p>
            </div>
          </div>

          {vizMode === 'network' ? (
            <BeforeAfterNetworkPanel
              title={selectedChange?.label || 'Selected change'}
              actors={actors}
              relationships={finalRelationships}
              highlightedActorIds={highlightedActorIds}
              highlightedRelationshipId={focusedRelationshipId}
            />
          ) : (
            <div className="space-y-3">
              {selectedChange?.meaning && (
                <div className="rounded-xl bg-blue-50/60 border border-blue-100 p-3 text-xs text-text-secondary">
                  {selectedChange.meaning}
                </div>
              )}
              {stateRows.map((row) => {
                const min = Math.min(row.initial, row.final, 0);
                const max = Math.max(row.initial, row.final, 1);
                const span = max - min || 1;
                const initialLeft = ((row.initial - min) / span) * 100;
                const finalLeft = ((row.final - min) / span) * 100;
                return (
                  <div key={row.key} className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-3">
                    <div className="flex items-center justify-between gap-2 text-sm">
                      <span className="font-medium text-text-primary">{row.key}</span>
                      <span className="font-mono text-text-muted">{row.initial.toFixed(2)} → {row.final.toFixed(2)}</span>
                    </div>
                    <div className="relative h-4 rounded-full bg-bg-primary mt-3">
                      <div
                        className="absolute top-1/2 h-1 -translate-y-1/2 rounded-full bg-zinc-300"
                        style={{
                          left: `${Math.min(initialLeft, finalLeft)}%`,
                          width: `${Math.abs(finalLeft - initialLeft)}%`,
                        }}
                      />
                      <div
                        className="absolute top-1/2 w-3 h-3 rounded-full bg-zinc-400 border-2 border-white -translate-y-1/2"
                        style={{ left: `${initialLeft}%`, transform: 'translate(-50%, -50%)' }}
                      />
                      <div
                        className="absolute top-1/2 w-3 h-3 rounded-full bg-accent-blue border-2 border-white -translate-y-1/2"
                        style={{ left: `${finalLeft}%`, transform: 'translate(-50%, -50%)' }}
                      />
                    </div>
                  </div>
                );
              })}
              {stateRows.length === 0 && (
                <div className="rounded-xl border border-dashed border-border-subtle p-6 text-sm text-text-muted">
                  This change is best read through the relationship network rather than a scalar state bar.
                </div>
              )}
              {selectedChange && (
                <div className="rounded-xl bg-blue-50/60 border border-blue-100 p-3 text-xs text-text-secondary">
                  <Sparkles size={14} className="inline mr-1 text-accent-blue" />
                  Affected actors: {selectedChange.affected_actor_ids.map((actorId) => actorNames[actorId] || actorId).join(', ') || 'system'}
                </div>
              )}
            </div>
          )}
        </GlassCard>

        <TriggerTracePanel
          change={selectedChange}
          triggers={selectedTriggers}
          actorNames={actorNames}
          selectedTurn={selectedTurn}
          onSelectTurn={setTurn}
        />
      </div>

    </section>
  );
}
