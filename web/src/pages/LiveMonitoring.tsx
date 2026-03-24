import { useEffect, useRef, useState, useMemo, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ArrowRight, HeartHandshake, Scale, Swords, ShieldAlert, Loader2 } from 'lucide-react';
import cytoscape from 'cytoscape';
import { useSimulationWS } from '../hooks/useSimulationWS';
import { ChatBubble } from '../components/transcript/ChatBubble';
import { PhaseDivider } from '../components/transcript/PhaseDivider';
import { ACTOR_COLORS, DISPOSITION_CONFIG } from '../types/simulation';
import type { Disposition, RelationshipEvent } from '../types/simulation';

const DISPOSITION_ICONS: Record<string, React.ReactNode> = {
  'heart-handshake': <HeartHandshake size={10} />,
  'scale': <Scale size={10} />,
  'swords': <Swords size={10} />,
  'shield-alert': <ShieldAlert size={10} />,
};

const SENTIMENT_LABELS: Record<string, string> = {
  positive: 'supporting',
  negative: 'tension builds',
  challenging: 'pushback',
  neutral: 'engaging',
};

export default function LiveMonitoring() {
  const { id: simulationId } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const ws = useSimulationWS(simulationId);
  const transcriptRef = useRef<HTMLDivElement>(null);
  const graphRef = useRef<HTMLDivElement>(null);
  const cyRef = useRef<cytoscape.Core | null>(null);
  const [pinToBottom, setPinToBottom] = useState(true);

  // Build actor color/index map from actors_init
  const actorIds = useMemo(() => ws.actors.map((a) => a.actor_id), [ws.actors]);

  // Phase progress
  const phases = useMemo(() => {
    const seen: string[] = [];
    for (const turn of ws.turns) {
      if (seen.length === 0 || seen[seen.length - 1] !== turn.phase) {
        seen.push(turn.phase);
      }
    }
    return seen;
  }, [ws.turns]);

  // Current speaker + last spoken content for edge label
  const lastTurn = ws.turns.length > 0 ? ws.turns[ws.turns.length - 1] : null;
  const activeSpeaker = lastTurn?.actor_id ?? null;

  // Detect who the speaker is addressing (mentioned actor names/roles in content)
  const addressedActors = useMemo(() => {
    if (!lastTurn) return [] as string[];
    const content = lastTurn.content.toLowerCase();
    return ws.actors
      .filter((a) => a.actor_id !== lastTurn.actor_id)
      .filter((a) => {
        const role = a.role.toLowerCase();
        const name = a.display_name.toLowerCase();
        return content.includes(role) || content.includes(name);
      })
      .map((a) => a.actor_id);
  }, [lastTurn, ws.actors]);

  // Get edge label from latest relationship event for this speaker
  const getEdgeLabel = useCallback((speakerId: string, targetId: string): string => {
    // Find the most recent relationship event between these actors
    for (let i = ws.relationships.length - 1; i >= 0; i--) {
      const rel = ws.relationships[i];
      if ((rel.source === speakerId && rel.target === targetId) ||
          (rel.source === targetId && rel.target === speakerId)) {
        return SENTIMENT_LABELS[rel.sentiment] || 'engaging';
      }
    }
    return 'engaging';
  }, [ws.relationships]);

  // Auto-scroll transcript
  useEffect(() => {
    if (pinToBottom && transcriptRef.current) {
      transcriptRef.current.scrollTop = transcriptRef.current.scrollHeight;
    }
  }, [ws.turns, pinToBottom]);

  // ── Cytoscape network graph ──────────────────────────────
  useEffect(() => {
    if (!graphRef.current || ws.actors.length === 0) return;

    // Build edges: fully connected mesh (dimmed by default)
    const nodes = ws.actors.map((actor, i) => ({
      data: {
        id: actor.actor_id,
        label: actor.role,
        color: ACTOR_COLORS[i % ACTOR_COLORS.length],
        disposition: actor.disposition,
      },
    }));

    const edges: { data: { id: string; source: string; target: string; label: string } }[] = [];
    for (let i = 0; i < ws.actors.length; i++) {
      for (let j = i + 1; j < ws.actors.length; j++) {
        edges.push({
          data: {
            id: `e-${ws.actors[i].actor_id}-${ws.actors[j].actor_id}`,
            source: ws.actors[i].actor_id,
            target: ws.actors[j].actor_id,
            label: '',
          },
        });
      }
    }

    if (cyRef.current) cyRef.current.destroy();

    const cy = cytoscape({
      container: graphRef.current,
      elements: [...nodes, ...edges],
      style: [
        {
          selector: 'node',
          style: {
            'background-color': 'data(color)',
            'label': 'data(label)',
            'color': '#374151',
            'font-size': '13px',
            'text-valign': 'bottom',
            'text-margin-y': 10,
            'width': 30,
            'height': 30,
            'border-width': 2,
            'border-color': '#ffffff',
            'text-outline-color': '#ffffff',
            'text-outline-width': 2,
            'font-weight': 600,
            'text-wrap': 'wrap' as any,
            'text-max-width': '120px',
          },
        },
        {
          selector: 'node.speaking',
          style: {
            'border-color': '#3b82f6',
            'border-width': 4,
            'width': 40,
            'height': 40,
          },
        },
        {
          selector: 'node.dimmed',
          style: {
            'opacity': 0.3,
          },
        },
        {
          selector: 'edge',
          style: {
            'width': 1,
            'line-color': '#e5e7eb',
            'curve-style': 'bezier',
            'opacity': 0.2,
          },
        },
        {
          selector: 'edge.active',
          style: {
            'width': 3,
            'line-color': '#3b82f6',
            'opacity': 1,
            'line-style': 'solid' as any,
            'label': 'data(label)',
            'font-size': '11px',
            'color': '#1f2937',
            'text-outline-color': '#ffffff',
            'text-outline-width': 2,
            'text-rotation': 'autorotate' as any,
            'text-margin-y': -10,
            'font-weight': 600,
            'text-wrap': 'wrap' as any,
            'text-max-width': '180px',
          },
        },
      ],
      layout: {
        name: 'circle',
        animate: false,
        padding: 60,
      },
      userZoomingEnabled: false,
      userPanningEnabled: false,
      boxSelectionEnabled: false,
    });

    cyRef.current = cy;

    return () => {
      cy.destroy();
      cyRef.current = null;
    };
  }, [ws.actors]);

  // Update graph highlighting when speaker changes
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy || !activeSpeaker) return;

    // Reset all
    cy.elements().removeClass('speaking dimmed active');
    cy.edges().data('label', '');

    // Dim all nodes, highlight speaker
    cy.nodes().addClass('dimmed');
    const speakerNode = cy.getElementById(activeSpeaker);
    speakerNode.removeClass('dimmed').addClass('speaking');

    // Highlight edges to addressed actors
    const targets = addressedActors.length > 0
      ? addressedActors
      : actorIds.filter((id) => id !== activeSpeaker); // if none detected, highlight all

    for (const targetId of targets) {
      const targetNode = cy.getElementById(targetId);
      targetNode.removeClass('dimmed');

      // Find connecting edge
      const edge = cy.edges().filter((e) => {
        const s = e.source().id();
        const t = e.target().id();
        return (s === activeSpeaker && t === targetId) || (s === targetId && t === activeSpeaker);
      });
      if (edge.length > 0) {
        edge.addClass('active');
        edge.data('label', getEdgeLabel(activeSpeaker, targetId));
      }
    }
  }, [activeSpeaker, addressedActors, actorIds, getEdgeLabel]);

  return (
    <div className="h-screen flex flex-col bg-bg-primary">
      {/* Phase Progress Bar */}
      <div className="border-b border-border-subtle px-4 py-2 flex items-center gap-2 text-xs shrink-0">
        {phases.length > 0 ? (
          phases.map((phase, i) => (
            <div key={i} className="flex items-center gap-1">
              {i > 0 && <ArrowRight size={12} className="text-text-muted mx-1" />}
              <span
                className={`px-2 py-0.5 rounded ${
                  phase === ws.currentPhase
                    ? 'bg-accent-blue/20 text-accent-blue font-semibold'
                    : i < phases.indexOf(ws.currentPhase)
                    ? 'bg-accent-green/20 text-accent-green'
                    : 'bg-bg-elevated text-text-muted'
                }`}
              >
                {phase}
              </span>
            </div>
          ))
        ) : (
          <span className="text-text-muted">Waiting for simulation to start...</span>
        )}
        <div className="flex-1" />
        <span className="text-text-muted">Turn {ws.turns.length}</span>
      </div>

      {/* Main 3-panel layout */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left Rail: All Actors (always visible) */}
        <div className="w-52 border-r border-border-subtle shrink-0 flex flex-col">
          <div className="p-2 border-b border-border-subtle">
            <span className="text-xs font-semibold text-text-muted">Stakeholders</span>
          </div>
          <div className="flex-1 overflow-y-auto p-2 space-y-1.5">
            {ws.actors.map((actor, i) => {
              const color = ACTOR_COLORS[i % ACTOR_COLORS.length];
              const isSpeaking = actor.actor_id === activeSpeaker;
              const dispConfig = DISPOSITION_CONFIG[actor.disposition as Disposition] || DISPOSITION_CONFIG.neutral;
              const turnCount = ws.turns.filter((t) => t.actor_id === actor.actor_id).length;

              return (
                <div
                  key={actor.actor_id}
                  className={`flex items-center gap-2.5 p-2 rounded-lg transition-all ${
                    isSpeaking ? 'bg-blue-50 ring-1 ring-blue-200' : 'bg-white'
                  }`}
                >
                  <div className="relative shrink-0">
                    <div
                      className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold text-white"
                      style={{ backgroundColor: color }}
                    >
                      {actor.role[0]}
                    </div>
                    {isSpeaking && (
                      <span className="absolute -bottom-0.5 -right-0.5 w-3 h-3 bg-green-500 rounded-full border-2 border-white" />
                    )}
                  </div>
                  <div className="min-w-0 flex-1">
                    <div className="text-xs font-semibold text-gray-800 truncate">{actor.role}</div>
                    <div className="flex items-center gap-1.5 mt-0.5">
                      <span className={`text-[10px] ${dispConfig.color}`}>
                        {DISPOSITION_ICONS[dispConfig.lucide] || <Scale size={10} />}
                      </span>
                      <span className="text-[10px] text-text-muted">
                        {turnCount > 0 ? `${turnCount} turns` : 'waiting'}
                      </span>
                    </div>
                  </div>
                </div>
              );
            })}

            {ws.actors.length === 0 && (
              <div className="text-xs text-text-muted py-4 text-center">
                Loading actors...
              </div>
            )}
          </div>
        </div>

        {/* Center: Dynamic Network Graph */}
        <div className="flex-1 flex flex-col min-w-0">
          <div className="px-3 py-1.5 border-b border-border-subtle text-xs text-text-muted font-semibold">
            Live Network
          </div>
          <div className="flex-1 relative">
            <div ref={graphRef} className="w-full h-full" />
            {ws.actors.length === 0 && (
              <div className="absolute inset-0 flex items-center justify-center text-text-muted text-sm">
                <div className="flex items-center gap-3">
                  <Loader2 size={20} className="text-accent-blue animate-spin" />
                  Waiting for simulation...
                </div>
              </div>
            )}
            {/* Current speaker badge */}
            {lastTurn && (
              <motion.div
                key={lastTurn.turn_index}
                initial={{ opacity: 0, y: 8 }}
                animate={{ opacity: 1, y: 0 }}
                className="absolute bottom-3 left-3 right-3 bg-white/90 backdrop-blur rounded-lg border border-gray-200 px-3 py-2 text-xs shadow-sm"
              >
                <span className="font-semibold text-gray-800">
                  {ws.actors.find((a) => a.actor_id === lastTurn.actor_id)?.role || lastTurn.display_name}
                </span>
                <span className="text-gray-500 ml-1.5">
                  {lastTurn.content.split(/[.!?]/)[0].trim().slice(0, 60)}{lastTurn.content.split(/[.!?]/)[0].trim().length > 60 ? '...' : ''}
                </span>
              </motion.div>
            )}
          </div>
        </div>

        {/* Right: Live Transcript */}
        <div className="w-[380px] border-l border-border-subtle shrink-0 flex flex-col">
          <div className="flex items-center justify-between px-3 py-1.5 border-b border-border-subtle text-xs">
            <span className="text-text-muted font-semibold">Live Transcript</span>
            <label className="flex items-center gap-1.5 text-text-muted cursor-pointer">
              <input
                type="checkbox"
                checked={pinToBottom}
                onChange={(e) => setPinToBottom(e.target.checked)}
                className="rounded"
              />
              Auto-scroll
            </label>
          </div>
          <div ref={transcriptRef} className="flex-1 overflow-y-auto px-2 py-3 space-y-1">
            {ws.turns.length === 0 && !ws.isComplete && (
              <div className="flex items-center justify-center h-full text-text-muted text-sm">
                <div className="flex items-center gap-3">
                  <Loader2 size={20} className="text-accent-blue animate-spin" />
                  Waiting for dialogue...
                </div>
              </div>
            )}
            {ws.turns.map((turn, i) => {
              const prevPhase = i > 0 ? ws.turns[i - 1].phase : '';
              const showDivider = turn.phase !== prevPhase;
              const colorIndex = actorIds.indexOf(turn.actor_id);
              const actor = ws.actors.find((a) => a.actor_id === turn.actor_id);
              const roleLabel = actor?.role || turn.display_name;

              return (
                <div key={i}>
                  {showDivider && <PhaseDivider phaseName={turn.phase} />}
                  <ChatBubble
                    actorId={turn.actor_id}
                    displayName={roleLabel}
                    content={turn.content}
                    turnIndex={turn.turn_index}
                    colorIndex={colorIndex}
                    highlighted={false}
                    dimmed={false}
                  />
                </div>
              );
            })}

            {ws.isComplete && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="flex flex-col items-center justify-center py-6 gap-3"
              >
                <span className="text-sm text-accent-green font-medium">Simulation complete</span>
                <button
                  onClick={() => navigate(`/simulation/${simulationId}/results`)}
                  className="bg-accent-blue text-white text-sm px-5 py-2 rounded-lg hover:bg-blue-600 cursor-pointer font-medium"
                >
                  View Results
                </button>
              </motion.div>
            )}

            {ws.error && (
              <div className="text-sm text-accent-red text-center py-4">
                {ws.error}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Status Bar */}
      <div className="border-t border-border-subtle px-4 py-1.5 flex items-center gap-4 text-xs text-text-muted shrink-0">
        <span className="flex items-center gap-1.5">
          <span className={`w-2 h-2 rounded-full ${ws.connected ? 'bg-accent-green' : 'bg-accent-red'}`} />
          {ws.connected ? 'Connected' : 'Disconnected'}
        </span>
        <span>Phase: {ws.currentPhase || '—'}</span>
        <span>Turn {ws.turns.length}</span>
        {ws.error && <span className="text-accent-red ml-auto">{ws.error}</span>}
      </div>
    </div>
  );
}
