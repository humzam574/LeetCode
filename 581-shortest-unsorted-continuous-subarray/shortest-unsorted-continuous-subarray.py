class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        r, mx, l, mn = -1, -10001, len(nums), 1e6
        for i in range(l):
            if nums[i] >= mx: mx = nums[i]
            else: r = i
        for i in range(l - 1, -1, -1):
            if nums[i] <= mn: mn = nums[i]
            else: l = i
        return max(0, r - l + 1)