# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, count, ans):
        if root:
            self.inorder(root.left, count, ans)
            #count.append(root.val)
            #print(count)
            if count[0] is not None and root.val <= count[0]:
                ans[0] = -1
            else:
                count[0] = root.val
                self.inorder(root.right, count, ans)
        #return True
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        count = [None]
        ans = [0]
        
        self.inorder(root, count, ans)
        return ans[0] != -1