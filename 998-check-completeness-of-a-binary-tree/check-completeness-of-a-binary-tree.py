# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        self.arr, end = [], False
        def los(dep, curr):
            if dep >= len(self.arr): self.arr.append([])
            if curr: self.arr[dep].append(curr.val); los(dep + 1, curr.left); los(dep + 1, curr.right)
            else: self.arr[dep].append(None)
        los(0, root); self.arr.pop()
        for i in range(len(self.arr) - 1):
            for n in self.arr[i]:
                if n == None: return False
        for n in self.arr[-1]:
            if n == None: end = True
            elif end: return False
        return True