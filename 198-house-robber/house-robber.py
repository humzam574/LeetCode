class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, cont, tot):
            if i == len(nums):
                return tot
            if (i, cont) in memo:
                return tot+memo[i, cont]
            if cont:
                memo[i, cont] = max(dp(i + 1, False, nums[i]), dp( i+ 1, True, 0))
                return tot+memo[i, cont]
            else:
                memo[i,cont] = dp(i + 1, True, 0)
                return tot+memo[i, cont]
        return dp(0, True, 0)