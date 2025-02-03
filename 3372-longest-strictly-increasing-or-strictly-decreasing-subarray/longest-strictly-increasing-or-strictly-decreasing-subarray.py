class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr = 1
        ans = 1
        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                curr = 1
            else:
                curr += 1
                ans = max(ans, curr)
        curr = 1
        for r in range(1, len(nums)):
            if nums[r] >= nums[r - 1]:
                curr = 1
            else:
                curr += 1
                ans = max(ans, curr)
        return ans