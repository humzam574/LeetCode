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
            inf = float('inf')
            min1 = min2 = inf
            idx1 = -1
            for j, v in enumerate(arr2):
                if v < min1:
                    min2, min1 = min1, v
                    idx1 = j
                elif v < min2:
                    min2 = v

            # 2) Build the answer in O(n)
            n = len(arr1)
            ans = [0]*n
            for i in range(n):
                if i != idx1:
                    ans[i] = arr1[i] + min1
                else:
                    ans[i] = arr1[i] + min2

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