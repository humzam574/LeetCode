class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        m, n, pq, visited = len(grid), len(grid[0]), [(grid[0][0], 0, 0)], set()
        while pq:
            curr, x, y = heapq.heappop(pq)
            if (x == m - 1 and y == n - 1): return curr
            if (x, y) in visited: continue
            visited.add((x,y))
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                if (0 <= x+dx < m and 0 <= y+dy < n) and (x+dx,y+dy) not in visited:
                    ndist, wait = max(grid[x+dx][y+dy], curr + grid[x+dx][y+dy] + (curr + grid[x+dx][y+dy] % 2)), 1 - (grid[x+dx][y+dy] - curr) % 2
                    heapq.heappush(pq, (max(curr + 1, grid[x+dx][y+dy] + wait), x+dx, y+dy))