# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.heap = []
        self.len = 0
        heapify(self.heap)
        def dfs(curr):
            if not curr:
                return
            heappush(self.heap, (-abs(curr.val-target), curr.val))
            self.len+=1
            if self.len > k:
                heappop(self.heap)
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return [a[1] for a in self.heap]