def print_formatted(number: int) -> list[str]:
    width = len(bin(number)[2:])
    result = []

    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        result.append(f"{decimal} {octal} {hexa} {binary}")

    return result
