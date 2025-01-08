class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                ans+= (1 if len(words[j]) >= len(words[i]) and words[i] == words[j][:len(words[i])] == words[j][-len(words[i]):] else 0)
        return ans