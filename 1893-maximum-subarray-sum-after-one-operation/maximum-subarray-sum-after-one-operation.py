class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        res = w = wo = 0
        for num in nums: wo, w = wo+num, max(w+num, wo+num*num); wo = max(0, wo); res = max(res, w)
        return res