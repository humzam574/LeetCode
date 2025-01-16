class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[-inf, -inf] for i in range(len(nums))]
        curr = max(0, nums[0])
        dp[0][0] = nums[0]
        for i, num in enumerate(nums[1:]):
            curr = max(num, curr + num)
            dp[i+1][0] = curr
        dp[0][1] = nums[0]**2
        for i, num in enumerate(nums[1:]):
            dp[i+1][1] = max(dp[i][1] + num, dp[i][0] + num**2, num**2)#, dp[i][0] + (num ** 2 - num))
        high = -inf
        for i in range(len(dp)):
            high = max(high, dp[i][1])
        return high