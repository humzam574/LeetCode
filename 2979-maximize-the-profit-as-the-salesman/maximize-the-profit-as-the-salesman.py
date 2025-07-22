class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key = lambda x : x[1])
        dp = [0] * (n+1)
        #dp[i] = max(curr + dp[start - 1], dp[i - 1])
        idx = 0
        
        for i in range(n):
            while idx < len(offers) and offers[idx][1] == i:
                dp[i] = max(dp[i], dp[offers[idx][0] - 1] + offers[idx][2])
                idx+=1
            dp[i] = max(dp[i], dp[i - 1])
        # print(dp)
        return dp[-2]
