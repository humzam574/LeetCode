class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10001] * amount
        if amount == 0: return 0
        if amount < min(coins): return -1
        for i in range(min(coins), amount + 1):
            val = 10001
            for coin in coins:
                if i >= coin:
                    val = min(val, dp[i - coin] + 1)
            dp[i] = val
        
        return dp[-1] if dp[-1] != 10001 else -1