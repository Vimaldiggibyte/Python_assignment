from src.runner_up.util import find_runner_up

def test_case_1():
    assert find_runner_up([2, 3, 6, 6, 5]) == 5


def test_case_2():
    assert find_runner_up([1, 2, 3, 4, 5]) == 4


def test_case_3():
    assert find_runner_up([10, 10, 9, 8]) == 9


def test_case_4():
    assert find_runner_up([-1, -2, -3, -1]) == -2


def test_case_5():
    assert find_runner_up([100, 50, 100, 75]) == 75
