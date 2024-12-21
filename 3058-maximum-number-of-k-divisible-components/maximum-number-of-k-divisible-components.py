class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        #what if you convert this into a binary tree where each node is the sum of all values below it
        tree = defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        
        self.ans = 0
        def dfs(node, parent):
            subsum = values[node]
            for n in tree[node]:
                if n != parent:
                    subsum += dfs(n, node)
            if subsum % k == 0:
                self.ans += 1
            return subsum
        dfs(0, None)
        return self.ans