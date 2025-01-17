class Solution:
    def wallsAndGates(self, rooms):
        m = len(rooms)
        n = len(rooms[0])
        q = collections.deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r,c))
        while q:
            x, y = q.popleft()
            distance = rooms[x][y]+1
            for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))
        return rooms