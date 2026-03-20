import { useMemo, useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft, ChevronUp, ChevronDown, Loader2, BarChart3, MessageCircle, Zap, Activity, AlertTriangle } from 'lucide-react';
import { motion } from 'framer-motion';
import { useResults } from '../hooks/useApi';
import { useSelectionStore } from '../stores/selectionStore';
import { GlassCard } from '../components/ui/GlassCard';
import { Tabs } from '../components/ui/Tabs';
import { Button } from '../components/ui/Button';
import { KPICard } from '../components/metrics/KPICard';
import { KeyMomentsPanel } from '../components/moments/KeyMomentsPanel';
import { DumbbellChart } from '../components/charts/DumbbellChart';
import { DriftTimeline } from '../components/charts/DriftTimeline';
import { RelationshipList } from '../components/metrics/RelationshipList';
import { RelationshipGraph } from '../components/network/RelationshipGraph';
import { RelationshipHeatmap } from '../components/metrics/Heatmap';
import { ChatBubble } from '../components/transcript/ChatBubble';
import { PhaseDivider } from '../components/transcript/PhaseDivider';
import { ActionEvent as ActionEventComponent } from '../components/transcript/ActionEvent';
import { ConclusionPanel } from '../components/conclusion/ConclusionPanel';
import { ActorArcsPanel } from '../components/conclusion/ActorArcsPanel';
import { ACTOR_COLORS } from '../types/simulation';

