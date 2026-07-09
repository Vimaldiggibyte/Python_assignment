def find_runner_up(scores: list[int]) -> int:
    unique_scores = list(set(scores))
    unique_scores.sort()
    return unique_scores[-2]
