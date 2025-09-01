class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        #1,2,3
        #4,5,6
        #7,8,9

        #1,4,7
        #2,5,8
        #3,6,9

        #do that swap and then flip

        for i in range(n):
            for j in range(i+1):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        

        for i in range(n):
            l = 0
            r = n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l+=1
                r-=1
        