from util import calculate_probability


def main():
    n = int(input())
    letters = input().split()
    k = int(input())

    probability = calculate_probability(letters, k)

    print(f"{probability:.4f}")


if __name__ == "__main__":
    main()
