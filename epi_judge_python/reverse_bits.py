def reverse_bits_64b(integer: int) -> int:
    reversed_bits: int = 0
    read_bit_mask: int = 1
    write_bit_mask: int = 1 << (64 - 1)
    for _ in range(64):
        if integer & read_bit_mask:
            reversed_bits |= write_bit_mask
        read_bit_mask <<= 1
        write_bit_mask >>= 1
    return reversed_bits


def reverse_bits_custom(*, integer: int, bits: int) -> int:
    reversed_bits: int = 0
    shifted_bits: int = integer
    bit_mask: int = 1 << (bits - 1)
    for _ in range(bits):
        if shifted_bits & 1:
            reversed_bits |= bit_mask
        shifted_bits >>= 1
        bit_mask >>= 1
    return reversed_bits


reversed_bits_16b_cache: dict = {}
for i in range(2**16):
    reversed_bits_16b_cache[i] = reverse_bits_custom(integer=i, bits=16)


def reverse_bits_cached(integer: int) -> int:
    shifted_bits: int = integer
    reversed_bits: int = 0
    bit_mask_16b: int = (1 << 16) - 1
    iterations = last = 4  # 64 bits (target) / 16 bits (cached results) = 4 iterations
    for iteration in range(1, iterations + 1):
        chunk_16b = shifted_bits & bit_mask_16b
        reversed_chunk_16b = reversed_bits_16b_cache[chunk_16b]
        reversed_bits ^= reversed_chunk_16b
        if iteration is not last:
            reversed_bits <<= 16
            shifted_bits >>= 16
    return reversed_bits


if __name__ == '__main__':
    from sys import exit

    from test_framework import generic_test

    reverse_bits = reverse_bits_cached
    exit(generic_test.generic_test_main(
        "reverse_bits.py", "reverse_bits.tsv", reverse_bits))
