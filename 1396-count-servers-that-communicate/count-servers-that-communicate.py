class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        tot = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    tot += 1
                    rows[x]+=1
                    cols[y]+=1
        # print(tot)
        # print(rows)
        # print(cols)
        # print()
        for x in range(m):
            for y in range(n):
                if rows[x] == 1 and cols[y] == 1 and grid[x][y] == 1:
                    #print([x, y])
                    tot -= 1
        return tot