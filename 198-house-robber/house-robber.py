class Solution:
    def rob(self, nums: List[int]) -> int:
        prevTwo = prevOne = 0
        for n in nums:
            temp = prevTwo
            prevTwo = prevOne
            prevOne = max(temp + n, prevOne)
        return prevOne