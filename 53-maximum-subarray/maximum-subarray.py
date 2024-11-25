class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, curr + num)
            maxSum = max(maxSum, curr)
        return maxSum