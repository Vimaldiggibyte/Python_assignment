import numpy as np


def numpy_min_max(array: list[list[int]]) -> int:
    arr = np.array(array)

    return int(np.max(np.min(arr, axis=1)))
