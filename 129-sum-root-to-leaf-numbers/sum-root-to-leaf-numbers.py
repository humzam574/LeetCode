# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(val, rt):
            if not rt:
                return
            if not (rt.right or rt.left):
                self.ans+=(val*10 + rt.val)
                return
            if rt.right:
                dfs(val*10 + rt.val, rt.right)
            if rt.left:
                dfs(val * 10 + rt.val, rt.left)
        dfs(0, root)
        return self.ans
            