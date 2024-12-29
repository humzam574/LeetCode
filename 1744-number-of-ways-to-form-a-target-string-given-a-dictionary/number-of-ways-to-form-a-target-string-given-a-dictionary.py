class Solution:
    def numWays(self, words: List[str], t: str) -> int:
        tl, wl, freq = len(t), len(words[0]), [defaultdict(int) for i in range(len(words[0]))]
        for idx in range(len(words) * wl): freq[idx % wl][words[idx // wl][idx % wl]] += 1
        @cache
        def bt(c, k): return c == t if c == t or tl - len(c) > len(words[0]) - k else freq[k][t[len(c)]] * bt(c + t[len(c)], k + 1) + bt(c, k + 1)
        return bt("", 0) % (10 ** 9 + 7)