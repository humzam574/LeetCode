class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = [-1] * len(nums)
        def dp(i):
            if i + nums[i] >= len(nums) - 1: return True
            if mem[i] != -1: return mem[i]
            for j in range(1,nums[i]+1):
                if dp(i+j):
                    mem[i] = True
                    return True
            mem[i] = False
            return False
        return dp(0)