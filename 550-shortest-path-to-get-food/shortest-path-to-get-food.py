class Solution:
    def getFood(self, grid):
        m, n, prev = len(grid), len(grid[0]), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    dq = deque([(i, j, 0)])
                    while dq:
                        x, y, dep = dq.popleft()
                        if grid[x][y] == '#': return dep
                        if (x, y) not in prev:
                            prev.add((x, y))
                            for n1, n2 in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                                dx, dy = x + n1, y + n2
                                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] != 'X' and (dx, dy) not in prev: dq.append((dx, dy, dep + 1))
                    return -1