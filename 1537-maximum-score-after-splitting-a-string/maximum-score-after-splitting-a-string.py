class Solution:
    def maxScore(self, s):
        score = s.count("1")
        ans = score - 1
        for i in range(len(s) - 1):
            if s[i] == "1": score -= 1
            else: score, ans = score + 1, max(ans, score + 1)
        return ans