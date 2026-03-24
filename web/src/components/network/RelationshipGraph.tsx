import { useEffect, useRef, useMemo } from 'react';
import cytoscape from 'cytoscape';
import { ACTOR_COLORS, type RelationshipRecord } from '../../types/simulation';
import type { StakeholderActor } from '../../types/simulation';
import { useSelectionStore } from '../../stores/selectionStore';

interface RelationshipGraphProps {
  actors: StakeholderActor[];
  events: RelationshipRecord[];
  phaseFilter?: string | null;
  phaseOrder?: string[];
}

export function RelationshipGraph({ actors, events, phaseFilter, phaseOrder = [] }: RelationshipGraphProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const cyRef = useRef<cytoscape.Core | null>(null);
  const { setRelationship, setActor } = useSelectionStore();

  // Cumulative filter: show all events up to and including the selected phase
  const filteredEvents = useMemo(() => {
    if (!phaseFilter) return events;
    // Build a set of phases up to and including the selected one
    const norm = (s: string) => s.trim().toLowerCase();
    const idx = phaseOrder.findIndex((p) => norm(p) === norm(phaseFilter));
    if (idx === -1) {
      // Fallback: exact (case-insensitive) match on this single phase
      return events.filter((e) => norm(e.phase_name) === norm(phaseFilter));
    }
    const allowedPhases = new Set(phaseOrder.slice(0, idx + 1).map(norm));
    return events.filter((e) => allowedPhases.has(norm(e.phase_name)));
  }, [events, phaseFilter, phaseOrder]);

  // Aggregate relationships
  const edges = useMemo(() => {
    const map = new Map<string, { trust: number; tension: number; count: number; evidence: string[] }>();
    for (const evt of filteredEvents) {
      const src = evt.source_actor_id || evt.source || '';
      const tgt = evt.target_actor_id || evt.target || '';
      const key = `${src}→${tgt}`;
      const existing = map.get(key) || { trust: 0, tension: 0, count: 0, evidence: [] };
      existing.trust += evt.trust_delta;
      existing.tension += evt.tension_delta;
      existing.count++;
      if (evt.evidence) existing.evidence.push(evt.evidence.slice(0, 60));
      map.set(key, existing);
    }
    return Array.from(map.entries()).map(([key, val]) => {
      const [source, target] = key.split('→');
      const label = val.trust >= 0
        ? `trust +${val.trust.toFixed(2)}`
        : `trust ${val.trust.toFixed(2)}`;
      return { source, target, label, ...val };
    });
  }, [filteredEvents]);

  useEffect(() => {
    if (!containerRef.current) return;

    const nodes = actors.map((actor, i) => ({
      data: {
        id: actor.actor_id,
        label: actor.role,
        color: ACTOR_COLORS[i % ACTOR_COLORS.length],
      },
    }));

    const cyEdges = edges.map((edge) => ({
      data: {
        id: `${edge.source}-${edge.target}`,
        source: edge.source,
        target: edge.target,
        trust: 0.5 + edge.trust,
        tension: edge.tension,
        width: Math.max(1, Math.min(6, Math.abs(edge.trust) * 20 + 1)),
        color: edge.trust >= 0 ? '#10b981' : '#ef4444',
        label: edge.label,
      },
    }));

    if (cyRef.current) {
      cyRef.current.destroy();
    }

    const cy = cytoscape({
      container: containerRef.current,
      elements: [...nodes, ...cyEdges],
      style: [
        {
          selector: 'node',
          style: {
            'background-color': 'data(color)',
            'label': 'data(label)',
            'color': '#374151',
            'font-size': '10px',
            'text-valign': 'bottom',
            'text-margin-y': 6,
            'width': 22,
            'height': 22,
            'border-width': 2,
            'border-color': '#ffffff',
            'text-outline-color': '#ffffff',
            'text-outline-width': 2,
            'font-weight': 600,
            'text-wrap': 'wrap' as any,
            'text-max-width': '90px',
          },
        },
        {
          selector: 'edge',
          style: {
            'width': 'data(width)',
            'line-color': 'data(color)',
            'target-arrow-color': 'data(color)',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'opacity': 0.7,
            'label': 'data(label)',
            'font-size': '8px',
            'text-rotation': 'autorotate' as any,
            'text-margin-y': -8,
            'color': '#6b7280',
            'text-outline-color': '#ffffff',
            'text-outline-width': 1.5,
            'text-wrap': 'wrap' as any,
            'text-max-width': '80px',
          },
        },
      ],
      layout: {
        name: 'circle',
        animate: true,
        animationDuration: 500,
        padding: 60,
      },
    });

    cy.on('tap', 'node', (evt) => {
      setActor(evt.target.id());
    });

    cy.on('tap', 'edge', (evt) => {
      const edge = evt.target;
      setRelationship([edge.data('source'), edge.data('target')]);
    });

    cyRef.current = cy;

    return () => {
      cy.destroy();
    };
  }, [actors, edges, setRelationship, setActor]);

  return (
    <div
      ref={containerRef}
      className="w-full h-80 bg-gray-50/50 rounded-lg border border-gray-200"
    />
  );
}
