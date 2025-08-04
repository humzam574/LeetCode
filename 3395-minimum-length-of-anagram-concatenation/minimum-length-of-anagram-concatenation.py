class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        if len(c) == 1:
            return 1
        x = reduce(gcd, c.values())
        if x == 1:
            return n
        for i in range(x, 1, -1):
            if x % i:
                continue
            dn = n // i
            arr = (
                sorted(s[j*dn:(j+1)*dn]) for j in range(i)
            )
            if all(a == b for a, b in pairwise(arr)):
                return n // i
        return n