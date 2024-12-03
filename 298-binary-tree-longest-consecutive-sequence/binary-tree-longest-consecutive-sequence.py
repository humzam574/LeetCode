class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        def dfs(rt, prev, curr):
            if rt:
                if rt.val - 1 == prev:
                    self.ans = max(self.ans, curr + 1)
                else:
                    curr = 0
                dfs(rt.right, rt.val, curr + 1)
                dfs(rt.left, rt.val, curr + 1)
        dfs(root, root.val, 1)
        return self.ans