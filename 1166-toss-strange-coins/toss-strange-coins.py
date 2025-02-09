class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [[0] * (target + 1) for i in range(len(prob))]
        # for row in dp:
        #     print(row)
        # print()
        dp[0][0] = 1 - prob[0]
        if target > 0:
            dp[0][1] = prob[0]
        m = len(prob)
        for x in range(1, len(prob)):
            for y in range(target + 1):
                curr = 0
                if y > 0:
                    curr += dp[x - 1][y - 1] * prob[x]
                curr += dp[x - 1][y] * (1 - prob[x])
                dp[x][y] = curr
        # for row in dp:
        #     print(row)
        return dp[-1][-1]