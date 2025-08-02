class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dq = deque()
        visited = set()
        ans = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 0:
                    dq.append((x, y, 0))
                    visited.add((x, y))
                    

        while dq:
            x, y, dist = dq.popleft()
            
            for dx, dy in ((1,0), (-1,0), (0, 1), (0, -1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                    dq.append((nx, ny, dist+1))
                    visited.add((nx, ny))
                    ans[nx][ny] = dist+1
        return ans