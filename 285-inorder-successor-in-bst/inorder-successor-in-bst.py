# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, p):
        if not root:
            return
        if root.val>p.val:
            self.successor = root
            self.dfs(root.left,p)
        else:
            self.dfs(root.right,p)

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.successor = None
        self.dfs(root, p)
        return self.successor