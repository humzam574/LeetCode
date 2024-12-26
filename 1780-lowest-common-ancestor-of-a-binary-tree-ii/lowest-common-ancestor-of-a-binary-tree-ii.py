# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.nodes_found = False
        def dfs(node):
            if not node: return node
            left, right = dfs(node.left), dfs(node.right)
            self.nodes_found = self.nodes_found or (2 == (int(node in (p,q)) + int(bool(left)) + bool(right)))
            return node if (left and right) or node in (p, q) else left or right
        ans = dfs(root)
        return ans if self.nodes_found else None