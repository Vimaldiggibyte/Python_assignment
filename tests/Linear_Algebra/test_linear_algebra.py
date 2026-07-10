from src.Linear_Algebra.util import matrix_determinant


def test_case_1():
    matrix = [
        [1.1, 1.1],
        [1.1, 1.1]
    ]

    assert matrix_determinant(matrix) == 0.0


def test_case_2():
    matrix = [
        [1, 2],
        [2, 1]
    ]

    assert matrix_determinant(matrix) == -3.0


def test_case_3():
    matrix = [
        [2, 0],
        [0, 2]
    ]

    assert matrix_determinant(matrix) == 4.0


def test_case_4():
    matrix = [
        [3]
    ]

    assert matrix_determinant(matrix) == 3.0


def test_case_5():
    matrix = [
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0]
    ]

    assert matrix_determinant(matrix) == 1.0
