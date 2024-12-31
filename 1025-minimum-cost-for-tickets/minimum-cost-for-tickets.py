class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l7, l30, dp = 0, 0, [0] * len(days)
        for i in range(len(days)):
            while days[i] - days[l7] >= 7: l7 += 1
            while days[i] - days[l30] >= 30: l30 += 1
            dp[i] = min(costs[0] + (i != 0) * dp[i - 1], costs[1] + (l7 != 0) * dp[l7 - 1], costs[2] + (l30 != 0) * dp[l30 - 1])
        return dp[-1]