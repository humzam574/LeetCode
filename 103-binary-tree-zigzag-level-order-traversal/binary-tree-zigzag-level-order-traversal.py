# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        def levelOrder(rt, dep):
            if dep >= len(self.ans): self.ans.append([])
            self.ans[dep].append(rt.val)
            if rt.left: levelOrder(rt.left, dep+1)
            if rt.right: levelOrder(rt.right, dep+1)
        if root: levelOrder(root, 0)
        for i in range(1, len(self.ans), 2):
            self.ans[i] = self.ans[i][::-1]
        return self.ans
