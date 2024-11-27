class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dijkstra():
            dist, dq = [0] + [inf] * (n-1), [(0, 0)]  # (distance, node)
            while dq:
                cd, node = heapq.heappop(dq)
                if node == n - 1: return dist[n - 1]
                if cd > dist[node]: continue
                for nbr, wt in graph[node]:
                    if cd + wt < dist[nbr]:
                        dist[nbr] = cd + wt
                        heapq.heappush(dq, (cd + wt, nbr))
            return dist[n - 1]
        graph, ans = [[] for i in range(n)], []
        for i in range(n - 1): graph[i].append((i + 1, 1))
        for query in queries:
            graph[query[0]].append((query[1], 1))
            ans.append(dijkstra())
        return ans