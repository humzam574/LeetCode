class Solution:
    def smallestNumber(self, pattern: str) -> str:
        s = ''.join(str(i) for i in range(1, len(pattern) + 2))
        for p in sorted("".join(p) for p in permutations(s)):
            prev = p[0]
            cont = True
            for i in range(len(p) - 1):
                if (pattern[i] == "I" and p[i] > p[i + 1]) or (pattern[i] == "D" and p[i] < p[i + 1]):
                    cont = False
                    break
            if cont:
                return p
        return "-1"
