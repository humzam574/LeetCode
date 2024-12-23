# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minswap(lev):
            dict = {num : idx for idx, num in enumerate(lev)}
            srt = sorted(lev)
            swap = 0
            for i, num in enumerate(srt):
                if i != dict[num]:
                    swp = dict[num]
                    dict[num], dict[lev[i]] = dict[lev[i]], dict[num]
                    lev[i], lev[swp] = lev[swp], lev[i]
                    swap += 1
            return swap
        # self.levs = []
        # def los(lev, curr):
        #     if curr:
        #         if lev >= len(self.levs):
        #             self.levs.append([])
        #         self.levs[lev].append(curr.val)
        #         los(lev+1, curr.left)
        #         los(lev+1, curr.right)
        # los(0, root)
        # ans = 0
        # for lev in self.levs:
        dq = deque()
        dq.append(root)
        ans = 0
        while dq:
            lev = []
            for i in range(len(dq)):
                if dq[0].left: dq.append(dq[0].left)
                if dq[0].right: dq.append(dq[0].right)
                lev.append(dq.popleft().val)
            ans += minswap(lev)
        return ans
                    