class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        steps += 1
        m = min(arrLen, 1 + steps // 2)
        dp = [[0] * steps for i in range(m)]
        dp[0][0] = 1
        mod = int(1e9 + 7)
        for y in range(1, steps):
            for x in range(m):
                curr = dp[x][y - 1]
                if x > 0:
                    curr += dp[x - 1][y - 1]
                if x < m - 1:
                    curr += dp[x + 1][y - 1]
                dp[x][y] = curr % mod
        return dp[0][-1] % mod
        