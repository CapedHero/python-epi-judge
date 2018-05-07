def find_closest_int_same_bit_count(integer: int) -> int:
    bit_mask: int = 1
    bit_0_found: bool = False
    bit_1_found: bool = False

    while True:
        current_bit: int = int(integer & bit_mask > 0)
        if current_bit == 1:
            bit_1_found = True
        else:
            bit_0_found = True
        if bit_0_found and bit_1_found:
            closest_int_same_bit_count: int = integer ^ (bit_mask | bit_mask >> 1)
            break
        bit_mask <<= 1

    return closest_int_same_bit_count


if __name__ == '__main__':
    from sys import exit
    from typing import Callable

    from test_framework import generic_test

    closest_int_same_bit_count: Callable = find_closest_int_same_bit_count
    exit(generic_test.generic_test_main(
        "closest_int_same_weight.py", "closest_int_same_weight.tsv", closest_int_same_bit_count))
