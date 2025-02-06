class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        ans = []
        seen = set()
        for q in queries[::-1]:
            if q not in seen:
                ans.append(q)
                seen.add(q)
        for w in windows:
            if w not in seen:
                ans.append(w)
        return ans