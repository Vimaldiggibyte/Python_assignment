def mutate_string(string: str, position: int, character: str) -> str:
    return string[:position] + character + string[position + 1:]
