class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        if (sm + target) % 2 != 0 or sm < abs(target): return 0
        st = (sm + target) // 2
        dp = [1] + [0] * st
        for n in nums:
            for i in range(st, n - 1, -1): dp[i] = dp[i - n] + dp[i]
        return dp[st]