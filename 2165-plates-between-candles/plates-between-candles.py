from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * n
        candles = []
        
        # Compute prefix sum of plates and store candle positions
        for i in range(n):
            if s[i] == '|':
                candles.append(i)
            prefix[i] = prefix[i - 1] + (s[i] == "*") if i > 0 else (s[i] == "*")
        
        ans = []
        for left, right in queries:
            # Find the leftmost candle >= left
            l, r = 0, len(candles) - 1
            while l <= r:
                m = (l + r) // 2
                if candles[m] < left:
                    l = m + 1
                else:
                    r = m - 1

            if l >= len(candles) or candles[l] > right:  # No valid candle found
                ans.append(0)
                continue
            
            left_candle = candles[l]

            # Find the rightmost candle <= right
            l, r = 0, len(candles) - 1
            while l <= r:
                m = (l + r) // 2
                if candles[m] > right:
                    r = m - 1
                else:
                    l = m + 1

            right_candle = candles[r]

            if left_candle < right_candle:  # Ensure at least one valid segment
                ans.append(prefix[right_candle] - prefix[left_candle])
            else:
                ans.append(0)

        return ans
