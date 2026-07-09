def merge_the_tools(string: str, k: int) -> list[str]:
    result = []

    for i in range(0, len(string), k):
        substring = string[i:i + k]

        unique = ""
        for ch in substring:
            if ch not in unique:
                unique += ch

        result.append(unique)

    return result
