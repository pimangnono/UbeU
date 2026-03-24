import { useEffect, useRef, useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import cytoscape from 'cytoscape';
import { ACTOR_COLORS } from '../../types/simulation';
import type { StakeholderActor, ActorRelationship } from '../../types/simulation';
import { ActorDetailPanel } from './ActorDetailPanel';

interface ActorNetworkViewProps {
  actors: StakeholderActor[];
  relationships: ActorRelationship[];
  onUpdateActor: (index: number, actor: StakeholderActor) => void;
  onUpdateRelationships: (relationships: ActorRelationship[]) => void;
}

export function ActorNetworkView({ actors, relationships, onUpdateActor, onUpdateRelationships }: ActorNetworkViewProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const cyRef = useRef<cytoscape.Core | null>(null);
  const [selectedIdx, setSelectedIdx] = useState<number | null>(null);
  const [editingEdge, setEditingEdge] = useState<ActorRelationship | null>(null);
  const [edgeLabelDraft, setEdgeLabelDraft] = useState('');
  const [edgeSourceDraft, setEdgeSourceDraft] = useState('');
  const [edgeTargetDraft, setEdgeTargetDraft] = useState('');

  const selectedActor = selectedIdx !== null ? actors[selectedIdx] : null;

  // Highlight edges connected to selected node, dim the rest
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;

    // Reset all
    cy.elements().removeClass('dimmed highlighted');

    if (selectedIdx !== null) {
      const actorId = actors[selectedIdx]?.actor_id;
      if (actorId) {
        const node = cy.getElementById(actorId);
        const connectedEdges = node.connectedEdges();
        const connectedNodes = connectedEdges.connectedNodes();

        // Dim everything first
        cy.edges().addClass('dimmed');
        cy.nodes().addClass('dimmed');

        // Highlight connected edges + nodes
        connectedEdges.removeClass('dimmed').addClass('highlighted');
        connectedNodes.removeClass('dimmed');
        node.removeClass('dimmed');

        node.select();
      }
    }

    if (editingEdge) {
      cy.getElementById(editingEdge.id).select();
    }
  }, [selectedIdx, editingEdge, actors]);

  useEffect(() => {
    if (!containerRef.current) return;

    const nodes = actors.map((actor, i) => ({
      data: {
        id: actor.actor_id,
        label: actor.role,
        color: ACTOR_COLORS[i % ACTOR_COLORS.length],
        index: i,
      },
    }));

    const edges = relationships.map((rel) => {
      const srcIdx = actors.findIndex((a) => a.actor_id === rel.source);
      const tgtIdx = actors.findIndex((a) => a.actor_id === rel.target);
      const srcDisp = actors[srcIdx]?.strategic_disposition;
      const tgtDisp = actors[tgtIdx]?.strategic_disposition;
      const srcAgg = srcDisp === 'cooperative' || srcDisp === 'neutral';
      const tgtAgg = tgtDisp === 'cooperative' || tgtDisp === 'neutral';
      const isConflict = !srcAgg || !tgtAgg;

      return {
        data: {
          id: rel.id,
          source: rel.source,
          target: rel.target,
          label: rel.label,
          color: isConflict ? '#ef4444' : '#10b981',
          relId: rel.id,
        },
      };
    });

    if (cyRef.current) {
      cyRef.current.destroy();
    }

    const cy = cytoscape({
      container: containerRef.current,
      elements: [...nodes, ...edges],
      style: [
        {
          selector: 'node',
          style: {
            'background-color': 'data(color)',
            'label': 'data(label)',
            'color': '#374151',
            'font-size': '11px',
            'text-valign': 'bottom',
            'text-margin-y': 8,
            'width': 26,
            'height': 26,
            'border-width': 2,
            'border-color': '#ffffff',
            'text-outline-color': '#ffffff',
            'text-outline-width': 2,
            'font-weight': 600,
            'text-wrap': 'wrap' as any,
            'text-max-width': '100px',
          },
        },
        {
          selector: 'node:selected',
          style: {
            'border-color': '#3b82f6',
            'border-width': 3,
            'width': 32,
            'height': 32,
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
            'width': 1.5,
            'line-color': 'data(color)',
            'line-style': 'dashed' as any,
            'curve-style': 'bezier',
            'opacity': 0.7,
            'label': 'data(label)',
            'font-size': '12px',
            'text-rotation': 'autorotate' as any,
            'text-margin-y': -8,
            'color': '#6b7280',
            'text-outline-color': '#ffffff',
            'text-outline-width': 1.5,
            'text-wrap': 'wrap' as any,
            'text-max-width': '120px',
          },
        },
        {
          selector: 'edge:selected',
          style: {
            'width': 2.5,
            'opacity': 1,
            'line-style': 'solid' as any,
          },
        },
        {
          selector: 'edge.dimmed',
          style: {
            'line-color': '#d1d5db',
            'opacity': 0.25,
            'color': 'transparent' as any,
          },
        },
        {
          selector: 'edge.highlighted',
          style: {
            'width': 2.5,
            'opacity': 1,
            'line-style': 'solid' as any,
            'font-size': '18px',
            'font-weight': 700,
            'color': '#111827',
            'text-outline-width': 2.5,
            'text-max-width': '160px',
          },
        },
      ],
      layout: {
        name: 'circle',
        animate: true,
        animationDuration: 600,
        padding: 60,
      },
    });

    cy.on('tap', 'node', (evt) => {
      const idx = evt.target.data('index') as number;
      setSelectedIdx(idx);
      setEditingEdge(null);
    });

    cy.on('tap', 'edge', (evt) => {
      const relId = evt.target.data('relId') as string;
      const rel = relationships.find((r) => r.id === relId);
      if (rel) {
        setEditingEdge(rel);
        setEdgeLabelDraft(rel.label);
        setEdgeSourceDraft(rel.source);
        setEdgeTargetDraft(rel.target);
        setSelectedIdx(null);
      }
    });

    cy.on('tap', (evt) => {
      if (evt.target === cy) {
        setSelectedIdx(null);
        setEditingEdge(null);
      }
    });

    cyRef.current = cy;

    return () => {
      cy.destroy();
    };
  }, [actors, relationships]);

  const saveEdgeEdit = () => {
    if (!editingEdge) return;
    const updated = relationships.map((r) =>
      r.id === editingEdge.id
        ? { ...r, label: edgeLabelDraft, source: edgeSourceDraft, target: edgeTargetDraft }
        : r
    );
    onUpdateRelationships(updated);
    setEditingEdge(null);
  };

  const deleteEdge = () => {
    if (!editingEdge) return;
    onUpdateRelationships(relationships.filter((r) => r.id !== editingEdge.id));
    setEditingEdge(null);
  };

  const addEdge = () => {
    if (actors.length < 2) return;
    const newRel: ActorRelationship = {
      id: `rel-${Date.now()}`,
      source: actors[0].actor_id,
      target: actors[1].actor_id,
      label: 'new relationship',
    };
    onUpdateRelationships([...relationships, newRel]);
  };

  return (
    <div className="space-y-4">
      {/* Network graph */}
      <div className="relative rounded-xl border border-gray-200 bg-gray-50/50">
        <div
          ref={containerRef}
          className="w-full h-[600px]"
        />

        {/* Add relationship button */}
        {!selectedActor && !editingEdge && actors.length >= 2 && (
          <div className="absolute bottom-3 right-3">
            <button
              onClick={addEdge}
              className="bg-white border border-gray-200 text-gray-600 text-xs px-3 py-1.5 rounded-lg hover:bg-gray-50 cursor-pointer shadow-sm font-medium"
            >
              + Add Relationship
            </button>
          </div>
        )}
      </div>

      {/* Detail panels — outside the network container */}
      <AnimatePresence mode="wait">
        {selectedActor && selectedIdx !== null && (
          <motion.div
            key="actor-panel"
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 16 }}
          >
            <ActorDetailPanel
              actor={selectedActor}
              color={ACTOR_COLORS[selectedIdx % ACTOR_COLORS.length]}
              onUpdate={(updated) => onUpdateActor(selectedIdx, updated)}
              onClose={() => setSelectedIdx(null)}
            />
          </motion.div>
        )}
        {editingEdge && (
          <motion.div
            key="edge-panel"
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 16 }}
            className="bg-white rounded-xl border border-gray-200 shadow-sm"
          >
            <div className="p-6 space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="font-semibold text-gray-900">Edit Relationship</h3>
                <button
                  onClick={() => setEditingEdge(null)}
                  className="text-gray-400 hover:text-gray-600 text-xl cursor-pointer p-1"
                >
                  ×
                </button>
              </div>

              <div className="grid grid-cols-3 gap-4">
                {/* Source */}
                <div>
                  <label className="text-xs text-gray-500 block mb-1">From</label>
                  <select
                    value={edgeSourceDraft}
                    onChange={(e) => setEdgeSourceDraft(e.target.value)}
                    className="w-full bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm text-gray-800"
                  >
                    {actors.map((a) => (
                      <option key={a.actor_id} value={a.actor_id} disabled={a.actor_id === edgeTargetDraft}>
                        {a.role}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Target */}
                <div>
                  <label className="text-xs text-gray-500 block mb-1">To</label>
                  <select
                    value={edgeTargetDraft}
                    onChange={(e) => setEdgeTargetDraft(e.target.value)}
                    className="w-full bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm text-gray-800"
                  >
                    {actors.map((a) => (
                      <option key={a.actor_id} value={a.actor_id} disabled={a.actor_id === edgeSourceDraft}>
                        {a.role}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Label */}
                <div>
                  <label className="text-xs text-gray-500 block mb-1">Relationship</label>
                  <input
                    type="text"
                    value={edgeLabelDraft}
                    onChange={(e) => setEdgeLabelDraft(e.target.value)}
                    className="w-full bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500/30"
                    placeholder="e.g., competing for budget"
                  />
                </div>
              </div>

              <div className="flex gap-2 pt-1">
                <button
                  onClick={saveEdgeEdit}
                  className="bg-blue-500 text-white text-sm px-4 py-1.5 rounded-lg hover:bg-blue-600 cursor-pointer font-medium"
                >
                  Save
                </button>
                <button
                  onClick={deleteEdge}
                  className="bg-red-50 text-red-500 text-sm px-4 py-1.5 rounded-lg hover:bg-red-100 cursor-pointer font-medium"
                >
                  Delete
                </button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
