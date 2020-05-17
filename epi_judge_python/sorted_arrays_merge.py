from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    '''
    First, add smallest element from every array to min_heap,
    then until min_heap is empty add the smallest element in min_heap
    to answer, and fetch the next element from the array it came from.

    Time Complexity: O(n log k), where k is number of arrays.
    Space Complexity: O(k) if we do not consider the space for answer.
    '''
    min_heap = []

    # get list of iterators for each array
    iters = [iter(x) for x in sorted_arrays]

    # push first element of each array into min_heap
    for i, it in enumerate(iters):
        first = next(it, None)
        if first is not None:
            heapq.heappush(min_heap, (first, i))

    result = []
    while min_heap:
        smallest, smallest_idx = heapq.heappop(min_heap)
        smallest_iter = iters[smallest_idx]
        
        result.append(smallest)

        next_element = next(smallest_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_idx))
            
    return result

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    '''
    Uses builtin heapq.merge function. Complexity should be similar
    to the one above.
    '''
    return list(heapq.merge(*sorted_arrays))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
