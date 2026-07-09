from util import merge_the_tools

def main():
    string = input()
    k = int(input())

    result = merge_the_tools(string, k)

    for item in result:
        print(item)

if __name__ == "__main__":
    main()
