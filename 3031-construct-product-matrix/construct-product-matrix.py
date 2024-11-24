class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        #create a prefix array and a suffix array
        m = len(grid)
        n = len(grid[0])
        prefix = [[1] * n for i in range(m)]
        #prefix[0][0] = grid[0][0]
        for i in range(1,m*n): #m = 3, n = 2
            prefix[i // n][i % n] = (prefix[(i-1) // n][(i - 1) % n] * grid[(i - 1) // n][(i - 1) % n]) % 12345
        
        suffix = [[1] * n for i in range(m)]
        #suffix[m-1][n-1] = grid[m-1][n-1]
        for i in range(m*n - 2, -1, -1):
            suffix[i // n][i % n] = (suffix[(i + 1) // n][(i + 1) % n] * grid[(i + 1) // n][(i + 1) % n]) % 12345
        #print(prefix)
        #print(suffix)

        for i in range(m):
            for j in range(n):
                grid[i][j] = (prefix[i][j] * suffix[i][j]) % 12345
        return grid