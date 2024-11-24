class Solution:
    def rob(self, nums: List[int]) -> int:
        prevTwo = prevOne = 0
        for n in nums:
            temp, prevTwo, prevOne = prevTwo, prevOne, max(prevTwo + n, prevOne)
        return prevOne