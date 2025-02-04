class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for x in range(m):
            curr = 0
            prev = 0
            for i in range(n):
                if grid[x][i] == 'W':
                    for j in range(prev, i):
                        if grid[x][j] == '0':
                            grid[x][j] = curr
                    curr = 0
                    prev = i + 1
                if grid[x][i] == 'E':
                    curr += 1
            for j in range(prev, n):
                if grid[x][j] == '0':
                    grid[x][j] = curr
            
        # for row in grid:
        #     print(row)
        for y in range(n):
            curr = 0
            prev = 0
            for i in range(m):
                if grid[i][y] == 'W':
                    for j in range(prev, i):
                        if isinstance(grid[j][y], int):
                            grid[j][y] += curr
                        elif grid[j][y] == '0':
                            grid[j][y] = curr
                    curr = 0
                    prev = i + 1
                if grid[i][y] == 'E':
                    curr += 1
            for j in range(prev, m):
                if isinstance(grid[j][y], int):
                    grid[j][y] += curr
                elif grid[j][y] == '0':
                    grid[j][y] = curr
            
        #print()
        #print()
        # for row in grid:
        #     print(row)
        ans = 0
        for row in grid:
            for item in row:
                if isinstance(item, int):
                    ans = max(ans, item)
        return ans