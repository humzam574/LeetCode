class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        ans = (len(word) + k - 1) // k
        pres = word
        for i in range(ans):
            word = word[k:] + ("*" * k)
            pos = True
            for j, c in enumerate(word):
                if word[j] != '*' and word[j] != pres[j]:
                    pos = False
                    break
            if pos:
                return i+1
        return ans