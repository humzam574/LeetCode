class Solution:
    def canFinish(self, numCourses: int, reqs: List[List[int]]) -> bool:
        #make an adjacency graph
        #dfs with a visited node

        self.adjacency = [[] for i in range(numCourses)]

        for a,b in reqs:
            #adjacency[a][b] = True
            #adjacency[a].add(b)
            self.adjacency[b].append(a)

        state = [0] * numCourses
        order = []  # optional: collect a valid topo order

        def dfs(u: int) -> bool:
            if state[u] == 1:  # found a back edge (cycle)
                return False
            if state[u] == 2:  # already processed
                return True

            state[u] = 1  # mark as visiting (gray)
            for v in self.adjacency[u]:
                if not dfs(v):
                    return False
            state[u] = 2  # mark as visited (black)
            order.append(u)  # postorder append → reverse later for topo sort
            return True

        
        for i in range(numCourses):
            if state[i] != 0:
                continue
            if not dfs(i):
                return False
        return True