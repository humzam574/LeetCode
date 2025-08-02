class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score = 0
        res = 0
        first_occurrence = {}

        for i, h in enumerate(hours):
            score += (1 if h > 8 else -1)
            if score > 0:
                res = i + 1
            else:
                if score - 1 in first_occurrence:
                    res = max(res, i - first_occurrence[score-1])
            if score not in first_occurrence:
                first_occurrence[score] = i
        
        return res