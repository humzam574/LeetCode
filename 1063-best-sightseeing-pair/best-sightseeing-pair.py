class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr, ans = values[0], 0
        for i in range(1, len(values)): ans, curr = max(ans, values[i] + curr - 1), max(curr - 1, values[i])
        return ans