import { ResponsiveHeatMap } from '@nivo/heatmap';
import type { RelationshipRecord } from '../../types/simulation';

interface HeatmapProps {
  events: RelationshipRecord[];
  actorNames: Record<string, string>;
  actorIds: string[];
}

export function RelationshipHeatmap({ events, actorNames, actorIds }: HeatmapProps) {
  // Aggregate trust per pair
  const trustMatrix = new Map<string, number>();
  for (const evt of events) {
    const src = evt.source_actor_id || evt.source || '';
    const tgt = evt.target_actor_id || evt.target || '';
    const key = `${src}→${tgt}`;
    trustMatrix.set(key, (trustMatrix.get(key) || 0) + evt.trust_delta);
  }

  const data = actorIds.map((srcId) => ({
    id: actorNames[srcId] || srcId,
    data: actorIds.map((tgtId) => ({
      x: actorNames[tgtId] || tgtId,
      y: srcId === tgtId ? 0 : 0.5 + (trustMatrix.get(`${srcId}→${tgtId}`) || 0),
    })),
  }));

  return (
    <div className="h-64">
      <ResponsiveHeatMap
        data={data}
        margin={{ top: 40, right: 20, bottom: 20, left: 80 }}
        valueFormat=".2f"
        colors={{
          type: 'diverging',
          scheme: 'red_yellow_green',
          minValue: 0,
          maxValue: 1,
        }}
        emptyColor="#f3f4f6"
        borderColor="rgba(0,0,0,0.08)"
        borderWidth={1}
        labelTextColor={{ from: 'color', modifiers: [['darker', 3]] }}
        theme={{
          background: 'transparent',
          text: { fill: '#6b7280', fontSize: 10 },
          axis: { ticks: { text: { fill: '#9ca3af', fontSize: 10 } } },
        }}
      />
    </div>
  );
}
