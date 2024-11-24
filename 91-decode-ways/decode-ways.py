class Solution:
    def numDecodings(self, s: str) -> int:
        #self.ans = 0
        memo = {}
        def dp(i, curr):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            if i < (len(s) - 1) and ((s[i] == "2" and s[i+1] <= "6") or s[i] < "2"):
                temp = dp(i + 1, 0) + dp(i + 2, 0)
                memo[i] = temp
                return curr + temp
            temp = dp(i + 1, 0)
            memo[i] = temp
            return curr + temp
        return dp(0,0)