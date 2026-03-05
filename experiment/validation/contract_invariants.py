"""
Contract invariant checks for BCFC v1.1.

Run before any reruns:
  python3 experiment/validation/contract_invariants.py
"""

from __future__ import annotations

import sys
from typing import Dict, List

from experiment.persona_compiler import compile_contract, NONNEGATIVE_FEATURES, _feature_type
from experiment.profiles import EXPERIMENT_PROFILES


def validate_contract_invariants() -> dict:
    errors: List[dict] = []
    total_features = 0

    for profile_id, profile in EXPERIMENT_PROFILES.items():
        vector = {"O": profile.O, "C": profile.C, "E": profile.E, "A": profile.A, "N": profile.N}
        contract = compile_contract(profile_id, vector)

        if contract.invalid_features:
            errors.append({
                "profile_id": profile_id,
                "error": "invalid_features",
                "details": contract.invalid_features,
            })

        for feature_name, spec in contract.target_features.items():
            total_features += 1
            min_raw = spec.get("min")
            max_raw = spec.get("max")
            if min_raw is None or max_raw is None:
                errors.append({
                    "profile_id": profile_id,
                    "feature": feature_name,
                    "error": "missing_range",
                })
                continue

            if max_raw <= min_raw:
                errors.append({
                    "profile_id": profile_id,
                    "feature": feature_name,
                    "error": "invalid_range",
                    "min": min_raw,
                    "max": max_raw,
                })

            ftype = _feature_type(feature_name)
            if ftype == "ratio":
                if min_raw < 0 or max_raw < 0 or min_raw > 1 or max_raw > 1:
                    errors.append({
                        "profile_id": profile_id,
                        "feature": feature_name,
                        "error": "ratio_out_of_bounds",
                        "min": min_raw,
                        "max": max_raw,
                    })
            elif ftype in ("count", "nonneg") or feature_name in NONNEGATIVE_FEATURES:
                if min_raw < 0 or max_raw < 0:
                    errors.append({
                        "profile_id": profile_id,
                        "feature": feature_name,
                        "error": "negative_bounds",
                        "min": min_raw,
                        "max": max_raw,
                    })

    return {
        "total_features": total_features,
        "total_profiles": len(EXPERIMENT_PROFILES),
        "errors": errors,
        "passed": len(errors) == 0,
    }


def main() -> int:
    result = validate_contract_invariants()
    if result["passed"]:
        print(f"Contract invariants: PASS ({result['total_profiles']} profiles, {result['total_features']} features)")
        return 0

    print(f"Contract invariants: FAIL ({len(result['errors'])} issues)")
    for err in result["errors"][:20]:
        print(err)
    if len(result["errors"]) > 20:
        print(f"... {len(result['errors']) - 20} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
