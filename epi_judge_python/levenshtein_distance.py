from test_framework import generic_test

import functools

def levenshtein_distance(A: str, B: str) -> int:
    '''
    dist[i][j] = distance(A[:i], B[:j])

    Note: this version of the solution uses Python's 
    functool.lru_cache decorator for memoization. There is a more
    traditional solution below.

    Time Complexity: O(len(a) * len(b))
    Space Complexity: O(len(a) * len(b))
    '''
    
    @functools.lru_cache(None)
    def edit_distance(i, j):
        if i < 0:
            return j + 1
        
        if j < 0:
            return i + 1

        if A[i] == B[j]:
            return edit_distance(i-1, j-1)
        
        rem = edit_distance(i-1, j)
        ins = edit_distance(i, j-1)
        sub = edit_distance(i-1, j-1)
        
        return 1 + min(sub, rem, ins)
    
    return edit_distance(len(A) - 1, len(B) - 1)


def levenshtein_distance(A: str, B: str) -> int:
    '''
    dist[i][j] = distance(A[:i], B[:j])

    Time Complexity: O(len(a) * len(b))
    Space Complexity: O(len(a) * len(b))
    '''
    def edit_distance(i, j, dist={}):
        if i < 0:
            return j + 1
        
        if j < 0:
            return i + 1

        if (i, j) not in dist:
            if A[i] == B[j]:
                dist[(i, j)] = edit_distance(i-1, j-1)
            else:
                rem = edit_distance(i-1, j)
                ins = edit_distance(i, j-1)
                sub = edit_distance(i-1, j-1)
                
                dist[(i, j)] = 1 + min(sub, rem, ins)

        return dist[(i,j)]
    
    return edit_distance(len(A) - 1, len(B) - 1)



def levenshtein_distance(A, B):
    '''
    Iterative version of edit distance.

    Time Complexity: O(len(A) * len(B))
    Space Complexity: O(len(A) * len(B))
    '''
    
    from itertools import product

    def edit_distance(m, n):
        for i, j in product(range(m+1), range(n+1)):
            if i == 0:
                dist[i][j] = j
            elif j == 0:
                dist[i][j] = i

            elif A[i-1] == B[j-1]:
                dist[i][j] = dist[i-1][j-1]
            
            else:
                ins = dist[i][j-1]
                rem = dist[i-1][j]
                sub = dist[i-1][j-1]

                dist[i][j] = 1 + min(ins, rem, sub)

        return dist[m][n]

    m, n = len(A), len(B)
    dist = [ [0] * (n + 1) for _ in range(m + 1)]
    
    return edit_distance(m, n)


def levenshtein_distance(A, B):
    '''
    Iterative version of edit distance optimized for space by
    recycling two rows. For this we can also make our rows k
    elements wide, where k = min(len(A), len(B)) to optmize it
    even further.

    Time Complexity: O(len(A) * len(B))
    Space Complexity: O(min(len(A), len(B))
    '''

    from itertools import product

    def edit_distance(m, n):
        for i, j in product(range(m+1), range(n+1)):
            k = i % 2

            if i == 0:
                dist[k][j] = j
            elif j == 0:
                dist[k][j] = i

            elif A[i-1] == B[j-1]:
                dist[k][j] = dist[abs(k-1)][j-1]
            
            else:
                ins = dist[k][j-1]
                rem = dist[abs(k-1)][j]
                sub = dist[abs(k-1)][j-1]

                dist[k][j] = 1 + min(ins, rem, sub)

        return dist[m % 2][n]

    if len(A) < len(B):
        A, B = B, A

    m, n = len(A), len(B)
    dist = [ [0] * (n + 1) for _ in range(2)]
    
    return edit_distance(m, n)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
