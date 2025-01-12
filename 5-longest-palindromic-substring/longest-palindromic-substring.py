class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = ""
        high = 0
        for l in range(len(s)):
            for r in range(l + 1 + high, len(s) + 1):
                #print(s[l:r] + " " + (s[l:r])[::-1] + " " + str((s[l:r])[::-1] == s[l:r]) + " " + str(high))
                if r- l > high and s[l:r] == (s[l:r])[::-1]:
                    high = r - l
                    ss = s[l:r]
        return ss