class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0] * n for _ in range(m)]
        i, j = 0, 0
        while(i < m and j < n):
            matrix[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]
            if(rowSum[i] == 0):
                i += 1
            else:
                j += 1
        return matrix