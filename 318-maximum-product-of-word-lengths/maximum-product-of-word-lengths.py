class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = low = 0; n = len(words); words.sort(key = lambda x: len(x))
        for i in range(n):
            val = 0
            for char in words[i]: val |= 1 << (ord(char) - ord('a'))
            words[i] = (val, len(words[i]))
            for j in range(low, i):
                if not words[j][0] & words[i][0]: ans = max(ans, words[j][1] * words[i][1])
        return ans