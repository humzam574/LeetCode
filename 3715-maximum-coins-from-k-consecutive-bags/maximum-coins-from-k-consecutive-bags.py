class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        n = len(coins)
        if n == 1:
            return min(coins[0][1] - coins[0][0] + 1, k) * coins[0][2]
        
        coins.sort(key=lambda x: x[0])
        
        max_coins = 0
        cur = 0
        start = coins[0][0]
        end = start + k - 1
        
        left = 0
        right = 0
        
        while right < n:
            rs, re, r_val = coins[right]
            
            if end >= re:
                cur += (re - rs + 1) * r_val
                right += 1
                continue
            
            max_coins = max(max_coins, (end - rs + 1) * r_val + cur if rs <= end else cur)
            
            le, l_val = coins[left][1], coins[left][2]
            new_start = re - k + 1
            
            if new_start <= le:
                cur += (re - rs + 1) * r_val - (new_start - start) * l_val
                end = re
                start = new_start
                right += 1
            else:
                cur -= (le - start + 1) * l_val
                left += 1
                start = coins[left][0]
                end = start + k - 1
        
        return max(max_coins, cur)