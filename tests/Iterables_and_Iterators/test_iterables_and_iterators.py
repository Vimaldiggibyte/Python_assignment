from src.Iterables_and_Iterators.util import calculate_probability


def test_case_1():
    letters = ["a", "a", "c", "d"]

    assert round(calculate_probability(letters, 2), 4) == 0.8333


def test_case_2():
    letters = ["a", "b", "c"]

    assert round(calculate_probability(letters, 2), 4) == 0.6667


def test_case_3():
    letters = ["b", "c", "d"]

    assert calculate_probability(letters, 2) == 0.0


def test_case_4():
    letters = ["a", "a", "a"]

    assert calculate_probability(letters, 2) == 1.0


def test_case_5():
    letters = ["a", "b", "a", "c" ]

    assert round(calculate_probability(letters, 2), 4) == 0.8333
