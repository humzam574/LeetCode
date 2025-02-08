class Solution:
    def moveZeroes(self, nums): nums.sort(key = lambda x : x == 0)