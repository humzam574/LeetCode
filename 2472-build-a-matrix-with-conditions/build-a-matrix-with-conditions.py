class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            indegree = [0]*(k+1)
            adj = [[] for _ in range(k+1)]
            for u,v in edges:
                adj[u].append(v)
                indegree[v] +=1
            order = []
            q = deque()
            for i in range(1,k+1):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    indegree[v]-=1
                    if indegree[v] ==0:
                        q.append(v)
            return order

        row_order = topo_sort(rowConditions)
        if len(row_order) != k: return []

        col_order = topo_sort(colConditions)
        if len(col_order) != k: return []

        res = [[0]*k for _ in range(k)]

        row_map = {}
        col_map = {}
        for i in range(k):
            row_map[row_order[i]] = i
            col_map[col_order[i]] = i
        
        for i in range(1,k+1):
            r,c = row_map[i], col_map[i]
            res[r][c] = i
        
        return res
