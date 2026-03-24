interface SkeletonProps {
  className?: string;
}

export function Skeleton({ className = '' }: SkeletonProps) {
  return (
    <div className={`animate-pulse bg-bg-elevated rounded ${className}`} />
  );
}

export function ActorCardSkeleton() {
  return (
    <div className="glass-card p-4 space-y-3">
      <div className="flex items-center gap-3">
        <Skeleton className="w-9 h-9 rounded-full" />
        <div className="space-y-1.5 flex-1">
          <Skeleton className="h-4 w-24" />
          <Skeleton className="h-3 w-32" />
        </div>
      </div>
      <div className="space-y-2">
        {[1, 2, 3, 4, 5].map((i) => (
          <div key={i} className="flex items-center gap-2">
            <Skeleton className="w-4 h-3" />
            <Skeleton className="h-1.5 flex-1" />
            <Skeleton className="w-8 h-3" />
          </div>
        ))}
      </div>
      <Skeleton className="h-6 w-20" />
    </div>
  );
}

export function ScenarioCardSkeleton() {
  return (
    <div className="glass-card p-4 space-y-2">
      <Skeleton className="h-4 w-32" />
      <Skeleton className="h-3 w-full" />
      <Skeleton className="h-3 w-3/4" />
      <div className="flex gap-2 pt-1">
        <Skeleton className="h-5 w-16 rounded-full" />
        <Skeleton className="h-5 w-12 rounded-full" />
      </div>
    </div>
  );
}
