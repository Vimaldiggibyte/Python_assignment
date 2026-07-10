from util import calculate_statistics


def main():
    n, m = map(int, input().split())

    array = []

    for _ in range(n):
        array.append(list(map(int, input().split())))

    mean, variance, standard_deviation = calculate_statistics(array)

    print(mean)
    print(variance)
    print(standard_deviation)


if __name__ == "__main__":
    main()
