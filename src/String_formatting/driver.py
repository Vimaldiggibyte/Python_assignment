from util import print_formatted

def main():
    number = int(input())

    result = print_formatted(number)

    for item in result:
        print(item)

if __name__ == "__main__":
    main()
