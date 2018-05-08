def reverse(integer: int) -> int:
    int_str: str = str(abs(integer))
    reversed_int_str: str = ''.join(reversed(int_str))
    reversed_int: int = int(reversed_int_str)
    return reversed_int if integer >= 0 else (-1) * reversed_int


if __name__ == '__main__':
    from test_framework import generic_test

    exit(generic_test.generic_test_main(
        "reverse_digits.py", 'reverse_digits.tsv', reverse))
