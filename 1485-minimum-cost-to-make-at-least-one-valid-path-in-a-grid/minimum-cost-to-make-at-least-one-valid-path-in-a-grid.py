class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mc = [[inf for i in range(n)] for j in range(m)]
        mc[0][0] = 0
        dq = deque([(0,0)])
        while dq:
            x, y = dq.popleft()
            d = ((0,1),(0,-1),(1,0),(-1,0))
            for i, (dx, dy) in enumerate(d):
                cost = int(grid[x][y] != i +1)
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and mc[x][y] + cost < mc[nx][ny]:
                    mc[nx][ny] = mc[x][y] + cost
                    if cost:
                        dq.append((nx, ny))
                    else:
                        dq.appendleft((nx, ny))
        return mc[m-1][n-1]