class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dx = -1
        dy = 1
        x = 0
        y = 0
        m = len(mat)
        n = len(mat[0])
        ans = [0] * (m*n)
        for i in range(m*n):
            # print(str(x) + ", " + str(y) + " " + str(not (0 <= x+dx < m and 0 <= y+dy < n)))
            # print(str(x) + ", " + str(y) + ", ", end = "")
            ans[i] = mat[x][y]
            # print(ans[i])
            x+=dx
            y+=dy
            if not (0 <= x < m and 0 <= y < n):
                if dx == -1:
                    x+=1
                    if not (0 <= x < m and 0 <= y < n):
                        x+=1
                        y-=1
                else:
                    y+=1
                    if not (0 <= x < m and 0 <= y < n):
                        x-=1
                        y+=1
                dx = 1 if dx == -1 else -1
                dy = 1 if dy == -1 else -1
                
        return ans