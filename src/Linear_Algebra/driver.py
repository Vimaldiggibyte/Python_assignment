from util import matrix_determinant


def main():
    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(float, input().split())))

    result = matrix_determinant(matrix)

    print(result)


if __name__ == "__main__":
    main()
