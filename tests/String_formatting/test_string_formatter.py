from src.String_formatting.util import print_formatted


def test_case_1():
    expected = [
        ["1", "1", "1", "1"]
    ]

    assert [line.split() for line in print_formatted(1)] == expected


def test_case_2():
    expected = [
        ["1", "1", "1", "1"],
        ["2", "2", "2", "10"]
    ]

    assert [line.split() for line in print_formatted(2)] == expected


def test_case_3():
    expected = [
        ["1", "1", "1", "1"],
        ["2", "2", "2", "10"],
        ["3", "3", "3", "11"]
    ]

    assert [line.split() for line in print_formatted(3)] == expected


def test_case_4():
    result = print_formatted(5)

    assert result[-1].split() == ["5", "5", "5", "101"]


def test_case_5():
    result = print_formatted(17)

    assert result[-1].split() == ["17", "21", "11", "10001"]
