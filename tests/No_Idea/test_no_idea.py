from src.No_Idea.util import calculate_happiness


def test_case_1():
    array = [1, 5, 3]
    set_a = {3, 1}
    set_b = {5, 7}

    assert calculate_happiness(array, set_a, set_b) == 1


def test_case_2():
    array = [1, 2, 3, 4]
    set_a = {1, 2}
    set_b = {3, 4}

    assert calculate_happiness(array, set_a, set_b) == 0


def test_case_3():
    array = [5, 5, 5]
    set_a = {5}
    set_b = {1}

    assert calculate_happiness(array, set_a, set_b) == 3


def test_case_4():
    array = [1, 2, 3]
    set_a = {4, 5}
    set_b = {6, 7}

    assert calculate_happiness(array, set_a, set_b) == 0


def test_case_5():
    array = [1, 2, 2, 3, 3]
    set_a = {2}
    set_b = {3}

    assert calculate_happiness(array, set_a, set_b) == 0
