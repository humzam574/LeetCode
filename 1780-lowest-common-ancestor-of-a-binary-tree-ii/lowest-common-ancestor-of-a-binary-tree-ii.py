# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.paths = [None, None]
        def dfs(curr, path):
            if not curr: return
            if curr.val == p.val:
                self.paths[0] = path
            elif curr.val == q.val:
                self.paths[1] = path
            dfs(curr.left, path + "l")
            dfs(curr.right, path + "r")
        dfs(root, "")
        if not self.paths[0] or not self.paths[1]: return None
        for i in range(min(len(self.paths[0]), len(self.paths[1]))):
            if self.paths[0][i] != self.paths[1][i]:
                return root
            if self.paths[0][i] == "l":
                root = root.left
            else:
                root = root.right
        return root