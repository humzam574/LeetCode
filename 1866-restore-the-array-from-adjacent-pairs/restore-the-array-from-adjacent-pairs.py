class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        self.dict = defaultdict(list)
        for a,b in adjacentPairs:
            self.dict[a].append(b)
            self.dict[b].append(a)
        self.ans = []
        def dfs(prev, curr):
            self.ans.append(curr)
            for val in self.dict[curr]:
                if val == prev:
                    continue
                dfs(curr, val)
        for k,v in self.dict.items():
            if len(v) == 1:
                dfs(None, k)
                return self.ans