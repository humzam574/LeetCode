class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.graph = [set() for _ in range(c+1)]
        for a,b in connections:
            self.graph[a].add(b)
            self.graph[b].add(a)
        
        offline = set()

        self.labels = [0] * (c+1)
        self.curr = 1
        def dfs(ptr, prev):
            self.labels[ptr] = self.curr
            for adj in self.graph[ptr]:
                if adj != prev and self.labels[adj] == 0:
                    dfs(adj, ptr)
        for i in range(1, c+1):
            if self.labels[i] == 0:
                dfs(i, None)
                self.curr+=1
        # print(self.labels)
        heaps = [[] for _ in range(self.curr)]
        for i in range(1, len(heaps)):
            heapify(heaps[i])
        
        for i in range(len(self.labels)):
            heappush(heaps[self.labels[i]],i)
        
        ans = []
        for a,b in queries:
            if a == 2:
                offline.add(b)
            else:
                if b not in offline:
                    ans.append(b)
                else:
                    lbl = self.labels[b]
                    while heaps[lbl] and heaps[lbl][0] in offline:
                        heappop(heaps[lbl])
                    if heaps[lbl]:
                        ans.append(heaps[lbl][0])
                    else:
                        ans.append(-1)
        return ans
