# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq = deque()
        bfs = deque([(root, 0)])
        offset = 0
        while bfs:
            node, delta = bfs.popleft()
            if delta < offset:
                dq.appendleft([])
                offset -= 1
            elif len(dq) <= delta - offset:
                dq.append([])
            dq[delta - offset].append(node.val)
            if node.left:
                bfs.append((node.left, delta - 1))
            if node.right:
                bfs.append((node.right, delta + 1))
        return list(dq)