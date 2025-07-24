class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #find the city which has the least number of neighbors which are within thresh
        #now i need to find a way to get the neighbor size of a given edge in O(n) or O(n^2)

        #djikstras:
        # H = makequeue(V)    (using dist-values as keys)
        # while H is not empty:
        #     u = deletemin(H)
        #     for all edges (u, v) ∈ E:
        #         if dist(v) > dist(u) + l(u, v):
        #             dist(v) = dist(u) + l(u, v)
        #             prev(v) = u
        #             decreasekey(H, v)

        #step 1: make an adjacency list
        #and make a way to lookup edge lengths (maybe using a dict key tup and value int)
        ans = 0
        cnt = inf
        adj = [[] for i in range(n)]
        for a, b, c in edges:
            adj[a].append((b, c))
            adj[b].append((a, c))
            #weights[(min(a,b), max(a,b))] = c
        for i in range(n):
            #run djikstras to find the shortest path length to each node from n
            #count up how many are less than or equal to thresh
            #if less than or equal to cnt, update ans to be i
            
            #logic for djikstras
            #choose a starting node (i)
            #keep an array for distance from i
            #make a set of visited nodes
                #make them all inf instead of i, which is 0
            #examine edges leaving i, and update
            #add i to visited
            #then look at the array and pick the smallest node connected to i which hasnt been picked (pretend its C)
            #mark C as visited
            #examine neighbors of C and update the shortest path list
            #repeat, choose the smallest connecting node that hasnt been visited

            dist = [inf] * n
            visited = [False] * n
            dist[i] = 0
            heap = [(0, i)]
            heapify(heap)
            while heap:
                ds, nd = heappop(heap)
                if visited[nd]:
                    continue
                visited[nd] = True

                for nb, wg in adj[nd]:
                    if dist[nb] > wg + dist[nd]:
                        dist[nb] = wg + dist[nd]
                        heappush(heap, (dist[nb], nb))
            val = -1
            for d in dist:
                if d <= distanceThreshold:
                    val+=1
            # print("i = " + str(i) + ", val = " + str(val))
            # print(dist)
            # print()
            if val <= cnt:
                cnt = val
                ans = i
        return ans