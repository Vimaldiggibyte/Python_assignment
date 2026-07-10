from util import word_order


def main():
    n = int(input())

    words = []

    for _ in range(n):
        words.append(input())

    distinct_count, occurrences = word_order(words)

    print(distinct_count)
    print(*occurrences)


if __name__ == "__main__":
    main()
