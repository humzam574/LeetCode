# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftLimit, rightLimit):
            if not node:
                return True
            
            if node.val <= leftLimit or node.val >= rightLimit:
                return False
            
            return dfs(node.left, leftLimit, node.val) and dfs(node.right, node.val, rightLimit)
        
        return dfs(root, -float('inf'), float('inf'))