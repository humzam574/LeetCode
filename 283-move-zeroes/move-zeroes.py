class Solution:
    def moveZeroes(self, nums):
        nums.sort(key = lambda x : int(not bool(x)))
        return nums