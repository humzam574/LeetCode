class Solution:
    def highestPeak(self, ans: List[List[int]]) -> List[List[int]]:
        dq = deque()
        m = len(ans)
        n = len(ans[0])
        for x in range(m):
            for y in range(n):
                if ans[x][y] == 1:
                    dq.append((x,y))
                ans[x][y] -= 1
        while dq:
            x, y = dq.popleft()
            val = ans[x][y] + 1
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    ans[nx][ny] = val
                    dq.append((nx, ny))
        return ans