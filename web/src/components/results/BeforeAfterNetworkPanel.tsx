import { useEffect, useMemo, useRef } from 'react';
import cytoscape from 'cytoscape';
import { ACTOR_COLORS, type FinalRelationshipSummary, type InitialRelationshipSummary, type StakeholderActor } from '../../types/simulation';

type RelationshipSummary = InitialRelationshipSummary | FinalRelationshipSummary;

interface BeforeAfterNetworkPanelProps {
  title: string;
  actors: StakeholderActor[];
  relationships: RelationshipSummary[];
  highlightedActorIds?: string[];
  highlightedRelationshipId?: string | null;
  changedOnly?: boolean;
  phaseLabel?: string | null;
  onSelectActor?: (actorId: string) => void;
  onSelectRelationship?: (relationshipId: string, sourceActorId: string, targetActorId: string) => void;
}

function relationshipVisuals(relationship: RelationshipSummary) {
  if ('final_trust' in relationship) {
    return {
      trust: relationship.final_trust,
      tension: relationship.final_tension,
      label: `${relationship.final_trust.toFixed(2)} trust`,
      width: Math.max(1.5, Math.abs(relationship.total_trust_delta) * 18 + 1.5),
    };
  }
  return {
    trust: relationship.trust,
    tension: relationship.tension,
    label: `${relationship.trust.toFixed(2)} trust`,
    width: Math.max(1.5, Math.abs(relationship.trust - 0.5) * 12 + 1.5),
  };
}

export function BeforeAfterNetworkPanel({
  title,
  actors,
  relationships,
  highlightedActorIds = [],
  highlightedRelationshipId = null,
  changedOnly = false,
  phaseLabel = null,
  onSelectActor,
  onSelectRelationship,
}: BeforeAfterNetworkPanelProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const cyRef = useRef<cytoscape.Core | null>(null);

  const relationshipMap = useMemo(() => {
    return relationships.filter((relationship) => {
      if (!changedOnly) return true;
      if ('event_count' in relationship) {
        return relationship.event_count > 0 || Math.abs(relationship.total_trust_delta) > 0.001 || Math.abs(relationship.total_tension_delta) > 0.001;
      }
      return relationship.label !== 'neutral' || relationship.trust !== 0.5 || relationship.tension !== 0;
    });
  }, [relationships, changedOnly]);
  const changedCount = useMemo(() => {
    return relationships.filter((relationship) => {
      if ('event_count' in relationship) {
        return relationship.event_count > 0 || Math.abs(relationship.total_trust_delta) > 0.001 || Math.abs(relationship.total_tension_delta) > 0.001;
      }
      return relationship.label !== 'neutral' || relationship.trust !== 0.5 || relationship.tension !== 0;
    }).length;
  }, [relationships]);

  useEffect(() => {
    if (!containerRef.current) return;

    const nodes = actors.map((actor, index) => ({
      data: {
        id: actor.actor_id,
        label: actor.role,
        color: ACTOR_COLORS[index % ACTOR_COLORS.length],
        highlighted: highlightedActorIds.includes(actor.actor_id),
      },
    }));

    const edges = relationshipMap.map((relationship) => {
      const visuals = relationshipVisuals(relationship);
      const positive = visuals.trust >= 0.5;
      const highlighted = highlightedRelationshipId === relationship.relationship_id;
      const unchanged = 'event_count' in relationship
        ? relationship.event_count === 0 && Math.abs(relationship.total_trust_delta) < 0.001 && Math.abs(relationship.total_tension_delta) < 0.001
        : relationship.label === 'neutral' && relationship.trust === 0.5 && relationship.tension === 0;
      return {
        data: {
          id: relationship.relationship_id,
          source: relationship.source_actor_id,
          target: relationship.target_actor_id,
          label: visuals.label,
          width: unchanged ? 1 : visuals.width,
          color: unchanged ? '#cbd5e1' : positive ? '#10b981' : '#ef4444',
          opacity: highlighted ? 0.95 : unchanged ? 0.16 : 0.6,
        },
      };
    });

    cyRef.current?.destroy();
    const cy = cytoscape({
      container: containerRef.current,
      elements: [...nodes, ...edges],
      style: [
        {
          selector: 'node',
          style: {
            'background-color': 'data(color)',
            'width': 24,
            'height': 24,
            'label': 'data(label)',
            'text-valign': 'bottom',
            'text-margin-y': 7,
            'font-size': '10px',
            'font-weight': 600,
            'text-wrap': 'wrap' as any,
            'text-max-width': '95px',
            'border-width': 'mapData(highlighted, 0, 1, 2, 4)' as any,
            'border-color': '#ffffff',
            'text-outline-color': '#ffffff',
            'text-outline-width': 2,
            'opacity': 'mapData(highlighted, 0, 1, 0.6, 1)' as any,
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
            'opacity': 'data(opacity)' as any,
            'label': 'data(label)',
            'font-size': '8px',
            'text-rotation': 'autorotate' as any,
            'text-margin-y': -8,
            'color': '#6b7280',
            'text-outline-color': '#ffffff',
            'text-outline-width': 1.5,
          },
        },
      ],
      layout: {
        name: 'circle',
        animate: true,
        animationDuration: 400,
        padding: 50,
      },
    });

    cy.on('tap', 'node', (evt) => onSelectActor?.(evt.target.id()));
    cy.on('tap', 'edge', (evt) => onSelectRelationship?.(evt.target.id(), evt.target.data('source'), evt.target.data('target')));
    cyRef.current = cy;
    return () => cy.destroy();
  }, [actors, relationshipMap, highlightedActorIds, highlightedRelationshipId, onSelectActor, onSelectRelationship]);

  return (
    <div className="rounded-2xl border border-border-subtle bg-bg-surface/70 p-4">
      <div className="flex items-start justify-between gap-3 mb-3">
        <div>
          <div className="text-sm font-semibold text-text-primary">{title}</div>
          <div className="text-xs text-text-muted mt-1">
            {changedCount} changed relationships out of {relationships.length} directed ties.
            {!changedOnly && ' Grey edges are unchanged context; colored edges carry meaningful shifts.'}
          </div>
          {phaseLabel && (
            <div className="text-[11px] uppercase tracking-wider text-text-muted mt-2">
              {phaseLabel}
            </div>
          )}
        </div>
      </div>
      <div ref={containerRef} className="h-72 rounded-xl bg-gray-50/70 border border-gray-200" />
    </div>
  );
}
