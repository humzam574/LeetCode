class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = 1
        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                l = r
            else:
                ans = max(ans, r - l + 1)
        l = 0
        for r in range(1, len(nums)):
            if nums[r] >= nums[r - 1]:
                l = r
            else:
                ans = max(ans, r - l + 1)
        return ans