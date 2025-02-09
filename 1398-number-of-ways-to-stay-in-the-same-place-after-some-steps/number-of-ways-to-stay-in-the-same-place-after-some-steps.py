class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(curr, remain):
            if remain == 0:
                return curr == 0
            ans = dp(curr, remain - 1)
            if curr > 0:
                ans = (ans + dp(curr - 1, remain - 1)) % MOD
            
            if curr < arrLen - 1:
                ans = (ans + dp(curr + 1, remain - 1)) % MOD
                
            return ans
        
        MOD = 10 ** 9 + 7
        return int(dp(0, steps))