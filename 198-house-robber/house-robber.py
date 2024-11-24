class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i, tot):
            if i >= len(nums) or i in memo:
                return tot+memo[i]
            memo[i] = max(dp(i + 2, nums[i]), dp(i+ 1, 0))
            return tot+memo[i]
        return dp(0, 0)