# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.r1 = set()
        def dfs(node, check):
            if not node:
                return False
            if check and target - node.val in self.r1:
                return True
            if not check:
                self.r1.add(node.val)
            return dfs(node.left, check) or dfs(node.right, check)
        dfs(root1, False)
        return dfs(root2, True)