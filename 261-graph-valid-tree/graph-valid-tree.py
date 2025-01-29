class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #n - 1 nodes
        self.graph = defaultdict(list)
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        #print(self.graph)
        arr = [False] * n
        def dfs(curr, prev, p):
            arr[curr] = True
            for item in self.graph[curr]:
                if item == p: continue
                if item in prev:
                    print(item)
                    return False
                prev.add(item)
                if not dfs(item, prev, curr):
                    return False
                prev.remove(item)
            return True
        if not dfs(0, set(), None):
            return False
        for item in arr:
            if not item: return False
        return True