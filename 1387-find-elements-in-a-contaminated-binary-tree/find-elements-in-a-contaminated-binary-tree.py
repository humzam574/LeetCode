# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.inside = {0}
        def dfs(root, val):
            if not root:
                return
            if root.right:
                #val = 2 * val + 
                self.inside.add(2*val + 2)
                dfs(root.right, 2*val + 2)
            if root.left:
                self.inside.add(2*val + 1)
                dfs(root.left, 2*val + 1)
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.inside


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)