class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(l, r): #0,1,
            if (l,r) in memo:
                return memo[(l,r)]
            if s[l:r] in wordDict:
                temp = dp(r,r) or dp(l,r+1)
                memo[(l, r)] = temp
                return temp
            elif r == len(s):
                return l == r
            temp = dp(l, r+1)
            memo[(l,r)] = temp
            return temp
        return dp(0,0)
            