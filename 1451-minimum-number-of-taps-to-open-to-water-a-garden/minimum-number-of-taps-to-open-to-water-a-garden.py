class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        #DEE PEE
        dp = [inf] * (n + 100)
        for i,r in enumerate(ranges):
            if r == 0:
                continue
            low = max(0, i - r)
            high = i + r
            if low != 0:
                val = min(dp[low:i]) + 1
            else:
                val = 1
            for x in range(low, high+1):
                dp[x] = min(dp[x], val)
            # print(dp[:n+1])
        
        if max(dp[:n+1]) == inf:
            return -1
        return dp[n]