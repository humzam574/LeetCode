# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.kids = {}
        self.ans = 1
        def dfs(curr):
            if not curr:
                return 0
            if not curr.left and not curr.right:
                self.kids[curr] = 1
                return 1
            val = 1 + dfs(curr.left) + dfs(curr.right)
            self.kids[curr] = val
            return val
        dfs(root)
        # for k, v in self.kids.items():
        #     print(v, end = " ")
        #     print(k)
        #     print()
        def bst(node, leftLimit, rightLimit):
            if not node:
                return True
            
            if node.val <= leftLimit or node.val >= rightLimit:
                return False

            return bst(node.left, leftLimit, node.val) and bst(node.right, node.val, rightLimit)
        def recurse(curr):
            if bst(curr, -inf, inf):
                self.ans = max(self.ans, self.kids[curr])
            else:
                if curr.left:
                    recurse(curr.left)
                if curr.right and self.ans < self.kids[curr.right]:
                    recurse(curr.right)
        recurse(root)
        return self.ans