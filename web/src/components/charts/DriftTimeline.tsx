import { ResponsiveLine } from '@nivo/line';
import { ACTOR_COLORS } from '../../types/simulation';
import type { ActorStateRecord } from '../../types/simulation';

interface DriftTimelineProps {
  actorStateEvents: ActorStateRecord[];
  actorIds: string[];
  actorNames: Record<string, string>;
}

export function DriftTimeline({ actorStateEvents, actorIds, actorNames }: DriftTimelineProps) {
  if (actorStateEvents.length === 0) {
    return <div className="text-xs text-text-muted p-4">No drift data available</div>;
  }

  const lineData = actorIds.map((actorId, idx) => {
    const events = actorStateEvents
      .filter((e) => e.actor_id === actorId)
      .sort((a, b) => a.turn_index - b.turn_index);

    return {
      id: actorNames[actorId] || actorId,
      color: ACTOR_COLORS[idx % ACTOR_COLORS.length],
      data: events.map((e) => ({
        x: e.turn_index,
        y: e.drift_score ?? e.new_state?.drift_score ?? 0,
      })),
    };
  }).filter((d) => d.data.length > 0);

  if (lineData.length === 0) {
    return <div className="text-xs text-text-muted p-4">No drift data available</div>;
  }

  return (
    <div className="h-64">
      <ResponsiveLine
        data={lineData}
        margin={{ top: 10, right: 120, bottom: 40, left: 50 }}
        xScale={{ type: 'linear' }}
        yScale={{ type: 'linear', min: 0, max: 'auto' }}
        enablePoints
        pointSize={4}
        enableArea={false}
        colors={{ datum: 'color' }}
        axisBottom={{
          legend: 'Turn',
          legendOffset: 32,
          legendPosition: 'middle',
        }}
        axisLeft={{
          legend: 'Drift',
          legendOffset: -40,
          legendPosition: 'middle',
        }}
        legends={[
          {
            anchor: 'bottom-right',
            direction: 'column',
            translateX: 110,
            itemWidth: 100,
            itemHeight: 16,
            symbolSize: 8,
            symbolShape: 'circle',
            itemTextColor: '#6b7280',
          },
        ]}
        theme={{
          background: 'transparent',
          text: { fill: '#6b7280', fontSize: 10 },
          axis: {
            ticks: { text: { fill: '#9ca3af', fontSize: 10 } },
            legend: { text: { fill: '#6b7280', fontSize: 11 } },
          },
          grid: { line: { stroke: 'rgba(0,0,0,0.06)' } },
          crosshair: { line: { stroke: '#9ca3af' } },
        }}
        enableGridX={false}
      />
    </div>
  );
}
