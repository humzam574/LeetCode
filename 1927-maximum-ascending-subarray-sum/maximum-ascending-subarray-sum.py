class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = curr = nums[0]
        for r in range(1, len(nums)): ans = max(ans, (curr := (curr + nums[r] if nums[r] > nums[r-1] else nums[r])))
        return ans