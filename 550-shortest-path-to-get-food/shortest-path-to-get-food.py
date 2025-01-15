class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        #implement a bfs
        m = len(grid)
        n = len(grid[0])
        def bfs(gx, gy):
            dq = deque([(gx, gy, 0)])
            prev = set()
            nb = ((1, 0), (-1, 0), (0, -1), (0, 1))
            while dq:
                #print(dq)
                x, y, dep = dq.popleft()
                if grid[x][y] == '#':
                    return dep
                if (x, y) not in prev:
                    prev.add((x,y))
                    for n1, n2 in nb:
                        dx, dy = x + n1, y + n2
                        if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in prev and grid[dx][dy] != 'X':
                            dq.append((dx, dy, dep + 1))
            return -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    return bfs(i, j)