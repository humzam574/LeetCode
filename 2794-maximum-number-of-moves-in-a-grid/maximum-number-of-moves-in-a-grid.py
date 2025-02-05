class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n, dep = len(grid), len(grid[0]), 1; dq = deque((x, 0) for x in range(m)); visited = set(dq)
        while dep < n and dq:
            for _ in range(len(dq)):
                x, y = dq.popleft(); val = grid[x][y]; y += 1
                for dx in (x - 1, x, x + 1):
                    if 0 <= dx < m and grid[dx][y] > val and (dx, y) not in visited: visited.add((dx, y)); dq.append((dx, y))
            dep += bool(dq)
        return dep - 1