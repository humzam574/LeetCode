class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        M, N = len(grid), len(grid[0])
        d = defaultdict(int)
        
        medianIdx = (M*N)//2

        for i in range(M):
            for j in range(N):
                d[grid[i][j]] += 1
                
        keys = sorted(d)
        curr = median = 0
        
        for k in keys:
            curr += d[k]
            if curr > medianIdx:
                median = k
                break
        ans = 0  
        for k in d:
            cnt = abs(k-median)/x
            if cnt%1 != 0:
                return -1
            ans += cnt*d[k]

        return int(ans)
        