class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        curr, ans = 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[curr]: ans, curr = ans + (i-curr)*nums[curr], i
        return ans + (len(nums)-1-curr)*nums[curr]