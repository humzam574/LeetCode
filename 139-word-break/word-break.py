class Solution:
    def wordBreak(self, s: str, wo: List[str]) -> bool:
        #ls = len(s)
        memo, ls = [-1] * len(s), len(s)
        def dp(i):
            if i == len(s) or memo[i] != -1: return True if i == len(s) else memo[i]
            for w in wo:
                if i + len(w) <= ls and s[i:i+len(w)] == w and dp(i+len(w)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dp(0)