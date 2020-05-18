from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                        scores: List[int]) -> int:

    '''
    Idea: At each step you either make a point with score = scores[i] or you don't.
    
    Solution: cache[i][j] = # of ways to make j points using plays from scores[0..i]

    cache[i][j] = cache[i-1][j] + cache[i][j - scores[i]]
                        = # of ways to score j with scores[0..i-1]
                            + # of ways to score (j-scores[i]) with scores[0..i]

    Time Complexity: O(final_score * len(scores))
    Space Complexity: O(final_score * len(scores))
    '''

    # Base Case: 1 way to have 0 points
    cache = [ [1] + [0] * final_score for _ in scores]

    for i in range(len(scores)):
        for j in range(1, final_score + 1):
            with_this_play = (cache[i][j - scores[i]] 
                                    if j >= scores[i] else 0)
        
            without_this_play = cache[i-1][j] if i >= 1 else 0
    
            cache[i][j] = with_this_play + without_this_play

    return cache[-1][final_score]

def num_combinations_for_final_score(final_score: int,
                                        scores: List[int]) -> int:
    '''
    Same solution as above, but optimized for space complexity by recycling
    two rows instead of len(scores) rows.

    Time Complexity: O(final_score * len(scores))
    Space Complexity: O(final_score)
    '''

    # Base Case: 1 way to have 0 points
    cache = [ [1] + [0] * final_score for _ in range(2)]

    for i in range(len(scores)):
        k = i % 2
        for j in range(1, final_score + 1):
            without_this_play = cache[abs(k-1)][j] if i >= 1 else 0
        
            with_this_play = (cache[k][j - scores[i]] 
                                    if j >= scores[i] else 0)
        
    
            cache[k][j] = with_this_play + without_this_play

    answer_row = len(scores) % 2 - 1
    return cache[answer_row][final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
