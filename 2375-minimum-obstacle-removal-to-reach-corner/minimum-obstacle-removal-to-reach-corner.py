class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        #def dijkstra(m, n):
        dist = [[inf] * n for i in range(m)]
        direct = [(0,1), (1,0), (0,-1), (-1,0)]
        pq = [(grid[0][0], 0, 0)]
        dist[0][0] = 0

        while pq:
            curr, x, y = heapq.heappop(pq)
            if (x == m - 1 and y == n - 1): return curr
            for dx, dy in direct:
                if (0 <= x+dx < m and 0 <= y+dy < n):
                    ndist = curr + grid[x+dx][y+dy]
                    if ndist < dist[x+dx][y+dy]:
                        dist[x+dx][y+dy] = ndist
                        heapq.heappush(pq, (ndist, x+dx, y+dy))
        return dist[m-1][n-1]
        #return dijkstra(len(grid), len(grid[0]))