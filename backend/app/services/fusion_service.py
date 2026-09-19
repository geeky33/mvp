def fuse_confidence(
    verification_score: float,
    consistency_score: float,
    verification_weight: float = 0.5,
    consistency_weight: float = 0.5,
) -> float:

    total_weight = (
        verification_weight
        + consistency_weight
    )

    if total_weight <= 0:
        raise ValueError(
            "Fusion weights must sum to a positive value."
        )

    confidence = (
        verification_weight * verification_score
        + consistency_weight * consistency_score
    ) / total_weight

    return max(
        0.0,
        min(1.0, confidence),
    )


def predict_error_step(
    confidences: dict[int, float],
) -> int | None:

    if not confidences:
        return None

    return min(
        confidences,
        key=confidences.get,
    )