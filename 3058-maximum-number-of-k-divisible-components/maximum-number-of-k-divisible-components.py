class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree, self.ans = defaultdict(list), 0
        for edge in edges: tree[edge[0]].append(edge[1]); tree[edge[1]].append(edge[0])
        def dfs(node, parent):
            subsum = values[node] + sum((0 if n == parent else dfs(n, node)) for n in tree[node])
            self.ans += (subsum % k == 0); return subsum
        return (dfs(0, None), self.ans)[1]