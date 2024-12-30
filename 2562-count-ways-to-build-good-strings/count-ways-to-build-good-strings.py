class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp, zero, one = [1] + [0] * high, min(zero, one), max(zero, one)
        for i in range(zero, one): dp[i] += (dp[i - zero]) % 1000000007
        for i in range(one, high + 1): dp[i] = (dp[i] + dp[i - zero] + dp[i - one]) % 1000000007
        return sum(dp[low : high + 1]) % 1000000007