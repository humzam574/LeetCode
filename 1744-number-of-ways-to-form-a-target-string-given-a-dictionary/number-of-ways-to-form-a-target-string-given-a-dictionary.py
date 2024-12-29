class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        #this has to be some sort of tabulation
        tl = len(target)
        freq = [defaultdict(int) for i in range(len(words[0]))]
        for i in range(len(words[0])):
            for j in range(len(words)):
                freq[i][words[j][i]]+=1
        @cache
        def bt(curr, k):
            if curr == target: return 1
            if tl - len(curr) > len(words[0]) - k: return 0
            char = target[len(curr)]
            return freq[k][char] * bt(curr + char, k + 1) + bt(curr, k + 1)
        return bt("", 0) % (10**9 + 7)