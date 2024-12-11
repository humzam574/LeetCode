class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans, n = 0, 0
        for c in s:
            if c == 'b': n += 1
            elif n != 0: ans, n = ans + 1, n - 1
        return ans