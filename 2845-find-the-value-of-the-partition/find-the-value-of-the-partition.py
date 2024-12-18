class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = inf
        for i in range(0, len(nums) - 1):
            ans = min(ans, abs(nums[i] - nums[i+1]))
        return ans