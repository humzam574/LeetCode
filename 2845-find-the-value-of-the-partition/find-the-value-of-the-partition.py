class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[1] - nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i+1] - nums[i] < ans: ans = nums[i+1] - nums[i]
        return ans