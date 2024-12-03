class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        dict, l, ans = defaultdict(int), 0, 0
        for r in range(len(s)):
            dict[s[r]] += 1
            while len(dict) > 2:
                dict[s[l]], l = dict[s[l]] - 1, l + 1
                if dict[s[l - 1]] == 0: del dict[s[l - 1]]
            ans = max(ans, r - l + 1)
        return ans