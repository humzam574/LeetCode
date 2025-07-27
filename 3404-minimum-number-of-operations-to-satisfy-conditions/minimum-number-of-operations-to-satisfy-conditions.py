class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        #design a dp algo
        #each row will have a tup of length 2
        #which is the min ops s.t. the last value != i
        #when you make a new row, you compare the optimal solution for that row with the second best

        #iterate through each row
        #get the two best solutions
        #put it in a tup
        #keep going and DP
        def best(arr1, arr2):
            ans = [inf] * 10
            for i in range(10):
                for j in range(10):
                    if j != i:
                        ans[i] = min(ans[i], arr1[i] + arr2[j])
            return ans

        m = len(grid)
        n = len(grid[0])
        dp = [[0] * 10 for i in range(n)]

        for j in range(n):
            curr = [m] * 10
            for i in range(m):
                temp = grid[i][j]
                curr[temp]-=1
            prev = dp[j-1]
            dp[j] = best(curr, prev)
        return min(dp[-1])

            