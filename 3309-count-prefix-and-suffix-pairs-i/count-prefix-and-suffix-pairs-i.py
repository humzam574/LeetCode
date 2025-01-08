class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(sum(words[i] == words[j][:len(words[i])] == words[j][-len(words[i]):] for j in range(i + 1, len(words))) for i in range(len(words) - 1))