"""Lightweight episodic relationship memory for stakeholder simulations."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class RelationalEpisode:
    turn_index: int
    source_actor_id: str
    target_actor_id: str
    sentiment: str              # positive/negative/challenging
    trust_delta: float
    tension_delta: float
    excerpt: str                # first 80 chars of the turn content
    phase_name: str
    salience: float = 1.0      # decays over time


class EpisodicMemory:
    """Stores and retrieves salient relationship episodes for prompt injection."""

    def __init__(self):
        self.episodes: list[RelationalEpisode] = []

    def add_episode(self, episode: RelationalEpisode) -> None:
        self.episodes.append(episode)

    def decay_all(self, rate: float = 0.15) -> None:
        """Reduce salience of all episodes (call once per turn)."""
        for ep in self.episodes:
            ep.salience = max(0.05, ep.salience - rate)
        # Negative/challenging episodes decay slower (memorable)
        for ep in self.episodes:
            if ep.sentiment in ("negative", "challenging"):
                ep.salience = min(1.0, ep.salience + rate * 0.5)

    def get_salient_for_actor(self, actor_id: str, max_count: int = 3) -> list[RelationalEpisode]:
        """Get the most salient episodes involving this actor."""
        relevant = [
            ep for ep in self.episodes
            if ep.source_actor_id == actor_id or ep.target_actor_id == actor_id
        ]
        relevant.sort(key=lambda ep: -ep.salience)
        return relevant[:max_count]

    def format_memory_context(self, actor_id: str) -> str:
        """Format episodic memory for prompt injection (~100 tokens)."""
        salient = self.get_salient_for_actor(actor_id)
        if not salient:
            return ""
        lines = []
        for ep in salient:
            other = ep.target_actor_id if ep.source_actor_id == actor_id else ep.source_actor_id
            direction = "from" if ep.target_actor_id == actor_id else "toward"
            lines.append(
                f"{other}:{ep.sentiment}(t{ep.turn_index},trust{ep.trust_delta:+.2f}) "
                f'"{ep.excerpt[:60]}"'
            )
        return "Relational memory: " + "; ".join(lines)

    def serialize(self) -> list[dict]:
        return [asdict(ep) for ep in self.episodes]

    def deserialize(self, data: list[dict]) -> None:
        self.episodes = [RelationalEpisode(**d) for d in data]
