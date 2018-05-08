def power(base: float, exponent: int) -> float:
    """
    Calculate and return power for the given base and exponent.

    This implementation is relatively fast due to the incorporation of bitwise
    logic, which substantially speeds up calculations.

    Explanation by example
    ----------------------
    Given that:
    a^(b+c) = a^b * a^c
    (a^b)^c = a^(b*c)

    4^31 == 4 ^ (   1         1         1        1        1 ) [2-based exponent]
    4^31 == 4 ^ (  16    +    8    +    4   +    2     +  1 ) [10-based exponent]
    4^31 ==       4^16   *   4^8   *   4^4  *   4^2    * 4^1
                <=======^2========^2========^2========^2====
    4^31 ==      4^(8+8) * 4^(4+4) * 4^(2+2) * 4^(1+1) * 4^1  [running base]

    All in all, while calculating from LSB to MSB, every turned `on` bit of
    exponent indicates that we should multiply running total by running base
    from current step of calculations.

    Running base for current step can be easily calculated by squaring base
    from previous step.
    """
    running_power: float = 1.0

    if exponent > 0:
        running_base: float = base
        shifted_exponent: int = exponent
    elif exponent < 0:
        running_base = 1 / base
        shifted_exponent = -exponent
    else:
        return 1

    while shifted_exponent:
        current_bit: int = shifted_exponent & 1
        if current_bit == 1:
            running_power *= running_base
        running_base **= 2
        shifted_exponent >>= 1

    return running_power


if __name__ == '__main__':
    from test_framework import generic_test

    exit(generic_test.generic_test_main(
        "power_x_y.py", 'power_x_y.tsv', power))
