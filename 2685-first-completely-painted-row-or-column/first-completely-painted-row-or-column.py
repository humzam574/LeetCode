class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n, hashset = len(mat), len(mat[0]), [None] * (len(arr) + 1); rows, cols = [0] * m, [0] * n
        for x in range(m):
            for y in range(n): hashset[mat[x][y]] = (x, y)
        for i in range(len(arr)):
            x, y = hashset[arr[i]]; rows[x], cols[y] = rows[x] + 1, cols[y] + 1
            if rows[x] == n or cols[y] == m: return i