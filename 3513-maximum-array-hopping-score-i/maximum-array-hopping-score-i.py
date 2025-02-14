class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for j in range(1, n):
            for i in range(j):
                dp[j] = max(dp[j], dp[i] + (j - i)*nums[j])
        return dp[-1]