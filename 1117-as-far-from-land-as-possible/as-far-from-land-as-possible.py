class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, q, ans = len(grid), collections.deque(), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: q.append((i, j))
        if not q or len(q) == n * n: return -1
        while q:
            size, ans = len(q), ans + 1
            while size:
                size = size - 1
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x + dx < n and 0 <= y + dy < n and grid[x+dx][y+dy] == 0:
                        grid[x + dx][y + dy] = 1
                        q.append((x + dx, y + dy))
        return ans - 1