class Solution:
    def minOperations(self, nums: List[int]) -> int:
        curr, targ = 0, 1
        for num in nums:
            if num != targ: curr, targ = curr + 1, 1 - targ
        return curr