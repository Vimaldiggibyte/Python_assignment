import numpy as np


def matrix_determinant(matrix: list[list[float]]) -> float:
    arr = np.array(matrix, dtype=float)

    return round(float(np.linalg.det(arr)), 2)
