class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        def exp(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            return res
        for i in range(len(s)):
            ans+=exp(i, i)
            ans+=exp(i,i+1)
        return ans