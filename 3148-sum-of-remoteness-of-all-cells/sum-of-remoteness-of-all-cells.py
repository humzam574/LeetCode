class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        #sum everything
        #find an island and find the value of each number in that island
        #add size of island * (tot sum - sum of island) to ans
        self.m = len(grid)
        self.n = len(grid[0])
        self.first = 0
        ans = 0
        self.tot = 0
        
        for row in grid:
            for num in row:
                if num != -1:
                    self.tot += num
        
        def bfs(sx, sy):
            self.first += 1
            dq = deque([(sx, sy)])
            visited = {(sx, sy)}
            sm = 0
            sz = 0
            while dq:
                #print(dq)
                sz += 1
                x, y = dq.popleft()
                sm += grid[x][y]
                grid[x][y] = -1
                
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < self.m and 0 <= ny < self.n and grid[nx][ny] != -1 and (nx, ny) not in visited:
                        dq.append((nx, ny))
                        visited.add((nx, ny))
            #print(str(sm) + " " + str(sz) + " " + str(sz * (self.tot - sm)))
            return sz * (self.tot - sm)
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != -1:
                    ans += bfs(i, j)
                    #print(ans)
        return 0 if self.first == 1 else ans
        

