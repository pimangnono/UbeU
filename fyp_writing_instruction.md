# FYP Writing Instructions

## 1. Explain all logics (that are not LLM wrapper) in pseudocode

All deterministic scoring, filtering, and state management logic must be presented as pseudocode in the paper. This covers:

- Persona State Controller candidate scoring (8 positive criteria + penalties)
- OCEAN trait estimation (30 behavioral features → sigmoid → weighted sum)
- Dynamic C calibration (relative-to-conversation-baseline)
- Envelope penalty (overshoot + overshoot²)
- Sycophancy risk detection
- Redundancy / genericity penalties
- Trait target alignment (polar signal library pattern matching + banded targeting)
- Social trait alignment (E/A/N tolerance bands)
- Expressive stability penalty (O/E overshoot detection)
- Action layer: sparse gate, conflict arbitration, family capping, phase action limits
- Commitment lifecycle: extraction → fulfillment → staleness → phase resolution
- Relationship tracking: sentiment keyword detection → trust/tension deltas
- State ledger: rolling trait estimate (exponential smoothing 0.6/0.4)

## 2. Create dashboard UI for demo video recording

Need to build a dashboard UI to record a demo video showing the simulation workflow. Should visualize:

- Real-time simulation progress (phases, turns, actors)
- Actor personality priors vs inferred traits (radar charts or bar charts)
- Candidate pool scoring (4 style variants with score breakdowns)
- Action layer proposals and arbitration results
- World state transitions (global + per-actor local state)
- Commitment lifecycle status
- Relationship graph with trust/tension edges
- Phase progression with drift tracking over time
