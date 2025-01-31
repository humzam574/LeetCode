class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        sizes = [-1, -1]
        label = 2
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dq = deque([(i, j)])
                    grid[i][j] = label
                    size = 0
                    while dq:
                        x, y = dq.popleft()
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
        ans = 0
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
