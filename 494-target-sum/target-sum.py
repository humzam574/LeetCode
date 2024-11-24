class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def bt(curr, i):
            if (curr, i) in memo: return memo[curr,i]
            if i == len(nums): return int(curr == target)
            temp = bt(curr + nums[i], i + 1) + bt(curr - nums[i], i + 1)
            memo[curr, i] = temp
            return temp
        return bt(0, 0)