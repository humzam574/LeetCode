class Solution:
    def maxSum(self, g: List[List[int]]) -> int:
        a=-inf
        for i in range(1,len(g)-1):
            for j in range(1,len(g[0])-1):
                s=g[i][j]+g[i-1][j-1]+g[i-1][j]+g[i-1][j+1]+g[i+1][j-1]+g[i+1][j]+g[i+1][j+1]
                if s>a:a=s
        return a