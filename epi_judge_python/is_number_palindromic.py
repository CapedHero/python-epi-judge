def is_palindrome_number(integer: int) -> bool:
    if integer < 0:
        return False
    integer_str: str = str(integer)
    reversed_integer_str: str = ''.join(reversed(integer_str))
    return integer_str == reversed_integer_str


if __name__ == '__main__':
    from test_framework import generic_test

    exit(generic_test.generic_test_main(
        "is_number_palindromic.py",
        "is_number_palindromic.tsv",
        is_palindrome_number
    ))
