class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #group the pairs together
        #for each group, get the group of chars
        #sort
        #make an answer array and insert
        n = len(s)
        ans = ['' for i in range(n)]
        self.groups = []
        self.adj = [[] for i in range(n)]
        for a, b in pairs:
            self.adj[a].append(b)
            self.adj[b].append(a)
        self.visited = [False] * n
        def dfs(node, prev):
            self.visited[node] = True
            self.groups[-1].add(node)
            for val in self.adj[node]:
                if not self.visited[val]:
                    dfs(val, node)
        for i in range(n):
            if not self.visited[i]:
                self.groups.append(set())
                dfs(i, None)
        # print(self.adj)
        # print(self.groups)
        for group in self.groups:
            arr = sorted([s[i] for i in group])
            # print(arr)
            idx = 0
            for i in sorted(list(group)):
                ans[i] = arr[idx]
                idx+=1
        return ''.join(ans)