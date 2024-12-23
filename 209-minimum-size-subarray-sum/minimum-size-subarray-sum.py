class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, curr, ans = 0, 0, 0, len(nums) + 1
        for r in range(0, ans - 1):
            curr += nums[r]
            while curr >= target: ans, curr, l = min(ans, r - l + 1), curr - nums[l], l + 1
        return (l != 0) * ans