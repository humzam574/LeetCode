class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = ans = nums[0]
        for i in nums[1:]:
            curr = i if curr < 0 else curr + i
            ans = max(ans, curr)
        return ans