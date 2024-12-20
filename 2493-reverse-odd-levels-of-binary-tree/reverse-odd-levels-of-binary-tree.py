# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(leftNode, rightNode, odd):
            if leftNode is None or rightNode is None:
                return
            if (odd): leftNode.val, rightNode.val = rightNode.val, leftNode.val
            traverse(leftNode.left, rightNode.right,  not odd)
            traverse(leftNode.right, rightNode.left, not odd)
        
        traverse(root.left, root.right, True)
        return root