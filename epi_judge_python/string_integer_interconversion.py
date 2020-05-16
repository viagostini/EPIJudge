from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    ans = [] if x else ['0']
    sign = '-' if x < 0 else ''

    while x := abs(x):
        ans.append(str(x % 10))
        x = x // 10

    return sign + ''.join(reversed(ans))


def string_to_int(s: str) -> int:
    ans, base = 0, 1
    sign = -1 if s[0] == '-' else 1

    if not s[0].isdigit():
        s = s[1:]

    for ch in s:
        ans = (ans * 10) + int(ch)
        base *= 10

    return ans * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
