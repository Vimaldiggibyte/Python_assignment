from src.Text_Alignment.util import text_alignment


def test_case_1():
    result = text_alignment(1)

    assert len(result) == 7


def test_case_2():
    result = text_alignment(3)

    assert result[0].strip() == "H"
    assert result[1].strip() == "HHH"
    assert result[2].strip() == "HHHHH"


def test_case_3():
    result = text_alignment(5)

    assert result[0].strip() == "H"
    assert result[4].strip() == "HHHHHHHHH"


def test_case_4():
    result = text_alignment(5)

    assert "HHHHHHHHHHHHHHHHHHHHHHHHH" in result[11]


def test_case_5():
    result = text_alignment(5)

    assert result[-1].strip() == "H"
