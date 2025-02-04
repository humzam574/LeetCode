class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l = 0
        curr = nums[0]
        ans = max(nums)
        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                curr = nums[r]
                l = r
            else:
                curr += nums[r]
                ans = max(ans, curr)
        return ans
