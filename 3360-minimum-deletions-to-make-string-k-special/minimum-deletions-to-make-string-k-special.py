class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        arr = Counter(word).values()
        ans = inf
        for x in arr:
            curr = 0
            for a in arr:
                curr += a if a < x else max(0, a - (x + k))
            ans = min(ans, curr)
        return ans