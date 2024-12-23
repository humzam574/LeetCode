# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        self.levs = []
        def los(lev, curr):
            if curr:
                if lev >= len(self.levs):
                    self.levs.append([])
                self.levs[lev].append(curr.val)
                los(lev+1, curr.left)
                los(lev+1, curr.right)
        los(0, root)
        #print(self.levs)
        ans = 0
        for lev in self.levs:
            dict = {num : idx for idx, num in enumerate(lev)}
            #print(dict)
            srt = sorted(lev)
            #print(ans)
            #seen = set()
            for i, num in enumerate(srt):
                if i != dict[num]:# and num not in seen:
                    swp = dict[num]
                    dict[num], dict[lev[i]] = dict[lev[i]], dict[num]
                    lev[i], lev[swp] = lev[swp], lev[i]
                    ans+=1
                #print(dict)
            #print()
        return ans
                    