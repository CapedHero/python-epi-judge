def check_parity_counting_chars(integer: int) -> bool:
    bits_str: str = f'{integer:b}'
    bit_1_num: int = bits_str.count('1')
    parity: bool = bit_1_num % 2 == 1
    return parity


def check_parity_shifting_bits(integer: int) -> bool:
    bit_1_num: int = 0
    shifted_bits: int = integer
    while shifted_bits:
        bit_1_num += shifted_bits & 1
        shifted_bits >>= 1
    parity: bool = bit_1_num % 2 == 1
    return parity


parity_16b_cache = {}
for i in range(2**16):
    parity_16b_cache[i] = check_parity_counting_chars(i)


def check_parity_cached(integer: int) -> int:
    parities_per_16b_chunks: list = []
    shifted_bits: int = integer
    bit_mask_16b: int = (1 << 16) - 1
    while shifted_bits:
        chunk_16b: int = shifted_bits & bit_mask_16b
        parities_per_16b_chunks.append(parity_16b_cache[chunk_16b])
        shifted_bits >>= 16
    parity: bool = sum(parities_per_16b_chunks) % 2 == 1
    return parity


if __name__ == '__main__':
    # Turns out that finding bit parity by checking bit-string is both simple
    # and relatively fast, though takes more memory than shifting bits (roughly
    # twice as much).
    #
    # On the other hand, cached solution was not as fast as checking bit-string.
    # Perhaps more extensive tests could reveal the source of this revelation?
    #
    # The tests provided by the authors resulted in below average times:
    #   + `check_parity_counting_chars`:  2 us.
    #   + `check_parity_shifting_bits`: 6 us.
    #   + `check_parity_cached`: 2-3 us.
    from sys import exit
    from typing import Callable

    from test_framework import generic_test

    parity_func: Callable = check_parity_counting_chars
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity_func))
