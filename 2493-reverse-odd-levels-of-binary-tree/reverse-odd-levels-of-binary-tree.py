# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #put all the odd values into a 2d array
        #go through with a left side dfs and use a ptr to keep track of which value it should be
        odds = []
        def dfs(lev, curr):
            if curr:
                if lev % 2 == 0:
                    dfs(lev + 1, curr.left)
                    dfs(lev + 1, curr.right)
                else:
                    dep = lev // 2
                    if len(odds) <= dep:
                        odds.append([])
                    odds[dep].append(curr.val)
                    dfs(lev + 1, curr.left)
                    dfs(lev + 1, curr.right)
        dfs(0, root)
        #print(odds)
        self.ptrs = [0] * len(odds)
        def dfs2(lev, curr):
            if curr:
                if lev % 2 == 0:
                    dfs2(lev + 1, curr.right)
                    dfs2(lev + 1, curr.left)
                else:
                    dep = lev // 2
                    #print("reassigning " + str(curr.val) + " to " + str(odds[dep][self.ptrs[dep]]))
                    curr.val = odds[dep][self.ptrs[dep]]
                    self.ptrs[dep]+=1
                    dfs2(lev + 1, curr.right)
                    dfs2(lev + 1, curr.left)
        dfs2(0, root)
        return root