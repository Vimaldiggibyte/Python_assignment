def process_commands(commands: list[str]) -> list[list]:
    data = []
    output = []

    for command in commands:
        parts = command.split()

        if parts[0] == "insert":
            data.insert(int(parts[1]), int(parts[2]))

        elif parts[0] == "print":
            output.append(data.copy())

        elif parts[0] == "remove":
            data.remove(int(parts[1]))

        elif parts[0] == "append":
            data.append(int(parts[1]))

        elif parts[0] == "sort":
            data.sort()

        elif parts[0] == "pop":
            data.pop()

        elif parts[0] == "reverse":
            data.reverse()

    return output
