class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        r, mx, l, mn = -1, -10001, len(nums), 10001
        for i in range(l):
            if nums[i] >= mx: mx = nums[i]
            else: r = i
        for i in range(r, -1, -1):
            if nums[i] <= mn: mn = nums[i]
            else: l = i
        return max(0, r - l + 1)