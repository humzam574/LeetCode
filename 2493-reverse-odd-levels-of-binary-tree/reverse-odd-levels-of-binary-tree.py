class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(l, r, odd):
            if l: l.val, r.val = (r.val, l.val) if odd else (l.val, r.val); traverse(l.left, r.right, not odd); traverse(l.right, r.left, not odd)
        return traverse(root.left, root.right, True) or root