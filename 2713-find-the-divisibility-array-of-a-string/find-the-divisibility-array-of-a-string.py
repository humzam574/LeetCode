class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = [0] * len(word)
        curr = 0
        for i, c in enumerate(word):
            curr = curr*10 + int(c)
            if curr % m == 0:
                ans[i] = 1
            curr = curr % m
        return ans