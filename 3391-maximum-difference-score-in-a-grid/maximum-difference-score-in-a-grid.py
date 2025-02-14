import sys
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-sys.maxsize] * n for _ in range(m)]
        
        # Fill rightmost column
        for i in range(m-1, -1, -1):
            if i == m-1:
                dp[i][n-1] = -sys.maxsize
            else:
                dp[i][n-1] = max(grid[i+1][n-1], dp[i+1][n-1])
        
        # Fill bottom row
        for j in range(n-1, -1, -1):
            if j == n-1:
                dp[m-1][j] = -sys.maxsize
            else:
                dp[m-1][j] = max(grid[m-1][j+1], dp[m-1][j+1])
        
        # Fill the rest of the DP table
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(grid[i][j+1], dp[i][j+1], grid[i+1][j], dp[i+1][j])
        
        # Compute the maximum score
        max_score = max(dp[i][j] - grid[i][j] for i in range(m) for j in range(n))
        return max_score