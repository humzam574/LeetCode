class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = curr
        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                curr = nums[r]
            else:
                curr += nums[r]
                ans = max(ans, curr)
        return ans
