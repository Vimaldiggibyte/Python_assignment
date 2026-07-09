from src.Collections_namedtuple.util import calculate_average


def test_case_1():
    columns = "ID MARKS NAME CLASS"

    students = [
        "1 97 Raymond 7",
        "2 50 Steven 4",
        "3 91 Adrian 9",
        "4 72 Stewart 5",
        "5 80 Peter 6"
    ]

    assert calculate_average(columns, students) == 78.0


def test_case_2():
    columns = "MARKS CLASS NAME ID"

    students = [
        "92 2 Calum 1",
        "82 5 Scott 2",
        "94 2 Jason 3",
        "55 8 Glenn 4",
        "82 2 Fergus 5"
    ]

    assert calculate_average(columns, students) == 81.0


def test_case_3():
    columns = "NAME ID CLASS MARKS"

    students = [
        "Alice 1 10 100",
        "Bob 2 10 90"
    ]

    assert calculate_average(columns, students) == 95.0


def test_case_4():
    columns = "CLASS NAME MARKS ID"

    students = [
        "8 John 60 1",
        "9 Jane 80 2"
    ]

    assert calculate_average(columns, students) == 70.0


def test_case_5():
    columns = "MARKS ID NAME CLASS"

    students = [
        "75 1 Tom 6",
        "85 2 Jerry 7",
        "95 3 Mike 8"
    ]

    assert calculate_average(columns, students) == 85.0
