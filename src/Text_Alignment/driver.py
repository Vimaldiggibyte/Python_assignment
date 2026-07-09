from util import text_alignment


def main():
    thickness = int(input())

    result = text_alignment(thickness)

    for line in result:
        print(line)


if __name__ == "__main__":
    main()
