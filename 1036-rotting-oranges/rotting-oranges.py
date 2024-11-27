class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans, self.m, self.n, dq = 0, len(grid), len(grid[0]), collections.deque()
        def search(dq):
            depth = 0
            while dq:
                for m in range(len(dq)):
                    x, y = dq.popleft()
                    for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                        if 0 <= x + dx < self.m and 0 <= y + dy < self.n and grid[x+dx][y+dy] == 1:
                            grid[x+dx][y+dy] = 3
                            dq.append((x+dx,y+dy))
                depth+=1
            return max(0, depth-1)
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    grid[i][j] = 3
                    dq.append((i, j))
        ans = search(dq)
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    return -1
        return ans

