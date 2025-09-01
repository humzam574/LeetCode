class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        

        for i in range(len(matrix)):
            l = 0
            r = len(matrix) - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l+=1
                r-=1
        