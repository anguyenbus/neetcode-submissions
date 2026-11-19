# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        count = 0
        while cur or stack:
            # go left: push every node on the way down
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # visit: the top of the stack is the next smallest value
            cur = stack.pop()
            count += 1

            # found it: this is the k-th value we've visited
            if count == k:
                return cur.val

            cur = cur.right
