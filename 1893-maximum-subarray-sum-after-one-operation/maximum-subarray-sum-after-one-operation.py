class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[-inf, -inf] for i in range(len(nums))]
        curr = max(0, nums[0])
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            dp[i][0] = curr
        dp[0][1] = nums[0]**2
        for i in range(1, len(nums)):
            dp[i][1] = max(dp[i - 1][1] + nums[i], dp[i - 1][0] + nums[i]**2, nums[i]**2)#, dp[i][0] + (num ** 2 - num))
        high = -inf
        for i in range(len(dp)):
            high = max(high, dp[i][1])
        return high