# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dq, end = deque([root]), False
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if not node: end = True
                else:
                    if end: return False
                    dq.append(node.left); dq.append(node.right)
        return True