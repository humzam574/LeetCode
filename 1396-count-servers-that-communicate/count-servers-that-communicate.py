class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        tot = 0
        #false -> true -> false -> false -> false -> false
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    tot += 1
                    rows[x] += 1
                    cols[y] += 1
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and rows[x] == 1 and cols[y] == 1:
                    tot -= 1
        return tot