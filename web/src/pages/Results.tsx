import { useEffect, useMemo, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ArrowLeft, Loader2, Search } from 'lucide-react';
import { motion } from 'framer-motion';
import { useResults } from '../hooks/useApi';
import { useSelectionStore } from '../stores/selectionStore';
import { GlassCard } from '../components/ui/GlassCard';
import { Button } from '../components/ui/Button';
import { KPICard } from '../components/metrics/KPICard';
import { ChatBubble } from '../components/transcript/ChatBubble';
import { PhaseDivider } from '../components/transcript/PhaseDivider';
import { ResultsTabs } from '../components/results/ResultsTabs';
import { GlobalPhaseFilter } from '../components/results/GlobalPhaseFilter';
import { OutcomeAnalysisPanel } from '../components/results/OutcomeAnalysisPanel';
import { ActorAnalysisPanel } from '../components/results/ActorAnalysisPanel';
import type {
  ActorEvidenceItem,
  FinalRelationshipSummary,
  RelationshipAnalysisItem,
  SimulationResults,
} from '../types/simulation';

function buildPhaseAwareRelationships(
  data: SimulationResults,
  selectedPhase: string | null,
): FinalRelationshipSummary[] {
  const finalRelationships = data.final_relationships ?? [];
  const pairs = data.relationship_analysis?.pairs ?? [];
  const phases = data.runtime_summary.phase_order ?? [];
  if (!selectedPhase) return finalRelationships;

  const phaseIndex = phases.indexOf(selectedPhase);
  if (phaseIndex < 0) return finalRelationships;

  const pairMap = Object.fromEntries(pairs.map((pair) => [pair.relationship_id, pair]));
  return finalRelationships.map((relationship) => {
    const pair = pairMap[relationship.relationship_id];
    if (!pair) return relationship;

    const cumulative = pair.phase_deltas
      .filter((phaseDelta) => phases.indexOf(phaseDelta.phase_name) <= phaseIndex)
      .reduce(
        (acc, phaseDelta) => ({
          trust_delta: acc.trust_delta + phaseDelta.trust_delta,
          tension_delta: acc.tension_delta + phaseDelta.tension_delta,
          event_count: acc.event_count + phaseDelta.event_count,
        }),
        { trust_delta: 0, tension_delta: 0, event_count: 0 },
      );

    return {
      ...relationship,
      total_trust_delta: cumulative.trust_delta,
      total_tension_delta: cumulative.tension_delta,
      final_trust: Math.max(0, Math.min(1, pair.initial.trust + cumulative.trust_delta)),
      final_tension: Math.max(0, Math.min(1, pair.initial.tension + cumulative.tension_delta)),
      event_count: cumulative.event_count,
    };
  });
}

function evidenceTurns(items: ActorEvidenceItem[]) {
  return items.map((item) => item.turn_index).filter((turnIndex) => turnIndex > 0);
}

function selectedPairEvidence(
  pair: RelationshipAnalysisItem | null,
  selectedPhase: string | null,
) {
  if (!pair) return [];
  return (pair.top_trigger_summaries || []).filter((item) => !selectedPhase || item.phase_name === selectedPhase);
}

