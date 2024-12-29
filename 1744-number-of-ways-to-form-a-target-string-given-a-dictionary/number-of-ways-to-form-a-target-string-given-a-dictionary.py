class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        tl, wl, freq = len(target), len(words[0]), [defaultdict(int) for i in range(len(words[0]))]
        for idx in range(len(words) * len(words[0])): freq[idx % len(words[0])][words[idx // len(words[0])][idx % len(words[0])]] += 1
        @cache
        def bt(curr, k): return curr == target if curr == target or tl - len(curr) > len(words[0]) - k else freq[k][target[len(curr)]] * bt(curr + target[len(curr)], k + 1) + bt(curr, k + 1)
        return bt("", 0) % (10**9 + 7)