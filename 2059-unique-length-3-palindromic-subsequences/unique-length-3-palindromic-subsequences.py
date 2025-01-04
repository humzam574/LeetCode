class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #use a two pointer
        locations = []
        for i in range(26):
            locations.append([-1, -1])
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            if locations[idx][0] == -1:
                locations[idx][0] = i
                locations[idx][1] = i
            else:
                locations[idx][1] = i
        ans = 0
        #print(locations)
        for l, r in locations:
            if r - l > 1:
                ans += len(set(s[l+1:r]))
        return ans