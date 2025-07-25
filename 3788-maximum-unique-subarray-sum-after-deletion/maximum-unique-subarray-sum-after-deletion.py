class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = 0
        st = set(nums)
        for num in st:
            if num > 0:
                ans += num
        if ans == 0:
            return max(st)
        return ans