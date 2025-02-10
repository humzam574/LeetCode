class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        a, b, c = nums[0], nums[0], 0
        for i in range(1,len(nums)):
            if nums[i] >= a:
                if nums[i] > b: b = nums[i]
            else: c, a = i, b
        return c + 1 