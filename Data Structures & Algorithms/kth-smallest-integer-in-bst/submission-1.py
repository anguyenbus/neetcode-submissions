# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None

        def inorder(node):
            # base case: empty node, or answer already found
            if not node or self.ans is not None:
                return
            # left child first: smaller values
            inorder(node.left)
            # visit the current node
            self.count += 1
            if self.count == k:
                self.ans = node.val
                return
            # right child: bigger values
            inorder(node.right)

        inorder(root)
        return self.ans
