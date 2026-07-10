from collections import deque


def can_stack(blocks: list[int]) -> str:
    cubes = deque(blocks)
    last = float("inf")

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            return "No"

        last = current

    return "Yes"
