class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(); n, ans, l, curr = len(nums), 1, 0, 0
        for r in range(1, n):
            curr += (nums[r] - nums[r-1])*(r - l)
            while curr > k and l <= r: curr, l = curr - nums[r] + nums[l], l + 1
            ans = max(ans, r - l + 1)
        return ans