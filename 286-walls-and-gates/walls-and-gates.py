class Solution:
    def wallsAndGates(self, rooms):
        m, n, q = len(rooms), len(rooms[0]), collections.deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0: q.append((r,c))
        while q:
            x, y = q.popleft(); d = rooms[x][y]+1
            for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and rooms[nx][ny] == 2147483647: rooms[nx][ny] = d; q.append((nx, ny))