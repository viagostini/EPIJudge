from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import namedtuple

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    answer = namedtuple('answer', ('balanced', 'height'))
    
    def check_balanced(tree):
        if not tree:
            return answer(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return answer(False, -1)
        
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return answer(False, -1)

        root_result = abs(right_result.height - left_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        
        return answer(root_result, height)

    return check_balanced(tree).balanced

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
