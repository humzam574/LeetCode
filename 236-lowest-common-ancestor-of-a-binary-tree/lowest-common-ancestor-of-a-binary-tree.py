# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancs = []
        def dfs(curr, anc):
            if curr:
                if curr == p or curr == q:
                    self.ancs.append(anc)
                dfs(curr.left, anc + ['l'])
                dfs(curr.right, anc + ['r'])
        dfs(root, [])
        p1 = self.ancs[0]
        p2 = self.ancs[1]
        for i in range(min(len(p1), len(p2))):
            if p1[i] != p2[i]:
                return root
            root = root.left if p1[i] == 'l' else root.right
        return root