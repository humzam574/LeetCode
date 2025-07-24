class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        #use some sort of head recursion to get the xor of every subtree
        #questions:
        #1. how to construct the tree?
        #2. how to recurse and do xor, and save those precomputed results
        #3. how to iterate through every edge pair and get these xor's in O(1)
        

        #observations
        #1. every leaf only has 1 connect. if you arent a leaf you have a parent and child
        #2. maybe construct a 2d array for adjacency
        #3. and go up to calculate
        #4. use a bfs to avoid going too far and allowing you to merge

        #final approach
        #1. create an adjacency 2d array
        #2. make a dq of node indices and do a modified bfs up the tree of the xor's, memoizing results
        #3. iterate through every edge and figure some shit out idk

        n = len(nums)
        self.adj = [set() for i in range(n)]
        # print(adj)
        for a, b in edges:
            self.adj[a].add(b)
            self.adj[b].add(a)
        self.xors = [0]*n#nums.copy()
        # print(self.adj)
        self.kids = [set() for i in range(n)]#{}#{0: set([i for i in range(1, n)])}
        def dfs(curr, prev):
            if len(self.adj[curr]) == 1 and self.adj[curr] == {prev}:
                self.xors[curr] = nums[curr]
                #self.kids[curr] = {curr}
                return
            val = nums[curr]
            desc = set()
            for nb in self.adj[curr]:
                if nb == prev:
                    continue
                desc.add(nb)
                # print("doing dfs of " + str(nb) + ", " + str(curr))
                dfs(nb, curr)
                desc = desc | self.kids[nb]
                val ^= self.xors[nb]
            self.kids[curr] = desc
            self.xors[curr] = val

        #11 ^ 4 ^ 5 ^ 5 ^ 1 = 14
        #5 ^ 5 ^ 4 ^ 11 = 15
        #5
        #11 ^ 4 = 15
        #11
        #     0
        #     1
        #    3  2
        #   4
        dfs(0, None)
        # print(self.kids)
        # print(self.xors)
        tot = self.xors[0]
        ans = inf
        for i in range(1, n):
            for j in range(i + 1, n):
                #get the two edges and process
                #case 1: one cut is in the others subtree
                #case 2: the two cuts are independent
                if i in self.kids[j]:
                    v1 = self.xors[i]
                    v2 = self.xors[i] ^ self.xors[j]
                    v3 = tot ^ self.xors[j]
                elif j in self.kids[i]:
                    v1 = self.xors[j]
                    v2 = self.xors[i] ^ self.xors[j]
                    v3 = tot ^ self.xors[i]
                else:
                    v1 = self.xors[i]
                    v2 = self.xors[j]
                    v3 = tot ^ v1 ^ v2
                ans = min(ans, max(v1, v2, v3) - min(v1, v2, v3))
        return ans






