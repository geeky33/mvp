def rank_steps_by_confidence(
    confidences: dict[int, float],
) -> list[int]:

    return sorted(
        confidences,
        key=confidences.get,
    )


def top1(
    predicted_steps: list[int],
    true_error_step: int,
) -> float:

    if not predicted_steps:
        return 0.0

    return float(
        predicted_steps[0]
        == true_error_step
    )


def top2(
    predicted_steps: list[int],
    true_error_step: int,
) -> float:

    return float(
        true_error_step
        in predicted_steps[:2]
    )