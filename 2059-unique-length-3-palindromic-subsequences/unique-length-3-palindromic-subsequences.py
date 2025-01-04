class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        locations, ans = [[-1, -1] for _ in range(26)], 0
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            if locations[idx][0] == -1: locations[idx] = [i, i]
            else: locations[idx][1] = i
        for l, r in locations: ans = ans + len(set(s[l+1:r])) if r - l > 1 else ans
        return ans