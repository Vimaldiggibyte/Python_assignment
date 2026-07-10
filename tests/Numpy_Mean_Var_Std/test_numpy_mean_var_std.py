import numpy as np

from src.Numpy_Mean_Var_Std.util import calculate_statistics


def test_case_1():
    array = [
        [1, 2],
        [3, 4]
    ]

    mean, variance, std = calculate_statistics(array)

    assert np.array_equal(mean, np.array([1.5, 3.5]))
    assert np.array_equal(variance, np.array([1.0, 1.0]))
    assert std == round(np.std(np.array(array)), 11)


def test_case_2():
    array = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    mean, variance, std = calculate_statistics(array)

    assert np.array_equal(mean, np.array([2.0, 5.0]))
    assert np.array_equal(variance, np.array([2.25, 2.25, 2.25]))
    assert std == round(np.std(np.array(array)), 11)


def test_case_3():
    array = [
        [5, 5],
        [5, 5]
    ]

    mean, variance, std = calculate_statistics(array)

    assert np.array_equal(mean, np.array([5.0, 5.0]))
    assert np.array_equal(variance, np.array([0.0, 0.0]))
    assert std == 0.0


def test_case_4():
    array = [
        [10, 20, 30]
    ]

    mean, variance, std = calculate_statistics(array)

    assert np.array_equal(mean, np.array([20.0]))
    assert np.array_equal(variance, np.array([0.0, 0.0, 0.0]))
    assert std == round(np.std(np.array(array)), 11)


def test_case_5():
    array = [
        [2, 4],
        [6, 8],
        [10, 12]
    ]

    mean, variance, std = calculate_statistics(array)

    assert np.array_equal(mean, np.array([3.0, 7.0, 11.0]))
    assert np.allclose(variance, np.array([10.66666667, 10.66666667]))
    assert std == round(np.std(np.array(array)), 11)
