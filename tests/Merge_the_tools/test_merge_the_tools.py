from src.Merge_the_tools.util import merge_the_tools


def test_case_1():
    assert merge_the_tools("AABCAAADA", 3) == [
        "AB",
        "CA",
        "AD"
    ]


def test_case_2():
    assert merge_the_tools("AAAA", 2) == [
        "A",
        "A"
    ]


def test_case_3():
    assert merge_the_tools("ABCDEFGH", 2) == [
        "AB",
        "CD",
        "EF",
        "GH"
    ]


def test_case_4():
    assert merge_the_tools("AAABBBCCC", 3) == [
        "A",
        "B",
        "C"
    ]


def test_case_5():
    assert merge_the_tools("ABABAB", 2) == [
        "AB",
        "AB",
        "AB"
    ]
