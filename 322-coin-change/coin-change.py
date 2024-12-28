class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [10001] * amount
        if amount == 0: return 0
        if amount < min(coins): return -1
        for coin in coins:
            for x in range(coin, amount + 1): dp[x] = min(dp[x], dp[x - coin] + 1)
        return -1 if dp[-1] == 10001 else dp[-1]