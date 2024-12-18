class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans, curr, idx, n = 0, nums[0], 0, len(nums)
        for i in range(1, n):
            if nums[i] > curr: ans, curr, idx = ans + (i - idx) * curr, nums[i], i
        return ans + (n - 1 - idx) * curr