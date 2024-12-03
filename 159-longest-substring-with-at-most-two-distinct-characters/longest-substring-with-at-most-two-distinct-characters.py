class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        dict = defaultdict(int)
        l = 0 

        ans = 0

        for r in range(len(s)):

            dict[s[r]] += 1

            while len(dict) > 2:
                dict[s[l]] -= 1

                if dict[s[l]] == 0:
                    del dict[s[l]]
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans