class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ans = set([i for i in range(n)])
        for edge in edges: ans.discard(edge[1])
        return -1 if len(ans) > 1 else ans.pop()