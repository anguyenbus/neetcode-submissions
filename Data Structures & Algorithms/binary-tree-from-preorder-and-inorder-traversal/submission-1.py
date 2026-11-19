# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # setup: find any value's inorder position instantly
        idx = {val: i for i, val in enumerate(inorder)}
        self.pre_i = 0  # next root in preorder

        def build(l, r):
            # base case: empty range means no node
            if l > r:
                return None

            # main work: take the next preorder value as the root
            root = TreeNode(preorder[self.pre_i])
            self.pre_i += 1

            # split: O(1) lookup instead of .index()
            mid = idx[root.val]

            # ask children: LEFT first (this matters!)
            root.left = build(l, mid - 1)
            # ask children: the rest is the right side
            root.right = build(mid + 1, r)

            return root

        return build(0, len(inorder) - 1)