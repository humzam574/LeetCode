class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        cs = set(coins)
        if amount == 0:
            return 0
        def dp(target):
            if target in cs:
                return 1
            low = inf
            neg = True
            for coin in coins:
                if target - coin >= 0:
                    if target - coin in memo:
                        temp = memo[target-coin]
                    else:
                        temp = min(low, dp(target - coin))
                    if temp != -1:
                        neg = False
                        low = min(low, 1 + temp)
            if neg:
                low = -1
            memo[target] = low
            return low
        return dp(amount)
                

