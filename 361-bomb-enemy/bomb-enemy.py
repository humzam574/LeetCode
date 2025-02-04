class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:  # Handle empty grid edge case
            return 0

        m, n = len(grid), len(grid[0])
        # Process rows to calculate horizontal enemy kills
        for x in range(m):
            curr = 0
            prev = 0
            for i in range(n):
                if grid[x][i] == 'W':  # Wall encountered
                    # Update '0' cells in the range [prev, i)
                    for j in range(prev, i):
                        if grid[x][j] == '0':
                            grid[x][j] = curr
                    curr = 0
                    prev = i + 1
                elif grid[x][i] == 'E':  # Enemy encountered
                    curr += 1
            # Update remaining '0' cells after the last wall in the row
            for j in range(prev, n):
                if grid[x][j] == '0':
                    grid[x][j] = curr

        # Process columns to calculate vertical enemy kills
        for y in range(n):
            curr = 0
            prev = 0
            for i in range(m):
                if grid[i][y] == 'W':  # Wall encountered
                    # Update numeric cells in the range [prev, i)
                    for j in range(prev, i):
                        if isinstance(grid[j][y], int):  # Already updated horizontally
                            grid[j][y] += curr
                        elif grid[j][y] == '0':
                            grid[j][y] = curr
                    curr = 0
                    prev = i + 1
                elif grid[i][y] == 'E':  # Enemy encountered
                    curr += 1
            # Update remaining numeric cells after the last wall in the column
            for j in range(prev, m):
                if isinstance(grid[j][y], int):
                    grid[j][y] += curr
                elif grid[j][y] == '0':
                    grid[j][y] = curr

        # Find the maximum kills from all '0' cells
        ans = 0
        for row in grid:
            for item in row:
                if isinstance(item, int):  # Check only numeric cells
                    ans = max(ans, item)

        return ans
