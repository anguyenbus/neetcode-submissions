# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: TreeNode, low:float, high:float) -> bool:
            # base case
            if node is None:
                return True

            # this node must be strictly between its allowed bounds
            if not (low < node.val < high):
                return False

            # ask children
            return (valid(node.left, low, node.val) and valid(node.right, node.val, high))
            

        return valid (root, float("-inf"), float("inf"))