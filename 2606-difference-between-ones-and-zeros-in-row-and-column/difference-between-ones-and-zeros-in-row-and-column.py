class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        srow = [sum(r) for r in grid]
        m = len(grid)
        n = len(grid[0])
        scol = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*srow[i]-m + 2*scol[j]-n
        return grid