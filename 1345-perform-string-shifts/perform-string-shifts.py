class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        tot = 0
        for direct, amt in shift:
            tot += (1 if direct == 1 else -1) * amt
        tot = tot % len(s)
        if tot == 0: return s
        if tot > 0:
            for i in range(tot):
                s = s[-1] + s[:len(s)-1]
            return s
        else:
            for i in range(tot):
                s = s[1:] + s[0]
            return s