class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        curr = 0
        seen = {}
        counter = defaultdict(int)
        for i, (x, y) in enumerate(queries):
            if x in seen:
                counter[seen[x]] -= 1
                if counter[seen[x]] == 0:
                    del counter[seen[x]]
            seen[x] = y
            counter[y] += 1
            ans[i] = len(counter.values())
        return ans