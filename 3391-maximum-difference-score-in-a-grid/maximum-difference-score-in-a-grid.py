class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = -inf
        dp = [[0] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        for x in range(1, m):
            dp[x][0] = min(grid[x][0], dp[x - 1][0])
            ans = max(ans, grid[x][0] - dp[x - 1][0])
        for y in range(1, n):
            dp[0][y] = min(grid[0][y], dp[0][y - 1])
            ans = max(ans, grid[0][y] - dp[0][y-1])
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = min(grid[x][y], dp[x - 1][y], dp[x][y - 1])
                ans = max(ans, grid[x][y] - dp[x - 1][y], grid[x][y] - dp[x][y - 1])
        return ans