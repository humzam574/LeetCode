# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_found = False
        self.q_found = False
        res = self.dfs(root, p, q)
        return res if self.p_found and self.q_found else None
    
    def dfs(self, root, p, q):
        if not root:
            return None
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if root.val == p.val:
            self.p_found = True
            return root
        if root.val == q.val:
            self.q_found = True
            return root
        
        if left and right:
            return root
        return left or right