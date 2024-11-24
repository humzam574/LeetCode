class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i, curr):
            if i >= len(s) or s[i] == "0" or i in memo: return int(i >= len(s)) if i not in memo else memo[i]
            memo[i] = dp(i + 1, 0)
            if i < (len(s) - 1) and ((s[i] == "2" and s[i+1] <= "6") or s[i] < "2"): memo[i] += dp(i + 2, 0)
            return curr + memo[i]
        return dp(0, 0)