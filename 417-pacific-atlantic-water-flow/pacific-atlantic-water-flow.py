class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        self.m = len(heights)
        self.n = len(heights[0])
        def bfs(start):
            prev = set()
            dq = deque()
            for x,y in start:
                prev.add((x,y))
                dq.append((x,y))
            
            while dq:
                x,y = dq.popleft()
                
                for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx,ny = x+dx, y+dy
                    if (nx,ny) not in prev and 0 <= nx < self.m and 0 <= ny < self.n and heights[nx][ny] >= heights[x][y]:
                        prev.add((nx,ny))
                        dq.append((nx,ny))
            return prev
        s1 = [(0, j) for j in range(self.n)] + [(i, 0) for i in range(self.m)]
        s2 = [(self.m-1, j) for j in range(self.n)] + [(i, self.n-1) for i in range(self.m)]
        # for row in heights:
        #     print(row)
        # print()
        # print(s1)
        # print(s2)
        # print()
        # print(bfs(s1))
        # print()
        # print(bfs(s2))
        return list(bfs(s1).intersection(bfs(s2)))