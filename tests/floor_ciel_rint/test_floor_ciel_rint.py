from src.floor_ciel_rint.util import floor_ceil_rint


def test_floor_ceil_rint():
    floor, ceil, rint = floor_ceil_rint(
        ["1.1", "2.2", "3.3", "4.4", "5.5", "6.6", "7.7", "8.8", "9.9"]
    )

    print("Floor :", floor)
    print("Ceil  :", ceil)
    print("Rint  :", rint)


test_floor_ceil_rint()
