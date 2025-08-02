class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        self.ans = float('inf')
        self.dep = [float('inf')] * n
        self.conn = [[] for _ in range(n)]

        for u, v in edges:
            self.conn[u].append(v)
            self.conn[v].append(u)

        def dfs(cur, par, d):
            self.dep[cur] = d
            for sub in self.conn[cur]:
                if sub != par:
                    if self.dep[sub] > d + 1:
                        dfs(sub, cur, d + 1)
                    elif self.dep[sub] < d:
                        # Cycle detected
                        self.ans = min(self.ans, d - self.dep[sub] + 1)

        for i in range(n):
            if self.dep[i] == float('inf'):
                dfs(i, -1, 0)

        return -1 if self.ans == float('inf') else self.ans