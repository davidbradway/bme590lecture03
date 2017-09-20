from mymod import add, sub, main


def test_main():
    assert main() is None


def test_add_positive():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(1, -2) == 0


def test_sub_positive():
    assert sub(2, 1) == 1


def test_sub_negative():
    assert sub(1, 3) == 0


def test_add_defaults():
    c = add()

    assert c == 8.1


def test_sub_defaults():
    d = sub()

    assert d == 5.9
