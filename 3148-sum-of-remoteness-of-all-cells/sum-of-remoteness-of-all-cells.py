class Solution:
    def sumRemoteness(self, grid):
        m, n, whole, ans, tot = len(grid), len(grid[0]), False, 0, 0
        for row in grid:
            for num in row:
                if num != -1:
                    whole, tot = True, tot + num
        if whole == False and ans != 0: return -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    dq, sm, sz, grid[i][j] = deque([(i, j)]), grid[i][j], 0, -1
                    while dq:
                        sz += 1; x, y = dq.popleft()
                        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1: dq.append((nx, ny)); sm, grid[nx][ny] = sm + grid[nx][ny], -1
                    ans += (sz * (tot - sm))
        return ans