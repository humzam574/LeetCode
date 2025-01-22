class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        n = len(isWater[0])
        m = len(isWater)
        output = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    output[i][j] = 0
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            if 0 < i < m and output[i-1][j] == -1:
                output[i-1][j] =  output[i][j] + 1
                q.append((i-1, j))
            if 0 < j < n and output[i][j-1] == -1:
                output[i][j-1] = output[i][j] + 1
                q.append((i,j-1))
            if 0 <= j < n - 1 and output[i][j + 1] == -1:
                output[i][j + 1] = output[i][j] + 1
                q.append((i,j+1))
            if 0 <= i < m - 1 and output[i + 1][j] == -1:
                output[i + 1][j] = output[i][j] + 1
                q.append((i+1,j))
        return output