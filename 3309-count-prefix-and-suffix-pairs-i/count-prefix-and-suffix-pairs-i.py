class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words) - 1):
            ans += sum(words[i] == words[j][:len(words[i])] == words[j][-len(words[i]):] for j in range(i + 1, len(words)))
        return ans