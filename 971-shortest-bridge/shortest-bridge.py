class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):

                if grid[i][j]:
                    queue = [(i, j)]
                    break

        next_queue = []

        while queue:

            x, y = queue.pop()
            grid[x][y] = -1

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                _x = x + dx
                _y = y + dy

                if _x >= 0 and _y >= 0 and _x < m and _y < n:

                    if grid[_x][_y] == 0:
                        next_queue.append((_x, _y, 1))
                        grid[_x][_y] = -1
                    elif grid[_x][_y] == 1:
                        queue.append((_x, _y))
                        grid[_x][_y] = -1

        # print(grid)

        while next_queue:

            x, y, depth = next_queue.pop(0)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                _x = x + dx
                _y = y + dy
                if _x >= 0 and _y >= 0 and _x < m and _y < n:
                    if grid[_x][_y] == 0:
                        next_queue.append((_x, _y, depth + 1))
                        grid[_x][_y] = -1

                    if grid[_x][_y] == 1:
                        return depth 