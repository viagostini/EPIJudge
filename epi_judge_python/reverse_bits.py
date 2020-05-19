from test_framework import generic_test


PRECOMPUTED_REVERSE = [0] * (1 << 16)

def reverse_bits(x: int) -> int:
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF

    y0 = PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE)
    y1 = PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE)
    y2 = PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
    y3 = PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK]

    return y0 | y1 | y2 | y3


def swap_bits(x, i, j):
    # bits are different
    if (x >> i) & 1 != (x >> j) & 1:
        # we swap by flipping both
        x ^= 1 << i
        x ^= 1 << j
    return x

def compute_reverse_bits(x, bits):
    '''
    For bits = 64, this is also a solution to the problem.
    '''
    for i in range(bits//2):
        x = swap_bits(x, i, bits-i-1)
    return x

# precomputes table of all 16-bit reverses
def compute_reverse_table():
    for i in range(1 << 16):
        PRECOMPUTED_REVERSE[i] = compute_reverse_bits(i, 16)

if __name__ == '__main__':
    compute_reverse_table()
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
