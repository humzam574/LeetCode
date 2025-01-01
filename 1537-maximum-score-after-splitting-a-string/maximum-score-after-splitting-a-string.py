class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count("1")
        high = 0
        for i in range(len(s) - 1):
            if s[i] == "1": score-=1
            else: score += 1
            high = max(high, score)
        return high