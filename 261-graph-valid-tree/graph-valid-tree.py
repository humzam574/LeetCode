class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, is_connected):
            if node in is_connected:
                return

            is_connected.add(node)
            for neighbor in dag[node]:
                dfs(neighbor, is_connected)
        v, e = n, len(edges)
        if v - 1 != e: return False

        dag = [[] for _ in range(v)]
        for i, j in edges:
            dag[i].append(j)
            dag[j].append(i)
        is_connected = set()
        dfs(0, is_connected)
        return len(is_connected) == v

    