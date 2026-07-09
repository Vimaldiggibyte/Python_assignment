from util import calendar_module


def main():
    month, day, year = map(int, input().split())

    result = calendar_module(month, day, year)

    print(result)


if __name__ == "__main__":
    main()
