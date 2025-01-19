class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = []
        for x in range(m):
            for y in range(n):
                if x in [0, m - 1] or y in [0, n - 1]:
                    heappush(heap, (grid[x][y], x, y))
                    grid[x][y] = -1
        
        ans = 0
        high = -1

        while heap:
            h, x, y = heappop(heap)
            high = max(high, h)
            ans += high - h
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x+dx, y+dy
                if (0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1):
                    heappush(heap, (grid[nx][ny], nx, ny))
                    grid[nx][ny] = -1
        return ans