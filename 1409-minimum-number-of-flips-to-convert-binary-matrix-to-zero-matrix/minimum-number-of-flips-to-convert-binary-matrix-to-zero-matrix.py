class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        high = int(2**(m*n))
        #print(high)
        arr = [i for i in range(high)]
        ans = 10
        for num in range(high):
            temp = []
            for row in mat:
                temp.append(list(row))
            bits = bin(num)[2:][::-1] + ("0" * (m*n))
            #print(bits)
            inc = 0
            for x in range(m):
                for y in range(n):
                    if bits[inc] == "1":
                        print(str(x) + ", " + str(y))
                        temp[x][y] = 1 - temp[x][y]
                        for dx, dy in ((1,0), (0,1), (-1,0), (0, -1)):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < m and 0 <= ny < n:
                                temp[nx][ny] = 1 - temp[nx][ny]
                    inc += 1
            # for row in temp:
            #     print(row)
            # print()
            # print()
            if sum(sum(row) for row in temp) == 0:
                ans = min(ans, bits.count("1"))
        return -1 if ans == 10 else ans