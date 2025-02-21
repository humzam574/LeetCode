# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        def dfs(node, val):
            if not node:
                return

            self.inside.add(val)
            dfs(node.left, 2 * val + 1)
            dfs(node.right, 2 * val + 2)
            
        self.inside = set()
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.inside


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)