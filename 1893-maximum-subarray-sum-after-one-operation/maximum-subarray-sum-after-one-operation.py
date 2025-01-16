class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[-inf, -inf] for i in range(len(nums))]; dp[0] = [nums[0], nums[0] ** 2]; curr = max(0, nums[0])
        for i in range(1, len(nums)): curr = max(nums[i], curr + nums[i]); dp[i][0] = curr; dp[i][1] = max(dp[i - 1][1] + nums[i], dp[i - 1][0] + nums[i]**2, nums[i]**2)
        return max(dp[i][1] for i in range(len(dp)))