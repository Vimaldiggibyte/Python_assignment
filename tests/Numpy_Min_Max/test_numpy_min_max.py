from src.Numpy_Min_Max.util import numpy_min_max


def test_case_1():
    array = [
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ]

    assert numpy_min_max(array) == 3


def test_case_2():
    array = [
        [5, 6, 7],
        [1, 2, 3],
        [8, 9, 4]
    ]

    assert numpy_min_max(array) == 5


def test_case_3():
    array = [
        [10, 20],
        [30, 40]
    ]

    assert numpy_min_max(array) == 30


def test_case_4():
    array = [
        [1, 1],
        [1, 1]
    ]

    assert numpy_min_max(array) == 1


def test_case_5():
    array = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    assert numpy_min_max(array) == 7
