class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans, n = 0, 2
        for c in s:
            n += (c=='b')
            if n != 2 and c != 'b': ans, n = ans + 1, n - 1
        return ans