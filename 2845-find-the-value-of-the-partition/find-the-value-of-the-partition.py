class Solution:
    def findValueOfPartition(self, nums):
        nums.sort()
        return min(nums[i+1] - nums[i] for i in range(len(nums) - 1))