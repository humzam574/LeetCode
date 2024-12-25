# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def los(dep, curr):
            if not curr: return
            if dep >= len(self.ans): self.ans.append(curr.val)
            else: self.ans[dep] = max(self.ans[dep], curr.val)
            los(dep + 1, curr.left); los(dep + 1, curr.right)

        self.ans = []
        los(0, root)
        return self.ans