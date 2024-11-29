class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        m, n, pq, visited = len(grid), len(grid[0]), [(grid[0][0], 0, 0)], [[False] * len(grid[0]) for _ in range(len(grid))]
        visited[0][0] = True
        while pq:
            curr, x, y = heappop(pq)
            visited[x][y] = True
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]: continue
                nt=curr+1+(grid[nx][ny]>curr+1)*((grid[nx][ny]-curr)//2*2)
                if nx == m - 1 and ny == n - 1: return nt
                visited[nx][ny] = True
                heappush(pq, (nt, nx, ny))