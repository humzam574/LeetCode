class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        minl = inf
        for m in range(1, n - 1):
            hl = -1
            minl = min(minl, prices[m - 1])
            if minl >= prices[m]: continue
            for l in range(m):
                if prices[l] < prices[m]:
                    hl = max(hl, profits[l])
            hr = -1
            for r in range(m + 1, n):
                if prices[r] > prices[m]:
                    hr = max(hr, profits[r])
            if hr == -1: continue
            ans = max(ans, hr + hl + profits[m])
        return ans