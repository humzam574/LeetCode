class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count("1"); return max(score := score + 1 - 2 * (s[i] == "1") for i in range(len(s) - 1))
