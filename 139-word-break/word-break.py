class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
        wo = set(wd)
        memo = [-1] * len(s)
        def dp(i):
            if i == len(s):
                return True
            if memo[i] != -1:
                return memo[i]
            ans = False
            for w in wo:
                if i + len(w) <= len(s):
                    if s[i:i+len(w)] == w:
                        ans = dp(i+len(w))
                        if ans:
                            break
            memo[i] = ans
            return ans
        return dp(0)