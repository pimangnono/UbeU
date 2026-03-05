"""
Profile coverage analysis for OCEAN space.
Computes pairwise distances and convex hull volume (if available).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import numpy as np

from experiment.profiles import EXPERIMENT_PROFILES


def _get_vectors() -> Dict[str, np.ndarray]:
    vectors = {}
    for pid, profile in EXPERIMENT_PROFILES.items():
        v = profile.get_vector()
        vectors[pid] = np.array([v["O"], v["C"], v["E"], v["A"], v["N"]])
    return vectors


def compute_coverage() -> dict:
    vectors = _get_vectors()
    ids = list(vectors.keys())
    mats = np.stack([vectors[i] for i in ids], axis=0)

    # Pairwise distances
    dists = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            dists.append(float(np.linalg.norm(mats[i] - mats[j])))

    result = {
        "n_profiles": len(ids),
        "pairwise_distance": {
            "mean": float(np.mean(dists)) if dists else 0.0,
            "min": float(np.min(dists)) if dists else 0.0,
            "max": float(np.max(dists)) if dists else 0.0,
        },
        "trait_ranges": {
            "O": [float(mats[:, 0].min()), float(mats[:, 0].max())],
            "C": [float(mats[:, 1].min()), float(mats[:, 1].max())],
            "E": [float(mats[:, 2].min()), float(mats[:, 2].max())],
            "A": [float(mats[:, 3].min()), float(mats[:, 3].max())],
            "N": [float(mats[:, 4].min()), float(mats[:, 4].max())],
        },
    }

    # Convex hull volume (optional)
    try:
        from scipy.spatial import ConvexHull
        hull = ConvexHull(mats)
        result["convex_hull_volume"] = float(hull.volume)
    except Exception:
        result["convex_hull_volume"] = None

    return result


def main(output_path: str = "experiment/profile_coverage.json") -> None:
    result = compute_coverage()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved profile coverage to {output_path}")


if __name__ == "__main__":
    main()

