class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        l = 0
        if 1 not in nums: return 0
        prev = nums.index(1)
        ans = 1
        for r in range(prev + 1, len(nums)):
            if nums[r]:
                ans = ans * (r - prev) %1_000_000_007
                prev = r
        return ans % (1_000_000_007)
                