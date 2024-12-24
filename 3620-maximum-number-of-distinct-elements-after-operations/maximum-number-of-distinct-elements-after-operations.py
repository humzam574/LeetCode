class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        low, ans = nums[0] - k - 1, 0
        for num in nums:
            if num + k > low: low, ans = max(low + 1, num - k), ans + 1
        return ans