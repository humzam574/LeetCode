class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = -inf
        for r in range(2, len(grid)):
            curr = sum(grid[r-2][:3]) + grid[r-1][1] + sum(grid[r][:3])
            ans = max(curr, ans)
            for c in range(3, len(grid[0])):
                curr = curr - grid[r-2][c-3] - grid[r-1][c-2] - grid[r][c-3] + grid[r-2][c] + grid[r-1][c-1] + grid[r][c]
                ans = max(curr, ans)
        return ans