class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        tp = [int(s[:2])*60 + int(s[3:]) for s in timePoints]
        tp.sort()
        print(tp)
        low = 1440
        high = 0
        for i in range(1, len(tp)):
            low = min(low, abs(tp[i] - tp[i-1]))
            high = max(high, abs(tp[i] - tp[i-1]))
        high = max(high, abs(tp[-1] - tp[0]))
        return min(low, 1440 - high)