class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 2
        if len(nums) == 1: return 0#nums[0]
        if nums[0] > nums[1]: return 0#nums[0]
        if nums[-1] > nums[-2]: return len(nums) - 1#nums[-1]
        while l <= r and r < len(nums) - 1 and l > 0:
            m = (l + r) // 2
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m
            elif nums[m - 1] < nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return -1