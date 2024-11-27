class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        ans = window = sum(cardPoints[-k:])
        for i in range(k):
            window = window + cardPoints[i] - cardPoints[size + i]
            ans = max(ans, window)
        return ans
