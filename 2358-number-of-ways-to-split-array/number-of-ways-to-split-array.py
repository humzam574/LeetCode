class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l, r, ans = 0, (sum(nums)+1)//2, 0
        for i in range(len(nums)-1): l, ans = l + nums[i], ans + (l + nums[i] >= r)
        return ans