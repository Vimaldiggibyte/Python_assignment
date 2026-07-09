from datetime import datetime


def time_delta(t1: str, t2: str) -> int:
    time_format = "%a %d %b %Y %H:%M:%S %z"

    date1 = datetime.strptime(t1, time_format)
    date2 = datetime.strptime(t2, time_format)

    return int(abs((date1 - date2).total_seconds()))
