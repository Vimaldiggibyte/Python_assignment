from src.Word_Order.util import word_order


def test_case_1():
    words = [
        "bcdef",
        "abcdefg",
        "bcde",
        "bcdef"
    ]

    assert word_order(words) == (3, [2, 1, 1])


def test_case_2():
    words = [
        "apple",
        "apple",
        "apple"
    ]

    assert word_order(words) == (1, [3])


def test_case_3():
    words = [
        "one",
        "two",
        "three"
    ]

    assert word_order(words) == (3, [1, 1, 1])


def test_case_4():
    words = [
        "cat",
        "dog",
        "cat",
        "dog",
        "bird"
    ]

    assert word_order(words) == (3, [2, 2, 1])


def test_case_5():
    words = [
        "a",
        "b",
        "a",
        "c",
        "b",
        "a"
    ]

    assert word_order(words) == (3, [3, 2, 1])
