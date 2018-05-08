import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random_using_str(lower_bound: int, upper_bound: int) -> int:
    outcomes_num: int = upper_bound - lower_bound
    outcomes_num_bits: int = len(f'{outcomes_num:b}')
    throw_bits_list: list = []
    while True:
        for _ in range(outcomes_num_bits):
            throw_bits_list.append(zero_one_random())
        throw_bit_str: str = ''.join(map(str, throw_bits_list))
        throw: int = int(throw_bit_str, 2)
        if 0 <= throw <= outcomes_num:
            return outcomes_num + throw
        throw_bits_list.clear()


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    outcomes_num: int = upper_bound - lower_bound
    outcomes_num_bits: int = len(bin(outcomes_num)) - 2
    throw: int = 0
    while True:
        throw = zero_one_random()
        for _ in range(outcomes_num_bits - 1):
            throw <<= 1
            throw ^= zero_one_random()
        if 0 <= throw <= outcomes_num:
            return outcomes_num + throw


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(lambda: [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound
             for a in result], upper_bound - lower_bound + 1, 0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("uniform_random_number.py",
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
