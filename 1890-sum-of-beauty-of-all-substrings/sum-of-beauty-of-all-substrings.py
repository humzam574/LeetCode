class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            dic = defaultdict(int)
            low = 0  
            high = 0
            for j in range(i,n):
                dic[s[j]] += 1
                if dic[s[j]] == high + 1:
                    high = dic[s[j]]
                if low == 0 or dic[s[j]]-1 == 0:
                    low = 1
                elif dic[s[j]]-1 == low:
                    low = min(dic.values())
                ans += high - low
        return ans