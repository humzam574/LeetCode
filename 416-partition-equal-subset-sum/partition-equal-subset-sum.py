class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        memo = {}
        def bt(curr, i):
            if 2*curr == tot:
                return True
            if i == len(nums) - 1:
                return False
            if (curr, i) in memo:
                return memo[curr,i]
            temp = bt(curr, i+1) or bt(curr + nums[i+1], i+1)
            memo[curr, i] = temp
            return temp
        return bt(0,0)