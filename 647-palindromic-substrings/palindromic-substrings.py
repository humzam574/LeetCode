class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        for i in range(ans - 1):
            for j in range(i + 2, len(s) + 1):
                if s[i:j] == s[i:j][::-1]: ans += 1
        return ans