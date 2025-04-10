class Solution:
    def findMinDifference(self, tp: List[str]) -> int:
        tp, low, high = sorted([int(s[:2])*60 + int(s[3:]) for s in tp]), 1440, 0
        for i in range(1, len(tp)): low = min(low, abs(tp[i] - tp[i-1]))
        return min(low, 1440 + tp[0] - tp[-1])