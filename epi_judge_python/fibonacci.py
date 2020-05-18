from test_framework import generic_test


def fibonacci(n, cache={}):
    if n <= 1:
        return n
    
    if n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)

    return cache[n]

import functools

@functools.lru_cache(None)
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
