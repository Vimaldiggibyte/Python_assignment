from util import calculate_average


def main():
    n = int(input())
    column_names = input()

    students = []

    for _ in range(n):
        students.append(input())

    result = calculate_average(column_names, students)

    print(f"{result:.2f}")


if __name__ == "__main__":
    main()
