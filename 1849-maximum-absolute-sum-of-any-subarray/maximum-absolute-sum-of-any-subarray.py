class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #find the highest and then the lowest
        high = 0
        curr = 0
        for num in nums:
            curr += num
            if curr > 0:
                high = max(curr, high)
            else:
                curr = 0
        low = 0
        curr = 0
        for num in nums:
            curr -= num
            if curr > 0:
                low = max(curr, low)
            else:
                curr = 0
        return max(high, low)