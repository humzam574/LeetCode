class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 10
        for bits in range(int(2**(m*n))):
            temp = [row[:] for row in mat]
            inc = 0
            for x in range(m):
                for y in range(n):
                    if (bits >> inc) & 1:
                        temp[x][y] ^= 1
                        for dx, dy in ((1,0), (0,1), (-1,0), (0, -1)):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < m and 0 <= ny < n:
                                temp[nx][ny] ^= 1
                    inc += 1
            update = True
            for row in temp:
                if 1 in row:
                    update = False
                    break
            if update:
                ans = min(ans, bin(bits).count('1'))
        return -1 if ans == 10 else ans