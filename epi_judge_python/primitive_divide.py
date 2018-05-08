from typing import Tuple


def divide(dividend: int, divisor: int) -> int:
    quotient: int = 0
    remaining_dividend: int = dividend
    quotient_to_add: int
    while remaining_dividend >= divisor:
        remaining_dividend, quotient_to_add = fit_squares_of_divisor(
            remaining_dividend,
            divisor,
        )
        quotient += quotient_to_add

    return quotient


def fit_squares_of_divisor(dividend: int, divisor: int) -> Tuple[int, int]:
    quotient: int = 1
    divisor_squares: int = divisor
    divisor_square_lookahead: int = divisor_squares << 1

    while dividend >= divisor_square_lookahead:
        quotient <<= 1
        divisor_squares = divisor_square_lookahead
        divisor_square_lookahead <<= 1

    remaining_dividend: int = dividend - divisor_squares
    return remaining_dividend, quotient


if __name__ == '__main__':
    from test_framework import generic_test

    exit(generic_test.generic_test_main(
        "primitive_divide.py", "primitive_divide.tsv", divide))
