class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = -inf
        for r in range(2, len(grid)):
            t = r - 2
            m = r - 1
            b = r
            curr = sum(grid[t][:3]) + grid[m][1] + sum(grid[b][:3])
            ans = max(curr, ans)
            f1, f2, f3 = 3, 2, 3
            b1, b2, b3 = 0, 1, 0
            n = len(grid[0])
            while f1 < n:
                curr = curr - grid[t][b1] - grid[m][b2] - grid[b][b3]
                curr = curr + grid[t][f1] + grid[m][f2] + grid[b][f3]
                f1+=1
                f2+=1
                f3+=1
                b1+=1
                b2+=1
                b3+=1
                ans = max(curr, ans)
        return ans