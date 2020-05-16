from test_framework import generic_test

def parity(x: int) -> int:
    '''
    Uses XOR associative and commutative properties and computes
    p(b_63, b_62, ..., b_0) = p(b_63, ..., b_32 XOR b_31, ..., b_0)
    and so on recursively.

    Time Complexity: O(log n) where n is the number of bits in x
    '''
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

def parity2(x: int) -> int:
    '''
    Tests each bit in x and stores the result in mod 2

    Time Complexity: O(n) where n is the number of bits in x
    Space Complexity: O(1)
    '''
    result = 0
    
    while x:
        result ^= x & 1
        x >>= 1
    
    return result

def parity3(x: int) -> int:
    '''
    Iterates through only the set bits in x and store the result mod 2

    Time Complexity: O(k) where k is number of set bits in x
    Space Complexity: O(1)
    '''
    result = 0

    while x:
        # store result mod 2
        result ^= 1
        x &= x-1

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
