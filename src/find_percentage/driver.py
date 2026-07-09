from util import find_percentage

def main():
    n = int(input())

    student_data = {}

    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_data[name] = marks

    query_name = input()

    result = find_percentage(student_data, query_name)

    print(f"{result:.2f}")

if __name__ == "__main__":
    main()
