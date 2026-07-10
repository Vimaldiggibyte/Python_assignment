def calculate_happiness(array: list[int], set_a: set[int], set_b: set[int]) -> int:
    happiness = 0

    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1

    return happiness
