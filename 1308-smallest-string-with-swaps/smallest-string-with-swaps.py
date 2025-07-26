class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
        component_map = {}
        
        res = list(s)
        
        for pair in pairs:
            self.union(pair[0], pair[1])

        
        for i in range(n):
            root = self.find(i)
            if root not in component_map:
                component_map[root] = []
            component_map[root].append(i)
        
        
        for indices in component_map.values():
            chars = [s[i] for i in indices]
            indices.sort()
            chars.sort()
            for i, ch in zip(indices, chars):
                res[i] = ch
                
        return ''.join(res)
        
        
        
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1    
        