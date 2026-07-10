from itertools import combinations


def calculate_probability(letters: list[str], k: int) -> float:
    all_combinations = list(combinations(letters, k))

    favorable = 0

    for combination in all_combinations:
        if "a" in combination:
            favorable += 1


    return favorable / len(all_combinations)
