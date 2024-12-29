class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        tl, wl, freq = len(target), len(words[0]), [defaultdict(int) for i in range(len(words[0]))]
        for i in range(wl):
            for j in range(len(words)): freq[i][words[j][i]]+=1
        #@cache
        memo = {}
        def bt(curr, k):
            if curr == target: return 1
            if tl - len(curr) > wl - k: return 0
            if (curr, k) in memo: return memo[(curr, k)]
            char = target[len(curr)]
            memo[(curr, k)] = (freq[k][char] * bt(curr + char, k + 1) + bt(curr, k + 1)) % (10 ** 9 + 7)
            return memo[(curr, k)]
        return bt("", 0) % (10 ** 9 + 7)