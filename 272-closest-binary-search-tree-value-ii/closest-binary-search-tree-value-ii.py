# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        queue = deque()

        def dfs(node):
            if not node: return

            dfs(node.left)
            queue.append(node.val)
            if len(queue) > k:
                if abs(queue[-1] - target) < abs(queue[0] - target):
                    queue.popleft()
                else:
                    queue.pop()
                    return
            dfs(node.right)

        dfs(root)
        return list(queue)