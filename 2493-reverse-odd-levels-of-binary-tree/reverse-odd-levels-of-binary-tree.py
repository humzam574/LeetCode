# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(l, r, odd):
            if l is None or r is None: return
            if odd: l.val, r.val = r.val, l.val
            traverse(l.left, r.right,  not odd); traverse(l.right, r.left, not odd)
        traverse(root.left, root.right, True)
        return root