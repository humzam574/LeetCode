class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans, st, words = "", set(words), sorted(words, key = len, reverse = True)
        for word in words:
            if len(word) < len(ans): break
            valid = (len(word) > len(ans) or (len(word) == len(ans) and word < ans))
            if valid:
                for i in range(len(word) - 1, 0, -1):
                    if word[:i] not in st:
                        valid = False
                        break
            if valid: ans = word
        return ans