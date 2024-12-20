# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(leftNode, rightNode, level):
            if leftNode is None or rightNode is None:
                return
            if (level % 2 != 0):
                leftNode.val, rightNode.val = rightNode.val, leftNode.val
            traverse(leftNode.left, rightNode.right,  level+1)
            traverse(leftNode.right, rightNode.left, level+1)
        
        traverse(root.left, root.right, 1)
        return root