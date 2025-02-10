class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        a = nums[0]
        b = nums[0]
        c = 0
        for i in range(1,len(nums)):
            if nums[i] >= a:
                if nums[i] > b:
                    b = nums[i]
            else:
                c = i
                a = b
        return c + 1 