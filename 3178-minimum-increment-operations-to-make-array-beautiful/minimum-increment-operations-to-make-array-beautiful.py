class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        # dp[0] = max(0, k - nums[0])
        # dp[1] = max(0, k - nums[1])
        # dp[2] = max(0, k - nums[2])
        for i in range(len(dp)):
            temp = k - nums[i]
            if temp >= 0:
                dp[i] = temp + min(dp[i - 3], dp[i - 2], dp[i - 1])
            else:
                dp[i] = min(dp[i - 3], dp[i - 2], dp[i - 1])
        return min(dp[-2], dp[-1], dp[-3])