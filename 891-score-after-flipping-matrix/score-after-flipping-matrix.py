class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            if grid[x][0] == 0:
                for y in range(n):
                    grid[x][y] ^= 1
        cutoff = m // 2
        # for row in grid:
        #     print(row)
        # print()
        # print()
        for y in range(n):
            if sum(grid[i][y] for i in range(m)) <= cutoff:
                for x in range(m):
                    grid[x][y] ^= 1
        ans = 0
        # for row in grid:
        #     print(row)
        for y in range(1, n+1):
            inc = sum(grid[i][-y] for i in range(m))
            ans += (inc * 2**(y-1))
        return ans