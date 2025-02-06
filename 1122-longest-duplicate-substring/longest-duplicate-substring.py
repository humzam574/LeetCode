class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A, mod, res, lo, hi = [ord(c) - ord('a') for c in S], 2**63 - 1, 0, 0, len(S)
        def test(L):
            p, cur = pow(26, L, mod), reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0); seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        while lo < hi:
            mi = (lo + hi + 1) // 2; pos = test(mi)
            if pos: lo, res = mi, pos
            else: hi = mi - 1
        return S[res:res + lo]