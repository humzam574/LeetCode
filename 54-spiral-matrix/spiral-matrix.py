class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        delta = (0, 1)
        dirs = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}

        x, y = 0, 0
        dx, dy = delta
        ans = [0] * (m*n)
        for i in range(m*n):
            ans[i] = matrix[x][y]
            visited[x][y] = True
            if x+dx >= m or y+dy >= n or x+dx < 0 or y+dy < 0 or visited[x+dx][y+dy]:
                dx, dy = dirs[(dx, dy)]
            x+=dx
            y+=dy
        return ans