export default function Results() {
  const { id: simulationId } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { data, isLoading, error } = useResults(simulationId);
  const { selectedActor, setActor, selectedTurn, setTurn, selectedPhase, setPhase, clearAll } = useSelectionStore();
  const [networkPhaseFilter, setNetworkPhaseFilter] = useState<string | null>(null);
  const [showHeatmap, setShowHeatmap] = useState(false);
  const [showResearchDetails, setShowResearchDetails] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [filterActorId, setFilterActorId] = useState<string>('all');
  const [filterPhase, setFilterPhase] = useState<string>('all');

  // Clear selections on mount
  useEffect(() => {
    clearAll();
  }, [simulationId]);

  // Scroll to selected turn
  useEffect(() => {
    if (selectedTurn !== null) {
      const el = document.getElementById(`result-turn-${selectedTurn}`);
      el?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }, [selectedTurn]);

  if (isLoading) {
    return (
      <div className="min-h-screen bg-bg-primary flex items-center justify-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="flex flex-col items-center gap-6"
        >
          <div className="relative">
            <Loader2 size={40} className="text-accent-blue animate-spin" />
          </div>
          <div className="text-center space-y-2">
            <h2 className="text-lg font-semibold text-text-primary">Analyzing Results</h2>
            <p className="text-sm text-text-muted max-w-xs">
              Crunching metrics, extracting key moments, and building relationship graphs...
            </p>
          </div>
          <div className="flex items-center gap-4 mt-2">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.3 }}
              className="flex items-center gap-1.5 text-xs text-text-muted"
            >
              <BarChart3 size={14} className="text-accent-green" /> Metrics
            </motion.div>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.6 }}
              className="flex items-center gap-1.5 text-xs text-text-muted"
            >
              <Zap size={14} className="text-accent-amber" /> Key Moments
            </motion.div>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.9 }}
              className="flex items-center gap-1.5 text-xs text-text-muted"
            >
              <MessageCircle size={14} className="text-accent-blue" /> Relationships
            </motion.div>
          </div>
        </motion.div>
      </div>
    );
  }

  if (error || !data || !data.runtime_summary) {
    return (
      <div className="min-h-screen bg-bg-primary flex items-center justify-center flex-col gap-4">
        <div className="text-text-muted">
          {(data && 'status' in data && (data as Record<string, unknown>).status !== 'complete')
            ? 'Simulation still running...'
            : 'Results not available'
          }
        </div>
        <Button variant="secondary" onClick={() => navigate('/setup')}><ArrowLeft size={14} className="inline mr-1" /> Back to Setup</Button>
      </div>
    );
  }

  const { runtime_summary: rs, metrics, key_moments, conclusion, script } = data;
  const actorIds = script?.stakeholders?.map((a) => a.actor_id) || Object.keys(rs.actor_display_names || {});
  // Use roles instead of display names for all actor labels
  const actorNames: Record<string, string> = {};
  for (const a of script?.stakeholders || []) {
    actorNames[a.actor_id] = a.role;
  }
  const phases = rs.phase_order || [];

  // User-friendly KPI values
  const turnCount = rs.turn_count || (rs.turns || []).length;
  const phaseCount = phases.length;
  const actionCount = (rs.executed_actions || []).length;
  const relationshipShiftCount = (rs.relationship_events || []).filter(
    (e) => Math.abs(e.trust_delta) > 0.05
  ).length;
  const isGuided = script?.simulation_mode === 'guided';

  // Filter transcript
  const filteredTurns = useMemo(() => {
    let turns = rs.turns || [];
    if (searchQuery) {
      const q = searchQuery.toLowerCase();
      turns = turns.filter((t) => t.content.toLowerCase().includes(q) || (actorNames[t.actor_id] || t.display_name).toLowerCase().includes(q));
    }
    if (filterActorId !== 'all') {
      turns = turns.filter((t) => t.actor_id === filterActorId);
    }
    if (filterPhase !== 'all') {
      turns = turns.filter((t) => t.phase_name === filterPhase);
    }
    return turns;
  }, [rs.turns, searchQuery, filterActorId, filterPhase]);

  return (
    <div className="min-h-screen bg-bg-primary">
      {/* Header */}
      <header className="border-b border-border-subtle px-6 py-3">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div>
            <h1 className="text-base font-bold text-text-primary">{rs.title || 'Simulation Results'}</h1>
            <p className="text-xs text-text-muted">{rs.objective}</p>
          </div>
          <div className="flex gap-2">
            <Button variant="ghost" size="sm" onClick={() => navigate('/setup')}>
              <ArrowLeft size={14} className="inline mr-1" /> New Simulation
            </Button>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-6 py-6 space-y-6">
        {/* KPI Summary Cards — user-friendly stats */}
        <div className={`grid grid-cols-2 ${isGuided ? 'md:grid-cols-5' : 'md:grid-cols-4'} gap-3`}>
          <KPICard label="Turns" value={turnCount} format="count" good="high" threshold={0} />
          <KPICard label="Phases" value={phaseCount} format="count" good="high" threshold={0} />
          <KPICard label="Actions Taken" value={actionCount} format="count" good="high" threshold={0} />
          <KPICard label="Relationship Shifts" value={relationshipShiftCount} format="count" good="high" threshold={0} />
          {isGuided && conclusion?.outcome_achieved && (
            <GlassCard className="p-3 text-center">
              <div className="text-xs text-text-muted mb-1">Outcome</div>
              <div className={`text-lg font-bold ${
                conclusion.outcome_achieved === 'achieved' ? 'text-accent-green' :
                conclusion.outcome_achieved === 'partial' ? 'text-accent-amber' :
                'text-accent-red'
              }`}>
                {conclusion.outcome_achieved === 'achieved' ? 'Achieved' :
                 conclusion.outcome_achieved === 'partial' ? 'Partial' :
                 'Not Achieved'}
              </div>
              <div className="mt-1 flex justify-center">
                {conclusion.outcome_achieved === 'achieved' ? (
                  <Activity size={14} className="text-accent-green" />
                ) : conclusion.outcome_achieved === 'partial' ? (
                  <AlertTriangle size={14} className="text-accent-amber" />
                ) : (
                  <AlertTriangle size={14} className="text-accent-red" />
                )}
              </div>
            </GlassCard>
          )}
        </div>

        {/* Main Tabbed Content */}
        <Tabs
          tabs={[
            { id: 'overview', label: 'Overview' },
            { id: 'relationships', label: 'Relationships' },
            { id: 'transcript', label: 'Transcript' },
          ]}
          defaultTab="overview"
        >
          {(tab) => (
            <>
              {/* ── Tab 1: Overview ─────────────────────────────────── */}
              {tab === 'overview' && (
                <div className="space-y-6">
                  {/* 1. Conclusion Hero Panel */}
                  {conclusion && (
                    <ConclusionPanel conclusion={conclusion} actorNames={actorNames} />
                  )}

                  {/* 2. Actor Arcs */}
                  {conclusion?.actor_arcs && conclusion.actor_arcs.length > 0 && (
                    <ActorArcsPanel arcs={conclusion.actor_arcs} actorIds={actorIds} />
                  )}

                  {/* 3. Key Moments */}
                  <KeyMomentsPanel moments={key_moments || []} actorNames={actorNames} />

                  {/* 4. Unresolved Tensions */}
                  {conclusion?.unresolved_tensions && conclusion.unresolved_tensions.length > 0 && (
                    <GlassCard className="p-5">
                      <h3 className="text-sm font-semibold text-text-secondary mb-3">Unresolved Tensions</h3>
                      <ul className="space-y-2">
                        {conclusion.unresolved_tensions.map((tension, i) => (
                          <li key={i} className="text-sm text-text-secondary flex items-start gap-2">
                            <AlertTriangle size={14} className="text-accent-amber mt-0.5 flex-shrink-0" />
                            {tension}
                          </li>
                        ))}
                      </ul>
                    </GlassCard>
                  )}

                  {/* 5. Actions Taken (moved from Transcript tab) */}
                  {(rs.executed_actions || []).length > 0 && (
                    <GlassCard className="p-5">
                      <h3 className="text-sm font-semibold text-text-secondary mb-3">
                        Actions Taken ({rs.executed_actions.length})
                      </h3>
                      <div className="space-y-1">
                        {rs.executed_actions.map((action, i) => {
                          const colorIndex = actorIds.indexOf(action.owner_actor_id);
                          return (
                            <ActionEventComponent
                              key={i}
                              actorId={action.owner_actor_id}
                              displayName={actorNames[action.owner_actor_id] || action.owner_actor_id}
                              actionType={action.action_type}
                              targetKey={action.target_key}
                              deltas={action.applied_delta}
                              colorIndex={colorIndex}
                            />
                          );
                        })}
                      </div>
                    </GlassCard>
                  )}

                  {/* 6. Research Details — collapsed accordion */}
                  <div>
                    <button
                      onClick={() => setShowResearchDetails(!showResearchDetails)}
                      className="flex items-center gap-1.5 text-xs text-text-muted hover:text-text-secondary cursor-pointer mb-2"
                    >
                      {showResearchDetails
                        ? <ChevronUp size={12} />
                        : <ChevronDown size={12} />
                      }
                      Research Details (OCEAN Fidelity, Drift, Violations)
                    </button>
                    {showResearchDetails && (
                      <div className="space-y-4">
                        {/* Research KPIs */}
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                          <KPICard label="Drift MAE" value={metrics.persona_drift_mae} threshold={0.15} />
                          <KPICard label="Contradiction" value={metrics.commitment_contradiction_rate} threshold={0.01} />
                          <KPICard
                            label="Diversity"
                            value={typeof (metrics as Record<string, unknown>).role_action_diversity_score === 'number'
                              ? (metrics as Record<string, unknown>).role_action_diversity_score as number
                              : 0.5}
                            good="high"
                            threshold={0.5}
                          />
                          <KPICard label="Violations" value={metrics.envelope_violations} format="count" threshold={5} />
                        </div>

                        {/* OCEAN Dumbbell */}
                        <GlassCard className="p-5">
                          <h3 className="text-sm font-semibold text-text-secondary mb-4">
                            OCEAN Trait Fidelity — Target vs Actual
                          </h3>
                          <DumbbellChart
                            actorPriors={rs.actor_personality_priors || {}}
                            actorEstimates={metrics.actor_trait_estimates || {}}
                            actorNames={actorNames}
                            actorIds={actorIds}
                          />
                        </GlassCard>

                        {/* Drift Timeline */}
                        <GlassCard className="p-5">
                          <h3 className="text-sm font-semibold text-text-secondary mb-4">
                            Persona Drift Over Time
                          </h3>
                          <DriftTimeline
                            actorStateEvents={rs.actor_state_events || []}
                            actorIds={actorIds}
                            actorNames={actorNames}
                          />
                        </GlassCard>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {/* ── Tab 2: Relationships ────────────────────────────── */}
              {tab === 'relationships' && (
                <div className="space-y-6">
                  {/* Relationship List */}
                  <GlassCard className="p-5">
                    <h3 className="text-sm font-semibold text-text-secondary mb-4">
                      Relationship Evidence Timeline
                    </h3>
                    <RelationshipList
                      events={rs.relationship_events || []}
                      actorNames={actorNames}
                      actorIds={actorIds}
                    />
                  </GlassCard>

                  {/* Network Graph */}
                  <GlassCard className="p-5">
                    <div className="flex items-center justify-between mb-4">
                      <h3 className="text-sm font-semibold text-text-secondary">
                        Relationship Network
                      </h3>
                      <div className="flex gap-1">
                        <button
                          onClick={() => setNetworkPhaseFilter(null)}
                          className={`px-2 py-0.5 rounded text-xs cursor-pointer ${
                            !networkPhaseFilter ? 'bg-accent-blue/20 text-accent-blue' : 'bg-bg-elevated text-text-muted'
                          }`}
                        >
                          All
                        </button>
                        {phases.map((p) => (
                          <button
                            key={p}
                            onClick={() => setNetworkPhaseFilter(p)}
                            className={`px-2 py-0.5 rounded text-xs cursor-pointer ${
                              networkPhaseFilter === p ? 'bg-accent-blue/20 text-accent-blue' : 'bg-bg-elevated text-text-muted'
                            }`}
                          >
                            {p}
                          </button>
                        ))}
                      </div>
                    </div>
                    {script?.stakeholders && (
                      <RelationshipGraph
                        actors={script.stakeholders}
                        events={rs.relationship_events || []}
                        phaseFilter={networkPhaseFilter}
                        phaseOrder={phases}
                      />
                    )}
                  </GlassCard>

                  {/* Heatmap toggle */}
                  <div className="flex justify-end">
                    <button
                      onClick={() => setShowHeatmap(!showHeatmap)}
                      className="text-xs text-text-muted hover:text-text-secondary cursor-pointer"
                    >
                      {showHeatmap
                        ? <><ChevronUp size={12} className="inline mr-0.5" /> Hide Heatmap</>
                        : <><ChevronDown size={12} className="inline mr-0.5" /> Show Trust Heatmap</>
                      }
                    </button>
                  </div>
                  {showHeatmap && (
                    <GlassCard className="p-5">
                      <h3 className="text-sm font-semibold text-text-secondary mb-4">
                        Trust Matrix
                      </h3>
                      <RelationshipHeatmap
                        events={rs.relationship_events || []}
                        actorNames={actorNames}
                        actorIds={actorIds}
                      />
                    </GlassCard>
                  )}
                </div>
              )}

              {/* ── Tab 3: Transcript ──────────────────────────────── */}
              {tab === 'transcript' && (
                <div className="space-y-4">
                  {/* Search & Filter bar */}
                  <div className="flex items-center gap-3 flex-wrap">
                    <input
                      type="text"
                      placeholder="Search transcript..."
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      className="bg-bg-elevated border border-border-subtle text-text-primary text-sm rounded-lg px-3 py-1.5 w-64 focus:outline-none focus:ring-1 focus:ring-accent-blue/40"
                    />
                    <select
                      value={filterActorId}
                      onChange={(e) => setFilterActorId(e.target.value)}
                      className="bg-bg-elevated border border-border-subtle text-text-secondary text-xs rounded px-2 py-1.5"
                    >
                      <option value="all">All actors</option>
                      {actorIds.map((id) => (
                        <option key={id} value={id}>{actorNames[id] || id}</option>
                      ))}
                    </select>
                    <select
                      value={filterPhase}
                      onChange={(e) => setFilterPhase(e.target.value)}
                      className="bg-bg-elevated border border-border-subtle text-text-secondary text-xs rounded px-2 py-1.5"
                    >
                      <option value="all">All phases</option>
                      {phases.map((p) => (
                        <option key={p} value={p}>{p}</option>
                      ))}
                    </select>
                    <span className="text-xs text-text-muted ml-auto">
                      {filteredTurns.length} / {(rs.turns || []).length} turns
                    </span>
                  </div>

                  {/* Transcript */}
                  <GlassCard className="p-4 max-h-[600px] overflow-y-auto">
                    {filteredTurns.length === 0 ? (
                      <div className="text-sm text-text-muted text-center py-8">No matching turns</div>
                    ) : (
                      <div className="space-y-1">
                        {filteredTurns.map((turn, i) => {
                          const prevPhase = i > 0 ? filteredTurns[i - 1].phase_name : '';
                          const showDivider = turn.phase_name !== prevPhase;
                          const colorIndex = actorIds.indexOf(turn.actor_id);

                          return (
                            <div key={i} id={`result-turn-${turn.turn_index}`}>
                              {showDivider && <PhaseDivider phaseName={turn.phase_name} />}
                              <ChatBubble
                                actorId={turn.actor_id}
                                displayName={actorNames[turn.actor_id] || turn.display_name}
                                content={turn.content}
                                turnIndex={turn.turn_index}
                                colorIndex={colorIndex}
                                highlighted={turn.turn_index === selectedTurn}
                                dimmed={selectedActor !== null && turn.actor_id !== selectedActor}
                                onClick={() => setTurn(turn.turn_index)}
                              />
                            </div>
                          );
                        })}
                      </div>
                    )}
                  </GlassCard>
                </div>
              )}
            </>
          )}
        </Tabs>
      </div>
    </div>
  );
}
