class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #find the first one and mark it as 2
        #put all the two coords in a list
        #put all the 1 coords in a list
        #find the shortest manhattan distance and return n-1
        m = len(grid)
        n = len(grid[0])
        twos = []
        ones = []
        cont = True
        for x in range(m):
            if not cont:
                x = m + 1
                break
            for y in range(n):
                if not cont:
                    y = n + 1
                    break
                if grid[x][y] == 1:
                    cont = False
                    dq = deque()
                    grid[x][y] = 2
                    dq.append((x, y))
                    twos.append((x, y))
                    #print("x and y " + str(x) + " " + str(y))
                    while dq:
                        nx, ny = dq.popleft()
                        for dx, dy in ((1,0), (0, 1), (-1, 0), (0, -1)):
                            #print(str(nx+dx) + " " + str(ny+dy))
                            if 0 <= (nx+dx) < m and 0 <= (ny + dy) < n and grid[nx+dx][ny+dy] == 1:
                                dq.append((nx + dx, ny + dy))
                                grid[nx+dx][ny+dy] = 2
                                twos.append((nx+dx, ny+dy))
                    
                    break
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    ones.append((x, y))
        # print(ones)
        # print(twos)
        ans = inf
        for a, b in twos:
            for c, d in ones:
                ans = min(ans, abs(d-b) + abs(c - a) - 1)
        return ans
