import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random_str(lower_bound: int, upper_bound: int) -> int:
    outcome_num: int = upper_bound - lower_bound
    outcome_num_bin_len: int = len(bin(outcome_num)) - 2
    throw_bin_digits: list = []
    while True:
        for _ in range(outcome_num_bin_len):
            throw_bin_digits.append(zero_one_random())
        throw_bin_str: str = ''.join(map(str, throw_bin_digits))
        throw: int = int(throw_bin_str, 2)
        if 0 <= throw <= outcome_num:
            return outcome_num + throw
        throw_bin_digits.clear()


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    outcome_num: int = upper_bound - lower_bound
    outcome_num_bin_len: int = len(bin(outcome_num)) - 2
    throw: int = 0
    while True:
        throw = zero_one_random()
        for _ in range(1, outcome_num_bin_len):
            throw <<= 1
            throw ^= zero_one_random()
        if 0 <= throw <= outcome_num:
            return outcome_num + throw
        throw = 0


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
