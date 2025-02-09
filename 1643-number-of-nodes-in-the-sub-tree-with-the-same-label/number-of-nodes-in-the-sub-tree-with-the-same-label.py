class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        count = [0] * 26
        ret = [0] * n
        def dfs(node, parent):
            index = ord(labels[node]) - 97
            prev = count[index]
            count[index] += 1
            for child in g[node]:
                if child != parent:
                    dfs(child, node)
            ret[node] = count[index] - prev
        dfs(0, -1)
        return ret