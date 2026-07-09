from util import process_commands

def main():
    n = int(input())

    commands = []

    for _ in range(n):
        commands.append(input())

    result = process_commands(commands)

    for item in result:
        print(item)

if __name__ == "__main__":
    main()
