class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        hashset = [None] * (len(arr) + 1)
        for x in range(m):
            for y in range(n):
                hashset[mat[x][y]] = (x, y)
        rows = [0] * m
        cols = [0] * n
        for i in range(len(arr)):
            x, y = hashset[arr[i]]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m:
                return i
        return 0