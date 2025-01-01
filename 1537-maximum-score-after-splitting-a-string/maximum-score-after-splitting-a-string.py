class Solution:
    def maxScore(self, s: str) -> int:
        score = (s[0] == "0") + s[1:].count("1")
        high = score
        for i in range(1, len(s) - 1):
            if s[i] == "1": score-=1
            else: score, high = score + 1, max(high, score + 1)
        return high