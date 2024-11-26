class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        memo = {}
        def bt(curr, i):
            if curr == 0:
                return True
            if i >= len(nums):
                return False
            if curr < 0:
                return False
            if (curr, i) in memo:
                return memo[curr,i]
            temp = bt(curr, i+1) or bt(curr -nums[i], i+1)
            memo[curr, i] = temp
            return temp
        return bt(tot // 2, 0)