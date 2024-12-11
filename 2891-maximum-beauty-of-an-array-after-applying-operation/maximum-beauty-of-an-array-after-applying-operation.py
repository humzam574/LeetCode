class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, ans = 0, 0, 1
        while r < len(nums):
            if nums[r] <= 2*k+nums[l]: r, ans = r + 1, max(ans, r - l + 1)
            else: l+=1
        return ans
