class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0,0,0] for _ in range(len(nums)+1)]
        # dp[0][nums[0]%3]=1
        for i in range(len(nums)):
            delta = nums[i] % 3
            #if True:#dp[i-1][0] or i==0:
            dp[i][delta] = dp[i-1][0] + nums[i]
            if dp[i-1][1]:
                dp[i][(delta+1)%3] = dp[i-1][1] + nums[i]
            if dp[i-1][2]:
                dp[i][(delta+2)%3] = dp[i-1][2] + nums[i]
            for j in range(3):
                dp[i][j] = max(dp[i][j],dp[i-1][j])
            
        for row in dp:
            print(row)
        return dp[-2][0]
            