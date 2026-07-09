from util import find_runner_up

def main():
    input()
    scores = list(map(int, input().split()))

    result = find_runner_up(scores)
    print(result)

if __name__ == "__main__":
    main()
