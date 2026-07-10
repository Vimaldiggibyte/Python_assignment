from src.Validate_Email.util import is_valid, filter_emails


def test_case_1():
    assert is_valid("lara@hackerrank.com") is True


def test_case_2():
    assert is_valid("brian-23@hackerrank.com") is True


def test_case_3():
    assert is_valid("britts_54@hackerrank.com") is True


def test_case_4():
    assert is_valid("abc@site.technology") is False


def test_case_5():
    emails = [
        "lara@hackerrank.com",
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com",
        "abc@site.technology",
        "abc@site.12"
    ]

    assert filter_emails(emails) == [
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com",
        "lara@hackerrank.com"
    ]
