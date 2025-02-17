class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        L, t, f, tiles = len(tiles), 0, math.factorial, sorted(list(tiles))
        for n in range(1,L+1):
            q = ('',)
            for p in itertools.combinations(tiles,n):
                if p > q: t, q = t + f(n)//prod(list(map(f,collections.Counter(p).values()))), p
        return t