class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        i = 1
        for p in sorted("".join(p) for p in product(('a', 'b', 'c'), repeat=n)):
            cont = True
            for j in range(n - 1):
                if p[j] == p[j + 1]:
                    cont = False
                    break
            if cont:
                if i == k:
                    return p
                i += 1
        return ""