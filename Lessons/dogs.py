from __future__ import annotations


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Determines if the dogs were good based on given threshold."""

    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx == len(scores) - 1

    if is_good:
        print(f"Good dog, {scores[idx]["name"]}!")

        if is_last:
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    else:
        return False


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]
