class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot, n = sum(nums), len(nums)
        if tot % 2: return False
        memo = [[-1] * (tot // 2 + 1) for i in range(n + 1)]
        def bt(curr, i):
            if curr == 0 or i >= n or curr < 0: return curr == 0
            if memo[i][curr] != -1: return memo[i][curr]
            memo[i][curr] = bt(curr, i + 1) or bt(curr - nums[i], i + 1)
            return memo[i][curr]
        return bt(tot // 2, 0)