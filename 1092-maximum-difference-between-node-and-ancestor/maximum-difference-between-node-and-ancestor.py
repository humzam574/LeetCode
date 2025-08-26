# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(curr, low, high):
            if not curr:
                return
            if abs(curr.val - low) > self.ans:
                self.ans = abs(curr.val - low)
            if abs(curr.val - high) > self.ans:
                self.ans = abs(curr.val - high)
            dfs(curr.left, min(curr.val, low), max(curr.val, high))
            dfs(curr.right, min(curr.val, low), max(curr.val, high))
        dfs(root, root.val, root.val)
        return self.ans