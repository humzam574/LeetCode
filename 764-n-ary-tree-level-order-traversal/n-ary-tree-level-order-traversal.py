"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.ans = []
        def dfs(curr, lev):
            if not curr:
                return
            if lev >= len(self.ans):
                self.ans.append([])
            self.ans[lev].append(curr.val)
            for c in curr.children:
                dfs(c, lev + 1)
        dfs(root, 0)
        return self.ans