class Solution:
    def canSplitArray(self,nums,m):
        return True if len(nums) < 3 else any(nums[i]+nums[i+1]>=m for i in range(len(nums)-1))