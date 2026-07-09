def text_alignment(thickness: int) -> list[str]:
    c = "H"
    result = []

    # Top Cone
    for i in range(thickness):
        result.append(
            (c * (2 * i + 1)).center(thickness * 2 - 1)
        )

    # Top Pillars
    for _ in range(thickness + 1):
        result.append(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    # Middle Belt
    for _ in range((thickness + 1) // 2):
        result.append(
            (c * thickness * 5).center(thickness * 6)
        )

    # Bottom Pillars
    for _ in range(thickness + 1):
        result.append(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    # Bottom Cone
    for i in range(thickness):
        result.append(
            (c * (2 * (thickness - i) - 1))
            .center(thickness * 2 - 1)
            .rjust(thickness * 6)
        )

    return result
