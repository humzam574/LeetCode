class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        nums = [0] + nums
        #print(nums)
        l, r, ans = 0, 1, len(nums)
        while r < len(nums):
            if nums[r] - nums[l] >= target:
                ans = min(ans, r - l)
                l += 1
            else:
                r += 1
        return 0 if ans == len(nums) else ans