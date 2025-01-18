class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n,dq= len(grid), len(grid[0]), deque([(0,0)]); mc = [[inf for i in range(n)] for j in range(m)]; mc[0][0] = 0
        while dq:
            x, y = dq.popleft()
            for i, (dx, dy) in enumerate(((0,1),(0,-1),(1,0),(-1,0))):
                cost, nx, ny = grid[x][y] != i +1, x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and mc[x][y] + cost < mc[nx][ny]:
                    mc[nx][ny] = mc[x][y] + cost
                    if cost: dq.append((nx, ny))
                    else: dq.appendleft((nx, ny))
        return mc[-1][-1]