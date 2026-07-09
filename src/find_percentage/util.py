def find_percentage(student_data: dict, query_name: str) -> float:
    marks = student_data[query_name]
    return sum(marks) / len(marks)
