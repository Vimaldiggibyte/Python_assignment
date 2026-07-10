from util import numpy_min_max


def main():
    n, m = map(int, input().split())

    array = []

    for _ in range(n):
        array.append(list(map(int, input().split())))

    result = numpy_min_max(array)

    print(result)


if __name__ == "__main__":
    main()
