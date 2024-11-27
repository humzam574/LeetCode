class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size, ans, window = len(cardPoints) - k, 0, sum(cardPoints[-k:])
        for i in range(k): window, ans = window + cardPoints[i] - cardPoints[size + i], max(ans, window)
        return max(ans, window)