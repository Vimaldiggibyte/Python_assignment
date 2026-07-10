import re


def is_valid(email: str) -> bool:
    pattern = r'^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return bool(re.match(pattern, email))



def filter_emails(emails: list[str]) -> list[str]:
    return sorted(list(filter(is_valid, emails)))
