import math


def brier_score(
    probability: float,
    label: int,
) -> float:

    return (
        probability - label
    ) ** 2


def binary_nll(
    probability: float,
    label: int,
) -> float:

    probability = min(
        max(probability, 1e-12),
        1 - 1e-12,
    )

    return -(
        label * math.log(probability)
        + (1 - label)
        * math.log(1 - probability)
    )


def expected_calibration_error(
    probabilities: list[float],
    labels: list[int],
    n_bins: int = 10,
) -> float:

    if not probabilities:
        return 0.0

    total = len(probabilities)

    ece = 0.0

    for bin_index in range(n_bins):

        lower = bin_index / n_bins
        upper = (bin_index + 1) / n_bins

        indices = [
            i
            for i, probability
            in enumerate(probabilities)
            if (
                lower <= probability < upper
                or (
                    bin_index == n_bins - 1
                    and probability == upper
                )
            )
        ]

        if not indices:
            continue

        confidence = (
            sum(
                probabilities[i]
                for i in indices
            )
            / len(indices)
        )

        accuracy = (
            sum(
                labels[i]
                for i in indices
            )
            / len(indices)
        )

        ece += (
            len(indices)
            / total
            * abs(
                confidence - accuracy
            )
        )

    return ece