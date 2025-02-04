class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        for x in range(m):
            curr = prev = 0
            for i in range(n):
                for j in range(prev,i if grid[x][i] == 'W' else -1): grid[x][j] = curr if grid[x][j] == '0' else grid[x][j]
                curr, prev = curr + int(grid[x][i] == 'E') if grid[x][i] != 'W' else 0, i + 1 if grid[x][i] == 'W' else prev
            for j in range(prev, n): grid[x][j] = curr if grid[x][j] == '0' else grid[x][j]
        for y in range(n):
            curr = prev = 0
            for i in range(m):
                for j in range(prev, i if grid[i][y] == 'W' else -1): grid[j][y] = grid[j][y] + curr if isinstance(grid[j][y], int) else curr if grid[j][y] == '0' else grid[j][y]
                curr, prev = curr + (grid[i][y] == 'E') if grid[i][y] != 'W' else 0, prev if grid[i][y] != 'W' else i + 1
            for j in range(prev, m): grid[j][y] = grid[j][y] + curr if isinstance(grid[j][y], int) else curr if grid[j][y] == '0' else grid[j][y]
        return max(max([item if isinstance(item, int) else 0 for item in row]) for row in grid)