class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        #visited = [[False] * n for _ in range(m)]
        #1,  2,  3,  4
        #12, 13, 14, 5
        #11, 16, 15, 6
        #10, 9,  8,  7
        #top right barrier moves down and to the left
        #bottom right barrier moves up and to the left
        #bottom left barrier moves up and to the right
        #top left moves down and to the right
        # barriers = [[0,0], [0,n], [m,n-1], [m-1,-1]]
        barriers = [[0,n], [m,n-1], [m-1,-1],[0,0]]
        # bdeltas =  [(1,1), (1,-1), (-1,-1), (-1,1)]
        bdeltas = [(1,-1), (-1,-1), (-1,1), (1,1)]
        dirs =     [(0,1), (1,0),  (0,-1),  (-1,0)]
        idx = 0
        # delta = (0, 1)
        #dirs = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}

        x, y = 0, 0
        # dx, dy = delta
        ans = [0] * (m*n)
        for i in range(m*n):
            print(str(x) + ", " + str(y) + ", " + str(matrix[x][y]))
            ans[i] = matrix[x][y]
            # visited[x][y] = True
            # if x+dx >= m or y+dy >= n or x+dx < 0 or y+dy < 0 or visited[x+dx][y+dy]:
            #     dx, dy = dirs[(dx, dy)]
            dx,dy = dirs[idx]
            if [x+dx,y+dy] == barriers[idx]:
                print("moving")
                barriers[idx][0] += bdeltas[idx][0]
                barriers[idx][1] += bdeltas[idx][1]
                idx = (idx + 1) % 4
                dx,dy = dirs[idx]
            x+=dx
            y+=dy
        return ans