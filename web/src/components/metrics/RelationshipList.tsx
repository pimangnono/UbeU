import { useState, useMemo } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { ArrowRight, TrendingUp, TrendingDown, AlertTriangle } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import { useSelectionStore } from '../../stores/selectionStore';
import type { RelationshipRecord } from '../../types/simulation';
import { ACTOR_COLORS } from '../../types/simulation';

interface RelationshipListProps {
  events: RelationshipRecord[];
  actorNames: Record<string, string>;
  actorIds: string[];
}

interface AggregatedRelationship {
  source: string;
  target: string;
  events: RelationshipRecord[];
  totalTrustDelta: number;
  totalTensionDelta: number;
  finalTrust: number;
}

export function RelationshipList({ events, actorNames, actorIds }: RelationshipListProps) {
  const { selectedRelationship, setRelationship, setTurn } = useSelectionStore();
  const [sortBy, setSortBy] = useState<'change' | 'trust'>('change');
  const [filterPhase, setFilterPhase] = useState<string>('all');

  const phases = useMemo(() => {
    const p = new Set(events.map((e) => e.phase_name));
    return ['all', ...Array.from(p)];
  }, [events]);

  const filteredEvents = useMemo(() => {
    if (filterPhase === 'all') return events;
    return events.filter((e) => e.phase_name === filterPhase);
  }, [events, filterPhase]);

  const aggregated = useMemo(() => {
    const map = new Map<string, AggregatedRelationship>();
    for (const evt of filteredEvents) {
      const src = evt.source_actor_id || evt.source || '';
      const tgt = evt.target_actor_id || evt.target || '';
      const key = `${src}__${tgt}`;
      if (!map.has(key)) {
        map.set(key, {
          source: src,
          target: tgt,
          events: [],
          totalTrustDelta: 0,
          totalTensionDelta: 0,
          finalTrust: 0.5,
        });
      }
      const agg = map.get(key)!;
      agg.events.push(evt);
      agg.totalTrustDelta += evt.trust_delta;
      agg.totalTensionDelta += evt.tension_delta;
      agg.finalTrust = 0.5 + agg.totalTrustDelta;
    }

    const arr = Array.from(map.values());
    if (sortBy === 'change') {
      arr.sort((a, b) => Math.abs(b.totalTrustDelta) - Math.abs(a.totalTrustDelta));
    } else {
      arr.sort((a, b) => a.finalTrust - b.finalTrust);
    }
    return arr;
  }, [filteredEvents, sortBy]);

  const isSelected = (src: string, tgt: string) =>
    selectedRelationship?.[0] === src && selectedRelationship?.[1] === tgt;

  return (
    <div className="space-y-3">
      {/* Filters */}
      <div className="flex items-center gap-3 text-xs">
        <label className="text-text-muted">Sort:</label>
        <select
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value as 'change' | 'trust')}
          className="bg-bg-elevated text-text-secondary px-2 py-1 rounded border border-border-subtle text-xs"
        >
          <option value="change">Biggest change</option>
          <option value="trust">Trust level</option>
        </select>
        <label className="text-text-muted ml-2">Phase:</label>
        <select
          value={filterPhase}
          onChange={(e) => setFilterPhase(e.target.value)}
          className="bg-bg-elevated text-text-secondary px-2 py-1 rounded border border-border-subtle text-xs"
        >
          {phases.map((p) => (
            <option key={p} value={p}>{p === 'all' ? 'All phases' : p}</option>
          ))}
        </select>
      </div>

      {/* Relationship items */}
      {aggregated.map((rel) => {
        const srcIdx = actorIds.indexOf(rel.source);
        const tgtIdx = actorIds.indexOf(rel.target);
        const selected = isSelected(rel.source, rel.target);

        return (
          <div key={`${rel.source}__${rel.target}`}>
            <GlassCard
              hover
              className={`p-3 cursor-pointer ${selected ? 'ring-1 ring-accent-blue/40' : ''}`}
              onClick={() =>
                setRelationship(selected ? null : [rel.source, rel.target])
              }
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-sm">
                  <span style={{ color: ACTOR_COLORS[srcIdx % ACTOR_COLORS.length] }} className="font-medium">
                    {actorNames[rel.source] || rel.source}
                  </span>
                  <ArrowRight size={12} className="text-text-muted" />
                  <span style={{ color: ACTOR_COLORS[tgtIdx % ACTOR_COLORS.length] }} className="font-medium">
                    {actorNames[rel.target] || rel.target}
                  </span>
                </div>
                <div className="flex items-center gap-3 text-xs font-mono">
                  <span className="text-text-muted">trust: 0.50 {'\u2192'} {rel.finalTrust.toFixed(2)}</span>
                  <span className={`inline-flex items-center gap-0.5 ${rel.totalTrustDelta >= 0 ? 'text-accent-green' : 'text-accent-red'}`}>
                    {rel.totalTrustDelta >= 0 ? <TrendingUp size={12} /> : <TrendingDown size={12} />}
                    {Math.abs(rel.totalTrustDelta).toFixed(2)}
                  </span>
                </div>
              </div>
            </GlassCard>

            {/* Evidence timeline (expanded) */}
            <AnimatePresence>
              {selected && (
                <motion.div
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: 'auto', opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  className="overflow-hidden"
                >
                  <div className="ml-4 mt-1 space-y-2 border-l-2 border-border-subtle pl-4 py-2">
                    {rel.events.map((evt, i) => {
                      const isMajor = Math.abs(evt.trust_delta) > 0.1;
                      return (
                        <div key={i} className="text-xs">
                          <div className="flex items-center gap-2 text-text-muted">
                            <span className="font-mono">Turn {evt.turn_index}</span>
                            <span className="px-1 py-0.5 rounded bg-bg-elevated">{evt.phase_name}</span>
                            {isMajor && (
                              <span className="text-accent-amber inline-flex items-center gap-0.5">
                                <AlertTriangle size={12} /> Major shift
                              </span>
                            )}
                          </div>
                          {evt.evidence && (
                            <div className="text-text-secondary mt-0.5 italic">
                              "{evt.evidence.slice(0, 120)}{evt.evidence.length > 120 ? '...' : ''}"
                            </div>
                          )}
                          <div className="flex gap-3 mt-0.5 font-mono">
                            <span className={evt.trust_delta >= 0 ? 'text-accent-green' : 'text-accent-red'}>
                              trust {evt.trust_delta >= 0 ? '+' : ''}{evt.trust_delta.toFixed(2)}
                            </span>
                            <span className={evt.tension_delta >= 0 ? 'text-accent-red' : 'text-accent-green'}>
                              tension {evt.tension_delta >= 0 ? '+' : ''}{evt.tension_delta.toFixed(2)}
                            </span>
                          </div>
                          <button
                            onClick={() => setTurn(evt.turn_index)}
                            className="text-accent-blue hover:text-blue-600 mt-0.5 cursor-pointer inline-flex items-center gap-0.5"
                          >
                            <ArrowRight size={10} /> Jump to transcript
                          </button>
                        </div>
                      );
                    })}
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        );
      })}
    </div>
  );
}
