from util import mutate_string

def main():
    string = input()
    position, character = input().split()

    result = mutate_string(string, int(position), character)

    print(result)

if __name__ == "__main__":
    main()
