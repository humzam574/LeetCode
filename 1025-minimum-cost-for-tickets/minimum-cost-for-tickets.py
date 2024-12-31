class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l7, l30 = 0, 0
        dp = [0] * (len(days))
        for i, day in enumerate(days):
            while days[i] - days[l7] >= 7: l7 += 1
            while days[i] - days[l30] >= 30: l30 += 1
            p1 = costs[0] + (0 if i == 0 else dp[i - 1])
            p30 = costs[2] + (0 if l30 == 0 else dp[l30 - 1])
            p7 = costs[1] + (0 if l7 == 0 else dp[l7 - 1])
            dp[i] = min(p1, p30, p7)
            print(dp)
            print(l7)
            print(l30)
        print(dp)
        return dp[-1]