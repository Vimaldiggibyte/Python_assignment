from src.Calendar.util import calendar_module


def test_case_1():
    assert calendar_module(8, 5, 2015) == "WEDNESDAY"


def test_case_2():
    assert calendar_module(1, 1, 2000) == "SATURDAY"


def test_case_3():
    assert calendar_module(12, 25, 2020) == "FRIDAY"


def test_case_4():
    assert calendar_module(2, 29, 2016) == "MONDAY"


def test_case_5():
    assert calendar_module(12, 31, 1999) == "FRIDAY"
