class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        ans = 0
        prev = set()
        for l in range(len(s)):
            dict = defaultdict(int)
            #dict[s[l]] += 1
            for r in range(l, len(s)):
                dict[s[r]] += 1
                if len(set(dict.values())) == 1 and s[l:(r+1)] not in prev:
                    prev.add(s[l:(r+1)])
                    ans += 1
                    #print(s[l:(r+1)])
        return ans