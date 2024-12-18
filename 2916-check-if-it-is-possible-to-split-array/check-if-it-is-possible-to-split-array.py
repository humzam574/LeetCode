class Solution:
    def canSplitArray(self,nums,m):
        if len(nums) < 3: return True
        for i in range(1, len(nums)): 
            if nums[i-1] + nums[i] >= m: return True
        return False