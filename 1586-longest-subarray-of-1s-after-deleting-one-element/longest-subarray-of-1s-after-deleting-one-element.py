class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr < r - l:
                curr -= nums[l]
                l += 1
            ans = max(ans, r - l)

        return min(len(nums) - 1, ans)