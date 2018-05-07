def multiply(x: int, y: int) -> int:
    x_shifted_left: int = x
    y_shifted_right: int = y
    running_total: int = 0
    while y_shifted_right:
        current_bit: int = y_shifted_right & 1
        if current_bit == 1:
            running_total = add(running_total, x_shifted_left)
        x_shifted_left <<= 1
        y_shifted_right >>= 1
    return running_total


def add(x: int, y: int) -> int:
    if not y:
        return x
    base: int = x ^ y
    carry: int = (x & y) << 1
    return add(base, carry)


if __name__ == '__main__':
    from sys import exit

    from test_framework import generic_test

    exit(generic_test.generic_test_main(
        "primitive_multiply.py", 'primitive_multiply.tsv', multiply))
