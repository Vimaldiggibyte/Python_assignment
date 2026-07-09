from src.Mutations.util import mutate_string


def test_case_1():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"


def test_case_2():
    assert mutate_string("hello", 0, "H") == "Hello"


def test_case_3():
    assert mutate_string("python", 5, "X") == "pythoX"


def test_case_4():
    assert mutate_string("abcdef", 2, "Z") == "abZdef"


def test_case_5():
    assert mutate_string("apple", 4, "Y") == "applY"
