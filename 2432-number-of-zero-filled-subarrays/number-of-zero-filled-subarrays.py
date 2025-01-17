class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = k = 0
        for n in nums:
            if (n == 0): k += 1
            else: ans, k = ans + (k * (k + 1)) // 2, 0
        return ans + (k * (k + 1)) // 2