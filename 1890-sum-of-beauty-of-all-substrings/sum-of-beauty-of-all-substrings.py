class Solution:
    def beautySum(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(n):
            dic, low, high = defaultdict(int), 0, 0
            for j in range(i,n): dic[s[j]] += 1; high, low = max(dic[s[j]], high), 1 if low == 0 or dic[s[j]] == 1 else min(dic.values()); ans += high - low
        return ans