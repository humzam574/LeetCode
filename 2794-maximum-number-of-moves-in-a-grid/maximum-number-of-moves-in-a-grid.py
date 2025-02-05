class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        #dfs
        #start a bfs from every number in the first column
        #find the numbers which can continue at column 2
        #find the numbers that can continue at column 3
        #so on and so forth
        m, n = len(grid), len(grid[0])
        #in each iteration, the row increases by one
        #but y is delta
        dep = 1
        dq = deque((x, 0) for x in range(m))
        visited = set(dq)
        while dep < n and dq:
            for _ in range(len(dq)):
                x, y = dq.popleft()
                val = grid[x][y]
                y += 1
                if y == n:
                    return n - 1
                for dx in (x - 1, x, x + 1):
                    if 0 <= dx < m and grid[dx][y] > val and (dx, y) not in visited:
                        visited.add((dx, y))
                        dq.append((dx, y))
            dep += bool(dq)
        return dep - 1