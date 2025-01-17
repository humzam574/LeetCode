class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            a, b, lm, rm, le, re = 0, 0, i, i, i, i + 1
            while lm >= 0 and rm < len(s) and s[lm] == s[rm]: lm, rm, a = lm - 1, rm + 1, a + 1
            while le >= 0 and re < len(s) and s[le] == s[re]: le, re, b = le - 1, re + 1, b + 1
            ans += (a+b)
        return ans