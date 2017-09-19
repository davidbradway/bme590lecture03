def main():
    c = add(2, 3.5)

    print('The result is {}. Oh yeah!'.format(c))

    d = sub(2, 3.5)

    print('The result is {}. Oh yeah!'.format(d))


def add(a=7, b=1.1):
    """add two numbers

    :param a: default=7
    :param b: default=1.1
    :returns: something
    """
    s = a + b
    if s < 0:
        return 0
    return s


def sub(a, b):
    """subtracts two numbers

    :param a: default=7
    :param b: default=1.1
    :returns: something
    """
    s = a - b
    if s < 0:
        return 0
    return s


if __name__ == "__main__":
    main()