export default function Results() {
  const { id: simulationId } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { data, isLoading, error } = useResults(simulationId);
  const {
    activeTab,
    selectedPhase,
    selectedActor,
    selectedRelationshipId,
    selectedEvidenceType,
    selectedTurn,
    setActiveTab,
    setPhase,
    setActor,
    setRelationshipId,
    setEvidenceType,
    setTurn,
    clearAll,
  } = useSelectionStore();
  const [searchQuery, setSearchQuery] = useState('');

  const actorAnalysisActors = data?.actor_analysis?.actors ?? [];
  const relationshipPairs = data?.relationship_analysis?.pairs ?? [];

  useEffect(() => {
    clearAll();
    setSearchQuery('');
  }, [simulationId, clearAll]);

  useEffect(() => {
    if (!selectedRelationshipId && relationshipPairs.length > 0) {
      setRelationshipId(relationshipPairs[0].relationship_id);
    }
  }, [relationshipPairs, selectedRelationshipId, setRelationshipId]);

  useEffect(() => {
    if (!selectedActor && actorAnalysisActors.length > 0) {
      setActor(actorAnalysisActors[0].actor_id);
    }
  }, [actorAnalysisActors, selectedActor, setActor]);

  useEffect(() => {
    if (selectedTurn !== null) {
      document.getElementById(`turn-${selectedTurn}`)?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }, [selectedTurn]);

  const rs = data?.runtime_summary;
  const script = data?.script;
  const actorNames = useMemo(
    () => Object.fromEntries((script?.stakeholders || []).map((actor) => [actor.actor_id, actor.role])),
    [script],
  );
  const phases = rs?.phase_order || [];
  const beforeRelationships = data?.initial_relationships ?? [];
  const afterRelationships = useMemo(
    () => (data ? buildPhaseAwareRelationships(data, selectedPhase) : []),
    [data, selectedPhase],
  );
  const selectedPair = relationshipPairs.find((pair) => pair.relationship_id === selectedRelationshipId) || relationshipPairs[0] || null;
  const selectedActorAnalysis = actorAnalysisActors.find((actor) => actor.actor_id === selectedActor) || actorAnalysisActors[0] || null;
  const phaseKey = selectedPhase || '__all__';
  const phaseEvidence = data?.phase_filtered_attribution?.[phaseKey] || data?.phase_filtered_attribution?.__all__ || {
    relationship: [],
    actor_drift: [],
    action: [],
    all: [],
  };
  const pairEvidence = selectedPairEvidence(selectedPair, selectedPhase);
  const actorEvidence = selectedActorAnalysis
    ? selectedActorAnalysis.evidence_by_type[selectedEvidenceType].filter((item) => !selectedPhase || item.phase_name === selectedPhase)
    : [];

  const highlightedTurns = useMemo(() => {
    const turns = activeTab === 'outcome'
      ? [...evidenceTurns(pairEvidence), ...evidenceTurns(phaseEvidence.all.slice(0, 6))]
      : evidenceTurns(actorEvidence);
    return new Set(turns);
  }, [activeTab, pairEvidence, phaseEvidence, actorEvidence]);

  const filteredTurns = useMemo(() => {
    const query = searchQuery.trim().toLowerCase();
    return (rs?.turns || []).filter((turn) => {
      if (selectedPhase && turn.phase_name !== selectedPhase) return false;
      if (query && !turn.content.toLowerCase().includes(query) && !(actorNames[turn.actor_id] || turn.display_name).toLowerCase().includes(query)) {
        return false;
      }
      return true;
    });
  }, [rs, searchQuery, selectedPhase, actorNames]);

  const turnCount = rs?.turn_count || (rs?.turns || []).length;
  const actionCount = selectedPhase
    ? (data?.phase_filtered_attribution?.[phaseKey]?.action.length || 0)
    : (rs?.executed_actions || []).length;
  const relationshipShiftCount = afterRelationships.filter((relationship) =>
    Math.abs(relationship.total_trust_delta) > 0.05 || Math.abs(relationship.total_tension_delta) > 0.05,
  ).length;
  const actorCount = actorAnalysisActors.length || (script?.stakeholders || []).length;

  if (isLoading) {
    return (
      <div className="min-h-screen bg-bg-primary flex items-center justify-center">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="flex flex-col items-center gap-4">
          <Loader2 size={38} className="text-accent-blue animate-spin" />
          <div className="text-center">
            <div className="text-lg font-semibold text-text-primary">Loading analysis workspace</div>
            <div className="text-sm text-text-muted mt-1">Preparing outcome and actor comparisons...</div>
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
            : 'Results not available'}
        </div>
        <Button variant="secondary" onClick={() => navigate('/setup')}>
          <ArrowLeft size={14} className="inline mr-1" /> Back to Setup
        </Button>
      </div>
    );
  }

  const safeRs = rs!;
  const safeScript = script!;

  return (
    <div className="min-h-screen bg-bg-primary">
      <header className="border-b border-border-subtle px-6 py-4 bg-bg-primary/95 backdrop-blur-sm sticky top-0 z-20">
        <div className="max-w-[1500px] mx-auto flex items-center justify-between gap-4">
          <div>
            <h1 className="text-lg font-bold text-text-primary">{safeRs.title || 'Simulation Results'}</h1>
            <p className="text-sm text-text-muted mt-0.5">{safeRs.objective}</p>
          </div>
          <Button variant="ghost" size="sm" onClick={() => navigate('/setup')}>
            <ArrowLeft size={14} className="inline mr-1" /> New Simulation
          </Button>
        </div>
      </header>

      <div className="max-w-[1500px] mx-auto px-6 py-6 space-y-5">
        <GlobalPhaseFilter phases={phases} selectedPhase={selectedPhase} onSelectPhase={setPhase} />

        <div className="flex items-center justify-between gap-4 flex-wrap">
          <ResultsTabs activeTab={activeTab} onChange={setActiveTab} />
          <div className="flex items-center gap-2 flex-wrap">
            {selectedPhase && (
              <Button size="sm" variant="secondary" onClick={() => setPhase(null)}>
                Clear phase
              </Button>
            )}
            {activeTab === 'actor' && selectedActor && (
              <Button size="sm" variant="secondary" onClick={() => setActor(actorAnalysisActors[0]?.actor_id || null)}>
                Reset actor
              </Button>
            )}
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          <KPICard label="Turns" value={turnCount} format="count" good="high" threshold={0} />
          <KPICard label="Actions" value={actionCount} format="count" good="high" threshold={0} />
          <KPICard label="Changed Relationships" value={relationshipShiftCount} format="count" good="high" threshold={0} />
          <KPICard label="Actors" value={actorCount} format="count" good="high" threshold={0} />
        </div>

        {activeTab === 'outcome' ? (
          <OutcomeAnalysisPanel
            mode={safeScript.simulation_mode}
            outcomeAnalysis={data.outcome_analysis ?? null}
            actors={safeScript.stakeholders}
            beforeRelationships={beforeRelationships}
            afterRelationships={afterRelationships}
            selectedPair={selectedPair}
            selectedPhase={selectedPhase}
            selectedActorId={selectedActor}
            selectedRelationshipId={selectedRelationshipId}
            outcomeEvidence={phaseEvidence.all}
            actorNames={actorNames}
            selectedTurn={selectedTurn}
            onSelectActor={(actorId) => setActor(actorId)}
            onSelectRelationship={(relationshipId, sourceActorId) => {
              setRelationshipId(relationshipId);
              setActor(sourceActorId);
            }}
            onSelectTurn={setTurn}
          />
        ) : (
          <ActorAnalysisPanel
            actors={actorAnalysisActors}
            selectedActorId={selectedActor}
            selectedPhase={selectedPhase}
            selectedEvidenceType={selectedEvidenceType}
            actorNames={actorNames}
            selectedTurn={selectedTurn}
            onSelectActor={setActor}
            onSelectEvidenceType={setEvidenceType}
            onSelectTurn={setTurn}
          />
        )}

        <GlassCard className="p-5">
          <div className="flex items-start justify-between gap-3 flex-wrap">
            <div>
              <h3 className="text-sm font-semibold text-text-primary">Transcript Evidence</h3>
              <p className="text-xs text-text-muted mt-1">
                Linked support transcript. The current phase filter applies here too.
              </p>
            </div>
            <div className="relative w-full sm:w-72">
              <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-text-muted" />
              <input
                value={searchQuery}
                onChange={(evt) => setSearchQuery(evt.target.value)}
                placeholder="Search transcript..."
                className="w-full rounded-xl border border-border-subtle bg-bg-elevated pl-10 pr-3 py-2 text-sm outline-none focus:border-accent-blue/40"
              />
            </div>
          </div>

          <div className="flex items-center gap-3 text-xs text-text-muted mt-4 flex-wrap">
            {selectedPhase && <span>Phase: {selectedPhase}</span>}
            {activeTab === 'actor' && selectedActorAnalysis && <span>Actor focus: {selectedActorAnalysis.before_summary.role}</span>}
            {activeTab === 'outcome' && selectedPair && <span>Relationship focus: {selectedPair.display_label}</span>}
          </div>

          <div className="space-y-2 mt-4">
            {filteredTurns.map((turn, index) => {
              const prevTurn = filteredTurns[index - 1];
              const showDivider = !prevTurn || prevTurn.phase_name !== turn.phase_name;
              const highlighted = turn.turn_index === selectedTurn || highlightedTurns.has(turn.turn_index);
              const dimmed = activeTab === 'actor' && selectedActor !== null && turn.actor_id !== selectedActor;

              return (
                <div key={turn.turn_index}>
                  {showDivider && <PhaseDivider phaseName={turn.phase_name} />}
                  <ChatBubble
                    actorId={turn.actor_id}
                    displayName={turn.display_name}
                    content={turn.content}
                    turnIndex={turn.turn_index}
                    colorIndex={safeScript.stakeholders.findIndex((actor) => actor.actor_id === turn.actor_id)}
                    highlighted={highlighted}
                    dimmed={dimmed}
                    onClick={() => {
                      setTurn(turn.turn_index);
                      if (activeTab === 'actor') {
                        setActor(turn.actor_id);
                      }
                    }}
                  />
                </div>
              );
            })}
            {filteredTurns.length === 0 && (
              <div className="text-sm text-text-muted py-6">
                No transcript turns matched the current phase filter and search query.
              </div>
            )}
          </div>
        </GlassCard>
      </div>
    </div>
  );
}
