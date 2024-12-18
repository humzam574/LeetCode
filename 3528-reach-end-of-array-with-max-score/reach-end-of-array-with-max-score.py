class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        curr = 0
        n = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] > n:
                ans+=((i-curr)*n)
                curr = i
                n = nums[i]
        return ans + (len(nums)-1-curr)*nums[curr]