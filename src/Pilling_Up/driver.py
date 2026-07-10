from util import can_stack


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))

        print(can_stack(blocks))


if __name__ == "__main__":
    main()
