import { useState, useCallback, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { Check, ArrowLeft, ArrowRight, Network, LayoutGrid, ChevronRight, Loader2, Rocket } from 'lucide-react';
import { GlassCard } from '../components/ui/GlassCard';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';
import { Tooltip, InfoLabel } from '../components/ui/Tooltip';
import { ActorCard } from '../components/actors/ActorCard';
import { ActorNetworkView } from '../components/actors/ActorNetworkView';
import { LoadingActors } from '../components/ui/LoadingActors';
import { useScenarios, useGenerateScript, useStartSimulation } from '../hooks/useApi';
import { ScenarioCardSkeleton } from '../components/ui/Skeleton';
import type { SimulationScript, StakeholderActor, ActorRelationship, ScenarioCard } from '../types/simulation';
import { ACTOR_COLORS } from '../types/simulation';

function generateInitialRelationships(actors: StakeholderActor[]): ActorRelationship[] {
  const rels: ActorRelationship[] = [];
  for (let i = 0; i < actors.length; i++) {
    for (let j = i + 1; j < actors.length; j++) {
      const a = actors[i];
      const b = actors[j];
      const aAgg = a.strategic_disposition === 'cooperative' || a.strategic_disposition === 'neutral';
      const bAgg = b.strategic_disposition === 'cooperative' || b.strategic_disposition === 'neutral';

      // Only create edges where there's a clear dynamic (not all pairs)
      if (aAgg && bAgg && a.strategic_disposition === 'cooperative' && b.strategic_disposition === 'cooperative') {
        rels.push({ id: `rel-${a.actor_id}-${b.actor_id}`, source: a.actor_id, target: b.actor_id, label: 'potential allies' });
      } else if (!aAgg || !bAgg) {
        // At least one is competitive/adversarial → tension
        const label = (!aAgg && !bAgg) ? 'competing interests' : 'tension';
        rels.push({ id: `rel-${a.actor_id}-${b.actor_id}`, source: a.actor_id, target: b.actor_id, label });
      }
      // Skip neutral-neutral pairs — no obvious initial relationship
    }
  }
  return rels;
}

type WizardStep = 1 | 2 | 3;

const STEP_LABELS = ['Scenario Brief', 'Actors & Config', 'Review & Launch'];

export default function Setup() {
  const navigate = useNavigate();
  const [step, setStep] = useState<WizardStep>(1);
  const [generateError, setGenerateError] = useState<string | null>(null);
  const [brief, setBrief] = useState('');
  const [actorCount, setActorCount] = useState<number>(3);
  const [simulationMode, setSimulationMode] = useState<'guided' | 'exploratory'>('guided');
  const [outcomeSpec, setOutcomeSpec] = useState('');
  const [script, setScript] = useState<SimulationScript | null>(null);
  const [relationships, setRelationships] = useState<ActorRelationship[]>([]);
  const [actorViewMode, setActorViewMode] = useState<'network' | 'cards'>('network');
  const [categoryFilter, setCategoryFilter] = useState<string>('All');

  const abortRef = useRef<AbortController | null>(null);

  const scenarios = useScenarios();
  const generateScript = useGenerateScript();
  const startSimulation = useStartSimulation();

  const handleScenarioSelect = (scenario: ScenarioCard) => {
    setBrief(scenario.brief);
    setActorCount(scenario.actor_count);
    if (scenario.simulation_mode === 'guided' || scenario.simulation_mode === 'exploratory') {
      setSimulationMode(scenario.simulation_mode);
    }
  };

  const categoryOptions = ['All', ...new Set((scenarios.data ?? []).map((s) => s.category).filter(Boolean))];

  const filteredScenarios = (scenarios.data ?? []).filter((s) => {
    if (categoryFilter === 'All') return true;
    return s.category === categoryFilter;
  });

  const handleGenerate = async () => {
    setGenerateError(null);
    setScript(null);
    setRelationships([]);
    setStep(2);
    abortRef.current = new AbortController();
    try {
      const result = await generateScript.mutateAsync({
        brief,
        actor_count: actorCount,
        simulation_mode: simulationMode,
        _signal: abortRef.current.signal,
      });
      if (!abortRef.current.signal.aborted) {
        setScript(result);
        setRelationships(generateInitialRelationships(result.stakeholders));
      }
    } catch (error) {
      if (!abortRef.current.signal.aborted) {
        setGenerateError(error instanceof Error ? error.message : 'Failed to generate stakeholders.');
      }
    } finally {
      abortRef.current = null;
    }
  };

  const handleBack = () => {
    if (generateScript.isPending && abortRef.current) {
      abortRef.current.abort();
      generateScript.reset();
    }
    const prevStep = (step > 1 ? (step - 1) as WizardStep : step);
    // Only clear script/relationships when going back to step 1 (brief input)
    if (prevStep === 1) {
      setScript(null);
      setRelationships([]);
      setGenerateError(null);
    }
    setStep(prevStep);
  };

  const handleActorUpdate = useCallback((index: number, updated: StakeholderActor) => {
    if (!script) return;
    const newStakeholders = [...script.stakeholders];
    newStakeholders[index] = updated;
    setScript({ ...script, stakeholders: newStakeholders });
  }, [script]);

  const handleLaunch = async () => {
    if (!script) return;
    // Inject outcomeSpec for guided mode + initial relationships
    const launchScript: Record<string, unknown> = {
      ...script,
      initial_relationships: relationships.map((r) => ({
        source: r.source,
        target: r.target,
        label: r.label,
      })),
    };
    if (simulationMode === 'guided' && outcomeSpec) {
      launchScript.outcome_spec = { desired_outcome: outcomeSpec };
    }
    const { simulation_id } = await startSimulation.mutateAsync({
      script: launchScript,
    });
    navigate(`/simulation/${simulation_id}`);
  };

  return (
    <div className="min-h-screen bg-bg-primary">
      {/* Header */}
      <header className="border-b border-border-subtle px-6 py-5">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <div>
            <h1 className="text-xl font-bold text-text-primary">UbeU Simulation Engine</h1>
            <p className="text-sm text-text-muted mt-0.5">Multi-stakeholder deliberation simulator</p>
          </div>
        </div>
      </header>

      <div className="max-w-6xl mx-auto px-6 py-8">
        {/* Step Indicator */}
        <div className="flex items-center justify-center mb-10">
          {STEP_LABELS.map((label, i) => (
            <div key={i} className="flex items-center">
              <div className="flex items-center gap-2.5">
                <div
                  className={`w-9 h-9 rounded-full flex items-center justify-center text-sm font-semibold transition-colors ${
                    step > i + 1 ? 'bg-accent-green text-white' :
                    step === i + 1 ? 'bg-accent-blue text-white' :
                    'bg-bg-elevated text-text-muted'
                  }`}
                >
                  {step > i + 1 ? <Check size={16} /> : i + 1}
                </div>
                <span className={`text-sm font-medium ${step === i + 1 ? 'text-text-primary' : 'text-text-muted'}`}>
                  {label}
                </span>
              </div>
              {i < STEP_LABELS.length - 1 && (
                <div className={`w-20 h-px mx-4 ${step > i + 1 ? 'bg-accent-green' : 'bg-border-subtle'}`} />
              )}
            </div>
          ))}
        </div>

        {/* Step Content */}
        <AnimatePresence mode="wait">
          {/* ── STEP 1: Scenario Brief ──────────────────────────── */}
          {step === 1 && (
            <motion.div
              key="step1"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="space-y-6"
            >
              {/* Scenario Picker (Demo) */}
              <div>
                <h2 className="text-base font-semibold text-text-secondary mb-3">Quick Start — Pre-built Scenarios</h2>

                {/* Category filter chips */}
                <div className="flex items-center gap-2 mb-4 flex-wrap">
                  {categoryOptions.map((cat) => {
                    const count = cat === 'All'
                      ? (scenarios.data?.length ?? 0)
                      : (scenarios.data ?? []).filter((s) => s.category === cat).length;
                    return (
                      <button
                        key={cat}
                        onClick={() => setCategoryFilter(cat)}
                        className={`px-3 py-1.5 text-sm rounded-full border transition-colors cursor-pointer font-medium ${
                          categoryFilter === cat
                            ? 'bg-accent-blue text-white border-accent-blue'
                            : 'bg-bg-elevated text-text-muted border-border-subtle hover:text-text-secondary hover:border-gray-300'
                        }`}
                      >
                        {cat}{cat === 'All' ? ` (${count})` : ''}
                      </button>
                    );
                  })}
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 max-h-[480px] overflow-y-auto pr-1">
                  {scenarios.isLoading && [1, 2, 3].map((i) => <ScenarioCardSkeleton key={i} />)}
                  {filteredScenarios.map((s) => (
                    <GlassCard
                      key={s.id}
                      hover
                      className={`p-5 cursor-pointer transition-all ${brief === s.brief ? 'ring-2 ring-accent-blue/50 bg-blue-50/50' : ''}`}
                      onClick={() => handleScenarioSelect(s)}
                    >
                      <div className="flex items-center gap-2 mb-1.5">
                        <div className="text-base font-semibold text-text-primary">{s.title}</div>
                      </div>
                      <div className="text-sm text-text-secondary line-clamp-2 mb-3">{s.brief}</div>
                      <div className="flex items-center gap-2 flex-wrap">
                        {s.tags?.map((t) => (
                          <Badge key={t} color="bg-gray-100 text-gray-500">{t}</Badge>
                        ))}
                      </div>
                    </GlassCard>
                  ))}
                </div>
              </div>

              {/* Custom Brief */}
              <GlassCard className="p-6">
                <h2 className="text-base font-semibold text-text-secondary mb-4">Or Write Your Own Brief</h2>
                <textarea
                  value={brief}
                  onChange={(e) => setBrief(e.target.value)}
                  placeholder="Describe the scenario you want to simulate. Include the key stakeholders, the decision at hand, and any tensions or competing interests..."
                  className="w-full h-36 bg-bg-elevated border border-border-subtle rounded-xl px-4 py-3 text-base text-text-primary placeholder:text-text-muted resize-none focus:outline-none focus:ring-2 focus:ring-accent-blue/40"
                />

                <div className="flex items-end gap-6 mt-5 flex-wrap">
                  {/* Actor count */}
                  <div>
                    <InfoLabel label="Actors" tooltip="Number of stakeholders to generate. More actors = richer debate, but longer simulation." className="text-sm text-text-muted block mb-1.5" />
                    <div className="flex gap-0.5 bg-bg-elevated rounded-lg p-0.5 border border-border-subtle">
                      {[2, 3, 4, 5, 6, 7, 8, 9, 10].map((n) => (
                        <button
                          key={n}
                          onClick={() => setActorCount(n)}
                          className={`w-9 py-2 text-sm rounded-md transition-colors cursor-pointer font-medium ${
                            actorCount === n ? 'bg-accent-blue text-white' : 'text-text-muted hover:text-text-secondary'
                          }`}
                        >
                          {n}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Mode toggle */}
                  <div>
                    <span className="text-sm text-text-muted block mb-1.5">Simulation Mode</span>
                    <div className="flex gap-0.5 bg-bg-elevated rounded-lg p-0.5 border border-border-subtle">
                      <Tooltip content="You define a target outcome. The engine steers the discussion toward it — best for training or 'what-if' scenarios.">
                        <button
                          onClick={() => setSimulationMode('guided')}
                          className={`px-4 py-2 text-sm rounded-md transition-colors cursor-pointer font-medium ${
                            simulationMode === 'guided' ? 'bg-accent-blue text-white' : 'text-text-muted hover:text-text-secondary'
                          }`}
                        >
                          Guided
                        </button>
                      </Tooltip>
                      <Tooltip content="No predetermined outcome. Actors debate freely and the result emerges organically — best for exploration and discovery.">
                        <button
                          onClick={() => setSimulationMode('exploratory')}
                          className={`px-4 py-2 text-sm rounded-md transition-colors cursor-pointer font-medium ${
                            simulationMode === 'exploratory' ? 'bg-accent-purple text-white' : 'text-text-muted hover:text-text-secondary'
                          }`}
                        >
                          Exploratory
                        </button>
                      </Tooltip>
                    </div>
                  </div>
                </div>

                {/* Outcome spec for guided mode */}
                <AnimatePresence>
                  {simulationMode === 'guided' && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: 'auto', opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.2 }}
                    >
                      <div className="mt-5 pt-4 border-t border-border-subtle">
                        <InfoLabel
                          label="Desired Outcome"
                          tooltip="Describe the outcome you want the simulation to converge toward. The engine will steer the discussion while keeping actor behavior authentic."
                          className="text-sm font-semibold text-text-secondary block mb-2"
                        />
                        <textarea
                          value={outcomeSpec}
                          onChange={(e) => setOutcomeSpec(e.target.value)}
                          placeholder="e.g., The committee reaches a compromise: a 6-month pilot program is approved with quarterly safety reviews..."
                          className="w-full h-24 bg-bg-elevated border border-border-subtle rounded-xl px-4 py-3 text-sm text-text-primary placeholder:text-text-muted resize-none focus:outline-none focus:ring-2 focus:ring-accent-blue/40"
                        />
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </GlassCard>
            </motion.div>
          )}

          {/* ── STEP 2: Actors & Config ─────────────────────────── */}
          {step === 2 && generateScript.isPending && (
            <motion.div
              key="step2-loading"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
            >
              <LoadingActors count={actorCount} />
            </motion.div>
          )}

          {step === 2 && !script && !generateScript.isPending && generateError && (
            <motion.div
              key="step2-error"
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
            >
              <GlassCard className="p-6 border border-red-200 bg-red-50/70">
                <h2 className="text-base font-semibold text-red-700 mb-2">Actor generation failed</h2>
                <p className="text-sm text-red-700/90">{generateError}</p>
                <p className="text-sm text-text-secondary mt-3">
                  모델이 유효하지 않은 JSON을 반환했거나 백엔드 생성 요청이 실패했습니다. 다시 시도하고, 반복되면 모델/프롬프트 설정을 확인하세요.
                </p>
              </GlassCard>
            </motion.div>
          )}

          {step === 2 && script && !generateScript.isPending && (
            <motion.div
              key="step2"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="space-y-4"
            >
              <div className="flex items-center justify-between">
                <h2 className="text-base font-semibold text-text-secondary">
                  {script.stakeholders.length} Stakeholders Generated
                </h2>
                {/* View toggle */}
                <div className="flex gap-0.5 bg-bg-elevated rounded-lg p-0.5 border border-border-subtle">
                  <button
                    onClick={() => setActorViewMode('network')}
                    className={`px-3 py-1.5 text-sm rounded-md transition-colors cursor-pointer ${
                      actorViewMode === 'network' ? 'bg-accent-blue text-white' : 'text-text-muted hover:text-text-secondary'
                    }`}
                  >
                    <Network size={14} className="inline mr-1" />Network
                  </button>
                  <button
                    onClick={() => setActorViewMode('cards')}
                    className={`px-3 py-1.5 text-sm rounded-md transition-colors cursor-pointer ${
                      actorViewMode === 'cards' ? 'bg-accent-blue text-white' : 'text-text-muted hover:text-text-secondary'
                    }`}
                  >
                    <LayoutGrid size={14} className="inline mr-1" />Cards
                  </button>
                </div>
              </div>

              <AnimatePresence mode="wait">
                {actorViewMode === 'network' ? (
                  <motion.div
                    key="network"
                    initial={{ opacity: 0, scale: 0.98 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.98 }}
                  >
                    <p className="text-sm text-text-secondary mb-3 font-medium">
                      Click a node to edit actor details. Click an edge to edit the relationship label or reconnect it. <span className="text-emerald-500">Green</span> = cooperative, <span className="text-red-500">Red</span> = conflict.
                    </p>
                    <ActorNetworkView
                      actors={script.stakeholders}
                      relationships={relationships}
                      onUpdateActor={handleActorUpdate}
                      onUpdateRelationships={setRelationships}
                    />
                  </motion.div>
                ) : (
                  <motion.div
                    key="cards"
                    initial={{ opacity: 0, scale: 0.98 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.98 }}
                  >
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                      {script.stakeholders.map((actor, i) => (
                        <ActorCard
                          key={actor.actor_id}
                          actor={actor}
                          color={ACTOR_COLORS[i % ACTOR_COLORS.length]}
                          index={i}
                          onUpdate={(updated) => handleActorUpdate(i, updated)}
                        />
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>

              {/* Advanced Settings */}
              <details className="group">
                <summary className="text-sm text-text-muted cursor-pointer hover:text-text-secondary font-medium">
                  <ChevronRight size={14} className="inline mr-1 group-open:rotate-90 transition-transform" />Advanced Settings
                </summary>
                <div className="mt-3 flex items-center gap-6 p-4 bg-bg-surface rounded-xl border border-border-subtle">
                  <div>
                    <InfoLabel label="Phases" tooltip="Number of discussion phases. Standard: OPENING → TENSION → NEGOTIATION → CLOSING. More phases give actors more room to evolve positions." className="text-sm text-text-muted block mb-1" />
                    <span className="text-base text-text-primary font-mono">{script.phases.length}</span>
                  </div>
                  <div>
                    <InfoLabel label="Total Turn Budget" tooltip="Maximum number of dialogue turns across all phases. More turns = deeper discussion but longer simulation time." className="text-sm text-text-muted block mb-1" />
                    <span className="text-base text-text-primary font-mono">
                      {script.phases.reduce((sum, p) => sum + p.max_turns, 0)} turns
                    </span>
                  </div>
                  <div>
                    <InfoLabel label="Phase Flow" tooltip="The sequence of discussion stages. OPENING: introductions. TENSION: conflicts surface. NEGOTIATION: trade-offs explored. CLOSING: resolution or stalemate." className="text-sm text-text-muted block mb-1" />
                    <span className="text-sm text-text-secondary">
                      {script.phases.map((p) => p.name).join(' → ')}
                    </span>
                  </div>
                </div>
              </details>
            </motion.div>
          )}

          {/* ── STEP 3: Review & Launch ─────────────────────────── */}
          {step === 3 && script && (
            <motion.div
              key="step3"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="space-y-5"
            >
              <GlassCard className="p-6">
                <h2 className="text-base font-semibold text-text-secondary mb-4">Simulation Summary</h2>
                <div className="space-y-3 text-base">
                  <div className="flex">
                    <span className="text-text-muted w-32 shrink-0">Title</span>
                    <span className="text-text-primary font-medium">{script.title}</span>
                  </div>
                  <div className="flex">
                    <span className="text-text-muted w-32 shrink-0">Objective</span>
                    <span className="text-text-secondary">{script.objective}</span>
                  </div>
                  <div className="flex items-center">
                    <span className="text-text-muted w-32 shrink-0">Mode</span>
                    <Badge color={simulationMode === 'guided' ? 'bg-accent-blue/15 text-accent-blue' : 'bg-accent-purple/15 text-accent-purple'}>
                      {simulationMode}
                    </Badge>
                  </div>
                  {simulationMode === 'guided' && outcomeSpec && (
                    <div className="flex">
                      <span className="text-text-muted w-32 shrink-0">Target Outcome</span>
                      <span className="text-accent-blue">{outcomeSpec}</span>
                    </div>
                  )}
                  <div className="flex">
                    <span className="text-text-muted w-32 shrink-0">Actors</span>
                    <span className="text-text-secondary">{script.stakeholders.length} stakeholders</span>
                  </div>
                  <div className="flex">
                    <span className="text-text-muted w-32 shrink-0">Phases</span>
                    <span className="text-text-secondary">
                      {script.phases.map((p) => p.name).join(' → ')}
                    </span>
                  </div>
                </div>
              </GlassCard>

              {/* Actor summary cards (readonly) */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                {script.stakeholders.map((actor, i) => (
                  <ActorCard
                    key={actor.actor_id}
                    actor={actor}
                    color={ACTOR_COLORS[i % ACTOR_COLORS.length]}
                    index={i}
                    readonly
                  />
                ))}
              </div>

              <div className="text-center text-sm text-text-muted">
                Estimated time: ~{Math.ceil(script.phases.reduce((s, p) => s + p.max_turns, 0) * 0.8)} minutes
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Navigation buttons */}
        <div className="flex justify-between mt-10 pt-5 border-t border-border-subtle">
          {step > 1 ? (
            <Button
              variant="ghost"
              size="lg"
              onClick={handleBack}
            >
              <ArrowLeft size={16} className="inline mr-1" /> Back
            </Button>
          ) : (
            <div />
          )}

          {step === 1 && (
            <Button
              size="lg"
              onClick={handleGenerate}
              disabled={!brief.trim() || generateScript.isPending}
            >
              {generateScript.isPending ? (
                <span className="flex items-center gap-2">
                  <Loader2 size={16} className="animate-spin" />
                  Generating...
                </span>
              ) : (
                <span className="flex items-center gap-1">Generate Stakeholders <ArrowRight size={16} /></span>
              )}
            </Button>
          )}

          {step === 2 && script && !generateScript.isPending && (
            <Button size="lg" onClick={() => setStep(3)}>
              <span className="flex items-center gap-1">Review & Launch <ArrowRight size={16} /></span>
            </Button>
          )}

          {step === 3 && (
            <Button
              onClick={handleLaunch}
              disabled={startSimulation.isPending}
              size="lg"
              className="bg-accent-green hover:bg-emerald-600"
            >
              {startSimulation.isPending ? (
                <span className="flex items-center gap-2">
                  <Loader2 size={16} className="animate-spin" />
                  Launching...
                </span>
              ) : (
                <span className="flex items-center gap-1"><Rocket size={16} /> Launch Simulation</span>
              )}
            </Button>
          )}
        </div>
      </div>
    </div>
  );
}
