import { ResponsiveLine } from '@nivo/line';

interface SparklineProps {
  data: number[];
  color?: string;
  height?: number;
  label?: string;
}

export function Sparkline({ data, color = '#3b82f6', height = 32, label }: SparklineProps) {
  if (data.length === 0) return null;

  const lineData = [{
    id: 'metric',
    data: data.map((v, i) => ({ x: i, y: v })),
  }];

  return (
    <div style={{ height }} className="w-full">
      {label && <div className="text-[10px] text-text-muted mb-0.5">{label}</div>}
      <ResponsiveLine
        data={lineData}
        margin={{ top: 2, right: 2, bottom: 2, left: 2 }}
        xScale={{ type: 'linear' }}
        yScale={{ type: 'linear', min: 'auto', max: 'auto' }}
        enableArea
        areaOpacity={0.15}
        enablePoints={false}
        enableGridX={false}
        enableGridY={false}
        isInteractive={false}
        colors={[color]}
        theme={{ background: 'transparent' }}
      />
    </div>
  );
}
