class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #keep a curr and ans variable
        curr = values[0]
        ans = 0
        for i in range(1, len(values)):
            curr -= 1
            ans = max(ans, values[i] + curr)
            if values[i] > curr:
                curr = values[i]
        return ans