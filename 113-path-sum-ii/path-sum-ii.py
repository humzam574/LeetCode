# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def dfs(curr, tot, node):
            if not node:
                return
            curr.append(node.val)
            tot += node.val
            if not node.left and not node.right and tot == targetSum: self.ans.append(curr[:])
            if node.left: dfs(curr, tot, node.left)
            if node.right: dfs(curr, tot, node.right)
            curr.pop()
        dfs([], 0, root)
        return self.ans