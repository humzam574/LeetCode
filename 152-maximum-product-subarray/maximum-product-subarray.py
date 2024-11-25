class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        high, low, ans = 1, 1, nums[0]
        for num in nums:
            temp = (num, num * high, num * low)
            high = max(temp)
            low = min(temp)
            ans = max(ans, high)
        return ans