class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        #left to right, top down search
        #keep a curr array of length 16
        n = len(grid)
        m = len(grid[0])
        if (n < 3 or m < 3):
            return 0
        comp = set()
        curr = [0] * 16
        ans = 0
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                comp.clear()
                curr = [0] * 16
                comp.add(grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1])
                comp.add(grid[x][y-1] + grid[x][y] + grid[x][y+1])
                comp.add(grid[x+1][y-1] + grid[x+1][y] + grid[x+1][y+1])
                comp.add(grid[x-1][y-1] + grid[x][y-1] + grid[x+1][y-1])
                comp.add(grid[x-1][y] + grid[x][y] + grid[x+1][y])
                comp.add(grid[x-1][y+1] + grid[x][y+1] + grid[x+1][y+1])
                comp.add(grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1])
                comp.add(grid[x+1][y-1] + grid[x][y] + grid[x-1][y+1])

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        curr[grid[x+i][y+j]] += 1

                if len(comp) == 1 and curr == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]:
                    ans+=1
        return ans