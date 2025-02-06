class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        #dont go for any numbers were i*j < ans
        #so j starts at ans / i
        n = len(words)
        #words[0] = set(words[0])
        words.sort(key = lambda x: len(x))
        low = 0
        ans = 0
        for i in range(n):
            val = 0
            for char in words[i]:
                val |= 1 << (ord(char) - ord('a'))
            words[i] = (val, len(words[i]))
            for j in range(low, i):
                if not words[j][0] & words[i][0]:
                    ans = max(ans, words[j][1] * words[i][1])
        return ans