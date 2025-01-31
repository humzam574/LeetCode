class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        #answer is dependent on a few cases
        #case 1: the entire grind is island. ans = m * n
        #case 2: there are no islands. return 1
        #case 3: there is only one island or no islands can be connected. ans = max(islands) + 1
        #case 4: islands can be connected. ans = 1 + i1 + i2 + i3 + i4
        #in case three, you want to search through every single index x,y and if
        #1. grid[x][y] == 0
        #2. grid[dx][dy] == island for 2-4 dx,dy combos
        #then ans = sum(islands) + 1

        #use a bfs to go through and label each island with a numbering system, from 2 onwards
        #if there is only one island of 
        #then do a left-right, top-down search and see if you can merge islands

        sizes = [-1, -1]
        label = 2
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    #bfs
                    dq = deque([(i, j)])
                    grid[i][j] = label
                    size = 0
                    while dq:
                        x, y = dq.popleft()
                        #grid[x][y] = label
                        size += 1
                        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                                dq.append((nx, ny))
                                grid[nx][ny] = label
                    sizes.append(size)
                    label += 1
        if len(sizes) == 2:
            return 1
        if len(sizes) == 3:
            return min(n*n, sizes[2]+1)
        #in case three, you want to search through every single index x,y and if
        #1. grid[x][y] == 0
        #2. grid[dx][dy] == island for 2-4 dx,dy combos
        #then ans = sum(islands) + 1
        ans = 0
        # print(sizes)
        # print()
        # for row in grid:
        #     print(row)
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    counted = {0}
                    curr = 1
                    for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] not in counted:
                            counted.add(grid[nx][ny])
                            curr+=sizes[grid[nx][ny]]
                    ans = max(curr, ans)
        return ans
