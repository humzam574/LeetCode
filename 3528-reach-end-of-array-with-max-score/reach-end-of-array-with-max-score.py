class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n, last, ans = len(nums), 1, 0
        for i in range(n - 1): last, ans = max(nums[i], last), ans + max(nums[i], last)
        return ans