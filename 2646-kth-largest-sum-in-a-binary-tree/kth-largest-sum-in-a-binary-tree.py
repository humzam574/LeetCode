# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def dfs(rt, dep):
            if not rt: return
            if dep >= len(self.arr):
                self.arr.append(rt.val)
            else:
                self.arr[dep] += rt.val
            dfs(rt.right, dep+1)
            dfs(rt.left, dep+1)
        dfs(root,0)
        if len(self.arr) < k:
            return -1
        self.arr.sort(reverse = True)
        return self.arr[k-1]