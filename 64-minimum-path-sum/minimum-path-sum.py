class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] + [2**24] * (n - 1)
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = dp[j] + grid[i][j] if dp[j] < dp[j - 1] else dp[j - 1] + grid[i][j]
        return dp[-1]