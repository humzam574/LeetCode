class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ""
        st = set(words)
        words = sorted(words, key = len, reverse = True)
        for word in words:
            if len(word) < len(ans):
                break
            valid = True
            for i in range(len(word) - 1, 0, -1):
                #print(word[:i])
                if word[:i] not in st:
                    valid = False
                    break
            if valid and (len(word) > len(ans) or (len(word) == len(ans) and word < ans)):
                ans = word
        return ans