def is_numeric(*values):
    numeric_types = (int, float)

    for v in values:
        if not isinstance(v, numeric_types):
            raise ValueError(f'{v} musi być wartością numeryczną!')


def rectangle(a, b):
    is_numeric(a, b)

    return a * b


def triangle(a, h):
    is_numeric(a, h)

    result = 0.5 * a * h
    return result


def trapeze(a, b, h):
    is_numeric(a, b, h)

    result = (a + b) * h / 2
    return result


def main():
    print(rectangle(4, 6) == 24)
    print(triangle(4, 6) == 12)
    trapeze(5, 2, "*")


if __name__ == "__main__":
    main()

