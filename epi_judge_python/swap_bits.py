def swap_bits(integer: int, bit_index_1: int, bit_index_2: int):
    """Least significant bit is at index `0`."""
    # If bits at indexes are the same, there is no need to swap.
    if (integer >> bit_index_1) & 1 == (integer >> bit_index_2) & 1:
        return integer
    swap_bit_mask: int = 1 << bit_index_1 | 1 << bit_index_2
    swapped_bits_integer: int = integer ^ swap_bit_mask
    return swapped_bits_integer


if __name__ == '__main__':
    from sys import exit

    from test_framework import generic_test

    exit(generic_test.generic_test_main(
        "swap_bits.py", 'swap_bits.tsv', swap_bits))
