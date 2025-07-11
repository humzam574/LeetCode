# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr
        curr = root
        prev = None
        v = p.val
        while curr and curr != p:
            if v < curr.val:
                prev = curr
                curr = curr.left
            else:
                curr = curr.right
        return prev
            