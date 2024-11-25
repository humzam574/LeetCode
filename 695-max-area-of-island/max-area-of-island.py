class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        def bfs(x, y):
            if (x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0): return 0
            grid[x][y] = 0
            return 1 + bfs(x + 1, y) + bfs(x, y + 1) + bfs(x, y - 1) + bfs(x - 1, y)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: ans = max(ans, bfs(i, j))
        return ans