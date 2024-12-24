class Solution:
    def maxDistinctElements(self, nums, k):
        #k = 2
        #2, 2, 2, 2, 2, 3, 3, 3
        #0, 1, 2, 3, 4, 5, x, x
        nums.sort()
        low = nums[0] - k - 1
        ans = 0
        for num in nums:
            if num - k > low:
                low = num - k
                ans += 1
            elif num + k > low:
                low += 1
                ans += 1
        return ans