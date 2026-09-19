from collections import Counter


def normalize(
    text: str,
) -> str:

    return " ".join(
        text.lower().split()
    )


def consistency_score(
    samples: list[str],
) -> float:

    if not samples:
        return 0.0

    normalized = [
        normalize(sample)
        for sample in samples
    ]

    counts = Counter(normalized)

    most_common_count = max(
        counts.values()
    )

    return most_common_count / len(samples)


def prefix_conditioned_consistency(
    question: str,
    prefix: str,
    generated_suffixes: list[str],
) -> float:

    return consistency_score(
        generated_suffixes
    )