class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0 for i in range(3)] for i in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            a,b,c = costs[i]
            dp[i][0] = a + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = b + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = c + min(dp[i-1][0], dp[i-1][1])
        # for row in dp:
        #     print(row)
        return min(dp[-1])