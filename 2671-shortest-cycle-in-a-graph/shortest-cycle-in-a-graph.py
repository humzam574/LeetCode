class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        #BFS
        ans = inf
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        for i in range(n):
            # if i in visited:
            #     continue
            visited = set()
            dq = deque()
            dq.append((i, None, 0))
            # visited[i] = 0
            while dq:
                curr, prev, ln = dq.popleft()
                if ln > ans:
                    continue
                # print(str(curr) + ", " + str(prev))
                visited.add(curr)
                
                for edge in adj[curr]:
                    if edge == prev:
                        continue
                    if edge == i:
                        ans = min(ans, ln + 1)
                        dq = None
                        break
                    dq.append((edge, curr, ln + 1))
        return ans if ans != inf else -1
            
        
        #3 ------> 2
        #|         |
        #0 -> 4    |
        #|    |   /
        #5 <- 1 -/