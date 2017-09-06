def func(a, b):
    if (a + b >= 0):
        return a + b
    else:
        return 0


def test_answer():
    assert func(1,2) == 3


def test_answer_neg():
    assert func(1,-2) == 0


