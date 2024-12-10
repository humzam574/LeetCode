class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        srow, scol, m, n = [sum(r) for r in grid], [sum(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))], len(grid), len(grid[0])
        for i in range(m):
            for j in range(n): grid[i][j] = 2*srow[i]-m + 2*scol[j]-n
        return grid