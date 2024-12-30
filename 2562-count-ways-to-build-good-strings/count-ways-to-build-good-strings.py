class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        #groups of zero
        #some sort of backtracking where you find the number of good strings at n times
        #dp tabulation?
        dp = [0] * (high + 1)
        dp[0] = 1
        #number of ways you can make it to that point at each index
        if one < zero:
            zero, one = one, zero
        for i in range(zero, one):
            dp[i] += (dp[i - zero]) % 1000000007
        for i in range(one, high + 1):
            dp[i] = (dp[i] + dp[i - zero]+ dp[i - one]) % 1000000007
        return sum(dp[low : high + 1]) % 1000000007