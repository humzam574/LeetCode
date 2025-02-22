# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dash_map = {}
        dash_cnt = 0
        first_num = ""
        for ch in traversal:
            if ch == '-': break
            first_num += ch
        dash_map[0] = TreeNode(int(first_num))
        s = re.findall(r'(-+)(\d+)', traversal)
        for dash, num in s:
            dash_num = len(dash)
            num = int(num)
            n = TreeNode(num)
            fa = dash_map[dash_num - 1]
            if not fa.left:
                fa.left = n
            elif not fa.right:
                fa.right = n
            dash_map[dash_num] = n
        return dash_map[0]