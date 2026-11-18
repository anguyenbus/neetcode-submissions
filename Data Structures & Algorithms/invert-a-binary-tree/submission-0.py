# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Step 1: swap the two children
        root.left, root.right = root.right, root.left

        # step 2: ask each child to invert its own subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        # step 3: return root
        return root