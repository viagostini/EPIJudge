from test_framework import generic_test


def swap_bits(x, i, j):
    # bits are different
    if (x >> i) & 1 != (x >> j) & 1:
        # we swap by flipping both
        x ^= 1 << i
        x ^= 1 << j
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
