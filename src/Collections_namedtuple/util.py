from collections import namedtuple


def calculate_average(column_names: str, students: list[str]) -> float:
    Student = namedtuple("Student", column_names)

    total_marks = 0

    for student in students:
        data = Student(*student.split())
        total_marks += int(data.MARKS)

    return total_marks / len(students)
