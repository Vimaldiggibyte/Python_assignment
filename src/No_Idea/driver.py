from util import calculate_happiness


def main():
    n, m = map(int, input().split())

    array = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    result = calculate_happiness(array, set_a, set_b)

    print(result)


if __name__ == "__main__":
    main()
