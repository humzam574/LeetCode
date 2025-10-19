class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        self.prev = set()
        def dfs(s):
            if s in self.prev:
                return s
            self.prev.add(s)
            o1 = ''.join([str((int(c) + a) % 10) if i % 2 == 1 else c for i,c in enumerate(s)])
            o2 = s
            # print(o1)
            if b != len(s):
                o2 = s[-b:] + s[:-b]
                # print(o2)
            # else:
            return min(s, dfs(o1), dfs(o2))
        return dfs(s)