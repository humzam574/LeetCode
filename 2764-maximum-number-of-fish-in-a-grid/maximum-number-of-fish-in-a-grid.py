class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    curr = grid[x][y]
                    grid[x][y] = 0
                    dq = deque([(x,y)])
                    while dq:
                        r, c = dq.popleft()
                        curr += grid[r][c]
                        grid[r][c] = 0
                        for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]:
                                dq.append((nr,nc))
                    ans = max(ans, curr)
        return ans