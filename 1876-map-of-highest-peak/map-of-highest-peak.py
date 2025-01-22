class Solution:
    def highestPeak(self, ans: List[List[int]]) -> List[List[int]]:
        #multisourced BFS
        dq = deque()
        m = len(ans)
        n = len(ans[0])
        visited = set()
        #ans = [[1024 for x in range(n)] for y in range(m)]
        for x in range(m):
            for y in range(n):
                if ans[x][y] == 1:
                    dq.append((x,y))
                    ans[x][y] = 0
                else:
                    ans[x][y] = inf
        
        while dq:
            #print(dq)
            x, y = dq.popleft()
            val = ans[x][y] + 1
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == inf:
                    ans[nx][ny] = min(ans[nx][ny], val)
                    dq.append((nx, ny))
            # val = 1025
            # for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            #     nx, ny = x+dx, y+dy
            #     if 0 <= nx < m and 0 <= ny < n:
            #         if ans[nx][ny] == 1024:
            #             dq.append((nx, ny))
            #         else:
            #             val = min(val, ans[nx][ny] + 1)
            #     ans[x][y] = val
        return ans