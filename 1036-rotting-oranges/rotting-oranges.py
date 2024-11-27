class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        self.m = len(grid)
        self.n = len(grid[0])
        def search(dq):
            #dq = collections.deque()
            #dq.append((x,y))
            depth = 0
            while dq:
                for m in range(len(dq)):
                    #print(dq)
                    x, y = dq.popleft()
                    direct = [(0,1), (1,0), (-1,0), (0,-1)]
                    for dx, dy in direct:
                        #print(str(0 <= x + dx < self.m) + ", " + str(0 <= y + dy < self.n) + ", ")
                        if 0 <= x + dx < self.m and 0 <= y + dy < self.n and grid[x+dx][y+dy] == 1:
                            #print("adding " + str(x+dx) + ", " + str(y + dy))
                            grid[x+dx][y+dy] = 3
                            dq.append((x+dx,y+dy))
                depth+=1
            return depth-1
        dq = collections.deque()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    grid[i][j] = 3
                    dq.append((i, j))
                    #print(grid)
        ans = max(0, search(dq))
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    return -1
        return ans

