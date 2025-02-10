class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        num = 0
        for d in word:
            num *= 10
            num += ord(d) - ord('0')
            num %= m
            ans.append(1 if num == 0 else 0)
        return ans