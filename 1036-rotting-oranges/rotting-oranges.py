class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m, self.n, self.depth, dq, self.orang = len(grid), len(grid[0]), 0, collections.deque(), 0
        def search(dq):
            while dq:
                for m in range(len(dq)):
                    x, y = dq.popleft()
                    for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                        if 0 <= x + dx < self.m and 0 <= y + dy < self.n and grid[x+dx][y+dy] == 1:
                            grid[x+dx][y+dy], self.orang = 3, self.orang - 1
                            dq.append((x+dx,y+dy))
                self.depth+=1
            self.depth = max(0, self.depth - 1)
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1: self.orang += 1
                elif grid[i][j] == 2:
                    grid[i][j] = 3
                    dq.append((i, j))
        search(dq)
        return self.depth if self.orang == 0 else -1