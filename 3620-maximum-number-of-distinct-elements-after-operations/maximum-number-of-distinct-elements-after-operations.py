class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        low, ans = nums[0] - k - 1, 0
        for n in nums:
            if n > low - k: low, ans = max(low + 1, n - k), ans + 1
        return ans