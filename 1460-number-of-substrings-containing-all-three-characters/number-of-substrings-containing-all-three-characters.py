class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        prev = [-1, -1, -1]
        ans = 0
        for i in range(len(s)):
            prev[ord(s[i]) - 97] = i
            ans += 1 + min(prev)
        return ans