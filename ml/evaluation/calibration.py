from .metrics import (
    binary_nll,
    brier_score,
    expected_calibration_error,
)


def evaluate_calibration(
    probabilities: list[float],
    labels: list[int],
) -> dict[str, float]:

    if len(probabilities) != len(labels):

        raise ValueError(
            "probabilities and labels "
            "must have equal length"
        )

    return {

        "ece": expected_calibration_error(
            probabilities,
            labels,
        ),

        "brier_score": sum(
            brier_score(
                probability,
                label,
            )
            for probability, label
            in zip(
                probabilities,
                labels,
            )
        ) / len(probabilities),

        "nll": sum(
            binary_nll(
                probability,
                label,
            )
            for probability, label
            in zip(
                probabilities,
                labels,
            )
        ) / len(probabilities),
    }